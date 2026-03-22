import pytest

from wbapi_async.types.stickers_for_assembly_orders_with_delivery_to_pickup_point_item import StickersForAssemblyOrdersWithDeliveryToPickupPointItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetStickersForAssemblyOrdersWithDeliveryToPickupPoint:

    async def test_get_stickers_for_assembly_orders_with_delivery_to_pickup_point(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "stickers": [{
                "orderId": 1,
                "partA": "partA",
                "partB": "partB",
                "barcode": "barcode",
                "file": "file",
            }]
        }
        )

        result = await api.get_stickers_for_assembly_orders_with_delivery_to_pickup_point(type="type", width=1, height=1, orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], StickersForAssemblyOrdersWithDeliveryToPickupPointItem)
        assert result[0].order_id == 1
        assert result[0].part_a == "partA"
        assert result[0].part_b == "partB"
