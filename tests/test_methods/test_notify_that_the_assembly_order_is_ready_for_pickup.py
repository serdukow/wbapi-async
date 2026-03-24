import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestNotifyThatTheAssemblyOrderIsReadyForPickup:
    async def test_notify_that_the_assembly_order_is_ready_for_pickup(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.notify_that_the_assembly_order_is_ready_for_pickup(order_id=1)

        assert result is None
