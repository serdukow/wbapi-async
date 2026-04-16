import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PalletTariffsItem


@pytest.mark.unit
class TestGetPalletTariffs:
    async def test_get_pallet_tariffs(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "response": {
                    "data": {
                        "warehouseList": [
                            {
                                "palletDeliveryExpr": "170",
                                "palletDeliveryValueBase": "51",
                                "palletDeliveryValueLiter": "11,9",
                                "palletStorageExpr": "155",
                                "palletStorageValueExpr": "35.65",
                                "warehouseName": "Коледино",
                            }
                        ]
                    }
                }
            }
        )

        result = await api.get_pallet_tariffs(date="date")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PalletTariffsItem)
        assert result[0].pallet_delivery_expr == "170"
        assert result[0].pallet_delivery_value_base == "51"
        assert result[0].pallet_delivery_value_liter == "11,9"
        assert result[0].pallet_storage_expr == "155"
        assert result[0].pallet_storage_value_expr == "35.65"
