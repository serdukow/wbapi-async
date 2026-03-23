from pydantic import Field

from ...types import EditResponseToFeedbackResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class EditResponseToFeedback(WbMethod):
    """
    Allows you to edit an already sent response to the feedback. You can edit the response only
    oncewithin 60 days. There is no validation by `feedback ID`: if an incorrect value is provided
    inthe request, you will not receive an error.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1answer/patch
    """

    __return__ = EditResponseToFeedbackResponse
    __empty_response__ = True
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/answer"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: str = Field()
    text: str = Field()
