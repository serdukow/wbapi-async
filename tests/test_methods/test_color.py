import pytest

from wbapi_async.types.color_response import ColorResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestColor:

    async def test_color(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": None,
                "error": True,
                "errorText": "errorText",
                "additionalErrors": "additionalErrors",
            }]
        )

        result = await api.color()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ColorResponse)
        assert result[0].error == True
        assert result[0].error_text == "errorText"
