from pydantic import Field

from ...methods.base import WbMethod
from ...types import ASuppliesListItem, RequestLimit


class GetASuppliesList(WbMethod):
    """
    Returns the supply list.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies/get
    """

    __return__ = ASuppliesListItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/supplies"
    __data_key__ = "supplies"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int = Field()
    next_: int = Field(alias="next")
