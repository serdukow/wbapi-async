import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestRenameCampaign:

    async def test_rename_campaign(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.rename_campaign(advert_id=1, name="name")

        assert result is None
