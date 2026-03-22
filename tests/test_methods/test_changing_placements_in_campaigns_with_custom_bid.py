import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestChangingPlacementsInCampaignsWithCustomBid:

    async def test_changing_placements_in_campaigns_with_custom_bid(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.changing_placements_in_campaigns_with_custom_bid(placements=[])

        assert result is None
