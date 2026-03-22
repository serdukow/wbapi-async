from typing import Any

from pydantic import Field

from ..types.add_data_matrix_codes_to_the_assembly_orders_chestny_znak_item import AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddDataMatrixCodesToTheAssemblyOrdersChestnyZnak(WbMethod):
    """
    The method sets Data Matrix codes (Chestny ZNAK) to the [assembly orders
    metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).<br><br>

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1sgtin/post
    """

    __return__ = AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/meta/sgtin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=20, interval=3, burst=500)

    orders: list[Any] = Field(None)
