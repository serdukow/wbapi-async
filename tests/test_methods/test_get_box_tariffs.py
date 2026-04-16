import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import BoxTariffsItem


@pytest.mark.unit
class TestGetBoxTariffs:
    async def test_get_box_tariffs(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "response": {
                    "data": {
                        "warehouseList": [
                            {
                                "boxDeliveryBase": "48",
                                "boxDeliveryCoefExpr": "160",
                                "boxDeliveryLiter": "11,2",
                                "boxDeliveryMarketplaceBase": "40",
                                "boxDeliveryMarketplaceCoefExpr": "125",
                                "boxDeliveryMarketplaceLiter": "11",
                                "boxStorageBase": "0,14",
                                "boxStorageCoefExpr": "115",
                                "boxStorageLiter": "0,07",
                                "geoName": "Центральный федеральный округ",
                                "warehouseName": "Коледино",
                            }
                        ]
                    }
                }
            }
        )

        result = await api.get_box_tariffs(date="date")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BoxTariffsItem)
        assert result[0].box_delivery_base == "48"
        assert result[0].box_delivery_coef_expr == "160"
        assert result[0].box_delivery_liter == "11,2"
        assert result[0].box_delivery_marketplace_base == "40"
        assert result[0].box_delivery_marketplace_coef_expr == "125"
