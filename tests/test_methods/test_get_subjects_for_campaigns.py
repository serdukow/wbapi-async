import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SubjectsForCampaignsResponse


@pytest.mark.unit
class TestGetSubjectsForCampaigns:
    async def test_get_subjects_for_campaigns(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "id": 1,
                    "name": "name",
                    "count": 1,
                }
            ]
        )

        result = await api.get_subjects_for_campaigns()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SubjectsForCampaignsResponse)
        assert result[0].id == 1
        assert result[0].name == "name"
        assert result[0].count == 1
