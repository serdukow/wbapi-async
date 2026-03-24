import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import WarehouseMeasurementsItem


@pytest.mark.unit
class TestGetWarehouseMeasurements:
    async def test_get_warehouse_measurements(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "reports": [
                        {
                            "nmId": 1,
                            "subjectName": "subjectName",
                            "dimId": 1,
                            "volume": 1.0,
                            "width": 1,
                            "length": 1,
                            "height": 1,
                            "photoUrls": [],
                            "dt": "dt",
                        }
                    ]
                }
            }
        )

        result = await api.get_warehouse_measurements(date_to="date_to", limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WarehouseMeasurementsItem)
        assert result[0].nm_id == 1
        assert result[0].subject_name == "subjectName"
        assert result[0].dim_id == 1
