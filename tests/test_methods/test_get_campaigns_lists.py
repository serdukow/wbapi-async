import pytest

from wbapi_async.types import CampaignsList

from tests.mocked_api import MockedAPI

RESPONSE = {
    "adverts": [
        {
            "type": 9,
            "status": 8,
            "count": 3,
            "advert_list": [
                {"advertId": 6485174, "changeTime": "2023-05-10T12:12:52.676254+03:00"},
                {"advertId": 6500443, "changeTime": "2023-05-10T17:08:46.370656+03:00"},
                {"advertId": 7936341, "changeTime": "2023-07-12T15:51:08.367478+03:00"},
            ],
        }
    ],
    "all": 3,
}


class TestGetCampaignsLists:
    @pytest.mark.unit
    async def test_returns_model(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_campaigns_lists()

        assert isinstance(result, CampaignsList)
        assert result.all == 3
        assert result.adverts is not None
        assert len(result.adverts) == 1

    @pytest.mark.unit
    async def test_campaign_group_fields(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_campaigns_lists()

        group = result.adverts[0]
        assert group.type == 9
        assert group.status == 8
        assert group.count == 3
        assert group.advert_list is not None
        assert len(group.advert_list) == 3

    @pytest.mark.unit
    async def test_campaign_item_fields(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_campaigns_lists()

        item = result.adverts[0].advert_list[0]
        assert item.advert_id == 6485174
        assert item.change_time == "2023-05-10T12:12:52.676254+03:00"

    @pytest.mark.unit
    async def test_request_url(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        await api.get_campaigns_lists()

        req = api.get_last_request()
        assert req.url == "https://advert-api.test.api.com/adv/v1/promotion/count"
        assert req.method == "GET"
