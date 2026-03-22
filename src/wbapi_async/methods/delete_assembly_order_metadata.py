from pydantic import Field

from ..types.delete_assembly_order_metadata_response import DeleteAssemblyOrderMetadataResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteAssemblyOrderMetadata(WbMethod):
    """
    This method is deprecated. It will be removed on [May
    19](https://dev.wildberries.ru/en/release-notes?id=474)

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1v3~1click-collect~1orders~1%7BorderId%7D~1meta/delete
    """

    __return__ = DeleteAssemblyOrderMetadataResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/click-collect/orders/{order_id}/meta"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
    key: str = Field(None)
