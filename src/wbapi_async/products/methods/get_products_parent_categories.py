from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProductsParentCategoriesResponse, RequestLimit


class GetProductsParentCategories(WbMethod):
    """
    Returns the list of all products parent categories

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1object~1parent~1all/get
    """

    __return__ = ProductsParentCategoriesResponse
    __api__ = "content-api"
    __method__ = "content/v2/object/parent/all"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field(None)
