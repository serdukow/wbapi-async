import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ListOfPinnedAndUnpinnedFeedbackResponse


@pytest.mark.unit
class TestGetListOfPinnedAndUnpinnedFeedback:
    async def test_get_list_of_pinned_and_unpinned_feedback(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "next": 200,
                }
            ]
        )

        result = await api.get_list_of_pinned_and_unpinned_feedback()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfPinnedAndUnpinnedFeedbackResponse)
        assert result[0].next_ == 200
