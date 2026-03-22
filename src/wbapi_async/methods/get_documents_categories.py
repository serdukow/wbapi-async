from pydantic import Field

from ..types.documents_categories_item import DocumentsCategoriesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetDocumentsCategories(WbMethod):
    """
    Returns documents categories

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1categories/get
    """

    __return__ = DocumentsCategoriesItem
    __api__ = "documents-api"
    __method__ = "api/v1/documents/categories"
    __data_key__ = "data.categories"

    request_limit: RequestLimit = RequestLimit(period=10, limit=1, interval=10, burst=5)

    locale: str | None = Field("en")
