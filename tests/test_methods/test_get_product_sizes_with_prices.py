import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductSizesWithPricesItem


@pytest.mark.unit
class TestGetProductSizesWithPrices:
    async def test_get_product_sizes_with_prices(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "listGoods": [
                        {
                            "nmID": 123,
                            "sizeID": 98989887,
                            "vendorCode": "34552332",
                            "price": 1000,
                            "currencyIsoCode4217": "RUB",
                            "discountedPrice": 700,
                            "clubDiscountedPrice": 665,
                            "discount": 30,
                            "clubDiscount": 5,
                            "techSizeName": "42",
                            "editableSizePrice": True,
                            "isBadTurnover": True,
                        }
                    ]
                }
            }
        )

        result = await api.get_product_sizes_with_prices(limit=1, nm_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductSizesWithPricesItem)
        assert result[0].nm_id == 123
        assert result[0].size_id == 98989887
        assert result[0].vendor_code == "34552332"
        assert result[0].price == 1000
        assert result[0].currency_iso_code4217 == "RUB"
