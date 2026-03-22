import pytest

from wbapi_async.types.delete_assembly_orders_metadata_item import DeleteAssemblyOrdersMetadataItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteAssemblyOrdersMetadata:

    async def test_delete_assembly_orders_metadata(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "results": [{
                "errors": [],
                "isError": True,
                "orderId": 1,
            }]
        }
        )

        result = await api.delete_assembly_orders_metadata(key="key", order_ids=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DeleteAssemblyOrdersMetadataItem)
        assert result[0].errors == []
        assert result[0].is_error == True
        assert result[0].order_id == 1
