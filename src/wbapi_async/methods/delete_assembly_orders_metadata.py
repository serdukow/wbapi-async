from pydantic import Field

from ..types.delete_assembly_orders_metadata_item import DeleteAssemblyOrdersMetadataItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteAssemblyOrdersMetadata(WbMethod):
    """
    Removes all [assembly order
    metadata](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post)
    values.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1delete/post
    """

    __return__ = DeleteAssemblyOrdersMetadataItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/delete"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=150, interval=400, burst=20)

    key: str = Field(None)
    order_ids: list[int] = Field(None, alias="orderIds")
