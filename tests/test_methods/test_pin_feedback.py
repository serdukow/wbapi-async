import pytest

from wbapi_async.types import PinFeedbackResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestPinFeedback:

    async def test_pin_feedback(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.pin_feedback()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PinFeedbackResponse)
