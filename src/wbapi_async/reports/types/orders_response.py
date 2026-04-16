from pydantic import Field

from ...types.base import BaseType


class OrdersResponse(BaseType):
    """Orders"""

    date: str | None = Field(None, alias="date")
    last_change_date: str | None = Field(None, alias="lastChangeDate")
    warehouse_name: str | None = Field(None, alias="warehouseName")
    warehouse_type: str | None = Field(None, alias="warehouseType")
    country_name: str | None = Field(None, alias="countryName")
    oblast_okrug_name: str | None = Field(None, alias="oblastOkrugName")
    region_name: str | None = Field(None, alias="regionName")
    supplier_article: str | None = Field(None, alias="supplierArticle")
    nm_id: int | None = Field(None, alias="nmId")
    barcode: str | None = Field(None, alias="barcode")
    category: str | None = Field(None, alias="category")
    subject: str | None = Field(None, alias="subject")
    brand: str | None = Field(None, alias="brand")
    tech_size: str | None = Field(None, alias="techSize")
    income_id: int | None = Field(None, alias="incomeID")
    is_supply: bool | None = Field(None, alias="isSupply")
    is_realization: bool | None = Field(None, alias="isRealization")
    total_price: float | None = Field(None, alias="totalPrice")
    discount_percent: int | None = Field(None, alias="discountPercent")
    spp: float | None = Field(None, alias="spp")
    finished_price: float | None = Field(None, alias="finishedPrice")
    price_with_disc: float | None = Field(None, alias="priceWithDisc")
    is_cancel: bool | None = Field(None, alias="isCancel")
    cancel_date: str | None = Field(None, alias="cancelDate")
    sticker: str | None = Field(None, alias="sticker")
    g_number: str | None = Field(None, alias="gNumber")
    srid: str | None = Field(None, alias="srid")
