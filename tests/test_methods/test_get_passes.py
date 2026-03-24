import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PassesResponse


@pytest.mark.unit
class TestGetPasses:
    async def test_get_passes(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "firstName": "firstName",
                    "dateEnd": "dateEnd",
                    "lastName": "lastName",
                    "carModel": "carModel",
                    "carNumber": "carNumber",
                    "officeName": "officeName",
                    "officeAddress": "officeAddress",
                    "officeId": 1,
                    "id": 1,
                }
            ]
        )

        result = await api.get_passes()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PassesResponse)
        assert result[0].first_name == "firstName"
        assert result[0].date_end == "dateEnd"
        assert result[0].last_name == "lastName"
