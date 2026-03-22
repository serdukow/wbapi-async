import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAddUinUniqueIdentificationNumberToTheOrder:

    async def test_add_uin_unique_identification_number_to_the_order(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.add_uin_unique_identification_number_to_the_order(order_id=1, uin="uin")

        assert result is None
