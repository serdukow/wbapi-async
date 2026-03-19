from pydantic import Field

from .base import BaseType


class Sale(BaseType):
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
    spp: int | None = Field(None, alias="spp")
    payment_sale_amount: int | None = Field(None, alias="paymentSaleAmount")
    for_pay: float | None = Field(None, alias="forPay")
    finished_price: float | None = Field(None, alias="finishedPrice")
    price_with_disc: float | None = Field(None, alias="priceWithDisc")
    sale_id: str | None = Field(None, alias="saleID")
    sticker: str | None = Field(None, alias="sticker")
    g_number: str | None = Field(None, alias="gNumber")
    srid: str | None = Field(None, alias="srid")
