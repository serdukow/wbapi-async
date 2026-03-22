from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProductCategoryCommissionResponse, RequestLimit


class GetProductCategoryCommission(WbMethod):
    """
    WB commission by parent categories of products according to sales model.

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Commissions/paths/~1api~1v1~1tariffs~1commission/get
    """

    __return__ = ProductCategoryCommissionResponse
    __api__ = "common-api"
    __method__ = "api/v1/tariffs/commission"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field(None)
