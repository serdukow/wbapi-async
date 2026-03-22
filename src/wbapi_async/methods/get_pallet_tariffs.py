from pydantic import Field

from ..types.pallet_tariffs_item import PalletTariffsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetPalletTariffs(WbMethod):
    """
    For items supplied to the WB warehouse on pallets, the method returns the
    [cost](https://seller.wildberries.ru/dynamic-product-categories):

    Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Stock-Tariffs/paths/~1api~1v1~1tariffs~1pallet/get
    """

    __return__ = PalletTariffsItem
    __api__ = "common-api"
    __method__ = "api/v1/tariffs/pallet"
    __data_key__ = "response.data.warehouseList"

    request_limit: RequestLimit = RequestLimit(period=60, limit=60, interval=1, burst=5)

    date: str = Field(None)
