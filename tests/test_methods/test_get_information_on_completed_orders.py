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
                        "address": {
                            "fullAddress": "Chelyabinsk Region, Chelyabinsk, 51st Arabkir Street, Building 10A, Apartment 42",
                            "longitude": 44.519068,
                            "latitude": 40.20192,
                        },
                        "options": {"isB2b": True},
                        "orderUid": "165918930_629fbc924b984618a44354475ca58675",
                        "groupId": "7a2c8810-1db2-4011-9682-5c7fa33afd83",
                        "article": "one-ring-7548",
                        "colorCode": "RAL 3017",
                        "rid": "f884001e44e511edb8780242ac120002",
                        "createdAt": "2022-05-04T07:56:29Z",
                        "skus": [],
                        "id": 13833711,
                        "warehouseId": 658434,
                        "nmId": 123456789,
                        "chrtId": 987654321,
                        "price": 1014,
                        "convertedPrice": 1014,
                        "currencyCode": 933,
                        "convertedCurrencyCode": 643,
                        "cargoType": 1,
                        "comment": "Упакуйте в пленку, пожалуйста",
                        "isZeroOrder": False,
                    }
                ]
            }
        )

        result = await api.get_information_on_completed_orders(limit=1, next_=1, date_from=1, date_to=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], InformationOnCompletedOrdersItem)
        assert result[0].order_uid == "165918930_629fbc924b984618a44354475ca58675"
        assert result[0].group_id == "7a2c8810-1db2-4011-9682-5c7fa33afd83"
        assert result[0].article == "one-ring-7548"
