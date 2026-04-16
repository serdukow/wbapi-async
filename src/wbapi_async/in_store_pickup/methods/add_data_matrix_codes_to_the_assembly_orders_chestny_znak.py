from pydantic import Field

from ...methods.base import WbMethod
from ...types import AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem, ApiSgtiNs, RequestLimit


class AddDataMatrixCodesToTheAssemblyOrdersChestnyZnak(WbMethod):
    """
    The method sets Data Matrix codes (Chestny ZNAK) to the [assembly orders
    metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).
    Youcan set the Data Matrix codes only for orders in the `confirm` status and if the field
    `sgtin`is returned in the response of the [Get order
    metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post)
    method.You can get the uploaded Data Matrix codes in the [assembly orders
    metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1sgtin/post
    """

    __return__ = AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/meta/sgtin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[ApiSgtiNs] = Field()
