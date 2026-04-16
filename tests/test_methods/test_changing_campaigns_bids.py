import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ChangingCampaignsBidsItem


@pytest.mark.unit
class TestChangingCampaignsBids:
    async def test_changing_campaigns_bids(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "bids": [
                    {
                        "advert_id": 1,
                        "nm_bids": [{"nm_id": 1, "bid_kopecks": 1, "placement": "placement"}],
                    }
                ]
            }
        )

        result = await api.changing_campaigns_bids(bids=[{"type": "combined", "value": 1}])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ChangingCampaignsBidsItem)
        assert result[0].advert_id == 1
