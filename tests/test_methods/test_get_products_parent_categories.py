import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductsParentCategoriesResponse


@pytest.mark.unit
class TestGetProductsParentCategories:
    async def test_get_products_parent_categories(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": [{"name": "Электроника", "id": 479, "isVisible": True}],
                    "error": False,
                    "errorText": "",
                    "additionalErrors": "",
                }
            ]
        )

        result = await api.get_products_parent_categories()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductsParentCategoriesResponse)
        assert not result[0].error
        assert result[0].error_text == ""
        assert result[0].additional_errors == ""
