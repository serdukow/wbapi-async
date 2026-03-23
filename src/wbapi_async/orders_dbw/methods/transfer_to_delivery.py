from pydantic import Field

from ...types import RequestLimit
from ...types import TransferToDeliveryResponse
from ...methods.base import WbMethod


class TransferToDelivery(WbMethod):
    """
    Transfers the [assembly
    order](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders/get)to the
    [status](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1status/post)
    `complete`— in delivery.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1assemble/patch
    """

    __return__ = TransferToDeliveryResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/orders/{order_id}/assemble"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
