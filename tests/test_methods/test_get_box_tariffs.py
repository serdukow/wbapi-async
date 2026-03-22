import pytest

from wbapi_async.types import BoxTariffsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetBoxTariffs:

    async def test_get_box_tariffs(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "response": {
            "data": {
            "warehouseList": [{
                "boxDeliveryBase": "boxDeliveryBase",
                "boxDeliveryCoefExpr": "boxDeliveryCoefExpr",
                "boxDeliveryLiter": "boxDeliveryLiter",
                "boxDeliveryMarketplaceBase": "boxDeliveryMarketplaceBase",
                "boxDeliveryMarketplaceCoefExpr": "boxDeliveryMarketplaceCoefExpr",
                "boxDeliveryMarketplaceLiter": "boxDeliveryMarketplaceLiter",
                "boxStorageBase": "boxStorageBase",
                "boxStorageCoefExpr": "boxStorageCoefExpr",
                "boxStorageLiter": "boxStorageLiter",
                "geoName": "geoName",
                "warehouseName": "warehouseName",
            }]
        }
        }
        }
        )

        result = await api.get_box_tariffs(date="date")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BoxTariffsItem)
        assert result[0].box_delivery_base == "boxDeliveryBase"
        assert result[0].box_delivery_coef_expr == "boxDeliveryCoefExpr"
        assert result[0].box_delivery_liter == "boxDeliveryLiter"
