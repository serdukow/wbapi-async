from pydantic import Field

from ...types import AddDataMatrixCodeToTheOrderResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class AddDataMatrixCodeToTheOrder(WbMethod):
    """
    This method allows you to assign a Data Matrix code (Chestny ZNAK marking) to an order. The
    assignmentof a Data Matrix code to an order is only possible if this field is returned in the
    responseof the [Get order
    metadata](/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get)
    methodand the order is in the `confirm` status.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta~1sgtin/put
    """

    __return__ = AddDataMatrixCodeToTheOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/orders/{order_id}/meta/sgtin"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    sgtins: list[str] | None = Field(None)
