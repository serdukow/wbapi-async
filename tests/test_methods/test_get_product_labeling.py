import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductLabelingItem


@pytest.mark.unit
class TestGetProductLabeling:
    async def test_get_product_labeling(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "report": [
                    {
                        "amount": 1.0,
                        "date": "date",
                        "incomeId": 1,
                        "nmID": 1,
                        "photoUrls": [],
                        "shkID": 1,
                        "sku": "sku",
                    }
                ]
            }
        )

        result = await api.get_product_labeling(date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductLabelingItem)
        assert result[0].amount == 1.0
        assert result[0].date == "date"
        assert result[0].income_id == 1
        assert result[0].nm_id == 1
