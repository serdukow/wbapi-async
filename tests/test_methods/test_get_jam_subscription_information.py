import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import JamSubscriptionInformationResponse


@pytest.mark.unit
class TestGetJamSubscriptionInformation:
    async def test_get_jam_subscription_information(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "state": "state",
                    "activationSource": "activationSource",
                    "level": "level",
                    "since": "since",
                    "till": "till",
                }
            ]
        )

        result = await api.get_jam_subscription_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], JamSubscriptionInformationResponse)
        assert result[0].state == "state"
        assert result[0].activation_source == "activationSource"
        assert result[0].level == "level"
