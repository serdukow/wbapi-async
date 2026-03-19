import pytest

from wbapi_async.exceptions import WbAPIError
from wbapi_async.types import ConnectionCheck

from tests.mocked_api import MockedAPI


@pytest.mark.unit
async def test_connection_check_returns_model(api: MockedAPI) -> None:
    api.add_response({"Status": "OK", "TS": "2025-01-01T00:00:00Z"})

    result = await api.connection_check()

    assert isinstance(result, ConnectionCheck)
    assert result.status == "OK"
    assert result.ts is not None


@pytest.mark.unit
async def test_connection_check_request_url(api: MockedAPI) -> None:
    api.add_response({"Status": "OK", "TS": "2025-01-01T00:00:00Z"})

    await api.connection_check()

    req = api.get_last_request()
    assert req.url == "https://common-api.test.api.com/ping"
    assert req.method == "GET"


@pytest.mark.unit
async def test_connection_check_sets_authorization_header(api: MockedAPI) -> None:
    api.add_response({"Status": "OK", "TS": "2025-01-01T00:00:00Z"})

    await api.connection_check()

    assert api.session.headers.authorization == f"Bearer {api._token}"


@pytest.mark.unit
async def test_connection_check_error_raises(api: MockedAPI) -> None:
    api.add_response({"errorText": "Unauthorized", "error": True}, status=401)

    with pytest.raises(WbAPIError) as exc_info:
        await api.connection_check()

    assert exc_info.value.http_status == 401
    assert exc_info.value.error.error_text == "Unauthorized"
