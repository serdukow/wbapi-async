import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestTransferToAssembly:
    async def test_transfer_to_assembly(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.transfer_to_assembly(order_id=1)

        assert result is None
