from pydantic import Field

from ...methods.base import WbMethod
from ...types import Good, RequestLimit, SetPricesAndDiscountsResponse


class SetPricesAndDiscounts(WbMethod):
    """
    Sets prices and discounts.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task/post
    """

    __return__ = SetPricesAndDiscountsResponse
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/upload/task"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    data: list[Good] = Field()
