import pytest

from wbapi_async.types import InformationAboutMediaCampaignItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetInformationAboutMediaCampaign:

    async def test_get_information_about_media_campaign(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "items": [{
                "id": 1,
                "name": "name",
                "status": 1,
                "place": 1,
                "budget": 1,
                "daily_limit": 1,
                "category_name": "category_name",
                "cpm": 1,
                "url": "url",
                "advert_type": 1,
                "created_at": "created_at",
                "updated_at": "updated_at",
                "date_from": "date_from",
                "date_to": "date_to",
                "nms": [],
                "bottomText1": "bottomText1",
                "bottomText2": "bottomText2",
                "message": "message",
                "additionalSettings": 1,
                "receiversCount": 1,
                "subject_id": 1,
                "subject_name": "subject_name",
                "action_name": "action_name",
                "show_hours": [],
                "Erid": "Erid",
            }]
        }
        )

        result = await api.get_information_about_media_campaign(id_=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], InformationAboutMediaCampaignItem)
        assert result[0].id_ == 1
        assert result[0].name == "name"
        assert result[0].status == 1
