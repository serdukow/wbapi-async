from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, TagManagementInTheProductCardResponse


class TagManagementInTheProductCard(WbMethod):
    """
    The method allows to add tags to the product card and remove tags from the product card. When
    removinga tag from a product card, the tag itself is not removed. It is possible to add 15 tags
    toa product card.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1nomenclature~1link/post
    """

    __return__ = TagManagementInTheProductCardResponse
    __api__ = "content-api"
    __method__ = "content/v2/tag/nomenclature/link"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nm_id: int | None = Field(None, alias="nmID")
    tags_i_ds: list[int] | None = Field(None, alias="tagsIDs")
