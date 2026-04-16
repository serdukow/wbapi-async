from pydantic import Field

from ...methods.base import WbMethod
from ...types import HscodesItem, RequestLimit


class GetHscodes(WbMethod):
    """
    The method provides list of HS-codes by category name and filter by HS-code.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1tnved/get
    """

    __return__ = HscodesItem
    __api__ = "content-api"
    __method__ = "content/v2/directory/tnved"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    subject_id: int = Field(alias="subjectID")
    search: int | None = Field(None, alias="search")
    locale: str | None = Field(None, alias="locale")
