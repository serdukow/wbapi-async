import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import OfficesResponse


@pytest.mark.unit
class TestGetOffices:
    async def test_get_offices(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "address": "ул. Троицкая, Подольск, Московская обл.",
                    "name": "Коледино",
                    "city": "Москва",
                    "id": 15,
                    "longitude": 55.386871,
                    "latitude": 37.588898,
                    "cargoType": 1,
                    "deliveryType": 1,
                    "federalDistrict": "Центральный",
                    "selected": True,
                }
            ]
        )

        result = await api.get_offices()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OfficesResponse)
        assert result[0].address == "ул. Троицкая, Подольск, Московская обл."
        assert result[0].name == "Коледино"
        assert result[0].city == "Москва"
        assert result[0].id_ == 15
        assert result[0].longitude == 55.386871
