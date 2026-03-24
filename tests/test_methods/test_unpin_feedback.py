import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import UnpinFeedbackResponse


@pytest.mark.unit
class TestUnpinFeedback:
    async def test_unpin_feedback(self, api: MockedAPI) -> None:
        api.add_response([{}])

        result = await api.unpin_feedback()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UnpinFeedbackResponse)
