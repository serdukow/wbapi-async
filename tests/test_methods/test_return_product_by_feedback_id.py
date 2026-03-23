import pytest

from wbapi_async.types import ReturnProductByFeedbackIdItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestReturnProductByFeedbackId:

    async def test_return_product_by_feedback_id(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "additionalErrors": [{

            }]
        }
        )

        result = await api.return_product_by_feedback_id()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReturnProductByFeedbackIdItem)
