from pydantic import Field

from ...methods.base import WbMethod
from ...types import DeleteAssemblyOrderMetadataResponse, RequestLimit


class DeleteAssemblyOrderMetadata(WbMethod):
    """
    Removes all assembly order metadata values for the passed key. Possible metadata are: - `imei`
    —
    [IMEI](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1imei/put)
    -`uin` —
    [UIN](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1uin/put)
    -`gtin` —
    [GTIN](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1gtin/put)
    -`sgtin` — [Data matrix
    code](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1sgtin/put)
    -`customsDeclaration` — [customs declaration
    number](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1%7BorderId%7D~1meta~1customs-declaration/put)

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta/delete
    """

    __return__ = DeleteAssemblyOrderMetadataResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/orders/{order_id}/meta"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    key: str | None = Field(None, alias="key")
