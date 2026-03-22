from pydantic import Field

from ...types.base import BaseType


class ReportItem(BaseType):
    """Get Report"""

    city_name: str | None = Field(None, alias="cityName")
    country_name: str | None = Field(None, alias="countryName")
    fo_name: str | None = Field(None, alias="foName")
    nm_id: int | None = Field(None, alias="nmID")
    region_name: str | None = Field(None, alias="regionName")
    sa: str | None = Field(None)
    sale_invoice_cost_price: float | None = Field(None, alias="saleInvoiceCostPrice")
    sale_invoice_cost_price_perc: float | None = Field(None, alias="saleInvoiceCostPricePerc")
    sale_item_invoice_qty: int | None = Field(None, alias="saleItemInvoiceQty")
