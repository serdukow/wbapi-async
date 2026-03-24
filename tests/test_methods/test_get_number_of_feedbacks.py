import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import NumberOfFeedbacksItem


@pytest.mark.unit
class TestGetNumberOfFeedbacks:
    async def test_get_number_of_feedbacks(self, api: MockedAPI) -> None:
        api.add_response({"additionalErrors": [{}]})

        result = await api.get_number_of_feedbacks()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NumberOfFeedbacksItem)
