import pytest

from wbapi_async.types import SellersBalanceResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSellersBalance:

    async def test_get_sellers_balance(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "currency": "currency",
                "current": 1.0,
                "for_withdraw": 1.0,
            }]
        )

        result = await api.get_sellers_balance()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SellersBalanceResponse)
        assert result[0].currency == "currency"
        assert result[0].current == 1.0
        assert result[0].for_withdraw == 1.0
