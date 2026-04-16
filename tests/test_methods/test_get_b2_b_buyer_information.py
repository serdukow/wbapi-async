import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import B2BBuyerInformationItem


@pytest.mark.unit
class TestGetB2BBuyerInformation:
    async def test_get_b2b_buyer_information(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "results": [
                    {
                        "data": {"inn": "inn", "kpp": "kpp", "orgName": "orgName"},
                        "errors": [{"code": 1, "detail": "detail"}],
                        "isError": True,
                        "orderId": 123456,
                    }
                ]
            }
        )

        result = await api.get_b2b_buyer_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], B2BBuyerInformationItem)
        assert result[0].is_error
        assert result[0].order_id == 123456
