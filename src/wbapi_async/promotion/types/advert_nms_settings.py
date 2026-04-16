from typing import Any

from pydantic import Field

from ...types.base import BaseType
from .advert_subject import AdvertSubject


class AdvertNmsSettings(BaseType):
    bids_kopecks: Any = Field(alias="bids_kopecks")
    subject: AdvertSubject = Field(alias="subject")
    nm_id: int = Field(alias="nm_id")
