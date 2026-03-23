from pydantic import Field

from ...types import DeleteThePassResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class DeleteThePass(WbMethod):
    """
    Deletes the seller's pass

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes~1%7BpassId%7D/delete
    """

    __return__ = DeleteThePassResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/passes/{pass_id}"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    pass_id: int = Field(alias="passId", exclude=True)
