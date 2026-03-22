from pydantic import Field

from ..types.create_pass_response import CreatePassResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreatePass(WbMethod):
    """
    Creates a supplier pass. <br> The pass is valid for 48 hours from the time of creation.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes/post
    """

    __return__ = CreatePassResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/passes"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    first_name: str = Field(None, alias="firstName")
    last_name: str = Field(None, alias="lastName")
    car_model: str = Field(None, alias="carModel")
    car_number: str = Field(None, alias="carNumber")
    office_id: int = Field(None, alias="officeId")
