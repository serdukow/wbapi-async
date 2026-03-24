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
                    "error": True,
                    "errorText": "errorText",
                    "additionalErrors": "additionalErrors",
                }
            ]
        )

        result = await api.get_color()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ColorResponse)
        assert result[0].error
        assert result[0].error_text == "errorText"
