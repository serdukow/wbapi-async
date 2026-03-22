import pytest

from wbapi_async.types import CreateANewSupplyResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestCreateANewSupply:

    async def test_create_a_new_supply(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "id": "id",
            }]
        )

        result = await api.create_a_new_supply()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreateANewSupplyResponse)
        assert result[0].id == "id"
