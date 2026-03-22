import pytest

from wbapi_async.types.create_the_report_response import CreateTheReportResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetCreateTheReport:

    async def test_get_create_the_report(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": {},
            }]
        )

        result = await api.get_create_the_report()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreateTheReportResponse)
        assert result[0].data == {}
