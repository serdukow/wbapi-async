from pydantic import Field

from ...types import AddGtinToTheOrderResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class AddGtinToTheOrder(WbMethod):
    """
    Sets the GTIN (Belarus product unique identifier) for the order. The order can only have one
    GTIN.You can add the code only for orders in the `confirmed` status.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta~1gtin/put
    """

    __return__ = AddGtinToTheOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/orders/{order_id}/meta/gtin"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    gtin: str = Field()
