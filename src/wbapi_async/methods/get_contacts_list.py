from pydantic import Field

from ..types.contacts_list_item import ContactsListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetContactsList(WbMethod):
    """
    Returns a list of contacts linked to the seller's warehouse.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1dbw~1warehouses~1%7BwarehouseId%7D~1contacts/get
    """

    __return__ = ContactsListItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/warehouses/{warehouse_id}/contacts"
    __data_key__ = "contacts"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
