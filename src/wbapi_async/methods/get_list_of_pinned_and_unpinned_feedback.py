from pydantic import Field

from ..types.list_of_pinned_and_unpinned_feedback_response import ListOfPinnedAndUnpinnedFeedbackResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetListOfPinnedAndUnpinnedFeedback(WbMethod):
    """
    The method allows to get the list of pinned and unpinned feedback.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/get
    """

    __return__ = ListOfPinnedAndUnpinnedFeedbackResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    state: str | None = Field(None)
    pin_on: str | None = Field(None, alias="pinOn")
    imt_id: int | None = Field(None, alias="imtId")
    nm_id: int | None = Field(None, alias="nmId")
    feedback_id: int | None = Field(None, alias="feedbackId")
    date_from: str | None = Field(None, alias="dateFrom")
    date_to: str | None = Field(None, alias="dateTo")
    next: int | None = Field(None)
    limit: int | None = Field(500)
