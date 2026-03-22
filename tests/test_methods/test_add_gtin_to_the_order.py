import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAddGtinToTheOrder:

    async def test_add_gtin_to_the_order(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.add_gtin_to_the_order(order_id=1, gtin="gtin")

        assert result is None
