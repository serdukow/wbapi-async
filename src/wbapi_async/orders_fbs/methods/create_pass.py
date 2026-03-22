from pydantic import Field

from ...methods.base import WbMethod
from ...types import CreatePassResponse, RequestLimit


class CreatePass(WbMethod):
    """
    Creates a supplier pass. The pass is valid for 48 hours from the time of creation. Maximum of 1
    requestper 10 minutes per one seller's account

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes/post
    """

    __return__ = CreatePassResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/passes"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    car_model: str = Field(alias="carModel")
    car_number: str = Field(alias="carNumber")
    office_id: int = Field(alias="officeId")
