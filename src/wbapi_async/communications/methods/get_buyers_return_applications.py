from pydantic import Field

from ...methods.base import WbMethod
from ...types import BuyersReturnApplicationsItem, RequestLimit


class GetBuyersReturnApplications(WbMethod):
    """
    Returns buyers applications for product returns for the current 14 days.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Returns/paths/~1api~1v1~1claims/get
    """

    __return__ = BuyersReturnApplicationsItem
    __api__ = "returns-api"
    __method__ = "api/v1/claims"
    __data_key__ = "claims"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    is_archive: bool = Field(alias="is_archive")
    id_: str | None = Field(None, alias="id")
    limit: int | None = Field(50, alias="limit")
    offset: int | None = Field(0, alias="offset")
    nm_id: int | None = Field(None, alias="nm_id")
