from pydantic import Field

from ..types.assembly_orders_metadata_item import AssemblyOrdersMetadataItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetAssemblyOrdersMetadata(WbMethod):
    """
    Returns [assembly orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)
    metadata.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post
    """

    __return__ = AssemblyOrdersMetadataItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/meta/info"
    __http_method__ = "POST"
    __data_key__ = "meta"

    request_limit: RequestLimit = RequestLimit(period=60, limit=150, interval=400, burst=20)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
