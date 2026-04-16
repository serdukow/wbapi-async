from pydantic import Field

from ...types.base import BaseType
from .show_hours_item import ShowHoursItem


class InformationAboutMediaCampaignItem(BaseType):
    """Information About Media Campaign"""

    id_: int | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")
    status: int | None = Field(None, alias="status")
    place: int | None = Field(None, alias="place")
    budget: int | None = Field(None, alias="budget")
    daily_limit: int | None = Field(None, alias="daily_limit")
    category_name: str | None = Field(None, alias="category_name")
    cpm: int | None = Field(None, alias="cpm")
    url: str | None = Field(None, alias="url")
    advert_type: int | None = Field(None, alias="advert_type")
    created_at: str | None = Field(None, alias="created_at")
    updated_at: str | None = Field(None, alias="updated_at")
    date_from: str | None = Field(None, alias="date_from")
    date_to: str | None = Field(None, alias="date_to")
    nms: list[int] | None = Field(None, alias="nms")
    bottom_text1: str | None = Field(None, alias="bottomText1")
    bottom_text2: str | None = Field(None, alias="bottomText2")
    message: str | None = Field(None, alias="message")
    additional_settings: int | None = Field(None, alias="additionalSettings")
    receivers_count: int | None = Field(None, alias="receiversCount")
    subject_id: int | None = Field(None, alias="subject_id")
    subject_name: str | None = Field(None, alias="subject_name")
    action_name: str | None = Field(None, alias="action_name")
    show_hours: list[ShowHoursItem] | None = Field(None, alias="show_hours")
    erid: str | None = Field(None, alias="Erid")
