import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ListOfCampaignMinusPhrasesItem


@pytest.mark.unit
class TestGetListOfCampaignMinusPhrases:
    async def test_get_list_of_campaign_minus_phrases(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "items": [
                    {
                        "advert_id": 1,
                        "nm_id": 1,
                        "norm_queries": [],
                    }
                ]
            }
        )

        result = await api.get_list_of_campaign_minus_phrases(items=[{"advert_id": 1, "nm_id": 1}])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfCampaignMinusPhrasesItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
