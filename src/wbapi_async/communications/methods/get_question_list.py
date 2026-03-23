from pydantic import Field

from ...methods.base import WbMethod
from ...types import QuestionListItem, RequestLimit


class GetQuestionList(WbMethod):
    """
    The method allows you to get a list of questions by the specified parameters with pagination
    andsorting. It is possible to get a maximum of 10,000 questions per query

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions/get
    """

    __return__ = QuestionListItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/questions"
    __data_key__ = "data.questions"
    __pagination__ = "take_skip"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    is_answered: bool = Field(alias="isAnswered")
    nm_id: int | None = Field(None, alias="nmId")
    take: int = Field()
    skip: int = Field()
    order: str | None = Field(None)
    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
