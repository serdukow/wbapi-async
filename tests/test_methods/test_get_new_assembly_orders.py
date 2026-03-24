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
                        "address": {},
                        "ddate": "ddate",
                        "sellerDate": "sellerDate",
                        "salePrice": 1,
                        "requiredMeta": [],
                        "optionalMeta": [],
                        "deliveryType": "deliveryType",
                        "comment": "comment",
                        "scanPrice": 1.0,
                        "orderUid": "orderUid",
                        "article": "article",
                        "colorCode": "colorCode",
                        "rid": "rid",
                        "createdAt": "createdAt",
                        "offices": [],
                        "skus": [],
                        "id": 1,
                        "warehouseId": 1,
                        "officeId": 1,
                        "nmId": 1,
                        "chrtId": 1,
                        "price": 1,
                        "finalPrice": 1,
                        "convertedPrice": 1,
                        "convertedFinalPrice": 1,
                        "currencyCode": 1,
                        "convertedCurrencyCode": 1,
                        "cargoType": 1,
                        "crossBorderType": 1,
                        "isZeroOrder": True,
                        "options": {},
                    }
                ]
            }
        )

        result = await api.get_new_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NewAssemblyOrdersItem)
        assert result[0].address == {}
        assert result[0].ddate == "ddate"
        assert result[0].seller_date == "sellerDate"
