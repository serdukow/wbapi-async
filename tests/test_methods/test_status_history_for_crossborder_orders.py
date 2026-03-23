import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import StatusHistoryForCrossborderOrdersItem


@pytest.mark.unit
class TestStatusHistoryForCrossborderOrders:
    async def test_status_history_for_crossborder_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "deliveryDate": "deliveryDate",
                        "statuses": [],
                        "orderID": 1,
                    }
                ]
            }
        )

        result = await api.status_history_for_crossborder_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], StatusHistoryForCrossborderOrdersItem)
        assert result[0].delivery_date == "deliveryDate"
        assert result[0].statuses == []
        assert result[0].order_id == 1
