import pytest

from wbapi_async.types import NewOrdersListItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetNewOrdersList:

    async def test_get_new_orders_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "salePrice": 1,
                "requiredMeta": [],
                "comment": "comment",
                "options": {},
                "address": {},
                "orderUid": "orderUid",
                "groupId": "groupId",
                "article": "article",
                "colorCode": "colorCode",
                "rid": "rid",
                "createdAt": "createdAt",
                "deliveryType": "deliveryType",
                "skus": [],
                "id": 1,
                "warehouseId": 1,
                "nmId": 1,
                "chrtId": 1,
                "price": 1,
                "finalPrice": 1,
                "convertedFinalPrice": 1,
                "convertedPrice": 1,
                "currencyCode": 1,
                "convertedCurrencyCode": 1,
                "cargoType": 1,
                "isZeroOrder": True,
                "wbStickerId": 1,
            }]
        }
        )

        result = await api.get_new_orders_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NewOrdersListItem)
        assert result[0].sale_price == 1
        assert result[0].required_meta == []
        assert result[0].comment == "comment"
