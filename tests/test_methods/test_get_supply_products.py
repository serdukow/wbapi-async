import pytest

from wbapi_async.types.supply_product import SupplyProduct

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSupplyProducts:

    async def test_get_supply_products(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "barcode": "1234567891234",
                    "vendorCode": "wb4sewt0vg",
                    "nmID": 987456654,
                    "needKiz": True,
                    "tnved": "6204430000",
                    "techSize": "C",
                    "color": "красный",
                    "supplierBoxAmount": 10,
                    "quantity": 10,
                    "readyForSaleQuantity": 0,
                    "unloadingQuantity": 0,
                    "acceptedQuantity": 0,
                }
            ]
        )

        result = await api.get_supply_products(supply_id=26596368)

        assert isinstance(result, list)
        assert len(result) == 1

        item = result[0]
        assert isinstance(item, SupplyProduct)
        assert item.barcode == "1234567891234"
        assert item.vendor_code == "wb4sewt0vg"
        assert item.nm_id == 987456654
        assert item.need_kiz is True
        assert item.tnved == "6204430000"
        assert item.tech_size == "C"
        assert item.color == "красный"
        assert item.supplier_box_amount == 10
        assert item.quantity == 10
        assert item.ready_for_sale_quantity == 0
        assert item.unloading_quantity == 0
        assert item.accepted_quantity == 0

    async def test_url_contains_supply_id(self, api: MockedAPI) -> None:
        api.add_response([])

        await api.get_supply_products(supply_id=12345)

        request = api.get_last_request()
        assert "12345" in request.url
