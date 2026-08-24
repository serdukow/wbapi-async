from __future__ import annotations

import importlib.util
import keyword
from pathlib import Path
import re
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
        ("Получить список поставок", "GET", "get"),
        ("Создать поставку", "POST", "create"),
        ("Обновить остатки", "PUT", "update"),
        ("Удалить поставку", "DELETE", "delete"),
        ("Отменить сборочное задание", "PATCH", "cancel"),
        ("Получить стикеры", "POST", "get"),
        ("Закрепить IMEI", "PUT", "set"),
    ],
)
def test_action_comes_from_the_summary(summary: str, verb: str, expected: str) -> None:
    """The action comes from the summary: Wildberries often uses POST for reads."""
    assert gen.action_for(summary, verb) == expected


@pytest.mark.parametrize(
    ("summary", "verb"),
    [
        ("Создать отчёт", "POST"),
        ("Удалить ставки поисковых кластеров", "DELETE"),
        ("Обновить список контактов", "PUT"),
    ],
)
def test_a_noun_later_in_the_summary_does_not_decide(summary: str, verb: str) -> None:
    """An unanchored match let "отчёт" in "Создать отчёт" read as a get."""
    assert gen.action_for(summary, verb) != "get"


@pytest.mark.parametrize(
    ("summary", "verb", "expected"),
    [
        ("Непонятное описание", "GET", "get"),
        ("Непонятное описание", "POST", "create"),
        ("Непонятное описание", "DELETE", "delete"),
    ],
)
def test_action_falls_back_to_the_verb(summary: str, verb: str, expected: str) -> None:
    assert gen.action_for(summary, verb) == expected


@pytest.mark.parametrize(
    ("path", "action", "section", "expected"),
    [
        ("/api/v3/supplies", "create", "orders_fbs", "create_supply"),
        ("/api/v3/orders/new", "get", "orders_fbs", "get_orders_new"),
        ("/api/v3/orders/{orderId}/cancel", "cancel", "orders_fbs", "cancel_order"),
        ("/api/v1/account/balance", "get", "finances", "get_account_balance"),
        # The section name is dropped only when what is left still names something.
        ("/api/finance/v1/acquiring/detailed", "get", "finances", "get_acquiring_detailed"),
        # Filler segments WB puts mid-path.
        ("/content/v2/get/cards/list", "get", "items", "get_content_cards_list"),
        ("/api/v1/offer/keys/{offer_id}/list", "get", "wbd", "get_offer_keys_list"),
        # A segment equal to the action, at either end.
        ("/api/v1/content/delete", "delete", "wbd", "delete_content"),
        ("/api/v1/upload/upload-chunk", "upload", "wbd", "upload_chunk"),
        # A keyword cannot end a method name.
        ("/api/v1/tariffs/return", "get", "rates", "get_tariffs_returns"),
    ],
)
def test_names_are_verb_first(path: str, action: str, section: str, expected: str) -> None:
    assert gen.compose_name(path, action, section) == expected


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
    # 300 requests a minute is 5/s; the bucket holds 20 of them at once.
    assert gen.parse_rate_limits(description) == {"all": (4000, 20)}


def test_the_sustained_rate_comes_from_the_period_columns() -> None:
    """ "Интервал | Всплеск" sizes the bucket; "Период | Лимит" sets the rate.

    Reading the burst columns as the rate let /news run at 10 req/min where
    the spec allows 1 — a tenfold overrun across 410 spec rows.
    """
    description = """
| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 1 запрос | 1 мин | 10 запросов |
"""
    interval_ms, burst = gen.parse_rate_limits(description)["personal"]

    assert burst / (interval_ms / 1000) == pytest.approx(1 / 60)


def test_no_generated_limit_outruns_its_spec_row() -> None:
    """No endpoint may be configured faster than the table permits."""
    import yaml

    row = re.compile(r"^\s*\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|\s*$", re.M)
    faster: list[str] = []
    for spec_name in gen.SECTIONS:
        spec_file = gen.SPECS_DIR / spec_name
        if not spec_file.exists():
            continue
        for path, item in (yaml.safe_load(spec_file.read_text()).get("paths") or {}).items():
            if not isinstance(item, dict):
                continue
            for verb, operation in item.items():
                if verb not in {"get", "post", "put", "patch", "delete"}:
                    continue
                if not isinstance(operation, dict):
                    continue
                description = operation.get("description") or ""
                limits = gen.parse_rate_limits(description)
                for match in row.finditer(description):
                    cells = [c.strip() for c in match.groups()]
                    if any(set(c) <= set("- ") for c in cells):
                        continue
                    if cells[0].lower() not in gen._TOKEN_KINDS:
                        continue
                    period = gen._NUM_UNIT.match(cells[1])
                    allowance = re.match(r"^(\d+)", cells[2])
                    if not period or not allowance:
                        continue
                    window = int(period.group(1)) * gen._TO_MS[period.group(2)] / 1000
                    allowed = int(allowance.group(1)) / window
                    limit = limits.get(gen._TOKEN_KINDS[cells[0].lower()])
                    if limit and limit[1] / (limit[0] / 1000) > allowed + 1e-9:
                        faster.append(f"{verb.upper()} {path} {cells[0]}")

    assert not faster, faster[:5]


