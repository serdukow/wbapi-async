import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CourierInfoItem


@pytest.mark.unit
class TestCourierInfo:
    async def test_courier_info(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "courierInfo": {},
                        "orderID": 1,
                    }
                ]
            }
        )

        result = await api.courier_info()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CourierInfoItem)
        assert result[0].courier_info == {}
        assert result[0].order_id == 1
