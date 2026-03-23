from pydantic import Field

from ...types import RecommendedBidsForItemsAndSearchClustersItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetRecommendedBidsForItemsAndSearchClusters(WbMethod):
    """
    The method returns recommended bids for items and search clusters of the campaign. Only for
    campaignswith cpm payment type — cost per mille.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1api~1advert~1v0~1bids~1recommendations/get
    """

    __return__ = RecommendedBidsForItemsAndSearchClustersItem
    __api__ = "advert-api"
    __method__ = "api/advert/v0/bids/recommendations"
    __data_key__ = "normQueries"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nm_id: int = Field(alias="nmId")
    advert_id: int = Field(alias="advertId")
