import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import TagManagementInTheProductCardResponse


@pytest.mark.unit
class TestTagManagementInTheProductCard:
    async def test_tag_management_in_the_product_card(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "error": True,
                    "errorText": "errorText",
                    "additionalErrors": "additionalErrors",
                }
            ]
        )

        result = await api.tag_management_in_the_product_card()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TagManagementInTheProductCardResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
