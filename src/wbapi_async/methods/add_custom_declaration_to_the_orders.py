from typing import Any

from pydantic import Field

from ..types.add_custom_declaration_to_the_orders_response import AddCustomDeclarationToTheOrdersResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddCustomDeclarationToTheOrders(WbMethod):
    """
    Sets the cargo customs declaration number in the metadata of the assembly orders.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1customs-declaration/post
    """

    __return__ = AddCustomDeclarationToTheOrdersResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/customs-declaration"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=500, interval=120, burst=20)

    orders: list[dict[str, Any]] | None = Field(None)
