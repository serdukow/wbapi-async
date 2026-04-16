import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PinFeedbackResponse


@pytest.mark.unit
class TestPinFeedback:
    async def test_pin_feedback(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                }
            ]
        )

        result = await api.pin_feedback()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PinFeedbackResponse)
