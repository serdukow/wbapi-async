from pydantic import Field

from ...types import AddImeiToTheAssemblyOrderResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class AddImeiToTheAssemblyOrder(WbMethod):
    """
    Sets the IMEI for the assembly order. The assembly order can have only one IMEI. If a device
    hastwo IMEIs — **IMEI** and **IMEI2** or **IMEI1** and **IMEI2** — you should only specify
    **IMEI**or **IMEI1**. You don't need to specify **IMEI2**. You can add the code only for
    assemblyorders in the `confirm` status.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1imei/put
    """

    __return__ = AddImeiToTheAssemblyOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/orders/{order_id}/meta/imei"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    imei: str = Field()
