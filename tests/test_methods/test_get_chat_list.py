import pytest

from wbapi_async.types.chat_list_item import ChatListItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetChatList:

    async def test_get_chat_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "result": [{
                "chatID": "chatID",
                "replySign": "replySign",
                "clientName": "clientName",
                "goodCard": {},
                "lastMessage": None,
            }]
        }
        )

        result = await api.get_chat_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ChatListItem)
        assert result[0].chat_id == "chatID"
        assert result[0].reply_sign == "replySign"
        assert result[0].client_name == "clientName"
