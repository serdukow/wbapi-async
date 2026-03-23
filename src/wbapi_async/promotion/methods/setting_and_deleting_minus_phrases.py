from pydantic import Field

from ...types import RequestLimit
from ...types import SettingAndDeletingMinusPhrasesResponse
from ...methods.base import WbMethod


class SettingAndDeletingMinusPhrases(WbMethod):
    """
    The method sets and deletes the minus phrases in campaigns with standard and custom bid.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1set-minus/post
    """

    __return__ = SettingAndDeletingMinusPhrasesResponse
    __empty_response__ = True
    __api__ = "advert-api"
    __method__ = "adv/v0/normquery/set-minus"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    advert_id: int = Field()
    nm_id: int = Field()
    norm_queries: list[str] = Field()
