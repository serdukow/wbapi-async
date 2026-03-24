import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ReturnProductByFeedbackIdItem


@pytest.mark.unit
class TestReturnProductByFeedbackId:
    async def test_return_product_by_feedback_id(self, api: MockedAPI) -> None:
        api.add_response({"additionalErrors": [{}]})

        result = await api.return_product_by_feedback_id()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReturnProductByFeedbackIdItem)
