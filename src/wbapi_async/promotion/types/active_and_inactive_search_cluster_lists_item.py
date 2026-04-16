from pydantic import Field

from ...types.base import BaseType
from .v0_get_norm_query_list_response_item_norm_queries import V0GetNormQueryListResponseItemNormQueries


class ActiveAndInactiveSearchClusterListsItem(BaseType):
    """Active and Inactive Search Cluster Lists"""

    advert_id: int | None = Field(None, alias="advertId")
    nm_id: int | None = Field(None, alias="nmId")
    norm_queries: V0GetNormQueryListResponseItemNormQueries | None = Field(None, alias="normQueries")
