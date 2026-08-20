"""URL resolution, the endpoint table's integrity, and rate-limit lookup."""

from __future__ import annotations

from urllib.parse import urlparse

import pytest

from wbapi.endpoints import (
    DEFAULT_PAGE_SIZE,
    DEFAULT_RATE_LIMIT,
    ENDPOINTS,
    PAGE_SIZES,
    PUBLIC_HOSTS,
    _match_template,
    page_size_for,
    rate_limit_for,
    resolve_url,
)
from wbapi.exceptions import WBConfigurationError


def test_known_path_resolves_to_its_host() -> None:
    assert resolve_url("/api/v3/supplies").startswith("https://marketplace-api.wildberries.ru")


def test_dynamic_segment_inherits_parent_host() -> None:
    assert resolve_url("/api/v3/supplies/WB-GI-123").startswith("https://marketplace-api.wildberries.ru")


def test_full_url_on_known_host_passes_through() -> None:
    url = "https://content-api.wildberries.ru/content/v3/brand-new"
    assert resolve_url(url) == url


def test_unknown_path_with_full_url_is_allowed() -> None:
    """New endpoints must be reachable before the table is regenerated."""
    url = "https://seller-analytics-api.wildberries.ru/api/v9/does-not-exist-yet"
    assert resolve_url(url) == url


def test_unknown_host_is_rejected() -> None:
    with pytest.raises(WBConfigurationError, match="unknown host"):
        resolve_url("https://evil.example.com/api")


def test_unknown_path_suggests_full_url() -> None:
    with pytest.raises(WBConfigurationError, match="full URL"):
        resolve_url("/totally/unknown/path")


def test_relative_path_must_start_with_slash() -> None:
    with pytest.raises(WBConfigurationError, match="must start with"):
        resolve_url("api/v3/supplies")


def test_public_host_is_known() -> None:
    for host in PUBLIC_HOSTS:
        assert resolve_url(f"https://{host}/anything")


def test_rate_limit_known_path() -> None:
    interval, burst = rate_limit_for("/api/v3/supplies")
    assert interval > 0 and burst > 0


def test_rate_limit_falls_back_for_unknown() -> None:
    assert rate_limit_for("/no/such/path") == DEFAULT_RATE_LIMIT


@pytest.mark.parametrize(
    ("concrete", "template"),
    [
        ("/api/v3/orders/13833711/cancel", "/api/v3/orders/{orderId}/cancel"),
        ("/api/v3/orders/13833711/meta", "/api/v3/orders/{orderId}/meta"),
        ("/api/v3/supplies/WB-GI-123/trbx", "/api/v3/supplies/{supplyId}/trbx"),
        ("/content/v2/tag/99", "/content/v2/tag/{id}"),
    ],
)
def test_concrete_path_matches_its_template(concrete: str, template: str) -> None:
    """Interpolated ids must keep the endpoint's own quota, not the parent's."""
    assert _match_template(concrete) == template
    assert rate_limit_for(concrete) == rate_limit_for(template)


def test_template_match_resolves_host() -> None:
    assert resolve_url("/api/v3/orders/13833711/cancel").startswith("https://marketplace-api.wildberries.ru")


def test_wrong_segment_count_does_not_match() -> None:
    assert _match_template("/api/v3/orders/123/cancel/extra") is None


def test_literal_segments_must_match_exactly() -> None:
    assert _match_template("/api/v3/orders/123/nonsense") is None


def test_unknown_path_has_no_template() -> None:
    assert _match_template("/totally/unknown/thing") is None


def test_page_size_follows_template() -> None:
    assert page_size_for("/api/v3/supplies/WB-1/trbx") == DEFAULT_PAGE_SIZE


def test_page_size_lookup() -> None:
    assert page_size_for("/content/v2/get/cards/list") == 100
    assert page_size_for("/api/v3/supplies") == DEFAULT_PAGE_SIZE


def test_every_host_is_https_wildberries() -> None:
    for host in ENDPOINTS:
        parsed = urlparse(host)
        assert parsed.scheme == "https"
        assert parsed.netloc.endswith("wildberries.ru"), host


def test_every_path_starts_with_slash() -> None:
    for paths in ENDPOINTS.values():
        for path in paths:
            assert path.startswith("/"), path


def test_every_rate_limit_is_positive() -> None:
    for paths in ENDPOINTS.values():
        for path, (interval, burst) in paths.items():
            assert interval > 0, path
            assert burst > 0, path


def test_no_path_is_served_by_two_hosts() -> None:
    seen: dict[str, str] = {}
    for host, paths in ENDPOINTS.items():
        for path in paths:
            assert path not in seen, f"{path} in both {seen.get(path)} and {host}"
            seen[path] = host


def test_page_size_paths_are_resolvable() -> None:
    for path in PAGE_SIZES:
        assert resolve_url(path).startswith("https://")
