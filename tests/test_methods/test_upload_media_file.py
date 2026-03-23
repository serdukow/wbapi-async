import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import UploadMediaFileResponse


@pytest.mark.unit
class TestUploadMediaFile:
    async def test_upload_media_file(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "error": True,
                    "errorText": "errorText",
                    "additionalErrors": {},
                }
            ]
        )

        result = await api.upload_media_file(x_nm_id="x_nm_id", x_photo_number=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UploadMediaFileResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
