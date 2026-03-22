import pytest

from wbapi_async.types.stickers_for_crossborder_assembly_orders_item import StickersForCrossborderAssemblyOrdersItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetStickersForCrossborderAssemblyOrders:

    async def test_get_stickers_for_crossborder_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "stickers": [{
                "file": "file",
                "orderId": 1,
                "parcelId": "parcelId",
            }]
        }
        )

        result = await api.get_stickers_for_crossborder_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], StickersForCrossborderAssemblyOrdersItem)
        assert result[0].file == "file"
        assert result[0].order_id == 1
        assert result[0].parcel_id == "parcelId"
