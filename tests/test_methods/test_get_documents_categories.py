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
                            "name": "redeem-notification",
                            "title": "Уведомление о выкупе",
                        }
                    ]
                }
            }
        )

        result = await api.get_documents_categories()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DocumentsCategoriesItem)
        assert result[0].name == "redeem-notification"
        assert result[0].title == "Уведомление о выкупе"
