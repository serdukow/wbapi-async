import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import InformationOnPaidDeliveryResponse


@pytest.mark.unit
class TestGetInformationOnPaidDelivery:
    async def test_get_information_on_paid_delivery(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "groupID": "0596a30a-d11c-4210-a231-ee1c39d61fe4",
                    "deliveryCost": 1108,
                    "convertedDeliveryCost": 29803,
                    "currencyCode": 933,
                    "convertedCurrencyCode": 643,
                }
            ]
        )

        result = await api.get_information_on_paid_delivery()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], InformationOnPaidDeliveryResponse)
        assert result[0].group_id == "0596a30a-d11c-4210-a231-ee1c39d61fe4"
        assert result[0].delivery_cost == 1108
        assert result[0].converted_delivery_cost == 29803
        assert result[0].currency_code == 933
        assert result[0].converted_currency_code == 643
