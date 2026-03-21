from typing import Any

from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.update_contacts_list_response import UpdateContactsListResponse
from .base import WbMethod


class UpdateContactsList(WbMethod):
    """
    Updates the seller's warehouse contact list. <br>

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1dbw~1warehouses~1%7BwarehouseId%7D~1contacts/put
    """

    __return__ = UpdateContactsListResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/warehouses/{warehouse_id}/contacts"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    contacts: list[dict[str, Any]] | None = Field(None)
