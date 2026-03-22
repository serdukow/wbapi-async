import pytest

from wbapi_async.types.unanswered_feedbacks_item import UnansweredFeedbacksItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetUnansweredFeedbacks:

    async def test_get_unanswered_feedbacks(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "additionalErrors": [{

            }]
        }
        )

        result = await api.get_unanswered_feedbacks()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UnansweredFeedbacksItem)
