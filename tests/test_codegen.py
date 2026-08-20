"""The endpoint generator: spec parsing, merge behaviour and rendering."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
from typing import Any

import pytest


def _load_generator() -> Any:
    path = Path(__file__).resolve().parent.parent / "scripts" / "generate_endpoints.py"
    spec = importlib.util.spec_from_file_location("generate_endpoints", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["generate_endpoints"] = module
    spec.loader.exec_module(module)
    return module


gen = _load_generator()

MARKETPLACE = "https://marketplace-api.wildberries.ru"
CONTENT = "https://content-api.wildberries.ru"


def _spec(host: str, paths: dict[str, Any]) -> dict[str, Any]:
    return {"servers": [{"url": host}], "paths": paths}


def test_collect_reads_paths_and_host() -> None:
    found = gen._collect([_spec(MARKETPLACE, {"/api/v3/supplies": {"get": {}}})])
    assert found["/api/v3/supplies"].host == MARKETPLACE


def test_collect_uses_default_rate_limit() -> None:
    found = gen._collect([_spec(MARKETPLACE, {"/api/v3/x": {"get": {}}})])
    endpoint = found["/api/v3/x"]
    assert endpoint.interval_ms == gen.DEFAULT_INTERVAL_MS
    assert endpoint.burst == gen.DEFAULT_BURST


def test_collect_reads_rate_limit_extensions() -> None:
    spec = _spec(
        MARKETPLACE,
        {"/api/v3/x": {"get": {"x-rate-limit-burst": 20, "x-rate-limit-interval": 200}}},
    )
    endpoint = gen._collect([spec])["/api/v3/x"]
    assert (endpoint.interval_ms, endpoint.burst) == (200, 20)


def test_collect_skips_specs_without_servers() -> None:
    assert gen._collect([{"paths": {"/api/v3/x": {"get": {}}}}]) == {}


def test_collect_skips_non_path_keys() -> None:
    found = gen._collect([_spec(MARKETPLACE, {"not-a-path": {"get": {}}})])
    assert found == {}


def test_render_groups_by_host() -> None:
    endpoints = {
        "/api/v3/a": gen.Endpoint("/api/v3/a", MARKETPLACE, 200, 20),
        "/content/v2/b": gen.Endpoint("/content/v2/b", CONTENT, 600, 5),
    }
    block = gen._render(endpoints, deprecated=set())
    assert f'"{MARKETPLACE}": {{' in block
    assert f'"{CONTENT}": {{' in block
    assert '"/api/v3/a": (200, 20),' in block


def test_render_marks_deprecated() -> None:
    endpoints = {"/api/v3/gone": gen.Endpoint("/api/v3/gone", MARKETPLACE, 200, 20)}
    block = gen._render(endpoints, deprecated={"/api/v3/gone"})
    assert "# deprecated" in block


def test_render_output_is_valid_python() -> None:
    endpoints = {"/api/v3/a": gen.Endpoint("/api/v3/a", MARKETPLACE, 200, 20)}
    block = gen._render(endpoints, deprecated=set())
    namespace: dict[str, Any] = {}
    exec(compile(block, "<generated>", "exec"), namespace)
    assert namespace["ENDPOINTS"][MARKETPLACE]["/api/v3/a"] == (200, 20)


def test_parse_existing_round_trips_render() -> None:
    endpoints = {
        "/api/v3/a": gen.Endpoint("/api/v3/a", MARKETPLACE, 200, 20),
        "/content/v2/b": gen.Endpoint("/content/v2/b", CONTENT, 600, 5),
    }
    parsed = gen._parse_existing(gen._render(endpoints, deprecated=set()))
    assert parsed == endpoints


def test_parse_existing_reads_the_shipped_table() -> None:
    """The real endpoints.py must stay parseable, or removals would be lost."""
    parsed = gen._parse_existing(gen.TARGET.read_text())
    assert len(parsed) > 200
    assert all(path.startswith("/") for path in parsed)


def test_removed_paths_are_preserved_as_deprecated() -> None:
    """A path vanishing from the spec must keep working for existing callers."""
    existing = {"/api/v3/old": gen.Endpoint("/api/v3/old", MARKETPLACE, 200, 20)}
    found = {"/api/v3/new": gen.Endpoint("/api/v3/new", MARKETPLACE, 200, 20)}

    deprecated = set(existing) - set(found)
    merged = {**{p: existing[p] for p in deprecated}, **found}

    assert "/api/v3/old" in merged
    block = gen._render(merged, deprecated)
    assert "/api/v3/old" in block and "# deprecated" in block


def test_servers_ignores_non_https() -> None:
    assert gen._servers({"servers": [{"url": "http://insecure.example"}]}) == []


@pytest.mark.parametrize("spec", [{}, {"servers": []}, {"servers": [{}]}])
def test_servers_handles_malformed_input(spec: dict[str, Any]) -> None:
    assert gen._servers(spec) == []
