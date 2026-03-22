from pydantic import Field

from ...methods.base import WbMethod
from ...types import CreateWarehouseResponse, RequestLimit


class CreateWarehouse(WbMethod):
    """
    Creates a seller's warehouse. You cannot link an office that is already in use.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses/post
    """

    __return__ = CreateWarehouseResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/warehouses"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    name: str = Field()
    office_id: int = Field(alias="officeId")
