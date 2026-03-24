import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DocumentsResponse


@pytest.mark.unit
class TestGetDocuments:
    async def test_get_documents(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                }
            ]
        )

        result = await api.get_documents()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DocumentsResponse)
        assert result[0].data == {}
