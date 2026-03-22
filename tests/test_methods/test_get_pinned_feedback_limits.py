import pytest

from wbapi_async.types.pinned_feedback_limits_response import PinnedFeedbackLimitsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetPinnedFeedbackLimits:

    async def test_get_pinned_feedback_limits(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.get_pinned_feedback_limits()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PinnedFeedbackLimitsResponse)
