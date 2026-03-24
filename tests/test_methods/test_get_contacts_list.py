import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ContactsListItem


@pytest.mark.unit
class TestGetContactsList:
    async def test_get_contacts_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "contacts": [
                    {
                        "comment": "comment",
                        "phone": "phone",
                    }
                ]
            }
        )

        result = await api.get_contacts_list(warehouse_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ContactsListItem)
        assert result[0].comment == "comment"
        assert result[0].phone == "phone"
