import pytest

from wbapi_async.types.get_products_with_prices_by_articles_item import GetProductsWithPricesByArticlesItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetProductsWithPricesByArticles:

    async def test_get_products_with_prices_by_articles(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "listGoods": [{
                "nmID": 1,
                "vendorCode": "vendorCode",
                "sizes": [],
                "currencyIsoCode4217": "currencyIsoCode4217",
                "discount": 1,
                "clubDiscount": 1,
                "editableSizePrice": True,
                "isBadTurnover": True,
            }]
        }
        }
        )

        result = await api.get_products_with_prices_by_articles(nm_list=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GetProductsWithPricesByArticlesItem)
        assert result[0].nm_id == 1
        assert result[0].vendor_code == "vendorCode"
        assert result[0].sizes == []
