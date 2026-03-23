import pytest

from wbapi_async.types import AssemblyOrdersStatusesItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetAssemblyOrdersStatuses:

    async def test_get_assembly_orders_statuses(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "id": 1,
                "supplierStatus": "supplierStatus",
                "wbStatus": "wbStatus",
            }]
        }
        )

        result = await api.get_assembly_orders_statuses(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrdersStatusesItem)
        assert result[0].id_ == 1
        assert result[0].supplier_status == "supplierStatus"
        assert result[0].wb_status == "wbStatus"
