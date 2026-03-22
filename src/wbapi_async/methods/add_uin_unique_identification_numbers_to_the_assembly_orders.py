from typing import Any

from pydantic import Field

from ..types.add_uin_unique_identification_numbers_to_the_assembly_orders_item import AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddUinUniqueIdentificationNumbersToTheAssemblyOrders(WbMethod):
    """
    The method sets the UIN (Unique Identification Numbers) for the [assembly orders
    metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1uin/post
    """

    __return__ = AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/meta/uin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=20, interval=3, burst=500)

    orders: list[Any] = Field(None)
