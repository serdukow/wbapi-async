import pytest

from wbapi_async.types import UpdateProductCardsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestUpdateProductCards:

    async def test_update_product_cards(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": {},
                "error": True,
                "errorText": "errorText",
                "additionalErrors": None,
            }]
        )

        result = await api.update_product_cards()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UpdateProductCardsResponse)
        assert result[0].data == {}
        assert result[0].error == True
        assert result[0].error_text == "errorText"
