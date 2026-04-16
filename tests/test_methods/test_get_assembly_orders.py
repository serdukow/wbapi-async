import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AssemblyOrdersItem


@pytest.mark.unit
class TestGetAssemblyOrders:
    async def test_get_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "address": {
                            "fullAddress": "Chelyabinsk Region, Chelyabinsk, 51st Arabkir Street, Building 10A, Apartment 42",
                            "longitude": 44.519068,
                            "latitude": 40.20192,
                        },
                        "scanPrice": 1500,
                        "deliveryType": "fbs",
                        "supplyId": "WB-GI-92937123",
                        "orderUid": "165918930_629fbc924b984618a44354475ca58675",
                        "article": "one-ring-7548",
                        "colorCode": "RAL 3017",
                        "rid": "f884001e44e511edb8780242ac120002",
                        "createdAt": "2022-05-04T07:56:29Z",
                        "offices": [],
                        "skus": [],
                        "id": 13833711,
                        "warehouseId": 658434,
                        "officeId": 123,
                        "nmId": 12345678,
                        "chrtId": 987654321,
                        "price": 1014,
                        "convertedPrice": 28322,
                        "currencyCode": 933,
                        "convertedCurrencyCode": 643,
                        "cargoType": 1,
                        "crossBorderType": 0,
                        "comment": "Упакуйте в плёнку, пожалуйста",
                        "isZeroOrder": False,
                        "options": {"isB2B": True},
                    }
                ]
            }
        )

        result = await api.get_assembly_orders(limit=1, next_=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrdersItem)
        assert result[0].scan_price == 1500
        assert result[0].delivery_type == "fbs"
        assert result[0].supply_id == "WB-GI-92937123"
        assert result[0].order_uid == "165918930_629fbc924b984618a44354475ca58675"
