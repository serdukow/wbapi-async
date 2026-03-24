import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SetSizePricesResponse


@pytest.mark.unit
class TestSetSizePrices:
    async def test_set_size_prices(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "error": True,
                    "errorText": "errorText",
                }
            ]
        )

        result = await api.set_size_prices(data=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SetSizePricesResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
