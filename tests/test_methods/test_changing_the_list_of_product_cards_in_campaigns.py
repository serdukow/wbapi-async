import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ChangingTheListOfProductCardsInCampaignsItem


@pytest.mark.unit
class TestChangingTheListOfProductCardsInCampaigns:
    async def test_changing_the_list_of_product_cards_in_campaigns(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "nms": [
                    {
                        "advert_id": 1,
                        "nms": {"added": [], "deleted": []},
                    }
                ]
            }
        )

        result = await api.changing_the_list_of_product_cards_in_campaigns(
            nms=[{"advert_id": 1, "nms": {"add": [], "delete": []}}]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ChangingTheListOfProductCardsInCampaignsItem)
        assert result[0].advert_id == 1
