import pytest

from wbapi_async.types import AssemblyOrdersMetadataItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetAssemblyOrdersMetadata:

    async def test_get_assembly_orders_metadata(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "id": 1,
                "meta": {},
            }]
        }
        )

        result = await api.get_assembly_orders_metadata(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrdersMetadataItem)
        assert result[0].id_ == 1
        assert result[0].meta == {}
