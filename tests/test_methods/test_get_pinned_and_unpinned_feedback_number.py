import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PinnedAndUnpinnedFeedbackNumberResponse


@pytest.mark.unit
class TestGetPinnedAndUnpinnedFeedbackNumber:
    async def test_get_pinned_and_unpinned_feedback_number(self, api: MockedAPI) -> None:
        api.add_response([{}])

        result = await api.get_pinned_and_unpinned_feedback_number()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PinnedAndUnpinnedFeedbackNumberResponse)
