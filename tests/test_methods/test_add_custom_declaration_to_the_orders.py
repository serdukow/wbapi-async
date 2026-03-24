import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAddCustomDeclarationToTheOrders:
    async def test_add_custom_declaration_to_the_orders(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.add_custom_declaration_to_the_orders()

        assert result is None
