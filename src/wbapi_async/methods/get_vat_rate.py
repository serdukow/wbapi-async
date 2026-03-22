from pydantic import Field

from ..types.vat_rate_item import VatRateItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetVatRate(WbMethod):
    """
    Returns a list of values for the **VAT rate** characteristic

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1vat/get
    """

    __return__ = VatRateItem
    __api__ = "content-api"
    __method__ = "content/v2/directory/vat"
    __data_key__ = "data"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    locale: str | None = Field(None)
