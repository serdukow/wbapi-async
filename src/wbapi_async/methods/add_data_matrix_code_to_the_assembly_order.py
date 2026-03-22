from pydantic import Field

from ..types.add_data_matrix_code_to_the_assembly_order_response import AddDataMatrixCodeToTheAssemblyOrderResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=1000, interval=60, burst=20)

    order_id: int = Field(alias="orderId", exclude=True)
    sgtins: list[str] | None = Field(None)
