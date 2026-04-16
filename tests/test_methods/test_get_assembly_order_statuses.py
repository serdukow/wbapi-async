import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AssemblyOrderStatusesItem


@pytest.mark.unit
class TestGetAssemblyOrderStatuses:
    async def test_get_assembly_order_statuses(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "errors": [{"code": 404, "detail": "NotFound"}],
                        "orderId": 123456,
                        "supplierStatus": "deliver",
                        "wbStatus": "waiting",
                    }
                ]
            }
        )

        result = await api.get_assembly_order_statuses()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrderStatusesItem)
        assert result[0].order_id == 123456
        assert result[0].supplier_status == "deliver"
        assert result[0].wb_status == "waiting"
