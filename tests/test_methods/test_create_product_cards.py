import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CreateProductCardsResponse


@pytest.mark.unit
class TestCreateProductCards:
    async def test_create_product_cards(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "error": True,
                    "errorText": "errorText",
                    "additionalErrors": None,
                }
            ]
        )

        result = await api.create_product_cards()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreateProductCardsResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
