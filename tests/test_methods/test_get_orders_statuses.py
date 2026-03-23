import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import OrdersStatusesItem


@pytest.mark.unit
class TestGetOrdersStatuses:
    async def test_get_orders_statuses(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "id": 1,
                        "supplierStatus": "supplierStatus",
                        "wbStatus": "wbStatus",
                    }
                ]
            }
        )

        result = await api.get_orders_statuses(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdersStatusesItem)
        assert result[0].id == 1
        assert result[0].supplier_status == "supplierStatus"
        assert result[0].wb_status == "wbStatus"
