import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import TheFeedbackByIdItem


@pytest.mark.unit
class TestGetTheFeedbackById:
    async def test_get_the_feedback_by_id(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "photoLinks": [
                        {
                            "fullSize": "fullSize",
                            "miniSize": "miniSize",
                        }
                    ]
                }
            }
        )

        result = await api.get_the_feedback_by_id(id="id")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TheFeedbackByIdItem)
        assert result[0].full_size == "fullSize"
        assert result[0].mini_size == "miniSize"
