from typing import Any

from pydantic import Field

from ...types import AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class AddDataMatrixCodesToAssemblyOrdersChestnyZnak(WbMethod):
    """
    Sets the Data Matrix code (Chestny ZNAK marking) for the assembly orders. You can set the Data
    Matrixcode only for orders in the `confirm` status and if the field `sgtin` is returned in the
    responseof the [Get order
    metadata](orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post)
    method.For more information about Data Matrix Codes please check: https://chestnyznak.ru/en/.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1sgtin/post
    """

    __return__ = AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/meta/sgtin"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[Any] = Field()
