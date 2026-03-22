from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, UpdatePassResponse


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    pass_id: int = Field(alias="passId", exclude=True)
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    car_model: str = Field(alias="carModel")
    car_number: str = Field(alias="carNumber")
    office_id: int = Field(alias="officeId")
