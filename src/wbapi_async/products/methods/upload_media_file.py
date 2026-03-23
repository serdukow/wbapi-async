from pydantic import Field

from ...types import RequestLimit
from ...types import UploadMediaFileResponse
from ...methods.base import WbMethod


class UploadMediaFile(WbMethod):
    """
    Uploads and adds one media file for the product card.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Media-Files/paths/~1content~1v3~1media~1file/post
    """

    __return__ = UploadMediaFileResponse
    __api__ = "content-api"
    __method__ = "content/v3/media/file"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    x_nm_id: str = Field(alias="X-Nm-Id")
    x_photo_number: int = Field(alias="X-Photo-Number")
