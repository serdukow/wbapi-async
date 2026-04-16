import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DocumentResponse


@pytest.mark.unit
class TestGetDocument:
    async def test_get_document(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {"freeLimits": 1, "paidLimits": 1},
                }
            ]
        )

        result = await api.get_document(service_name="service_name", extension="extension")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DocumentResponse)
