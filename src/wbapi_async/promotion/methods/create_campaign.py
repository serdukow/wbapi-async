from pydantic import Field

from ...enums import BidType
from ...enums import PaymentType
from ...types import CreateCampaignResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class CreateCampaign(WbMethod):
    """
    The method creates campaign: - with custom bid for promotion products in search and/or
    recommendations- with standard bid for promotion products both in search and recommendations

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1adv~1v2~1seacat~1save-ad/post
    """

    __return__ = CreateCampaignResponse
    __api__ = "advert-api"
    __method__ = "adv/v2/seacat/save-ad"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    name: str | None = Field(None)
    nms: list[int] | None = Field(None)
    bid_type: BidType | None = Field(BidType.MANUAL)
    payment_type: PaymentType | None = Field(PaymentType.CPM)
    placement_types: list[str] | None = Field(('search',))
