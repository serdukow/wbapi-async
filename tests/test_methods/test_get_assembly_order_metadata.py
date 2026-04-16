import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AssemblyOrderMetadataItem


@pytest.mark.unit
class TestGetAssemblyOrderMetadata:
    async def test_get_assembly_order_metadata(self, api: MockedAPI) -> None:
        api.add_response({"meta": {"sgtin": {"value": [{}]}}})

        result = await api.get_assembly_order_metadata(order_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrderMetadataItem)
