import pytest

from wbapi_async.types import LogisticsAndStorageCostsMultiplierItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetLogisticsAndStorageCostsMultiplier:

    async def test_get_logistics_and_storage_costs_multiplier(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "reports": [{
                "nmId": 1,
                "subjectName": "subjectName",
                "dimId": 1,
                "prcOver": 1.0,
                "volume": 1.0,
                "width": 1,
                "length": 1,
                "height": 1,
                "volumeSup": 1.0,
                "widthSup": 1,
                "lengthSup": 1,
                "heightSup": 1,
                "photoUrls": [],
                "dtBonus": "dtBonus",
                "isValid": True,
                "isValidDt": "isValidDt",
                "reversalAmount": 1.0,
                "penaltyAmount": 1.0,
            }]
        }
        }
        )

        result = await api.get_logistics_and_storage_costs_multiplier(date_to="date_to", limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LogisticsAndStorageCostsMultiplierItem)
        assert result[0].nm_id == 1
        assert result[0].subject_name == "subjectName"
        assert result[0].dim_id == 1
