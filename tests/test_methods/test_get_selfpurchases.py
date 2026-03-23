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
                        "nmID": 1,
                        "sum": 1,
                        "currency": "currency",
                        "dateFrom": "dateFrom",
                        "dateTo": "dateTo",
                    }
                ]
            }
        )

        result = await api.get_selfpurchases()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SelfpurchasesItem)
        assert result[0].nm_id == 1
        assert result[0].sum == 1
        assert result[0].currency == "currency"
