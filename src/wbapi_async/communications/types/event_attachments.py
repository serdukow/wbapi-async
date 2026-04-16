from pydantic import Field

from ...types.base import BaseType
from .file import File
from .good_card import GoodCard
from .image import Image


class EventAttachments(BaseType):
    """Attachments"""

    good_card: GoodCard | None = Field(None, alias="goodCard")
    files: list[File] | None = Field(None, alias="files")
    images: list[Image] | None = Field(None, alias="images")
