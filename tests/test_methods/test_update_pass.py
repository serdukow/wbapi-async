import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestUpdatePass:
    async def test_update_pass(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.update_pass(
            pass_id=1,
            first_name="first_name",
            last_name="last_name",
            car_model="car_model",
            car_number="car_number",
            office_id=1,
        )

        assert result is None
