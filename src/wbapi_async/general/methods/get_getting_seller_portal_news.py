from pydantic import Field

from ...types import GettingSellerPortalNewsItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetGettingSellerPortalNews(WbMethod):
    """
    The method allows getting news from the seller portal. To receive a successful response, one of
    theparameters `from` or `fromID` must be specified. You can get up to 100 news items per
    request.

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/News-API/paths/~1api~1communications~1v2~1news/get
    """

    __return__ = GettingSellerPortalNewsItem
    __api__ = "common-api"
    __method__ = "api/communications/v2/news"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    from_: str | None = Field(None, alias="from")
    from_id: int | None = Field(None, alias="fromID")
