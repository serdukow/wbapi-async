import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ColorResponse


@pytest.mark.unit
class TestGetColor:
    async def test_get_color(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": None,
                    "error": False,
                    "errorText": "",
                    "additionalErrors": "",
                }
            ]
        )

        result = await api.get_color()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ColorResponse)
        assert not result[0].error
        assert result[0].error_text == ""
        assert result[0].additional_errors == ""
