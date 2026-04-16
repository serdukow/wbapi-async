from pydantic import Field

from ...types.base import BaseType


class Video(BaseType):
    """Video structure"""

    preview_image: str | None = Field(None, alias="previewImage")
    link: str | None = Field(None)
    duration_sec: int | None = Field(None, alias="durationSec")
