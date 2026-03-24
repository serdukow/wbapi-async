import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import RegenerateTheReportResponse


@pytest.mark.unit
class TestRegenerateTheReport:
    async def test_regenerate_the_report(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": "data",
                }
            ]
        )

        result = await api.regenerate_the_report()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], RegenerateTheReportResponse)
        assert result[0].data == "data"
