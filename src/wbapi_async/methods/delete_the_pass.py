from pydantic import Field

from ..types.delete_the_pass_response import DeleteThePassResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    pass_id: int = Field(alias="passId", exclude=True)
