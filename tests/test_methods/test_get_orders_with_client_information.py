import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import OrdersWithClientInformationItem


@pytest.mark.unit
class TestGetOrdersWithClientInformation:
    async def test_get_orders_with_client_information(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "firstName": "Иван",
                        "fullName": "Андреев Иван Васильевич",
                        "lastName": "Андреев",
                        "middleName": "Васильевич",
                        "orderID": 134567,
                        "phone": "79871234567",
                        "phoneCode": "0",
                    }
                ]
            }
        )

        result = await api.get_orders_with_client_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdersWithClientInformationItem)
        assert result[0].first_name == "Иван"
        assert result[0].full_name == "Андреев Иван Васильевич"
        assert result[0].last_name == "Андреев"
        assert result[0].middle_name == "Васильевич"
        assert result[0].order_id == 134567
