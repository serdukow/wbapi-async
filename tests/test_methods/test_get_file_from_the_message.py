import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetFileFromTheMessage:
    async def test_get_file_from_the_message(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.get_file_from_the_message(id="id")

        assert result is None
