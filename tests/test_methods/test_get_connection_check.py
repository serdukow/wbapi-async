import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ConnectionCheckResponse


@pytest.mark.unit
class TestGetConnectionCheck:
    async def test_get_connection_check(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "TS": "TS",
                    "Status": "OK",
                }
            ]
        )

        result = await api.get_connection_check()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ConnectionCheckResponse)
        assert result[0].ts == "TS"
        assert result[0].status == "OK"
