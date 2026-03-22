import pytest

from wbapi_async.types import CreatePassResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestCreatePass:

    async def test_create_pass(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "id": 1,
            }]
        )

        result = await api.create_pass(first_name="first_name", last_name="last_name", car_model="car_model", car_number="car_number", office_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreatePassResponse)
        assert result[0].id == 1
