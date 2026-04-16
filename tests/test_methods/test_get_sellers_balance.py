import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SellersBalanceResponse


@pytest.mark.unit
class TestGetSellersBalance:
    async def test_get_sellers_balance(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "currency": "RUB",
                    "current": 10196.21,
                    "for_withdraw": 6395.8,
                }
            ]
        )

        result = await api.get_sellers_balance()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SellersBalanceResponse)
        assert result[0].currency == "RUB"
        assert result[0].current == 10196.21
        assert result[0].for_withdraw == 6395.8
