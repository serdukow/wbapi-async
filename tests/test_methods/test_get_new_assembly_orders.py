import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import NewAssemblyOrdersItem


@pytest.mark.unit
class TestGetNewAssemblyOrders:
    async def test_get_new_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "address": {
                            "fullAddress": "Chelyabinsk Region, Chelyabinsk, 51st Arabkir Street, Building 10A, Apartment 42",
                            "longitude": 44.519068,
                            "latitude": 40.20192,
                        },
                        "ddate": "17.05.2024",
                        "sellerDate": "02.06.2025",
                        "salePrice": 504600,
                        "requiredMeta": [],
                        "optionalMeta": [],
                        "deliveryType": "fbs",
                        "comment": "Упакуйте в плёнку, пожалуйста",
                        "scanPrice": 1.0,
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
                        "nmId": 123456789,
                        "chrtId": 987654321,
                        "price": 1014,
                        "finalPrice": 1014,
                        "convertedPrice": 28322,
                        "convertedFinalPrice": 1014,
                        "currencyCode": 933,
                        "convertedCurrencyCode": 643,
                        "cargoType": "1",
                        "crossBorderType": "0",
                        "isZeroOrder": False,
                        "options": {"isB2B": True},
                    }
                ]
            }
        )

        result = await api.get_new_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NewAssemblyOrdersItem)
        assert result[0].ddate == "17.05.2024"
        assert result[0].seller_date == "02.06.2025"
        assert result[0].sale_price == 504600
