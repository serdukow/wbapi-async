from typing import Any

from pydantic import Field

from ...types.base import BaseType
from .advert_subject import AdvertSubject


class AdvertNMsSettings(BaseType):
    bids_kopecks: Any = Field()
    subject: AdvertSubject = Field()
    nm_id: int = Field()
