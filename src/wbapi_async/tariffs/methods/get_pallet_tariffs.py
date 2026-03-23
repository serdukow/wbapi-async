from pydantic import Field

from ...types import PalletTariffsItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetPalletTariffs(WbMethod):
    """
    For items supplied to the WB warehouse on pallets, the method returns the
    [cost](https://seller.wildberries.ru/dynamic-product-categories):- of delivery from warehouse
    tothe buyer - of delivery from the buyer to warehouse - of storage on WB warehouse

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Stock-Tariffs/paths/~1api~1v1~1tariffs~1pallet/get
    """

    __return__ = PalletTariffsItem
    __api__ = "common-api"
    __method__ = "api/v1/tariffs/pallet"
    __data_key__ = "response.data.warehouseList"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date: str = Field()
