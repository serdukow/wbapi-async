import pytest

from wbapi_async.types.assembly_orders_item import AssemblyOrdersItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetAssemblyOrders:

    async def test_get_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "address": {},
                "scanPrice": 1.0,
                "deliveryType": "deliveryType",
                "supplyId": "supplyId",
                "orderUid": "orderUid",
                "article": "article",
                "colorCode": "colorCode",
                "rid": "rid",
                "createdAt": "createdAt",
                "offices": [],
                "skus": [],
                "id": 1,
                "warehouseId": 1,
                "officeId": 1,
                "nmId": 1,
                "chrtId": 1,
                "price": 1,
                "convertedPrice": 1,
                "currencyCode": 1,
                "convertedCurrencyCode": 1,
                "cargoType": 1,
                "crossBorderType": 1,
                "comment": "comment",
                "isZeroOrder": True,
                "options": {},
            }]
        }
        )

        result = await api.get_assembly_orders(limit=1, next=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrdersItem)
        assert result[0].address == {}
        assert result[0].scan_price == 1.0
        assert result[0].delivery_type == "deliveryType"
