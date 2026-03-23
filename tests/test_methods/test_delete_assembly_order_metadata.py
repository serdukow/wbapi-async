import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteAssemblyOrderMetadata:
    async def test_delete_assembly_order_metadata(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.delete_assembly_order_metadata(order_id=1)

        assert result is None
