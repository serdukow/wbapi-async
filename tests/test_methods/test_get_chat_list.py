import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ChatListItem


@pytest.mark.unit
class TestGetChatList:
    async def test_get_chat_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "result": [
                    {
                        "chatID": "1:4019cd7d-cca8-4e90-8b11-f78afbea42e3",
                        "replySign": "1:4019cd7d-cca8-4e90-8b11-f78afbea42e3:54828159:bc3a4c04079f5956cff170b25e73523aa1208b5c0bd7aea1e520a64ae3e212b1ebae6712661f3afd27520fa785fa3042254e8a3100ce00644322054ae7cfcd0e",
                        "clientName": "Иван",
                        "goodCard": {
                            "date": "date",
                            "nmID": 1,
                            "price": 1,
                            "priceCurrency": "priceCurrency",
                            "rid": "rid",
                            "size": "size",
                        },
                        "lastMessage": {"text": "text", "addTimestamp": 1},
                    }
                ]
            }
        )

        result = await api.get_chat_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ChatListItem)
        assert result[0].chat_id == "1:4019cd7d-cca8-4e90-8b11-f78afbea42e3"
        assert (
            result[0].reply_sign
            == "1:4019cd7d-cca8-4e90-8b11-f78afbea42e3:54828159:bc3a4c04079f5956cff170b25e73523aa1208b5c0bd7aea1e520a64ae3e212b1ebae6712661f3afd27520fa785fa3042254e8a3100ce00644322054ae7cfcd0e"
        )
        assert result[0].client_name == "Иван"
