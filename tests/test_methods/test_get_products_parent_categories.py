import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductsParentCategoriesResponse


@pytest.mark.unit
class TestGetProductsParentCategories:
    async def test_get_products_parent_categories(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": None,
                    "error": True,
                    "errorText": "errorText",
                    "additionalErrors": "additionalErrors",
                }
            ]
        )

        result = await api.get_products_parent_categories()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductsParentCategoriesResponse)
        assert result[0].error
        assert result[0].error_text == "errorText"
