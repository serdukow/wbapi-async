import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DeliveryDateAndTimeItem


@pytest.mark.unit
class TestGetDeliveryDateAndTime:
    async def test_get_delivery_date_and_time(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "dTimeFrom": "11:11",
                        "dTimeTo": "22:22",
                        "dTimeFromOld": "12:30",
                        "dTimeToOld": "22:30",
                        "dDateOld": "2025-01-28",
                        "dDate": "2025-02-20",
                        "id": 1234567890,
                    }
                ]
            }
        )

        result = await api.get_delivery_date_and_time()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DeliveryDateAndTimeItem)
        assert result[0].d_time_from == "11:11"
        assert result[0].d_time_to == "22:22"
        assert result[0].d_time_from_old == "12:30"
        assert result[0].d_time_to_old == "22:30"
        assert result[0].d_date_old == "2025-01-28"
