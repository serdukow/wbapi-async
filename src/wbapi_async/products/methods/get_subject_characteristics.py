from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SubjectCharacteristicsItem


class GetSubjectCharacteristics(WbMethod):
    """
    Returns list of the subject characteristics by its ID

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get
    """

    __return__ = SubjectCharacteristicsItem
    __api__ = "content-api"
    __method__ = ""
    __method_template__ = "content/v2/object/charcs/{subject_id}"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    subject_id: int = Field(alias="subjectId", exclude=True)
    locale: str | None = Field(None)
