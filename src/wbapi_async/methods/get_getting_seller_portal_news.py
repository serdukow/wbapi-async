from pydantic import Field

from ..types.getting_seller_portal_news_item import GettingSellerPortalNewsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetGettingSellerPortalNews(WbMethod):
    """
    The method allows getting news from the seller portal.

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/News-API/paths/~1api~1communications~1v2~1news/get
    """

    __return__ = GettingSellerPortalNewsItem
    __api__ = "common-api"
    __method__ = "api/communications/v2/news"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=10)

    from_: str | None = Field(None, alias="from")
    from_id: int | None = Field(None, alias="fromID")
