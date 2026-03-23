from pydantic import Field

from ...types import RequestLimit
from ...types import SupplyPackageResponse
from ...methods.base import WbMethod


class GetSupplyPackage(WbMethod):
    """
    The method returns information about the package of the supply.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies~1%7BID%7D~1package/get
    """

    __return__ = SupplyPackageResponse
    __api__ = "supplies-api"
    __method__ = ""
    __method_template__ = "api/v1/supplies/{id}/package"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: int = Field(alias="ID", exclude=True)
