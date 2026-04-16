from pydantic import Field

from ...methods.base import WbMethod
from ...types import DeleteOrderMetadataResponse, RequestLimit


class DeleteOrderMetadata(WbMethod):
    """
    Removes all order metadata values for the passed key. Possible metadata is `imei`, `uin`,
    `gtin`,`sgtin`.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/delete
    """

    __return__ = DeleteOrderMetadataResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/orders/{order_id}/meta"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    key: str | None = Field(None, alias="key")
