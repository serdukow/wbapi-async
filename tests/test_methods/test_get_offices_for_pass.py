import pytest

from wbapi_async.types import OfficesForPassResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetOfficesForPass:

    async def test_get_offices_for_pass(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "name": "name",
                "address": "address",
                "id": 1,
            }]
        )

        result = await api.get_offices_for_pass()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OfficesForPassResponse)
        assert result[0].name == "name"
        assert result[0].address == "address"
        assert result[0].id == 1
