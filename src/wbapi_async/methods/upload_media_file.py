from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.upload_media_file_response import UploadMediaFileResponse
from .base import WbMethod


class UploadMediaFile(WbMethod):
    """
    Upload Media File

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Media-Files/paths/~1content~1v3~1media~1file/post
    """

    __return__ = UploadMediaFileResponse
    __api__ = "content-api"
    __method__ = "content/v3/media/file"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    x_nm_id: str = Field(None, alias="X-Nm-Id")
    x_photo_number: int = Field(None, alias="X-Photo-Number")
