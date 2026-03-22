from typing import Any

from pydantic import Field

from ..types.add_data_matrix_codes_to_assembly_orders_chestny_znak_item import AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddDataMatrixCodesToAssemblyOrdersChestnyZnak(WbMethod):
    """
    Sets the Data Matrix code (Chestny ZNAK marking) for the assembly orders. <br>

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1sgtin/post
    """

    __return__ = AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/sgtin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=500, interval=120, burst=20)

    orders: list[Any] = Field(None)
