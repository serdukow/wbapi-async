import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import NewOrdersListItem


@pytest.mark.unit
class TestGetNewOrdersList:
    async def test_get_new_orders_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "salePrice": 504600,
                        "requiredMeta": [],
                        "comment": "Упакуйте в пленку, пожалуйста",
                        "options": {"isB2b": True},
                        "address": {
                            "fullAddress": "Chelyabinsk Region, Chelyabinsk, 51st Arabkir Street, Building 10A, Apartment 42",
                            "longitude": 44.519068,
                            "latitude": 40.20192,
                        },
                        "orderUid": "165918930_629fbc924b984618a44354475ca58675",
                        "groupId": "7a2c8810-1db2-4011-9682-5c7fa33afd83",
                        "article": "one-ring-7548",
                        "colorCode": "RAL 3017",
                        "rid": "f884001e44e511edb8780242ac120002",
                        "createdAt": "2022-05-04T07:56:29Z",
                        "deliveryType": "deliveryType",
                        "skus": [],
                        "id": 13833711,
                        "warehouseId": 658434,
                        "nmId": 123456789,
                        "chrtId": 987654321,
                        "price": 1014,
                        "finalPrice": 1014,
                        "convertedFinalPrice": 1014,
                        "convertedPrice": 1014,
                        "currencyCode": 643,
                        "convertedCurrencyCode": 643,
                        "cargoType": 1,
                        "isZeroOrder": False,
                        "wbStickerId": 123456,
                    }
                ]
            }
        )

        result = await api.get_new_orders_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NewOrdersListItem)
        assert result[0].sale_price == 504600
        assert result[0].comment == "Упакуйте в пленку, пожалуйста"
