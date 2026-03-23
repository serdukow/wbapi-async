import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestNotifyThatTheBuyerHasDeclinedTheOrder:

    async def test_notify_that_the_buyer_has_declined_the_order(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.notify_that_the_buyer_has_declined_the_order(order_id=1)

        assert result is None
