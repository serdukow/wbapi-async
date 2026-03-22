import pytest

from wbapi_async.types.changing_the_list_of_product_cards_in_campaigns_item import ChangingTheListOfProductCardsInCampaignsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestChangingTheListOfProductCardsInCampaigns:

    async def test_changing_the_list_of_product_cards_in_campaigns(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "nms": [{
                "advert_id": 1,
                "nms": {},
            }]
        }
        )

        result = await api.changing_the_list_of_product_cards_in_campaigns(nms=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ChangingTheListOfProductCardsInCampaignsItem)
        assert result[0].advert_id == 1
        assert result[0].nms == {}
