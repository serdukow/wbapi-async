from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SuppliesIdResponse


class GetSuppliesId(WbMethod):
    """
    The method returns supply details by ID.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies~1%7BID%7D/get
    """

    __return__ = SuppliesIdResponse
    __api__ = "supplies-api"
    __method__ = ""
    __method_template__ = "api/v1/supplies/{id_}"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id_: int = Field(alias="ID", exclude=True)
    is_preorder_id: bool | None = Field(False, alias="isPreorderID")
