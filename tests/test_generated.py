from __future__ import annotations

import importlib
import pkgutil
import re

import msgspec
import pytest

from wbapi import WBApi
from wbapi.client.method import WBMethod
from wbapi.client.model import WBModel
import wbapi.resources as resources
from wbapi.utils import Scope


def all_methods() -> list[tuple[str, str, type[WBMethod]]]:
    found = []
    for module in pkgutil.iter_modules(resources.__path__):
        methods = importlib.import_module(f"wbapi.resources.{module.name}.methods")
        for name in dir(methods):
            cls = getattr(methods, name)
            if isinstance(cls, type) and issubclass(cls, WBMethod) and cls is not WBMethod:
                found.append((module.name, name, cls))
    return found


def all_models() -> list[tuple[str, str, type[WBModel]]]:
    found = []
    for module in pkgutil.iter_modules(resources.__path__):
        models = importlib.import_module(f"wbapi.resources.{module.name}.models")
        for name in dir(models):
            cls = getattr(models, name)
            if isinstance(cls, type) and issubclass(cls, WBModel) and cls is not WBModel:
                found.append((module.name, name, cls))
    return found


METHODS = all_methods()
MODELS = all_models()


def test_client_exposes_every_section() -> None:
    sections = {module.name for module in pkgutil.iter_modules(resources.__path__)}
    api = WBApi(token="t")
    missing = {name for name in sections if not hasattr(api, name)}
    assert not missing


def test_methods_were_generated() -> None:
    assert len(METHODS) > 250


@pytest.mark.parametrize(("section", "name", "cls"), METHODS, ids=lambda x: getattr(x, "__name__", x))
def test_method_declares_path_and_verb(section: str, name: str, cls: type[WBMethod]) -> None:
    assert cls.__path__.startswith("/")
    assert cls.__http_method__ in {"GET", "POST", "PUT", "PATCH", "DELETE"}


@pytest.mark.parametrize(("section", "name", "cls"), METHODS, ids=lambda x: getattr(x, "__name__", x))
def test_method_host_is_wildberries(section: str, name: str, cls: type[WBMethod]) -> None:
    host = getattr(cls, "__host__", "")
    assert host.startswith("https://")
    assert host.endswith("wildberries.ru")


def test_path_placeholders_are_declared() -> None:
    problems = []
    for section, name, _cls in METHODS:
        declared = set(getattr(_cls, "__path_params__", ()))
        in_path = set(re.findall(r"\{(\w+)\}", _cls.__path__))
        if in_path - declared:
            problems.append(f"{section}.{name}: {in_path - declared}")
    assert not problems


def test_rate_limits_are_positive() -> None:
    problems = []
    for section, name, cls in METHODS:
        for kind, (interval, burst) in getattr(cls, "__rate_limits__", {}).items():
            if interval <= 0 or burst <= 0:
                problems.append(f"{section}.{name}[{kind}]")
    assert not problems


def test_pagination_scheme_is_implemented() -> None:
    problems = []
    for section, name, cls in METHODS:
        scheme = getattr(cls, "__paginate__", None)
        if scheme and not hasattr(WBMethod, f"_walk_{scheme}"):
            problems.append(f"{section}.{name}: {scheme}")
    assert not problems


def test_scopes_are_known() -> None:
    for _section, _name, cls in METHODS:
        scope = getattr(cls, "__scope__", None)
        assert scope is None or isinstance(scope, Scope)


def test_sandbox_hosts_look_right() -> None:
    for _section, _name, cls in METHODS:
        host = getattr(cls, "__sandbox_host__", "")
        if host:
            assert "sandbox" in host
            assert host.startswith("https://")


def test_models_were_generated() -> None:
    assert len(MODELS) > 500


def test_models_convert_to_dict() -> None:
    for _section, _name, cls in MODELS[:200]:
        instance = cls()
        assert isinstance(instance.to_dict(), dict)
        assert isinstance(instance.to_dict(by_alias=True), dict)


def test_model_round_trip() -> None:
    from wbapi.resources.orders_fbs.models import OrdersNewResponse

    source = {"orders": [{"id": 1, "nmId": 55, "salePrice": 100}]}
    parsed = msgspec.convert(source, OrdersNewResponse, strict=False)
    assert parsed.to_dict(by_alias=True)["orders"][0]["nmId"] == 55
    assert parsed.orders[0].nm_id == 55


def test_facade_methods_match_classes() -> None:
    """Every method class must be exposed on its section facade."""
    api = WBApi(token="t")
    problems = []
    for section, name, _cls in METHODS:
        facade = getattr(api, section)
        expected = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name).lower()
        if not hasattr(facade, expected):
            problems.append(f"{section}.{expected}")
    assert not problems, problems[:5]


def test_paginated_methods_have_iterators() -> None:
    api = WBApi(token="t")
    problems = []
    for section, name, cls in METHODS:
        if not getattr(cls, "__paginate__", None):
            continue
        base = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name).lower()
        if not hasattr(getattr(api, section), f"iter_{base}"):
            problems.append(f"{section}.iter_{base}")
    assert not problems, problems[:5]
