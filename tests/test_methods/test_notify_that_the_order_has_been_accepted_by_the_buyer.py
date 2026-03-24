import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestNotifyThatTheOrderHasBeenAcceptedByTheBuyer:
    async def test_notify_that_the_order_has_been_accepted_by_the_buyer(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.notify_that_the_order_has_been_accepted_by_the_buyer(order_id=1)

        assert result is None
