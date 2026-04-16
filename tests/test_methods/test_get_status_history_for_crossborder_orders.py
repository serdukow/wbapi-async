import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import StatusHistoryForCrossborderOrdersItem


@pytest.mark.unit
class TestGetStatusHistoryForCrossborderOrders:
    async def test_get_status_history_for_crossborder_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "deliveryDate": "deliveryDate",
                        "statuses": [{"date": "date", "code": "SORTED"}],
                        "orderID": 123456789,
                    }
                ]
            }
        )

        result = await api.get_status_history_for_crossborder_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], StatusHistoryForCrossborderOrdersItem)
        assert result[0].delivery_date == "deliveryDate"
        assert result[0].order_id == 123456789
