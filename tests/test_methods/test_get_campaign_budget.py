import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CampaignBudgetResponse


@pytest.mark.unit
class TestGetCampaignBudget:
    async def test_get_campaign_budget(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "cash": 1,
                    "netting": 1,
                    "total": 1,
                }
            ]
        )

        result = await api.get_campaign_budget(id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CampaignBudgetResponse)
        assert result[0].cash == 1
        assert result[0].netting == 1
        assert result[0].total == 1
