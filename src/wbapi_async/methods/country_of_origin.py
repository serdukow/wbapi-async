from pydantic import Field

from ..types.country_of_origin_response import CountryOfOriginResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CountryOfOrigin(WbMethod):
    """
    Country of Origin

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1directory~1countries/get
    """

    __return__ = CountryOfOriginResponse
    __api__ = "content-api"
    __method__ = "content/v2/directory/countries"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    locale: str | None = Field(None)
