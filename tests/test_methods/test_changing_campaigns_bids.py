import pytest

from wbapi_async.types.changing_campaigns_bids_item import ChangingCampaignsBidsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestChangingCampaignsBids:

    async def test_changing_campaigns_bids(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "bids": [{
                "advert_id": 1,
                "nm_bids": [],
            }]
        }
        )

        result = await api.changing_campaigns_bids(bids=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ChangingCampaignsBidsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_bids == []
