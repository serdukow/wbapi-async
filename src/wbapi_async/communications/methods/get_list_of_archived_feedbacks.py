from pydantic import Field

from ...methods.base import WbMethod
from ...types import ListOfArchivedFeedbacksItem, RequestLimit


class GetListOfArchivedFeedbacks(WbMethod):
    """
    The method allows you to get a list of archived feedbacks. The feedback becomes archived if: -
    Aresponse to the feedback is received. - No response to the feedback is received within 30
    days.- The feedback contains no text or photos.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1archive/get
    """

    __return__ = ListOfArchivedFeedbacksItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/archive"
    __data_key__ = "data.feedbacks"
    __pagination__ = "take_skip"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    nm_id: int | None = Field(None, alias="nmId")
    take: int = Field(alias="take")
    skip: int = Field(alias="skip")
    order: str | None = Field(None, alias="order")
