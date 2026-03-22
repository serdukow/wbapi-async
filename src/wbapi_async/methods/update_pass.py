from pydantic import Field

from ..types.update_pass_response import UpdatePassResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class UpdatePass(WbMethod):
    """
    Updates the seller's pass detail

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes~1%7BpassId%7D/put
    """

    __return__ = UpdatePassResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/passes/{pass_id}"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    pass_id: int = Field(alias="passId", exclude=True)
    first_name: str = Field(None, alias="firstName")
    last_name: str = Field(None, alias="lastName")
    car_model: str = Field(None, alias="carModel")
    car_number: str = Field(None, alias="carNumber")
    office_id: int = Field(None, alias="officeId")
