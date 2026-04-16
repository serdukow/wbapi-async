import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import OfficesForPassResponse


@pytest.mark.unit
class TestGetOfficesForPass:
    async def test_get_offices_for_pass(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "name": "Koledino",
                    "address": "Kosmonavtov 10А",
                    "id": 1,
                }
            ]
        )

        result = await api.get_offices_for_pass()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OfficesForPassResponse)
        assert result[0].name == "Koledino"
        assert result[0].address == "Kosmonavtov 10А"
        assert result[0].id_ == 1
