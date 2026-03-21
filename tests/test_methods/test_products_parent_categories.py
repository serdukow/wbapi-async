import pytest

from wbapi_async.types.products_parent_categories_response import ProductsParentCategoriesResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestProductsParentCategories:

    async def test_products_parent_categories(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": None,
                "error": True,
                "errorText": "errorText",
                "additionalErrors": "additionalErrors",
            }]
        )

        result = await api.products_parent_categories()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductsParentCategoriesResponse)
        assert result[0].error == True
        assert result[0].error_text == "errorText"
