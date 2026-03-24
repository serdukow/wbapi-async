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
                        "errors": [],
                        "orderId": 1,
                        "supplierStatus": "supplierStatus",
                        "wbStatus": "wbStatus",
                    }
                ]
            }
        )

        result = await api.get_assembly_order_statuses()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrderStatusesItem)
        assert result[0].errors == []
        assert result[0].order_id == 1
        assert result[0].supplier_status == "supplierStatus"
