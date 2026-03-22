import pytest

from wbapi_async.types import CampaignsInformationItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetCampaignsInformation:

    async def test_get_campaigns_information(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "adverts": [{
                "bid_type": "bid_type",
                "id": 1,
                "nm_settings": [],
                "settings": {},
                "status": 1,
                "timestamps": {},
            }]
        }
        )

        result = await api.get_campaigns_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CampaignsInformationItem)
        assert result[0].bid_type == "bid_type"
        assert result[0].id == 1
        assert result[0].nm_settings == []
