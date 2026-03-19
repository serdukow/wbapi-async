import pytest

from wbapi_async.types import ProductWithPrice, Size

from tests.mocked_api import MockedAPI


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
                            "sizes": [
                                {
                                    "sizeID": 3123515574,
                                    "price": 500,
                                    "discountedPrice": 350,
                                    "clubDiscountedPrice": 332.5,
                                    "techSizeName": "42",
                                }
                            ],
                            "currencyIsoCode4217": "RUB",
                            "discount": 30,
                            "clubDiscount": 5,
                            "editableSizePrice": True,
                            "isBadTurnover": True,
                        }
                    ]
                },
                "error": False,
                "errorText": "",
            }
        )

        result = await api.get_products_with_prices()

        assert isinstance(result, list)
        assert len(result) == 1

        product = result[0]
        assert isinstance(product, ProductWithPrice)
        assert product.nm_id == 98486
        assert product.vendor_code == "07326060"
        assert product.currency_iso_code_4217 == "RUB"
        assert product.discount == 30
        assert product.club_discount == 5
        assert product.editable_size_price is True
        assert product.is_bad_turnover is True

        assert product.sizes is not None
        size = product.sizes[0]
        assert isinstance(size, Size)
        assert size.size_id == 3123515574
        assert size.price == 500
        assert size.discounted_price == 350.0
        assert size.club_discounted_price == 332.5
        assert size.tech_size_name == "42"
