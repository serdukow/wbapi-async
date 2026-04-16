import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import LimitsForTheProductCardsResponse


@pytest.mark.unit
class TestGetLimitsForTheProductCards:
    async def test_get_limits_for_the_product_cards(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {"freeLimits": 1, "paidLimits": 1},
                    "error": True,
                    "errorText": "errorText",
                    "additionalErrors": "additionalErrors",
                }
            ]
        )

        result = await api.get_limits_for_the_product_cards()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], LimitsForTheProductCardsResponse)
        assert result[0].error
        assert result[0].error_text == "errorText"
        assert result[0].additional_errors == "additionalErrors"
