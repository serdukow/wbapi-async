import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import UnprocessedUploadStateResponse


@pytest.mark.unit
class TestGetUnprocessedUploadState:
    async def test_get_unprocessed_upload_state(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "error": True,
                    "errorText": "errorText",
                }
            ]
        )

        result = await api.get_unprocessed_upload_state(upload_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UnprocessedUploadStateResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
