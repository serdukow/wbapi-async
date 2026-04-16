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
                            "nmID": 206025152,
                            "sizeID": 1,
                            "techSizeName": "",
                            "currencyIsoCode4217": "RUB",
                            "newPrice": 134,
                            "oldPrice": 4000,
                            "newDiscount": 25,
                            "oldDiscount": 25,
                            "priceDiff": -2899.5,
                        }
                    ]
                }
            }
        )

        result = await api.get_products_in_quarantine(limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductsInQuarantineItem)
        assert result[0].nm_id == 206025152
        assert result[0].size_id == 1
        assert result[0].tech_size_name == ""
        assert result[0].currency_iso_code4217 == "RUB"
        assert result[0].new_price == 134
