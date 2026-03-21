from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.upload_media_files_via_links_response import UploadMediaFilesViaLinksResponse
from .base import WbMethod


class UploadMediaFilesViaLinks(WbMethod):
    """
    Upload Media Files via Links

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Media-Files/paths/~1content~1v3~1media~1save/post
    """

    __return__ = UploadMediaFilesViaLinksResponse
    __api__ = "content-api"
    __method__ = "content/v3/media/save"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    nm_id: int | None = Field(None, alias="nmId")
    data: list[str] | None = Field(None)
