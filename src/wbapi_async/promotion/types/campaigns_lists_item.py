from typing import Any

from pydantic import Field

from ...types.base import BaseType


class CampaignsListsItem(BaseType):
    """Campaigns Lists"""

    type_: int | None = Field(None, alias="type")
    status: int | None = Field(None)
    count: int | None = Field(None)
    advert_list: list[dict[str, Any]] | None = Field(None)
