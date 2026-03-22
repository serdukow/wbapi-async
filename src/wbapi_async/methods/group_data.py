from ..types.group_data_item import GroupDataItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GroupData(WbMethod):
    """
    Forms a dataset for inventory by product group.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1groups/post
    """

    __return__ = GroupDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/groups"
    __http_method__ = "POST"
    __data_key__ = "data.groups"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)
