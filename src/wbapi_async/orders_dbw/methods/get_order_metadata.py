from pydantic import Field

from ...types import OrderMetadataItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetOrderMetadata(WbMethod):
    """
    Returns assembly order metadata. The list of metadata available for the assembly order can be
    obtainedin the [list of new assembly
    orders](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1new/get),
    field`requiredMeta`.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get
    """

    __return__ = OrderMetadataItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/dbw/orders/{order_id}/meta"
    __data_key__ = "meta.sgtin.value"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    order_id: int = Field(alias="orderId", exclude=True)
