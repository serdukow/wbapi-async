import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetLaunchCampaign:

    async def test_get_launch_campaign(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.get_launch_campaign(id_=1)

        assert result is None
