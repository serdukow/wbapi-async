from pydantic import Field

from ...types.base import BaseType


class PaidStorageTasksTaskIdDownloadResponse(BaseType):
    """Get the Report"""

    date: str | None = Field(None, alias="date")
    log_warehouse_coef: float | None = Field(None, alias="logWarehouseCoef")
    office_id: int | None = Field(None, alias="officeId")
    warehouse: str | None = Field(None, alias="warehouse")
    warehouse_coef: float | None = Field(None, alias="warehouseCoef")
    gi_id: int | None = Field(None, alias="giId")
    chrt_id: int | None = Field(None, alias="chrtId")
    size: str | None = Field(None, alias="size")
    barcode: str | None = Field(None, alias="barcode")
    subject: str | None = Field(None, alias="subject")
    brand: str | None = Field(None, alias="brand")
    vendor_code: str | None = Field(None, alias="vendorCode")
    nm_id: int | None = Field(None, alias="nmId")
    volume: float | None = Field(None, alias="volume")
    calc_type: str | None = Field(None, alias="calcType")
    warehouse_price: float | None = Field(None, alias="warehousePrice")
    barcodes_count: int | None = Field(None, alias="barcodesCount")
    pallet_place_code: int | None = Field(None, alias="palletPlaceCode")
    pallet_count: float | None = Field(None, alias="palletCount")
    original_date: str | None = Field(None, alias="originalDate")
    loyalty_discount: float | None = Field(None, alias="loyaltyDiscount")
    tariff_fix_date: str | None = Field(None, alias="tariffFixDate")
    tariff_lower_date: str | None = Field(None, alias="tariffLowerDate")
