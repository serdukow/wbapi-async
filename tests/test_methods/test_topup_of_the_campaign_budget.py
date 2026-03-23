import pytest

from wbapi_async.types import TopupOfTheCampaignBudgetResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestTopupOfTheCampaignBudget:

    async def test_topup_of_the_campaign_budget(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.topup_of_the_campaign_budget(id_=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TopupOfTheCampaignBudgetResponse)
