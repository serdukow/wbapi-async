import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CreatePassResponse


@pytest.mark.unit
class TestCreatePass:
    async def test_create_pass(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "id": 2,
                }
            ]
        )

        result = await api.create_pass(
            first_name="first_name",
            last_name="last_name",
            car_model="car_model",
            car_number="car_number",
            office_id=1,
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreatePassResponse)
        assert result[0].id_ == 2
