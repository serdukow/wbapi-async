import pytest

from wbapi_async.types import RetrieveInformationOnCompletedAssemblyOrdersItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetRetrieveInformationOnCompletedAssemblyOrders:

    async def test_get_retrieve_information_on_completed_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "article": "article",
                "cargoType": 1,
                "chrtId": 1,
                "createdAt": "createdAt",
                "price": 1,
                "finalPrice": 1,
                "convertedPrice": 1,
                "convertedFinalPrice": 1,
                "currencyCode": 1,
                "convertedCurrencyCode": 1,
                "id": 1,
                "isZeroOrder": True,
                "nmId": 1,
                "orderCode": "orderCode",
                "payMode": "payMode",
                "rid": "rid",
                "skus": [],
                "warehouseAddress": "warehouseAddress",
                "warehouseId": 1,
            }]
        }
        )

        result = await api.get_retrieve_information_on_completed_assembly_orders(limit=1, next=1, date_from=1, date_to=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], RetrieveInformationOnCompletedAssemblyOrdersItem)
        assert result[0].article == "article"
        assert result[0].cargo_type == 1
        assert result[0].chrt_id == 1
