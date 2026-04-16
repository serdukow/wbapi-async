import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAssignADataMatrixCodeToTheAssemblyOrder:
    async def test_assign_a_data_matrix_code_to_the_assembly_order(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.assign_a_data_matrix_code_to_the_assembly_order(order_id=1)

        assert result is None
