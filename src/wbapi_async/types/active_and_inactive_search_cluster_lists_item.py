from typing import Any

from pydantic import Field

from .base import BaseType


class ActiveAndInactiveSearchClusterListsItem(BaseType):
    """Active and Inactive Search Cluster Lists"""

    advert_id: int | None = Field(None, alias="advertId")
    nm_id: int | None = Field(None, alias="nmId")
    norm_queries: dict[str, Any] | None = Field(None, alias="normQueries")
