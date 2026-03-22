from pydantic import Field

from ...methods.base import WbMethod
from ...types import AssemblyOrdersMetadataItem, RequestLimit


class GetAssemblyOrdersMetadata(WbMethod):
    """
    The method returns metadata for [assembly
    orders](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get)by the list of
    theirIDs. You can get the list of metadata available for an assembly order in the
    `requiredMeta`and `optionalMeta` fields in the response of the [Get New Assembly
    Orders](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1new/get)method.
    Possiblemetadata: - `imei` —
    [IMEI](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1imei/put)
    -`uin` —
    [UIN](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1uin/put)
    -`gtin` —
    [GTIN](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1gtin/put)
    -`sgtin` — [Data matrix
    code](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1sgtin/put)
    -`expiration` — [Expiration
    date](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1expiration/put)
    -`customsDeclaration` — [customs declaration
    number](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1%7BorderId%7D~1meta~1customs-declaration/put)

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1meta/post
    """

    __return__ = AssemblyOrdersMetadataItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/orders/meta"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] = Field()
