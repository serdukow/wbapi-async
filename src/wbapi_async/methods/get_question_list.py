from pydantic import Field

from ..types.question_list_item import QuestionListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetQuestionList(WbMethod):
    """
    The method allows you to get a list of questions by the specified parameters with pagination
    andsorting.<br> It is possible to get a maximum of 10,000 questions per query

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions/get
    """

    __return__ = QuestionListItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/questions"
    __data_key__ = "data.questions"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    is_answered: bool = Field(None, alias="isAnswered")
    nm_id: int | None = Field(None, alias="nmId")
    take: int = Field(None)
    skip: int = Field(None)
    order: str | None = Field(None)
    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
