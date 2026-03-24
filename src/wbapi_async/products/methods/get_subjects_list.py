from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SubjectsListItem


class GetSubjectsList(WbMethod):
    """
    Returns the list of all available subjects, subjects parent categories and their IDs

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1object~1all/get
    """

    __return__ = SubjectsListItem
    __api__ = "content-api"
    __method__ = "content/v2/object/all"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field(None)
    name: str | None = Field(None)
    limit: int | None = Field(30)
    offset: int | None = Field(0)
    parent_id: int | None = Field(None, alias="parentID")
