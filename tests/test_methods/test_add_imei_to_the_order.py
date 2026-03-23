import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAddImeiToTheOrder:
    async def test_add_imei_to_the_order(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.add_imei_to_the_order(order_id=1, imei="imei")

        assert result is None
