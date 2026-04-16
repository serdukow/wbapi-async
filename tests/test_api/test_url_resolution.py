import pytest

from wbapi_async.exceptions import WbAPIError
from wbapi_async.method import resolve_url


@pytest.mark.unit
class TestResolveUrl:
    """Tests for URL resolution from spec paths."""
    def test_exact_path_match(self) -> None:
        url = resolve_url("/api/v3/supplies")
        assert url == "https://marketplace-api.wildberries.ru/api/v3/supplies"

    def test_exact_path_different_subdomain(self) -> None:
        url = resolve_url("/api/v1/feedbacks")
        assert url == "https://feedbacks-api.wildberries.ru/api/v1/feedbacks"

    def test_dynamic_path_resolves_via_prefix(self) -> None:
        url = resolve_url("/api/v3/supplies/WB-GI-123456/orders")
        assert url == "https://marketplace-api.wildberries.ru/api/v3/supplies/WB-GI-123456/orders"

    def test_dynamic_path_with_numeric_id(self) -> None:
        url = resolve_url("/api/v3/orders/13833711/cancel")
        assert url == "https://marketplace-api.wildberries.ru/api/v3/orders/13833711/cancel"

    def test_unknown_path_raises_wbapi_error(self) -> None:
        with pytest.raises(WbAPIError):
            resolve_url("/api/v99/nonexistent/endpoint")
