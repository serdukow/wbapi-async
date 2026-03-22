from pydantic import Field

from ...methods.base import WbMethod
from ...types import BrandsItem, RequestLimit


class GetBrands(WbMethod):
    """
    The method returns list of brands by subject ID.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1api~1content~1v1~1brands/get
    """

    __return__ = BrandsItem
    __api__ = "content-api"
    __method__ = "api/content/v1/brands"
    __data_key__ = "brands"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    subject_id: int = Field(alias="subjectId")
    next: int | None = Field(None)
