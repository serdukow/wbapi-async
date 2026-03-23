import pytest

from wbapi_async.types import ListOfPinnedAndUnpinnedFeedbackResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetListOfPinnedAndUnpinnedFeedback:

    async def test_get_list_of_pinned_and_unpinned_feedback(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.get_list_of_pinned_and_unpinned_feedback()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfPinnedAndUnpinnedFeedbackResponse)
