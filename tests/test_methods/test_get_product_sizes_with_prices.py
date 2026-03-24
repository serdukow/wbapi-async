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
                            "nmID": 1,
                            "sizeID": 1,
                            "vendorCode": "vendorCode",
                            "price": 1,
                            "currencyIsoCode4217": "currencyIsoCode4217",
                            "discountedPrice": 1.0,
                            "clubDiscountedPrice": 1.0,
                            "discount": 1,
                            "clubDiscount": 1,
                            "techSizeName": "techSizeName",
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
        assert result[0].nm_id == 1
        assert result[0].size_id == 1
        assert result[0].vendor_code == "vendorCode"
