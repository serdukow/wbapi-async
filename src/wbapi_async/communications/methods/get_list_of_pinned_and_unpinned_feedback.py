from pydantic import Field

from ...enums import PinOn, State
from ...methods.base import WbMethod
from ...types import ListOfPinnedAndUnpinnedFeedbackResponse, RequestLimit


class GetListOfPinnedAndUnpinnedFeedback(WbMethod):
    """
    The method allows to get the list of pinned and unpinned feedback. Only automatically unpinned
    feedbackcause of the reasons specified in the response in the `unpinnedCause` field are
    consideredunpinned.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/get
    """

    __return__ = ListOfPinnedAndUnpinnedFeedbackResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins"
    __pagination__ = "next"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    state: State | None = Field(None)
    pin_on: PinOn | None = Field(None, alias="pinOn")
    imt_id: int | None = Field(None, alias="imtId")
    nm_id: int | None = Field(None, alias="nmId")
    feedback_id: int | None = Field(None, alias="feedbackId")
    date_from: str | None = Field(None, alias="dateFrom")
    date_to: str | None = Field(None, alias="dateTo")
    next_: int | None = Field(None, alias="next")
    limit: int | None = Field(500)
