import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CreateCampaignResponse


@pytest.mark.unit
class TestCreateCampaign:
    async def test_create_campaign(self, api: MockedAPI) -> None:
        api.add_response([{}])

        result = await api.create_campaign()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreateCampaignResponse)
