import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import RegenerateTheReportResponse


@pytest.mark.unit
class TestGetRegenerateTheReport:
    async def test_get_regenerate_the_report(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": "Retry",
                }
            ]
        )

        result = await api.get_regenerate_the_report()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], RegenerateTheReportResponse)
        assert result[0].data == "Retry"
