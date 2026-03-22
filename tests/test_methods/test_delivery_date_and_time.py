import pytest

from wbapi_async.types import DeliveryDateAndTimeItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeliveryDateAndTime:

    async def test_delivery_date_and_time(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "dTimeFrom": "dTimeFrom",
                "dTimeTo": "dTimeTo",
                "dTimeFromOld": "dTimeFromOld",
                "dTimeToOld": "dTimeToOld",
                "dDateOld": "dDateOld",
                "dDate": "dDate",
                "id": 1,
            }]
        }
        )

        result = await api.delivery_date_and_time()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DeliveryDateAndTimeItem)
        assert result[0].d_time_from == "dTimeFrom"
        assert result[0].d_time_to == "dTimeTo"
        assert result[0].d_time_from_old == "dTimeFromOld"
