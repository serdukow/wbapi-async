import pytest

from wbapi_async.types import CampaignStatistics

from tests.mocked_api import MockedAPI

RESPONSE = [
    {
        "advertId": 22161678,
        "atbs": 9,
        "boosterStats": [
            {"avg_position": 24, "date": "2025-09-07", "nm": 221725278},
            {"avg_position": 35, "date": "2025-09-08", "nm": 221725278},
        ],
        "canceled": 0,
        "clicks": 139,
        "cpc": 4.76,
        "cr": 0,
        "ctr": 10.12,
        "days": [
            {
                "apps": [
                    {
                        "appType": 1,
                        "atbs": 0,
                        "canceled": 0,
                        "clicks": 1,
                        "cpc": 10.19,
                        "cr": 0,
                        "ctr": 4.76,
                        "nms": [
                            {
                                "atbs": 0,
                                "canceled": 0,
                                "clicks": 1,
                                "cpc": 10.19,
                                "cr": 0,
                                "ctr": 4.76,
                                "name": "постер 2",
                                "nmId": 221725278,
                                "orders": 0,
                                "shks": 0,
                                "sum": 10.19,
                                "sum_price": 0,
                                "views": 21,
                            }
                        ],
                        "orders": 0,
                        "shks": 0,
                        "sum": 10.19,
                        "sum_price": 0,
                        "views": 21,
                    }
                ],
                "atbs": 2,
                "canceled": 0,
                "clicks": 75,
                "cpc": 5.05,
                "cr": 0,
                "ctr": 9.57,
                "date": "2025-09-07T00:00:00Z",
                "orders": 0,
                "shks": 0,
                "sum": 378.49,
                "sum_price": 0,
                "views": 784,
            }
        ],
        "orders": 0,
        "shks": 0,
        "sum": 661.25,
        "sum_price": 0,
        "views": 1373,
    }
]


class TestGetCampaignsStatistics:
    @pytest.mark.unit
    async def test_returns_list(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_campaigns_statistics(
            ids=[22161678], begin_date="2025-09-07", end_date="2025-09-08"
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CampaignStatistics)

    @pytest.mark.unit
    async def test_campaign_fields(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_campaigns_statistics(
            ids=[22161678], begin_date="2025-09-07", end_date="2025-09-08"
        )

        stat = result[0]
        assert stat.advert_id == 22161678
        assert stat.clicks == 139
        assert stat.cpc == 4.76
        assert stat.views == 1373
        assert stat.sum == 661.25

    @pytest.mark.unit
    async def test_nested_booster_stats(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_campaigns_statistics(
            ids=[22161678], begin_date="2025-09-07", end_date="2025-09-08"
        )

        booster = result[0].booster_stats[0]
        assert booster.avg_position == 24
        assert booster.date == "2025-09-07"
        assert booster.nm == 221725278

    @pytest.mark.unit
    async def test_request_url(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        await api.get_campaigns_statistics(
            ids=[22161678, 28449281], begin_date="2025-09-07", end_date="2025-09-08"
        )

        req = api.get_last_request()
        assert req.url == "https://advert-api.test.api.com/adv/v3/fullstats"
        assert req.method == "GET"
        assert req.params["ids"] == "22161678,28449281"
