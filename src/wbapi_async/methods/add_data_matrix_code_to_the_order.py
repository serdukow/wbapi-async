from pydantic import Field

from ..types.add_data_matrix_code_to_the_order_response import AddDataMatrixCodeToTheOrderResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddDataMatrixCodeToTheOrder(WbMethod):
    """
    This method is deprecated. It will be removed on [April
    13](https://dev.wildberries.ru/en/release-notes?id=378)

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1v3~1dbs~1orders~1%7BorderId%7D~1meta~1sgtin/put
    """

    __return__ = AddDataMatrixCodeToTheOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbs/orders/{order_id}/meta/sgtin"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    sgtins: list[str] | None = Field(None)
