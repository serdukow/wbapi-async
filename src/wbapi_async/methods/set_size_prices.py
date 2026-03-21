from typing import Any

from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.set_size_prices_response import SetSizePricesResponse
from .base import WbMethod


class SetSizePrices(WbMethod):
    """
    Sets different prices for different sizes.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task~1size/post
    """

    __return__ = SetSizePricesResponse
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/upload/task/size"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    data: list[Any] = Field(None)
