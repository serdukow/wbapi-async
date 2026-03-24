import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestUpdateContactsList:
    async def test_update_contacts_list(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.update_contacts_list(warehouse_id=1)

        assert result is None
