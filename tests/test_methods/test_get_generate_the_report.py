import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import GenerateTheReportResponse


@pytest.mark.unit
class TestGetGenerateTheReport:
    async def test_get_generate_the_report(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {"taskId": "taskId"},
                }
            ]
        )

        result = await api.get_generate_the_report(date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GenerateTheReportResponse)
