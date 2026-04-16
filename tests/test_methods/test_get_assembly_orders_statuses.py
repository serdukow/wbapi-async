import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AssemblyOrdersStatusesItem


@pytest.mark.unit
class TestGetAssemblyOrdersStatuses:
    async def test_get_assembly_orders_statuses(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "id": 5632423,
                        "supplierStatus": "new",
                        "wbStatus": "waiting",
                    }
                ]
            }
        )

        result = await api.get_assembly_orders_statuses(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrdersStatusesItem)
        assert result[0].id_ == 5632423
        assert result[0].supplier_status == "new"
        assert result[0].wb_status == "waiting"
