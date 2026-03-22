import pytest

from wbapi_async.types.number_of_questions_item import NumberOfQuestionsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetNumberOfQuestions:

    async def test_get_number_of_questions(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "additionalErrors": [{

            }]
        }
        )

        result = await api.get_number_of_questions()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NumberOfQuestionsItem)
