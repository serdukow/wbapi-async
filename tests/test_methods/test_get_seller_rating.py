import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SellerRatingResponse


@pytest.mark.unit
class TestGetSellerRating:
    async def test_get_seller_rating(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "feedbackCount": 1,
                    "valuation": 1.0,
                }
            ]
        )

        result = await api.get_seller_rating()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SellerRatingResponse)
        assert result[0].feedback_count == 1
        assert result[0].valuation == 1.0
