import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem


@pytest.mark.unit
class TestAddDataMatrixCodesToTheAssemblyOrdersChestnyZnak:
    async def test_add_data_matrix_codes_to_the_assembly_orders_chestny_znak(self, api: MockedAPI) -> None:
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

        result = await api.add_data_matrix_codes_to_the_assembly_orders_chestny_znak(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem)
        assert result[0].order_id == 1
        assert result[0].is_error
        assert result[0].errors == []
