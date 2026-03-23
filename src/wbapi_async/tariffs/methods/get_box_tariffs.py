from pydantic import Field

from ...types import BoxTariffsItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetBoxTariffs(WbMethod):
    """
    For items inventory supplied to the warehouse in boxes, the method returns the
    [rates](https://seller.wildberries.ru/dynamic-product-categories):- for delivery from warehouse
    orsorting center to the buyer - for delivery from the buyer to the sorting center - for storage
    onWB warehouse

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Stock-Tariffs/paths/~1api~1v1~1tariffs~1box/get
    """

    __return__ = BoxTariffsItem
    __api__ = "common-api"
    __method__ = "api/v1/tariffs/box"
    __data_key__ = "response.data.warehouseList"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date: str = Field()
