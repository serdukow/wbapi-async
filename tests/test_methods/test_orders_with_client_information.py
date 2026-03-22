import pytest

from wbapi_async.types import OrdersWithClientInformationItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestOrdersWithClientInformation:

    async def test_orders_with_client_information(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "firstName": "firstName",
                "fullName": "fullName",
                "lastName": "lastName",
                "middleName": "middleName",
                "orderID": 1,
                "phone": "phone",
                "phoneCode": "phoneCode",
            }]
        }
        )

        result = await api.orders_with_client_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdersWithClientInformationItem)
        assert result[0].first_name == "firstName"
        assert result[0].full_name == "fullName"
        assert result[0].last_name == "lastName"
