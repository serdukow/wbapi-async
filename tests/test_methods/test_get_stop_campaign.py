import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetStopCampaign:

    async def test_get_stop_campaign(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.get_stop_campaign(id=1)

        assert result is None
