import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import TheReportsListItem


@pytest.mark.unit
class TestGetTheReportsList:
    async def test_get_the_reports_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": [
                    {
                        "id": "06eae887-9d9f-491f-b16a-bb1766fcb8d2",
                        "createdAt": "2024-06-26 20:05:32",
                        "status": "SUCCESS",
                        "name": "Card report",
                        "size": 123,
                        "startDate": "2024-06-21",
                        "endDate": "2023-04-23",
                    }
                ]
            }
        )

        result = await api.get_the_reports_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TheReportsListItem)
        assert result[0].id_ == "06eae887-9d9f-491f-b16a-bb1766fcb8d2"
        assert result[0].created_at == "2024-06-26 20:05:32"
        assert result[0].status == "SUCCESS"
        assert result[0].name == "Card report"
        assert result[0].size == 123
