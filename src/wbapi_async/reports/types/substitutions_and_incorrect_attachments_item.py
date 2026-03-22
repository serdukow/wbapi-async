from pydantic import Field

from ...types.base import BaseType


class SubstitutionsAndIncorrectAttachmentsItem(BaseType):
    """Substitutions and Incorrect Attachments"""

    dt_bonus: str | None = Field(None, alias="dtBonus")
    nm_id: int | None = Field(None, alias="nmId")
    old_shk_id: int | None = Field(None, alias="oldShkId")
    old_color: str | None = Field(None, alias="oldColor")
    old_size: str | None = Field(None, alias="oldSize")
    old_sku: str | None = Field(None, alias="oldSku")
    old_vendor_code: str | None = Field(None, alias="oldVendorCode")
    new_shk_id: int | None = Field(None, alias="newShkId")
    new_color: str | None = Field(None, alias="newColor")
    new_size: str | None = Field(None, alias="newSize")
    new_sku: str | None = Field(None, alias="newSku")
    new_vendor_code: str | None = Field(None, alias="newVendorCode")
    bonus_summ: float | None = Field(None, alias="bonusSumm")
    bonus_type: str | None = Field(None, alias="bonusType")
    photo_urls: list[str] | None = Field(None, alias="photoUrls")
