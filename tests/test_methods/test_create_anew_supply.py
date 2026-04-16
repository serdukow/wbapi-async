import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CreateANewSupplyResponse


@pytest.mark.unit
class TestCreateANewSupply:
    async def test_create_a_new_supply(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "id": "WB-GI-1234567",
                }
            ]
        )

        result = await api.create_a_new_supply()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreateANewSupplyResponse)
        assert result[0].id_ == "WB-GI-1234567"
