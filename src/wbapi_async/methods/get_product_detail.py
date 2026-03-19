from __future__ import annotations

from pydantic import Field

from ..types.product_detail import ProductDetail
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetProductDetail(WbMethod):
    __return__ = ProductDetail
    __api__ = ""
    __method__ = ""
    __url__ = "https://card.wb.ru/cards/v4/detail"
    __unofficial__ = True
    __data_key__ = "products"

    request_limit: RequestLimit = RequestLimit(period=60, limit=60, interval=1000, burst=5)

    nm: int = Field(alias="nm")
    dest: int = Field(..., alias="dest")
    spp: int | None = Field(None, alias="spp")
    rate: int | None = Field(None, alias="rate")
