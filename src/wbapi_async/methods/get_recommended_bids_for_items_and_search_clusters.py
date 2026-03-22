from pydantic import Field

from ..types.recommended_bids_for_items_and_search_clusters_item import RecommendedBidsForItemsAndSearchClustersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetRecommendedBidsForItemsAndSearchClusters(WbMethod):
    """
    The method returns recommended bids for items and search clusters of the campaign.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1api~1advert~1v0~1bids~1recommendations/get
    """

    __return__ = RecommendedBidsForItemsAndSearchClustersItem
    __api__ = "advert-api"
    __method__ = "api/advert/v0/bids/recommendations"
    __data_key__ = "normQueries"

    request_limit: RequestLimit = RequestLimit(period=60, limit=5, interval=12, burst=5)

    nm_id: int = Field(None, alias="nmId")
    advert_id: int = Field(None, alias="advertId")
