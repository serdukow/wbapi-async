import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestCancelTheOrder:
    async def test_cancel_the_order(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.cancel_the_order(order_id=1)

        assert result is None
