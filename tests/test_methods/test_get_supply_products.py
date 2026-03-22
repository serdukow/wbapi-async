import pytest

from wbapi_async.types import SupplyProductsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSupplyProducts:

    async def test_get_supply_products(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "barcode": "barcode",
                "vendorCode": "vendorCode",
                "nmID": 1,
                "needKiz": True,
                "tnved": "tnved",
                "techSize": "techSize",
                "color": "color",
                "supplierBoxAmount": 1,
                "quantity": 1,
                "readyForSaleQuantity": 1,
                "acceptedQuantity": 1,
                "unloadingQuantity": 1,
            }]
        )

        result = await api.get_supply_products(id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SupplyProductsResponse)
        assert result[0].barcode == "barcode"
        assert result[0].vendor_code == "vendorCode"
        assert result[0].nm_id == 1
