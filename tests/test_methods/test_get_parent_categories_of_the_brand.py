import pytest

from wbapi_async.types.parent_categories_of_the_brand_item import ParentCategoriesOfTheBrandItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetParentCategoriesOfTheBrand:

    async def test_get_parent_categories_of_the_brand(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{
                "parentId": 1,
                "parentName": "parentName",
            }]
        }
        )

        result = await api.get_parent_categories_of_the_brand(brand="brand", date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ParentCategoriesOfTheBrandItem)
        assert result[0].parent_id == 1
        assert result[0].parent_name == "parentName"
