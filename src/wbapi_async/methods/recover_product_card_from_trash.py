from pydantic import Field

from ..types.recover_product_card_from_trash_response import RecoverProductCardFromTrashResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class RecoverProductCardFromTrash(WbMethod):
    """
    Returns the product card from trash

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1recover/post
    """

    __return__ = RecoverProductCardFromTrashResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/recover"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=5)

    nm_i_ds: list[int] | None = Field(None, alias="nmIDs")
