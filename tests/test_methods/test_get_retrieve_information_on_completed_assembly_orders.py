import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import RetrieveInformationOnCompletedAssemblyOrdersItem


@pytest.mark.unit
class TestGetRetrieveInformationOnCompletedAssemblyOrders:
    async def test_get_retrieve_information_on_completed_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "article": "wb6scpbwvp",
                        "cargoType": "1",
                        "chrtId": 12345676,
                        "createdAt": "2025-03-21T09:53:31Z",
                        "price": 5000,
                        "finalPrice": 5000,
                        "convertedPrice": 5000,
                        "convertedFinalPrice": 5000,
                        "currencyCode": 643,
                        "convertedCurrencyCode": 643,
                        "id": 123456789,
                        "isZeroOrder": False,
                        "nmId": 1234567898765,
                        "orderCode": "21117866-0006",
                        "payMode": "prepaid",
                        "rid": "5044304527347733263.0.0",
                        "skus": [],
                        "warehouseAddress": "Москва, район Якиманка, Софийская набережная, 4 с1",
                        "warehouseId": 1162157,
                    }
                ]
            }
        )

        result = await api.get_retrieve_information_on_completed_assembly_orders(
            limit=1, next_=1, date_from=1, date_to=1
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], RetrieveInformationOnCompletedAssemblyOrdersItem)
        assert result[0].article == "wb6scpbwvp"
        assert result[0].cargo_type == "1"
        assert result[0].chrt_id == 12345676
        assert result[0].created_at == "2025-03-21T09:53:31Z"
        assert result[0].price == 5000
