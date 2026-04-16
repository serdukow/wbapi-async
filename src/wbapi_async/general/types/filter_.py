from pydantic import Field

from ...types.base import BaseType


class Filter(BaseType):
    """Filters"""

    with_photo: int | None = Field(None, alias="withPhoto")
    text_search: str | None = Field(None, alias="textSearch")
    tag_i_ds: list[int] | None = Field(None, alias="tagIDs")
    allowed_categories_only: bool | None = Field(None, alias="allowedCategoriesOnly")
    object_i_ds: list[int] | None = Field(None, alias="objectIDs")
    brands: list[str] | None = Field(None)
    imt_id: int | None = Field(None, alias="imtID")
