import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import LogisticsAndStorageCostsMultiplierItem


@pytest.mark.unit
class TestGetLogisticsAndStorageCostsMultiplier:
    async def test_get_logistics_and_storage_costs_multiplier(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "reports": [
                        {
                            "nmId": 123456789,
                            "subjectName": "Костюмы спортивные",
                            "dimId": 123456789,
                            "prcOver": 130.71,
                            "volume": 6.47,
                            "width": 7,
                            "length": 28,
                            "height": 33,
                            "volumeSup": 4.95,
                            "widthSup": 8,
                            "lengthSup": 33,
                            "heightSup": 33,
                            "photoUrls": [],
                            "dtBonus": "2025-06-02T00:00:00Z",
                            "isValid": True,
                            "isValidDt": "2025-05-29T13:35:57Z",
                            "reversalAmount": 0,
                            "penaltyAmount": 449.83,
                        }
                    ]
                }
            }
        )

        result = await api.get_logistics_and_storage_costs_multiplier(date_to="date_to", limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LogisticsAndStorageCostsMultiplierItem)
        assert result[0].nm_id == 123456789
        assert result[0].subject_name == "Костюмы спортивные"
        assert result[0].dim_id == 123456789
        assert result[0].prc_over == 130.71
        assert result[0].volume == 6.47
