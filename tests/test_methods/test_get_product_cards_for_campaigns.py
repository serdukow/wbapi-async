import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsForCampaignsResponse


@pytest.mark.unit
class TestGetProductCardsForCampaigns:
    async def test_get_product_cards_for_campaigns(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "title": "Плед",
                    "nm": 146168367,
                    "subjectId": 765,
                }
            ]
        )

        result = await api.get_product_cards_for_campaigns()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsForCampaignsResponse)
        assert result[0].title == "Плед"
        assert result[0].nm == 146168367
        assert result[0].subject_id == 765
