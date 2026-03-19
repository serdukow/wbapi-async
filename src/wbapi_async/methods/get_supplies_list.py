from pydantic import Field

from ..enums.supply_dates_type import SupplyDatesType
from ..enums.supply_status import SupplyStatus
from ..types.base import BaseType
from ..types.request_limit import RequestLimit
from ..types.supply import Supply
from .base import WbMethod


class SupplyDateFilter(BaseType):
    from_: str = Field(alias="from")
    till: str = Field(alias="till")
    type: SupplyDatesType = Field(alias="type")


class GetSuppliesList(WbMethod):
    """
    Returns a list of supplies (last 1000 by default).

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies/post
    """

    __return__ = Supply
    __api__ = "supplies-api"
    __method__ = "api/v1/supplies"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=30, interval=2000, burst=10)

    dates: list[SupplyDateFilter] = Field(alias="dates")
    limit: int | None = Field(1000, alias="limit")
    offset: int = Field(0, alias="offset")
    status_ids: list[SupplyStatus] | None = Field(None, alias="statusIDs")
