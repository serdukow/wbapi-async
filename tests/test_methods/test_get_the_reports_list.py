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
                        "id": "id",
                        "createdAt": "createdAt",
                        "status": "status",
                        "name": "name",
                        "size": 1,
                        "startDate": "startDate",
                        "endDate": "endDate",
                    }
                ]
            }
        )

        result = await api.get_the_reports_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TheReportsListItem)
        assert result[0].id == "id"
        assert result[0].created_at == "createdAt"
        assert result[0].status == "status"
