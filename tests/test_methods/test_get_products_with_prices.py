import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductsWithPricesItem


@pytest.mark.unit
class TestGetProductsWithPrices:
    async def test_get_products_with_prices(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "listGoods": [
                        {
                            "nmID": 98486,
                            "vendorCode": "07326060",
                            "sizes": [{"chrtID": 1, "techSize": "techSize", "wbSize": "wbSize", "skus": []}],
                            "currencyIsoCode4217": "RUB",
                            "discount": 30,
                            "clubDiscount": 5,
                            "editableSizePrice": True,
                            "isBadTurnover": True,
                        }
                    ]
                }
            }
        )

        result = await api.get_products_with_prices(limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductsWithPricesItem)
        assert result[0].nm_id == 98486
        assert result[0].vendor_code == "07326060"
        assert result[0].currency_iso_code4217 == "RUB"
        assert result[0].discount == 30
