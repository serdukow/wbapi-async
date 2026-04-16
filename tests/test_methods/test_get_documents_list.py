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
                            "serviceName": "redeem-notification-44841941",
                            "name": "redeem-notification",
                            "category": "Уведомление о выкупе",
                            "extensions": [],
                            "creationTime": "2023-10-03T00:18:06.879Z",
                            "viewed": False,
                        }
                    ]
                }
            }
        )

        result = await api.get_documents_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DocumentsListItem)
        assert result[0].service_name == "redeem-notification-44841941"
        assert result[0].name == "redeem-notification"
        assert result[0].category == "Уведомление о выкупе"
        assert result[0].creation_time == "2023-10-03T00:18:06.879Z"
