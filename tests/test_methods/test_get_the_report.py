import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetTheReport:

    async def test_get_the_report(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.get_the_report(download_id="download_id")

        assert result is None
