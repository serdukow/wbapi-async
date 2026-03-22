from pydantic import Field

from ..types.box_tariffs_item import BoxTariffsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetBoxTariffs(WbMethod):
    """
    For items inventory supplied to the warehouse in boxes, the method returns the
    [rates](https://seller.wildberries.ru/dynamic-product-categories):

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Stock-Tariffs/paths/~1api~1v1~1tariffs~1box/get
    """

    __return__ = BoxTariffsItem
    __api__ = "common-api"
    __method__ = "api/v1/tariffs/box"
    __data_key__ = "response.data.warehouseList"

    request_limit: RequestLimit = RequestLimit(period=60, limit=60, interval=1, burst=5)

    date: str = Field(None)
