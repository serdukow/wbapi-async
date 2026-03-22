from pydantic import Field

from ..types.a_supplies_list_item import ASuppliesListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetASuppliesList(WbMethod):
    """
    Returns the supply list.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies/get
    """

    __return__ = ASuppliesListItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/supplies"
    __data_key__ = "supplies"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    limit: int = Field(None)
    next: int = Field(None)
