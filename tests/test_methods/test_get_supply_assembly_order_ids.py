import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SupplyAssemblyOrderIdsItem


@pytest.mark.unit
class TestGetSupplyAssemblyOrderIds:
    async def test_get_supply_assembly_order_ids(self, api: MockedAPI) -> None:
        api.add_response({"orderIds": [{}]})

        result = await api.get_supply_assembly_order_ids(supply_id="supply_id")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SupplyAssemblyOrderIdsItem)
