import pytest

from wbapi_async.types.contacts_list_item import ContactsListItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestContactsList:

    async def test_contacts_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "contacts": [{
                "comment": "comment",
                "phone": "phone",
            }]
        }
        )

        result = await api.contacts_list(warehouse_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ContactsListItem)
        assert result[0].comment == "comment"
        assert result[0].phone == "phone"
