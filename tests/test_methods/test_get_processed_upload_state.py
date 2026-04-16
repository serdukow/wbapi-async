import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProcessedUploadStateResponse


@pytest.mark.unit
class TestGetProcessedUploadState:
    async def test_get_processed_upload_state(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {
                        "uploadID": 395643565,
                        "status": 3,
                        "uploadDate": "2022-08-21T22:00:13+02:00",
                        "activationDate": "2022-08-21T22:00:13+02:00",
                        "overAllGoodsNumber": 1,
                        "successGoodsNumber": 1,
                    },
                    "error": False,
                    "errorText": "",
                }
            ]
        )

        result = await api.get_processed_upload_state(upload_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProcessedUploadStateResponse)
        assert not result[0].error
        assert result[0].error_text == ""
