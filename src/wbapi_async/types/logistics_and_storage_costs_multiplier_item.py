from pydantic import Field

from .base import BaseType


class LogisticsAndStorageCostsMultiplierItem(BaseType):
    """Logistics and Storage Costs Multiplier"""

    nm_id: int | None = Field(None, alias="nmId")
    subject_name: str | None = Field(None, alias="subjectName")
    dim_id: int | None = Field(None, alias="dimId")
    prc_over: float | None = Field(None, alias="prcOver")
    volume: float | None = Field(None)
    width: int | None = Field(None)
    length: int | None = Field(None)
    height: int | None = Field(None)
    volume_sup: float | None = Field(None, alias="volumeSup")
    width_sup: int | None = Field(None, alias="widthSup")
    length_sup: int | None = Field(None, alias="lengthSup")
    height_sup: int | None = Field(None, alias="heightSup")
    photo_urls: list[str] | None = Field(None, alias="photoUrls")
    dt_bonus: str | None = Field(None, alias="dtBonus")
    is_valid: bool | None = Field(None, alias="isValid")
    is_valid_dt: str | None = Field(None, alias="isValidDt")
    reversal_amount: float | None = Field(None, alias="reversalAmount")
    penalty_amount: float | None = Field(None, alias="penaltyAmount")
