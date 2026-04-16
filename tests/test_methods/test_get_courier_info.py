import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CourierInfoItem


@pytest.mark.unit
class TestGetCourierInfo:
    async def test_get_courier_info(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "courierInfo": {
                            "contacts": {
                                "carNumber": "х111хх11",
                                "fullName": "Иванов Иван Иванович",
                                "phone": "71230971931",
                                "pTimeFrom": "2025-09-06T08:00:00Z",
                                "pTimeTo": "2025-09-06T11:00:00Z",
                            },
                            "mustBeAssigned": True,
                            "updatedAt": "2025-09-06T11:33:10+03:00",
                        },
                        "orderID": 2876979713,
                    }
                ]
            }
        )

        result = await api.get_courier_info()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CourierInfoItem)
        assert result[0].order_id == 2876979713
