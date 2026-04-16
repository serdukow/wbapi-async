from pydantic import Field

from ...methods.base import WbMethod
from ...types import PinnedAndUnpinnedFeedbackNumberResponse, RequestLimit
from ..enums.pin_on import PinOn
from ..enums.state import State


class GetPinnedAndUnpinnedFeedbackNumber(WbMethod):
    """
    The method returns the number of pinned and unpinned feedback for the period.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins~1count/get
    """

    __return__ = PinnedAndUnpinnedFeedbackNumberResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins/count"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    state: State | None = Field(None)
    pin_on: PinOn | None = Field(None, alias="pinOn")
    imt_id: int | None = Field(None, alias="imtId")
    nm_id: int | None = Field(None, alias="nmId")
    feedback_id: int | None = Field(None, alias="feedbackId")
    date_from: str | None = Field(None, alias="dateFrom")
    date_to: str | None = Field(None, alias="dateTo")
