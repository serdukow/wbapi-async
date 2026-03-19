import pytest
from pytest_httpx import HTTPXMock

from wbapi_async.client.session.base import BaseSession
from wbapi_async.exceptions import WbAPIError


@pytest.mark.unit
class TestBaseSession:

    async def test_error_raises_on_4xx(self, session: BaseSession, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            status_code=401,
            json={"error": True, "errorText": "Unauthorized"},
        )

        with pytest.raises(WbAPIError) as exc_info:
            await session.get("https://common-api.wildberries.ru/ping")

        assert exc_info.value.http_status == 401
        assert exc_info.value.error.error_text == "Unauthorized"

    async def test_error_raises_on_5xx(self, session: BaseSession, httpx_mock: HTTPXMock) -> None:
        httpx_mock.add_response(
            status_code=500,
            json={"error": True, "errorText": "Internal Server Error"},
        )

        with pytest.raises(WbAPIError) as exc_info:
            await session.get("https://common-api.wildberries.ru/ping")

        assert exc_info.value.http_status == 500
