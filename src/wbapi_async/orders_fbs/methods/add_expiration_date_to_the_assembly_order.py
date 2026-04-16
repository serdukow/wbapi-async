from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddExpirationDateToTheAssemblyOrderResponse, RequestLimit


class AddExpirationDateToTheAssemblyOrder(WbMethod):
    """
    Sets the expiration date for the assembly order. The expiration date can only be added for
    assemblyorders that are delivered by WB and are in the `confirm` status. You can get the
    uploadeddata in the [metadata of the assembly
    order](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1meta/post).To
    changethe expiration date, send a request with the new date. It is impossible to remove the
    expirationdate from the metadata of the assembly order.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1expiration/put
    """

    __return__ = AddExpirationDateToTheAssemblyOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/orders/{order_id}/meta/expiration"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    expiration: str | None = Field(None, alias="expiration")
