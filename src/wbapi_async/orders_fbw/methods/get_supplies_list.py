from pydantic import Field

from ...methods.base import WbMethod
from ...types import ModelsDateFilterRequest, RequestLimit, SuppliesListResponse
from ..enums.status_i_ds_item import StatusIDsItem


class GetSuppliesList(WbMethod):
    """
    The method returns a list of supplies, the last 1000 supplies by default.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies/post
    """

    __return__ = SuppliesListResponse
    __api__ = "supplies-api"
    __method__ = "api/v1/supplies"
    __http_method__ = "POST"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    limit: int | None = Field(1000)
    offset: int | None = Field(0)
    dates: list[ModelsDateFilterRequest] | None = Field(None)
    status_i_ds: list[StatusIDsItem] | None = Field(None, alias="statusIDs")
