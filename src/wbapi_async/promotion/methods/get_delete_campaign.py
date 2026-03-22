from pydantic import Field

from ...methods.base import WbMethod
from ...types import DeleteCampaignResponse, RequestLimit


class GetDeleteCampaign(WbMethod):
    """
    The method allows to delete campaigns in the status `4` — ready to launch.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1delete/get
    """

    __return__ = DeleteCampaignResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/delete"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: int = Field()
