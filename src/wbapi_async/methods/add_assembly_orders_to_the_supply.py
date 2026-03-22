from pydantic import Field

from ..types.add_assembly_orders_to_the_supply_response import AddAssemblyOrdersToTheSupplyResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddAssemblyOrdersToTheSupply(WbMethod):
    """
    The method adds up to 100 [assembly
    orders](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get)to the supply
    andmoves it to the `confirm`
    [status](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1status/post).

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1marketplace~1v3~1supplies~1%7BsupplyId%7D~1orders/patch
    """

    __return__ = AddAssemblyOrdersToTheSupplyResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/marketplace/v3/supplies/{supply_id}/orders"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    supply_id: str = Field(alias="supplyId", exclude=True)
    orders: list[int] | None = Field(None)
