import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ChatEventsItem


@pytest.mark.unit
class TestGetChatEvents:
    async def test_get_chat_events(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "result": {
                    "events": [
                        {
                            "chatID": "chatID",
                            "eventID": "eventID",
                            "eventType": "eventType",
                            "isNewChat": True,
                            "message": {},
                            "source": "source",
                            "addTimestamp": 1,
                            "addTime": "addTime",
                            "replySign": "replySign",
                            "sender": "sender",
                            "clientName": "clientName",
                        }
                    ]
                }
            }
        )

        result = await api.get_chat_events()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ChatEventsItem)
        assert result[0].chat_id == "chatID"
        assert result[0].event_id == "eventID"
        assert result[0].event_type == "eventType"
