from pydantic import Field

from ..types.add_custom_declaration_number_to_the_order_response import AddCustomDeclarationNumberToTheOrderResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddCustomDeclarationNumberToTheOrder(WbMethod):
    """
    The method updates the customs declaration number in the [metadata of the assembly
    order](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1meta/post).

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1%7BorderId%7D~1meta~1customs-declaration/put
    """

    __return__ = AddCustomDeclarationNumberToTheOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/marketplace/v3/orders/{order_id}/meta/customs-declaration"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1000, interval=60, burst=20)

    order_id: int = Field(alias="orderId", exclude=True)
    customs_declaration: str | None = Field(None, alias="customsDeclaration")
