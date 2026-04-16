import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CountryOfOriginResponse


@pytest.mark.unit
class TestGetCountryOfOrigin:
    async def test_get_country_of_origin(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": [{"name": "Электроника", "id": 479, "isVisible": True}],
                    "error": False,
                    "errorText": "",
                    "additionalErrors": "",
                }
            ]
        )

        result = await api.get_country_of_origin()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CountryOfOriginResponse)
        assert not result[0].error
        assert result[0].error_text == ""
        assert result[0].additional_errors == ""
