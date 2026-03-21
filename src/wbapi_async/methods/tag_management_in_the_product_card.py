from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.tag_management_in_the_product_card_response import (
    TagManagementInTheProductCardResponse,
)
from .base import WbMethod


class TagManagementInTheProductCard(WbMethod):
    """
    The method allows to add tags to the product card and remove tags from the product card.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1nomenclature~1link/post
    """

    __return__ = TagManagementInTheProductCardResponse
    __api__ = "content-api"
    __method__ = "content/v2/tag/nomenclature/link"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    nm_id: int | None = Field(None, alias="nmID")
    tags_i_ds: list[int] | None = Field(None, alias="tagsIDs")
