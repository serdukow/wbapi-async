import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import NotifyThatTheOrdersAreDeclinedItem


@pytest.mark.unit
class TestNotifyThatTheOrdersAreDeclined:
    async def test_notify_that_the_orders_are_declined(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "results": [
                    {
                        "errors": [],
                        "isError": True,
                        "orderId": 1,
                    }
                ]
            }
        )

        result = await api.notify_that_the_orders_are_declined(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NotifyThatTheOrdersAreDeclinedItem)
        assert result[0].errors == []
        assert result[0].is_error
        assert result[0].order_id == 1
