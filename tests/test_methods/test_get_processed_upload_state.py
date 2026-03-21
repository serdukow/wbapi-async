import pytest

from wbapi_async.types.processed_upload_state_response import ProcessedUploadStateResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetProcessedUploadState:

    async def test_get_processed_upload_state(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": {},
                "error": True,
                "errorText": "errorText",
            }]
        )

        result = await api.get_processed_upload_state(upload_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProcessedUploadStateResponse)
        assert result[0].data == {}
        assert result[0].error == True
        assert result[0].error_text == "errorText"
