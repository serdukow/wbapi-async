from pydantic import Field

from ...types import AddUinUniqueIdentificationNumberToTheAssemblyOrderResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class AddUinUniqueIdentificationNumberToTheAssemblyOrder(WbMethod):
    """
    Sets the UIN for the assembly order. The assembly order can only have one UIN. You can add the
    codeonly for assembly orders in the `confirm` status.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1uin/put
    """

    __return__ = AddUinUniqueIdentificationNumberToTheAssemblyOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/orders/{order_id}/meta/uin"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    uin: str = Field()
