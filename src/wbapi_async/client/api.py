from typing import Any

from ..client.session.base import BaseSession
from ..enums.realization_sales_report_period import RealizationSalesReportPeriod
from ..methods.base import WbMethod
from ..methods.connection_check import ConnectionCheck as ConnectionCheckMethod
from ..methods.get_products_with_prices import GetProductsWithPrices
from ..methods.get_realization_sales_report import GetRealizationSalesReport
from ..types import ConnectionCheck, ProductWithPrice, RealizationSalesReport
from ..utils.token import validate_token


class WbAPI:
    def __init__(self, token: str, session: BaseSession | None = None, **kwargs: Any) -> None:
        """
        WbAPI class.

        Attributes:

            token: Access token

            Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Authorization/How-to-create-a-personal-access-base-or-test-token
        """
        validate_token(token)
        if session is None:
            read_timeout = kwargs.get("read_timeout", 60)
            base = kwargs.get("base", "wildberries.ru")
            session = BaseSession(
                base=base,
                timeout=read_timeout,
            )

        self._token = token
        self.session = session

    async def __aenter__(self) -> "WbAPI":
        return self

    async def __aexit__(self, exc_type: Any, _exc: Any, _tb: Any) -> None:
        await self.session.close()

    async def __call__(self, method: WbMethod) -> Any:
        return await method.emit(self)

    async def connection_check(self) -> ConnectionCheck:
        call = ConnectionCheckMethod()
        return await self(call)

    async def get_products_with_prices(
        self, limit: int | None = 1000, offset: int | None = 0, filter_nm_id: int | None = None
    ) -> list[ProductWithPrice]:
        """
        Returns product data.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/get

        :param limit: Number of elements per page (pagination)
        :param offset: How many results to skip
        :param filter_nm_id: WB article for search
        :return: :class:`ProductWithPrice`: Product data
        """
        call = GetProductsWithPrices(limit=limit, offset=offset, filter_nm_id=filter_nm_id)
        return await self(call)

    async def get_realization_sales_report(
        self,
        date_from: str,
        date_to: str,
        limit: int = 100000,
        rrdid: int = 0,
        period: RealizationSalesReportPeriod = RealizationSalesReportPeriod.WEEKLY,
    ) -> list[RealizationSalesReport]:
        """
        Details for the realization reports.

        Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Financial-Reports/paths/~1api~1v5~1supplier~1reportDetailByPeriod/get

        :param date_from: Starting date of the report (RFC3339)
        :param date_to: Report end date (RFC3339)
        :param limit: Number of strings in the response (max 100000)
        :param rrdid: Unique ID of the report line for pagination (start with 0)
        :param period: Report periodicity: "weekly" or "daily"
        :return: List of :class:`RealizationSalesReport`
        """
        call = GetRealizationSalesReport(
            date_from=date_from,
            date_to=date_to,
            limit=limit,
            rrdid=rrdid,
            period=period,
        )
        return await self(call)
