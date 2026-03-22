import pytest

from wbapi_async.types.supply_tariffs_response import SupplyTariffsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSupplyTariffs:

    async def test_get_supply_tariffs(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "date": "date",
                "coefficient": 1.0,
                "warehouseID": 1,
                "warehouseName": "warehouseName",
                "allowUnload": True,
                "boxTypeID": 1,
                "storageCoef": "storageCoef",
                "deliveryCoef": "deliveryCoef",
                "deliveryBaseLiter": "deliveryBaseLiter",
                "deliveryAdditionalLiter": "deliveryAdditionalLiter",
                "storageBaseLiter": "storageBaseLiter",
                "storageAdditionalLiter": "storageAdditionalLiter",
                "isSortingCenter": True,
            }]
        )

        result = await api.get_supply_tariffs()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SupplyTariffsResponse)
        assert result[0].date == "date"
        assert result[0].coefficient == 1.0
        assert result[0].warehouse_id == 1
