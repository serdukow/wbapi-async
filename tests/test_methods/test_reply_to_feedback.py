import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestReplyToFeedback:
    async def test_reply_to_feedback(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.reply_to_feedback(id="id", text="text")

        assert result is None
