from pydantic import Field

from ...types import CancelTheOrderResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class CancelTheOrder(WbMethod):
    """
    Moves the assembly order to `cancel` status — canceled by the seller.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1cancel/patch
    """

    __return__ = CancelTheOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/orders/{order_id}/cancel"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
