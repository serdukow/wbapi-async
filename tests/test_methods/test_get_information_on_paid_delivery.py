import pytest

from wbapi_async.types.information_on_paid_delivery_response import InformationOnPaidDeliveryResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetInformationOnPaidDelivery:

    async def test_get_information_on_paid_delivery(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "groupID": "groupID",
                "deliveryCost": 1,
                "convertedDeliveryCost": 1,
                "currencyCode": 1,
                "convertedCurrencyCode": 1,
            }]
        )

        result = await api.get_information_on_paid_delivery()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], InformationOnPaidDeliveryResponse)
        assert result[0].group_id == "groupID"
        assert result[0].delivery_cost == 1
        assert result[0].converted_delivery_cost == 1
