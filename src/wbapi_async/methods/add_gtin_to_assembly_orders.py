from typing import Any

from pydantic import Field

from ..types.add_gtin_to_assembly_orders_item import AddGtinToAssemblyOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddGtinToAssemblyOrders(WbMethod):
    """
    Sets the GTIN, Belarus product unique identifier, for the assembly order
    metadata(./orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).
    <br>

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1gtin/post
    """

    __return__ = AddGtinToAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/gtin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=500, interval=120, burst=20)

    orders: list[Any] = Field(None)
