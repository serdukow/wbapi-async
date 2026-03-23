import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAddCustomDeclarationNumberToTheOrder:

    async def test_add_custom_declaration_number_to_the_order(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.add_custom_declaration_number_to_the_order(order_id=1)

        assert result is None
