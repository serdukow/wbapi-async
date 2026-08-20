from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
from typing import Any

import pytest


def load_generator() -> Any:
    path = Path(__file__).resolve().parent.parent / "scripts" / "codegen.py"
    spec = importlib.util.spec_from_file_location("codegen", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["codegen"] = module
    spec.loader.exec_module(module)
    return module


gen = load_generator()


@pytest.mark.parametrize(
    ("summary", "verb", "expected"),
    [
        ("Получить список поставок", "GET", ""),
        ("Создать поставку", "POST", "create"),
        ("Обновить остатки", "PUT", "update"),
        ("Удалить поставку", "DELETE", "delete"),
        ("Отменить сборочное задание", "PATCH", "cancel"),
        ("Получить стикеры", "POST", ""),
        ("Закрепить IMEI", "PUT", "update"),
    ],
)
def test_action_comes_from_the_summary(summary: str, verb: str, expected: str) -> None:
    """The action comes from the summary: Wildberries often uses POST for reads."""
    assert gen.action_for(summary, verb) == expected


@pytest.mark.parametrize(
    ("summary", "verb", "expected"),
    [
        ("Непонятное описание", "GET", ""),
        ("Непонятное описание", "POST", "create"),
        ("Непонятное описание", "DELETE", "delete"),
    ],
)
def test_action_falls_back_to_the_verb(summary: str, verb: str, expected: str) -> None:
    assert gen.action_for(summary, verb) == expected


@pytest.mark.parametrize(
    ("base", "action", "expected"),
    [
        ("supplies", "create", "supplies_create"),
        ("supplies", "", "supplies"),
        ("orders_cancel", "cancel", "orders_cancel"),
        ("delete", "delete", "delete"),
    ],
)
def test_action_is_not_duplicated(base: str, action: str, expected: str) -> None:
    assert gen.compose_name(base, action) == expected


@pytest.mark.parametrize(
    ("source", "expected"),
    [
        ("nmID", "nm_id"),
        ("updatedAt", "updated_at"),
        ("already_snake", "already_snake"),
        ("class", "class_"),
    ],
)
def test_snake_case(source: str, expected: str) -> None:
    assert gen.snake(source) == expected


@pytest.mark.parametrize("name", ["type", "filter", "next", "id"])
def test_argument_names_avoid_builtins(name: str) -> None:
    assert gen.arg(name).endswith("_")


def test_rate_limits_from_a_simple_table() -> None:
    description = """
| Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- |
| 1 мин | 300 запросов | 200 мс | 20 запросов |
"""
    assert gen.parse_rate_limits(description) == {"all": (200, 20)}


def test_rate_limits_per_token_kind() -> None:
    description = """
| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 100 запросов | 600 мс | 5 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос |
"""
    limits = gen.parse_rate_limits(description)
    assert limits["personal"] == (600, 5)
    assert limits["basic"] == (1_800_000, 1)


def test_rate_limits_absent() -> None:
    assert gen.parse_rate_limits("Описание без таблицы") == {}


@pytest.mark.parametrize(
    ("query", "body", "response", "path", "expected"),
    [
        ({"next"}, set(), set(), "/api/v3/orders", "next"),
        (set(), set(), {"next"}, "/api/v3/orders", "next"),
        (set(), {"cursor"}, set(), "/content/v2/cards", "cursor"),
        (set(), {"rrdId"}, set(), "/api/finance/v1/x", "rrdid"),
        ({"skip", "take"}, set(), set(), "/api/v1/feedbacks", "skip_take"),
        ({"offset"}, set(), set(), "/api/v1/users", "offset_query"),
        (set(), {"offset"}, set(), "/api/v2/report", "offset_body"),
        ({"next"}, set(), set(), "/api/v1/feedbacks/count", None),
        (set(), set(), set(), "/api/v3/orders", None),
    ],
)
def test_pagination_detection(
    query: set[str], body: set[str], response: set[str], path: str, expected: str | None
) -> None:
    assert gen.detect_pagination(query, body, response, path) == expected


def test_docstring_quotes_are_made_safe() -> None:
    assert not gen.safe_doc('время доставки "с"').endswith('"')
    assert '"""' not in gen.safe_doc('text """ inside')


def test_scope_mapping_covers_known_categories() -> None:
    from wbapi.utils import Scope

    for category, scope_name in gen._SCOPE_BY_CATEGORY.items():
        assert hasattr(Scope, scope_name), category


def test_every_spec_has_a_section() -> None:
    """Every spec must map to a client section."""
    specs = {path.name for path in (gen.ROOT / "specs").glob("*.yaml")}
    known = set(gen.SECTIONS)
    unmapped = specs - known
    assert unmapped <= {"05-orders-dbs.yaml"}, unmapped


def test_generation_is_reproducible(tmp_path: Path) -> None:
    """Regenerating the same section twice produces identical output."""
    import yaml

    spec_file = gen.ROOT / "specs" / "07-orders-fbw.yaml"
    spec = yaml.safe_load(spec_file.read_text())

    first = gen.Generator(spec, "orders_fbw")
    first.collect()
    second = gen.Generator(spec, "orders_fbw")
    second.collect()

    assert first.render_methods() == second.render_methods()
    assert first.render_types() == second.render_types()


def test_name_clashes_are_resolved() -> None:
    """Colliding names are disambiguated by the HTTP verb."""
    import yaml

    spec = yaml.safe_load((gen.ROOT / "specs" / "02-items.yaml").read_text())
    generator = gen.Generator(spec, "items")
    generator.collect()
    names = [method["name"] for method in generator.methods]
    assert len(names) == len(set(names))
