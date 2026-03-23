from typing import Any

from pydantic import Field

from ...types.base import BaseType


class InformationAboutMediaCampaignItem(BaseType):
    """Information About Media Campaign"""

    id_: int | None = Field(None, alias="id")
    name: str | None = Field(None)
    status: int | None = Field(None)
    place: int | None = Field(None)
    budget: int | None = Field(None)
    daily_limit: int | None = Field(None)
    category_name: str | None = Field(None)
    cpm: int | None = Field(None)
    url: str | None = Field(None)
    advert_type: int | None = Field(None)
    created_at: str | None = Field(None)
    updated_at: str | None = Field(None)
    date_from: str | None = Field(None)
    date_to: str | None = Field(None)
    nms: list[int] | None = Field(None)
    bottom_text1: str | None = Field(None, alias="bottomText1")
    bottom_text2: str | None = Field(None, alias="bottomText2")
    message: str | None = Field(None)
    additional_settings: int | None = Field(None, alias="additionalSettings")
    receivers_count: int | None = Field(None, alias="receiversCount")
    subject_id: int | None = Field(None)
    subject_name: str | None = Field(None)
    action_name: str | None = Field(None)
    show_hours: list[dict[str, Any]] | None = Field(None)
    erid: str | None = Field(None, alias="Erid")
