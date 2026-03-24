import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import BalanceItem


@pytest.mark.unit
class TestGetBalance:
    async def test_get_balance(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "cashbacks": [
                    {
                        "sum": 1,
                        "percent": 1,
                        "expiration_date": "expiration_date",
                    }
                ]
            }
        )

        result = await api.get_balance()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BalanceItem)
        assert result[0].sum_ == 1
        assert result[0].percent == 1
        assert result[0].expiration_date == "expiration_date"
