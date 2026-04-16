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
                            "nmId": 123456789,
                            "subjectName": "",
                            "dimId": 123456789,
                            "volume": 1.0,
                            "width": 66,
                            "length": 54,
                            "height": 11,
                            "photoUrls": [],
                            "dt": "2025-04-01T00:06:00Z",
                        }
                    ]
                }
            }
        )

        result = await api.get_warehouse_measurements(date_to="date_to", limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WarehouseMeasurementsItem)
        assert result[0].nm_id == 123456789
        assert result[0].subject_name == ""
        assert result[0].dim_id == 123456789
        assert result[0].volume == 1.0
        assert result[0].width == 66
