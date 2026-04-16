import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import NewAssemblyOrdersListItem


@pytest.mark.unit
class TestGetNewAssemblyOrdersList:
    async def test_get_new_assembly_orders_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "ddate": "ddate",
                        "salePrice": 504600,
                        "requiredMeta": [],
                        "article": "article",
                        "rid": "rid",
                        "createdAt": "createdAt",
                        "warehouseAddress": "warehouseAddress",
                        "orderCode": "orderCode",
                        "payMode": "prepaid",
                        "skus": [],
                        "id": 1,
                        "warehouseId": 1,
                        "nmId": 1,
                        "chrtId": 1,
                        "price": 1,
                        "finalPrice": 1014,
                        "convertedPrice": 5000,
                        "convertedFinalPrice": 1014,
                        "currencyCode": 643,
                        "convertedCurrencyCode": 643,
                        "cargoType": "1",
                        "isZeroOrder": True,
                    }
                ]
            }
        )

        result = await api.get_new_assembly_orders_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NewAssemblyOrdersListItem)
        assert result[0].ddate == "ddate"
        assert result[0].sale_price == 504600
        assert result[0].article == "article"
        assert result[0].rid == "rid"
