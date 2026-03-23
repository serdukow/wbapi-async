from pydantic import Field

from ...types import CancelTheAssemblyOrderResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class CancelTheAssemblyOrder(WbMethod):
    """
    Moves the assembly orders to `cancel` ("Canceled by the supplier") status.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1%7BorderId%7D~1cancel/patch
    """

    __return__ = CancelTheAssemblyOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/orders/{order_id}/cancel"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
