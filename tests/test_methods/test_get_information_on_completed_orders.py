import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import InformationOnCompletedOrdersItem


@pytest.mark.unit
class TestGetInformationOnCompletedOrders:
    async def test_get_information_on_completed_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "address": {},
                        "options": {},
                        "orderUid": "orderUid",
                        "groupId": "groupId",
                        "article": "article",
                        "colorCode": "colorCode",
                        "rid": "rid",
                        "createdAt": "createdAt",
                        "skus": [],
                        "id": 1,
                        "warehouseId": 1,
                        "nmId": 1,
                        "chrtId": 1,
                        "price": 1,
                        "convertedPrice": 1,
                        "currencyCode": 1,
                        "convertedCurrencyCode": 1,
                        "cargoType": 1,
                        "comment": "comment",
                        "isZeroOrder": True,
                    }
                ]
            }
        )

        result = await api.get_information_on_completed_orders(limit=1, next=1, date_from=1, date_to=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], InformationOnCompletedOrdersItem)
        assert result[0].address == {}
        assert result[0].options == {}
        assert result[0].order_uid == "orderUid"
