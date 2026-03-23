from pydantic import Field

from ...types import CountryOfOriginResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetCountryOfOrigin(WbMethod):
    """
    Provides value of characteristic country of origin.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1countries/get
    """

    __return__ = CountryOfOriginResponse
    __api__ = "content-api"
    __method__ = "content/v2/directory/countries"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    locale: str | None = Field(None)
