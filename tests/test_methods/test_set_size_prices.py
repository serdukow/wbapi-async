import pytest

from wbapi_async.types.set_size_prices_response import SetSizePricesResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSetSizePrices:

    async def test_set_size_prices(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": {},
                "error": True,
                "errorText": "errorText",
            }]
        )

        result = await api.set_size_prices(data=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SetSizePricesResponse)
        assert result[0].data == {}
        assert result[0].error == True
        assert result[0].error_text == "errorText"
