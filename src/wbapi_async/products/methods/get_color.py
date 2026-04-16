from pydantic import Field

from ...methods.base import WbMethod
from ...types import ColorResponse, RequestLimit


class GetColor(WbMethod):
    """
    Provides values of color characteristic.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1colors/get
    """

    __return__ = ColorResponse
    __api__ = "content-api"
    __method__ = "content/v2/directory/colors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field(None, alias="locale")
