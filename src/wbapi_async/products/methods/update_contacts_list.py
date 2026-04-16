from pydantic import Field

from ...methods.base import WbMethod
from ...types import ContactsItem, RequestLimit, UpdateContactsListResponse


class UpdateContactsList(WbMethod):
    """
    Updates the seller's warehouse contact list.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1dbw~1warehouses~1%7BwarehouseId%7D~1contacts/put
    """

    __return__ = UpdateContactsListResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/warehouses/{warehouse_id}/contacts"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    contacts: list[ContactsItem] | None = Field(None)
