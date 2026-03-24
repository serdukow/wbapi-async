import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem


@pytest.mark.unit
class TestAddDataMatrixCodesToAssemblyOrdersChestnyZnak:
    async def test_add_data_matrix_codes_to_assembly_orders_chestny_znak(self, api: MockedAPI) -> None:
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

        result = await api.add_data_matrix_codes_to_assembly_orders_chestny_znak(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem)
        assert result[0].errors == []
        assert result[0].is_error
        assert result[0].order_id == 1
