import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DocumentsListItem


@pytest.mark.unit
class TestGetDocumentsList:
    async def test_get_documents_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "documents": [
                        {
                            "serviceName": "serviceName",
                            "name": "name",
                            "category": "category",
                            "extensions": [],
                            "creationTime": "creationTime",
                            "viewed": True,
                        }
                    ]
                }
            }
        )

        result = await api.get_documents_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DocumentsListItem)
        assert result[0].service_name == "serviceName"
        assert result[0].name == "name"
        assert result[0].category == "category"
