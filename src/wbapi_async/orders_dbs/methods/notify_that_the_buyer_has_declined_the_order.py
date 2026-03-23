from pydantic import Field

from ...types import NotifyThatTheBuyerHasDeclinedTheOrderResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class NotifyThatTheBuyerHasDeclinedTheOrder(WbMethod):
    """
    This method is deprecated. It will be removed on [April
    13](https://dev.wildberries.ru/en/release-notes?id=378)

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders~1%7BorderId%7D~1reject/patch
    """

    __return__ = NotifyThatTheBuyerHasDeclinedTheOrderResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbs/orders/{order_id}/reject"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    code: str | None = Field(None)
