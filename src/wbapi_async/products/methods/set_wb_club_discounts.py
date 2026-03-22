from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SetWbClubDiscountsResponse


class SetWbClubDiscounts(WbMethod):
    """
    Sets WB Club subscription discounts.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task~1club-discount/post
    """

    __return__ = SetWbClubDiscountsResponse
    __api__ = "discounts-prices-api"
    __method__ = "api/v2/upload/task/club-discount"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    data: list[Any] = Field()
