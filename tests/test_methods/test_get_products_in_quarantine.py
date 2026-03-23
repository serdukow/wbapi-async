import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductsInQuarantineItem


@pytest.mark.unit
class TestGetProductsInQuarantine:
    async def test_get_products_in_quarantine(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "quarantineGoods": [
                        {
                            "nmID": 1,
                            "sizeID": 1,
                            "techSizeName": "techSizeName",
                            "currencyIsoCode4217": "currencyIsoCode4217",
                            "newPrice": 1.0,
                            "oldPrice": 1.0,
                            "newDiscount": 1,
                            "oldDiscount": 1,
                            "priceDiff": 1.0,
                        }
                    ]
                }
            }
        )

        result = await api.get_products_in_quarantine(limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductsInQuarantineItem)
        assert result[0].nm_id == 1
        assert result[0].size_id == 1
        assert result[0].tech_size_name == "techSizeName"
