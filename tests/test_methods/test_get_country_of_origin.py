import pytest

from wbapi_async.types.country_of_origin_response import CountryOfOriginResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetCountryOfOrigin:

    async def test_get_country_of_origin(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": None,
                "error": True,
                "errorText": "errorText",
                "additionalErrors": "additionalErrors",
            }]
        )

        result = await api.get_country_of_origin()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CountryOfOriginResponse)
        assert result[0].error == True
        assert result[0].error_text == "errorText"
