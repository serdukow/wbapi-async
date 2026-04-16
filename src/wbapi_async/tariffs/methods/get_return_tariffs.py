from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, ReturnTariffsItem


class GetReturnTariffs(WbMethod):
    """
    Returns [tariffs](https://seller.wildberries.ru/dynamic-product-categories/return-cost): - on
    transferfrom Wildberries warehouse or sorting center to the seller - on transfer of returned
    productsthat were not picked up by seller

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Return-Cost-to-Seller/paths/~1api~1v1~1tariffs~1return/get
    """

    __return__ = ReturnTariffsItem
    __api__ = "common-api"
    __method__ = "api/v1/tariffs/return"
    __data_key__ = "response.data.warehouseList"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date: str = Field(alias="date")
