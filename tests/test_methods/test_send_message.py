import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SendMessageItem


@pytest.mark.unit
class TestSendMessage:
    async def test_send_message(self, api: MockedAPI) -> None:
        api.add_response({"errors": [{}]})

        result = await api.send_message()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SendMessageItem)