def test_rate_limits_per_token_kind() -> None:
    description = """
| Тип | Период | Лимит | Интервал | Всплеск |
| --- | --- | --- | --- | --- |
| Персональный | 1 мин | 100 запросов | 600 мс | 5 запросов |
| Базовый | 1 ч | 2 запроса | 30 мин | 1 запрос |
"""
    limits = gen.parse_rate_limits(description)
    # 100 requests a minute is 1.667/s, and 2 an hour is one per 30 minutes.
    assert limits["personal"] == (3000, 5)
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


@pytest.mark.parametrize(
    ("name", "text"),
    [
        ("invalid yaml", "a: [1,\nb"),
        ("not a mapping", "- one\n- two"),
        ("no paths key", "info:\n  title: X"),
        ("empty paths", "info:\n  title: X\npaths: {}"),
        ("an antibot page", "<!DOCTYPE html><html>498</html>"),
    ],
)
def test_unusable_specs_are_refused(tmp_path: Path, name: str, text: str) -> None:
    """A spec that would generate nothing must raise, not return empty.

    Writing an empty section would erase every method the package already has.
    """
    spec_file = tmp_path / "spec.yaml"
    spec_file.write_text(text)

    with pytest.raises(gen.SpecError):
        gen.load_spec(spec_file)


def test_a_section_is_not_written_when_no_methods_survive(tmp_path: Path) -> None:
    spec_file = tmp_path / "spec.yaml"
    spec_file.write_text("info:\n  title: X\npaths:\n  /a: {}\n")

    with pytest.raises(gen.SpecError, match="no methods"):
        gen.generate_section(spec_file, "items")


def test_a_real_spec_still_loads() -> None:
    spec = gen.load_spec(gen.SPECS_DIR / "10-rates.yaml")
    assert spec["paths"]


KEYWORD_SEGMENTS = ["class", "pass", "return", "is", "import", "try", "del", "for", "not"]


@pytest.mark.parametrize("segment", KEYWORD_SEGMENTS)
def test_a_keyword_segment_still_yields_a_usable_name(segment: str) -> None:
    """A path segment that is a Python keyword cannot end a method name.

    Appending "s" alone tripled the letter on words already ending in one:
    /api/v3/class became create_classs, the same defect as create_passs.
    """
    name = gen.compose_name(f"/api/v3/{segment}", "create", "items")

    assert name.isidentifier()
    assert not keyword.iskeyword(name)
    assert not re.search(r"(.)\1\1", name)


def test_generated_names_are_well_formed() -> None:
    """Every name the specs produce must survive the rules we fixed one by one.

    Each rule here is a defect we hit while reworking the naming: a tripled
    letter, a repeated word, filler left mid-name, a bare verb.
    """
    import yaml

    problems: list[str] = []
    for spec_name, package in gen.SECTIONS.items():
        spec_file = gen.SPECS_DIR / spec_name
        if not spec_file.exists():
            continue
        spec = yaml.safe_load(spec_file.read_text())
        for path, item in (spec.get("paths") or {}).items():
            if not isinstance(item, dict):
                continue
            for verb, operation in item.items():
                if verb not in {"get", "post", "put", "patch", "delete"}:
                    continue
                if not isinstance(operation, dict):
                    continue
                action = gen.action_for(operation.get("summary") or "", verb.upper())
                name = gen.compose_name(path, action, package)
                words = name.split("_")
                if not name.isidentifier() or keyword.iskeyword(name):
                    problems.append(f"{package}.{name}: not a usable identifier")
                if name.endswith("_"):
                    problems.append(f"{package}.{name}: trailing underscore")
                if any(words[i] == words[i + 1] for i in range(len(words) - 1)):
                    problems.append(f"{package}.{name}: repeated word")
                if re.search(r"(.)\1\1", name):
                    problems.append(f"{package}.{name}: tripled letter")
                if "get" in words[1:]:
                    problems.append(f"{package}.{name}: filler left mid-name")
                if len(words) == 1:
                    problems.append(f"{package}.{name}: a bare verb says nothing")

    assert not problems, problems[:5]
