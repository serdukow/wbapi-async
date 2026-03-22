import pytest

from wbapi_async.types.new_orders_item import NewOrdersItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetNewOrders:

    async def test_get_new_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "address": {},
                "salePrice": 1,
                "requiredMeta": [],
                "comment": "comment",
                "options": {},
                "orderUid": "orderUid",
                "groupId": "groupId",
                "article": "article",
                "colorCode": "colorCode",
                "rid": "rid",
                "createdAt": "createdAt",
                "skus": [],
                "id": 1,
                "warehouseId": 1,
                "nmId": 1,
                "chrtId": 1,
                "price": 1,
                "convertedPrice": 1,
                "currencyCode": 1,
                "convertedCurrencyCode": 1,
                "cargoType": 1,
                "isZeroOrder": True,
            }]
        }
        )

        result = await api.get_new_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NewOrdersItem)
        assert result[0].address == {}
        assert result[0].sale_price == 1
        assert result[0].required_meta == []
