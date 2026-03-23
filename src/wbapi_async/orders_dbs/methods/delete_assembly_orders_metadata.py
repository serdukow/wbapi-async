from pydantic import Field

from ...types import DeleteAssemblyOrdersMetadataItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class DeleteAssemblyOrdersMetadata(WbMethod):
    """
    Removes all [assembly order
    metadata](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post)
    values.You can only delete one type of metadata in one request. Specify the metadata type in
    therequest: - `imei` —
    [IMEI](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1imei/post)
    -`uin` —
    [UIN](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1uin/post)
    -`gtin` —
    [GTIN](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1gtin/post)
    -`sgtin` — [Data Matrix
    code](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1sgtin/post)
    -`customsDeclaration` — [customs declaration
    number](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1meta~1customs-declaration/post)

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1delete/post
    """

    __return__ = DeleteAssemblyOrdersMetadataItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/delete"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    key: str = Field()
    order_ids: list[int] = Field(alias="orderIds")
