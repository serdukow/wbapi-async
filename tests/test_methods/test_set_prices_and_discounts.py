import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SetPricesAndDiscountsResponse


@pytest.mark.unit
class TestSetPricesAndDiscounts:
    async def test_set_prices_and_discounts(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "error": True,
                    "errorText": "errorText",
                }
            ]
        )

        result = await api.set_prices_and_discounts(data=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SetPricesAndDiscountsResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
