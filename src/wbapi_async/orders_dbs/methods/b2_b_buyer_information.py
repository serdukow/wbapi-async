from pydantic import Field

from ...types import B2BBuyerInformationItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class B2BBuyerInformation(WbMethod):
    """
    The method returns B2B buyers data by assembly orders ID: - Taxpayer Identification Number (TIN
    orINN in Russian) - Code of Reason for Registration (CRR or KPP in Russian) - Company name

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1b2b~1info/post
    """

    __return__ = B2BBuyerInformationItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/b2b/info"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
