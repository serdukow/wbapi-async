from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SupplyTariffsResponse


class GetSupplyTariffs(WbMethod):
    """
    The method returns the supply tariffs for specific warehouses for the next 14 days.

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Supply-Tariffs/paths/~1api~1tariffs~1v1~1acceptance~1coefficients/get
    """

    __return__ = SupplyTariffsResponse
    __api__ = "common-api"
    __method__ = "api/tariffs/v1/acceptance/coefficients"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    warehouse_ids: str | None = Field(None, alias="warehouseIDs")
