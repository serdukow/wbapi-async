import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAddExpirationDateToTheAssemblyOrder:

    async def test_add_expiration_date_to_the_assembly_order(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.add_expiration_date_to_the_assembly_order(order_id=1)

        assert result is None
