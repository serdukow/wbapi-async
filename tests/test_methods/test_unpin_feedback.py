import pytest

from wbapi_async.types.unpin_feedback_response import UnpinFeedbackResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestUnpinFeedback:

    async def test_unpin_feedback(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.unpin_feedback()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UnpinFeedbackResponse)
