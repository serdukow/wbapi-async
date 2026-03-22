from pydantic import Field

from ..types.supply_tariffs_response import SupplyTariffsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSupplyTariffs(WbMethod):
    """
    The method returns the supply tariffs for specific warehouses for the next 14 days.

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Supply-Tariffs/paths/~1api~1tariffs~1v1~1acceptance~1coefficients/get
    """

    __return__ = SupplyTariffsResponse
    __api__ = "common-api"
    __method__ = "api/tariffs/v1/acceptance/coefficients"

    request_limit: RequestLimit = RequestLimit(period=60, limit=6, interval=10, burst=6)

    warehouse_i_ds: str | None = Field(None, alias="warehouseIDs")
