from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddDataMatrixCodeToTheAssemblyOrderResponse, RequestLimit


class AddDataMatrixCodeToTheAssemblyOrder(WbMethod):
    """
    The method allows attaching a Data Matrix code [Chestny ZNAK](https://chestnyznak.ru/en) to an
    assemblyorder.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1sgtin/put
    """

    __return__ = AddDataMatrixCodeToTheAssemblyOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/orders/{order_id}/meta/sgtin"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    sgtins: list[str] | None = Field(None, alias="sgtins")
