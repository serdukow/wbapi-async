import pytest

from wbapi_async.types.create_campaign_response import CreateCampaignResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestCreateCampaign:

    async def test_create_campaign(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.create_campaign()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreateCampaignResponse)
