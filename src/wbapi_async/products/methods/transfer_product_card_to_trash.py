from pydantic import Field

from ...types import RequestLimit
from ...types import TransferProductCardToTrashResponse
from ...methods.base import WbMethod


class TransferProductCardToTrash(WbMethod):
    """
    Transfers the product card to the trash. In doing so, the product card would not be deleted.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1delete~1trash/post
    """

    __return__ = TransferProductCardToTrashResponse
    __api__ = "content-api"
    __method__ = "content/v2/cards/delete/trash"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nm_i_ds: list[int] | None = Field(None, alias="nmIDs")
