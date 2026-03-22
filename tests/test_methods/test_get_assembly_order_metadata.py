import pytest

from wbapi_async.types import AssemblyOrderMetadataResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetAssemblyOrderMetadata:

    async def test_get_assembly_order_metadata(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "meta": {},
            }]
        )

        result = await api.get_assembly_order_metadata(order_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrderMetadataResponse)
        assert result[0].meta == {}
