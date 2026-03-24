import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsForCampaignsResponse


@pytest.mark.unit
class TestProductCardsForCampaigns:
    async def test_product_cards_for_campaigns(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "title": "title",
                    "nm": 1,
                    "subjectId": 1,
                }
            ]
        )

        result = await api.product_cards_for_campaigns()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsForCampaignsResponse)
        assert result[0].title == "title"
        assert result[0].nm == 1
        assert result[0].subject_id == 1
