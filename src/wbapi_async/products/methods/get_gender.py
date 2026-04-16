from pydantic import Field

from ...methods.base import WbMethod
from ...types import GenderItem, RequestLimit


class GetGender(WbMethod):
    """
    Provides values of gender characteristic.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1kinds/get
    """

    __return__ = GenderItem
    __api__ = "content-api"
    __method__ = "content/v2/directory/kinds"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field(None, alias="locale")
