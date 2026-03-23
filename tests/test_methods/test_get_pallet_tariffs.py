import pytest

from wbapi_async.types import PalletTariffsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetPalletTariffs:

    async def test_get_pallet_tariffs(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "response": {
            "data": {
            "warehouseList": [{
                "palletDeliveryExpr": "palletDeliveryExpr",
                "palletDeliveryValueBase": "palletDeliveryValueBase",
                "palletDeliveryValueLiter": "palletDeliveryValueLiter",
                "palletStorageExpr": "palletStorageExpr",
                "palletStorageValueExpr": "palletStorageValueExpr",
                "warehouseName": "warehouseName",
            }]
        }
        }
        }
        )

        result = await api.get_pallet_tariffs(date="date")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PalletTariffsItem)
        assert result[0].pallet_delivery_expr == "palletDeliveryExpr"
        assert result[0].pallet_delivery_value_base == "palletDeliveryValueBase"
        assert result[0].pallet_delivery_value_liter == "palletDeliveryValueLiter"
