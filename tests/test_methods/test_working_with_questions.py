import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import WorkingWithQuestionsItem


@pytest.mark.unit
class TestWorkingWithQuestions:
    async def test_working_with_questions(self, api: MockedAPI) -> None:
        api.add_response({"additionalErrors": [{}]})

        result = await api.working_with_questions()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WorkingWithQuestionsItem)
