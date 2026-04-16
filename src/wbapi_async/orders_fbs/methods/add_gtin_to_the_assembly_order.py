from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddGtinToTheAssemblyOrderResponse, RequestLimit


class AddGtinToTheAssemblyOrder(WbMethod):
    """
    Sets the GTIN (Belarus product unique identifier) for the assembly order. The assembly order
    canonly have one GTIN. You can add the code only for assembly orders in the `confirm` status.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1gtin/put
    """

    __return__ = AddGtinToTheAssemblyOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/orders/{order_id}/meta/gtin"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    gtin: str = Field(alias="gtin")
