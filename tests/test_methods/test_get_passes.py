import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PassesResponse


@pytest.mark.unit
class TestGetPasses:
    async def test_get_passes(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "firstName": "Alex",
                    "dateEnd": "2022-07-31 17:53:13+00:00",
                    "lastName": "Petrov",
                    "carModel": "Lamborghini",
                    "carNumber": "A456BC123",
                    "officeName": "Koledino",
                    "officeAddress": "Kosmonavtov 10А",
                    "officeId": 15,
                    "id": 1,
                }
            ]
        )

        result = await api.get_passes()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PassesResponse)
        assert result[0].first_name == "Alex"
        assert result[0].date_end == "2022-07-31 17:53:13+00:00"
        assert result[0].last_name == "Petrov"
        assert result[0].car_model == "Lamborghini"
        assert result[0].car_number == "A456BC123"
