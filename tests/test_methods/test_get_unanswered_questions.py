import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import UnansweredQuestionsItem


@pytest.mark.unit
class TestGetUnansweredQuestions:
    async def test_get_unanswered_questions(self, api: MockedAPI) -> None:
        api.add_response({"additionalErrors": [{}]})

        result = await api.get_unanswered_questions()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UnansweredQuestionsItem)
