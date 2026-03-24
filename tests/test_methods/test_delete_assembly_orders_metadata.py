import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DeleteAssemblyOrdersMetadataItem


@pytest.mark.unit
class TestDeleteAssemblyOrdersMetadata:
    async def test_delete_assembly_orders_metadata(self, api: MockedAPI) -> None:
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

        result = await api.delete_assembly_orders_metadata(key="key", order_ids=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DeleteAssemblyOrdersMetadataItem)
        assert result[0].errors == []
        assert result[0].is_error
        assert result[0].order_id == 1
