from pydantic import Field

from ...methods.base import WbMethod
from ...types import CheckIfTheOrderBelongsToTheBuyerResponse, RequestLimit


class CheckIfTheOrderBelongsToTheBuyer(WbMethod):
    """
    The method indicates whether the checked order belongs to the buyer based on the provided code.
    Availableif at least one assembly order from the order is in `prepare` status — ready for
    pickup.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders~1client~1identity/post
    """

    __return__ = CheckIfTheOrderBelongsToTheBuyerResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/click-collect/orders/client/identity"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_code: str | None = Field(None, alias="orderCode")
    passcode: str | None = Field(None)
