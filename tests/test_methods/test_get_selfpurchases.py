import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SelfpurchasesItem


@pytest.mark.unit
class TestGetSelfpurchases:
    async def test_get_selfpurchases(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "details": [
                    {
                        "nmID": 123456789,
                        "sum": 3540,
                        "currency": "RUB",
                        "dateFrom": "2023-08-23",
                        "dateTo": "2023-08-29",
                    }
                ]
            }
        )

        result = await api.get_selfpurchases()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SelfpurchasesItem)
        assert result[0].nm_id == 123456789
        assert result[0].sum_ == 3540
        assert result[0].currency == "RUB"
        assert result[0].date_from == "2023-08-23"
        assert result[0].date_to == "2023-08-29"
