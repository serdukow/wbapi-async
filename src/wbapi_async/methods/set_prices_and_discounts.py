from typing import Any

from pydantic import Field

from ..types.set_prices_and_discounts_response import SetPricesAndDiscountsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class SetPricesAndDiscounts(WbMethod):
    """
    Sets prices and discounts.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task/post
    """

    __return__ = SetPricesAndDiscountsResponse
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/upload/task"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    data: list[Any] = Field(None)
