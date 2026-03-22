import pytest

from wbapi_async.types.new_assembly_orders_list_item import NewAssemblyOrdersListItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetNewAssemblyOrdersList:

    async def test_get_new_assembly_orders_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "ddate": "ddate",
                "salePrice": 1,
                "requiredMeta": [],
                "article": "article",
                "rid": "rid",
                "createdAt": "createdAt",
                "warehouseAddress": "warehouseAddress",
                "orderCode": "orderCode",
                "payMode": "payMode",
                "skus": [],
                "id": 1,
                "warehouseId": 1,
                "nmId": 1,
                "chrtId": 1,
                "price": 1,
                "finalPrice": 1,
                "convertedPrice": 1,
                "convertedFinalPrice": 1,
                "currencyCode": 1,
                "convertedCurrencyCode": 1,
                "cargoType": 1,
                "isZeroOrder": True,
            }]
        }
        )

        result = await api.get_new_assembly_orders_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NewAssemblyOrdersListItem)
        assert result[0].ddate == "ddate"
        assert result[0].sale_price == 1
        assert result[0].required_meta == []
