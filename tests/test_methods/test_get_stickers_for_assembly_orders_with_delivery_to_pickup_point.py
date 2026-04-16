import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import StickersForAssemblyOrdersWithDeliveryToPickupPointItem


@pytest.mark.unit
class TestGetStickersForAssemblyOrdersWithDeliveryToPickupPoint:
    async def test_get_stickers_for_assembly_orders_with_delivery_to_pickup_point(
        self, api: MockedAPI
    ) -> None:
        api.add_response(
            {
                "stickers": [
                    {
                        "orderId": 5346346,
                        "partA": "231648",
                        "partB": "9753",
                        "barcode": "!uKEtQZVx",
                        "file": "JVBER...ZWYKMTM5MQolJUVPRg==",
                    }
                ]
            }
        )

        result = await api.get_stickers_for_assembly_orders_with_delivery_to_pickup_point(
            type_="type_", width=1, height=1, orders=[]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], StickersForAssemblyOrdersWithDeliveryToPickupPointItem)
        assert result[0].order_id == 5346346
        assert result[0].part_a == "231648"
        assert result[0].part_b == "9753"
        assert result[0].barcode == "!uKEtQZVx"
        assert result[0].file == "JVBER...ZWYKMTM5MQolJUVPRg=="
