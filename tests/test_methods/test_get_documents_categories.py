import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DocumentsCategoriesItem


@pytest.mark.unit
class TestGetDocumentsCategories:
    async def test_get_documents_categories(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "categories": [
                        {
                            "name": "name",
                            "title": "title",
                        }
                    ]
                }
            }
        )

        result = await api.get_documents_categories()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DocumentsCategoriesItem)
        assert result[0].name == "name"
        assert result[0].title == "title"
