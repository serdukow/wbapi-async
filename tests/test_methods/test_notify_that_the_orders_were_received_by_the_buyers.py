import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import NotifyThatTheOrdersWereReceivedByTheBuyersItem


@pytest.mark.unit
class TestNotifyThatTheOrdersWereReceivedByTheBuyers:
    async def test_notify_that_the_orders_were_received_by_the_buyers(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "results": [
                    {
                        "orderId": 1,
                        "isError": True,
                        "errors": [],
                    }
                ]
            }
        )

        result = await api.notify_that_the_orders_were_received_by_the_buyers()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NotifyThatTheOrdersWereReceivedByTheBuyersItem)
        assert result[0].order_id == 1
        assert result[0].is_error
        assert result[0].errors == []
