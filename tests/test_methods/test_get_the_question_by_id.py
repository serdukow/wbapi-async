import pytest

from wbapi_async.types.the_question_by_id_item import TheQuestionByIdItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetTheQuestionById:

    async def test_get_the_question_by_id(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "additionalErrors": [{

            }]
        }
        )

        result = await api.get_the_question_by_id(id="id")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TheQuestionByIdItem)
