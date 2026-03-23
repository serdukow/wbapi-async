import pytest

from wbapi_async.types import NotifyThatTheAssemblyOrdersAreReadyForPickupItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestNotifyThatTheAssemblyOrdersAreReadyForPickup:

    async def test_notify_that_the_assembly_orders_are_ready_for_pickup(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "results": [{
                "orderId": 1,
                "isError": True,
                "errors": [],
            }]
        }
        )

        result = await api.notify_that_the_assembly_orders_are_ready_for_pickup()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NotifyThatTheAssemblyOrdersAreReadyForPickupItem)
        assert result[0].order_id == 1
        assert result[0].is_error == True
        assert result[0].errors == []
