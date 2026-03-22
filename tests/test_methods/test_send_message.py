import pytest

from wbapi_async.types import SendMessageItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSendMessage:

    async def test_send_message(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "errors": [{

            }]
        }
        )

        result = await api.send_message()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SendMessageItem)
