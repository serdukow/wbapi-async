import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import UploadMediaFilesViaLinksResponse


@pytest.mark.unit
class TestUploadMediaFilesViaLinks:
    async def test_upload_media_files_via_links(self, api: MockedAPI) -> None:
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

        result = await api.upload_media_files_via_links()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UploadMediaFilesViaLinksResponse)
        assert result[0].error
        assert result[0].error_text == "errorText"
