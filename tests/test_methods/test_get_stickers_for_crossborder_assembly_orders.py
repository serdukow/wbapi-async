import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import StickersForCrossborderAssemblyOrdersItem


@pytest.mark.unit
class TestGetStickersForCrossborderAssemblyOrders:
    async def test_get_stickers_for_crossborder_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "stickers": [
                    {
                        "orderId": 1,
                        "status": "status",
                        "parcelId": "parcelId",
                        "file": "file",
                        "partA": "partA",
                        "partB": "partB",
                        "barcode": "barcode",
                    }
                ]
            }
        )

        result = await api.get_stickers_for_crossborder_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], StickersForCrossborderAssemblyOrdersItem)
        assert result[0].order_id == 1
        assert result[0].status == "status"
        assert result[0].parcel_id == "parcelId"
