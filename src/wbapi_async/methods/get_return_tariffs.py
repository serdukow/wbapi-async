from pydantic import Field

from ..types.return_tariffs_item import ReturnTariffsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetReturnTariffs(WbMethod):
    """
    Returns [tariffs](https://seller.wildberries.ru/dynamic-product-categories/return-cost):

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Return-Cost-to-Seller/paths/~1api~1v1~1tariffs~1return/get
    """

    __return__ = ReturnTariffsItem
    __api__ = "common-api"
    __method__ = "api/v1/tariffs/return"
    __data_key__ = "response.data.warehouseList"

    request_limit: RequestLimit = RequestLimit(period=60, limit=60, interval=1, burst=5)

    date: str = Field(None)
