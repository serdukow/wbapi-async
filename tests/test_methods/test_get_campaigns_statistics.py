import pytest

from wbapi_async.types.campaigns_statistics_response import CampaignsStatisticsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetCampaignsStatistics:

    async def test_get_campaigns_statistics(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "advertId": 1,
                "atbs": 1,
                "boosterStats": None,
                "canceled": 1,
                "clicks": 1,
                "cpc": 1.0,
                "cr": 1.0,
                "ctr": 1.0,
                "days": None,
                "orders": 1,
                "shks": 1,
                "sum": 1.0,
                "sum_price": 1.0,
                "views": 1,
            }]
        )

        result = await api.get_campaigns_statistics(ids="ids", begin_date="begin_date", end_date="end_date")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CampaignsStatisticsResponse)
        assert result[0].advert_id == 1
        assert result[0].atbs == 1
