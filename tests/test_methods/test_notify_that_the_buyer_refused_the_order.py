import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestNotifyThatTheBuyerRefusedTheOrder:
    async def test_notify_that_the_buyer_refused_the_order(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.notify_that_the_buyer_refused_the_order(order_id=1)

        assert result is None
