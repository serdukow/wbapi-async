import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CampaignsInformationItem


@pytest.mark.unit
class TestGetCampaignsInformation:
    async def test_get_campaigns_information(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "adverts": [
                    {
                        "bid_type": "bid_type",
                        "id": 1,
                        "nm_settings": [
                            {"bids_kopecks": None, "subject": {"id": 1, "name": "name"}, "nm_id": 1}
                        ],
                        "settings": {
                            "payment_type": "payment_type",
                            "name": "name",
                            "placements": {"search": True, "recommendations": True},
                        },
                        "status": 1,
                        "timestamps": {
                            "created": "created",
                            "updated": "updated",
                            "started": "started",
                            "deleted": "deleted",
                        },
                    }
                ]
            }
        )

        result = await api.get_campaigns_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CampaignsInformationItem)
        assert result[0].bid_type == "bid_type"
        assert result[0].id_ == 1
        assert result[0].status == 1
