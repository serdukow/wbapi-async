import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import UnseenFeedbacksAndQuestionsItem


@pytest.mark.unit
class TestGetUnseenFeedbacksAndQuestions:
    async def test_get_unseen_feedbacks_and_questions(self, api: MockedAPI) -> None:
        api.add_response({"additionalErrors": [{}]})

        result = await api.get_unseen_feedbacks_and_questions()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UnseenFeedbacksAndQuestionsItem)
