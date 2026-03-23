import pytest

from wbapi_async.types import AllAssemblyOrdersForReshipmentItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetAllAssemblyOrdersForReshipment:

    async def test_get_all_assembly_orders_for_reshipment(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "supplyID": None,
                "orderID": None,
            }]
        }
        )

        result = await api.get_all_assembly_orders_for_reshipment()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AllAssemblyOrdersForReshipmentItem)
