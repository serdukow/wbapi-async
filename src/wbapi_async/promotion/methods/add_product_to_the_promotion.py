from typing import Any

from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddProductToThePromotionResponse, RequestLimit


class AddProductToThePromotion(WbMethod):
    """
    Creates a product upload for the promotion. The upload status can be checked using [separate
    methods](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1tasks/get).

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Promotions-Calendar/paths/~1api~1v1~1calendar~1promotions~1upload/post
    """

    __return__ = AddProductToThePromotionResponse
    __api__ = "dp-calendar-api"
    __method__ = "api/v1/calendar/promotions/upload"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    data: dict[str, Any] | None = Field(None)
