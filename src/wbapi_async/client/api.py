from typing import Any

from ..client.session.base import BaseSession
from ..enums.product_data_availability import ProductDataAvailability
from ..enums.product_data_order_field import ProductDataOrderField
from ..enums.product_data_order_mode import ProductDataOrderMode
from ..enums.product_data_stock_type import ProductDataStockType
from ..enums.realization_sales_report_period import RealizationSalesReportPeriod
from ..enums.sales_funnel_order_field import SalesFunnelOrderField
from ..methods.base import WbMethod
from ..methods.connection_check import ConnectionCheck as ConnectionCheckMethod
from ..methods.get_campaigns_lists import GetCampaignsLists
from ..methods.get_campaigns_statistics import GetCampaignsStatistics
from ..methods.get_product_cards_list import (
    CardListCursor,
    CardListFilter,
    CardListSettings,
    CardListSort,
    GetProductCardsList,
)
from ..methods.get_product_cards_statistics import (
    GetProductCardsStatistics,
    SalesFunnelOrderBy,
    SalesFunnelPeriod,
)
from ..methods.get_product_data import GetProductData, OrderBy, Period
from ..methods.get_product_detail import GetProductDetail
from ..methods.get_products_with_prices import GetProductsWithPrices
from ..methods.get_realization_sales_report import GetRealizationSalesReport
from ..methods.get_sales import GetSales
from ..types import (
    CampaignsList,
    CampaignStatistics,
    ConnectionCheck,
    ProductCard,
    ProductCardStatistics,
    ProductDataItem,
    ProductDetail,
    ProductWithPrice,
    RealizationSalesReport,
    Sale,
)
from ..utils.token import validate_token
from ..utils.unofficial import unofficial


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

    async def get_sales(self, date_from: str, flag: int = 0) -> list[Sale]:
        """
        Returns sale and return information.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1sales/get

        :param date_from: Date and time of last change (RFC3339)
        :param flag: 0 — changes since dateFrom, 1 — all sales on dateFrom date
        :return: List of :class:`Sale`
        """
        call = GetSales(date_from=date_from, flag=flag)
        return await self(call)

    async def get_product_data(
        self,
        date_from: str,
        date_to: str,
        stock_type: ProductDataStockType,
        order_by_field: ProductDataOrderField,
        order_by_mode: ProductDataOrderMode,
        availability_filters: list[ProductDataAvailability],
        skip_deleted_nm: bool = False,
        limit: int = 100,
        offset: int = 0,
        nm_ids: list[int] | None = None,
        subject_id: int | None = None,
        brand_name: str | None = None,
        tag_id: int | None = None,
    ) -> list[ProductDataItem]:
        """
        Forms a dataset for inventory by products.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post

        :param date_from: Start date of the period (YYYY-MM-DD)
        :param date_to: End date of the period (YYYY-MM-DD)
        :param stock_type: Type of products storage warehouse
        :param order_by_field: Field to sort by
        :param order_by_mode: Sort order (asc/desc)
        :param availability_filters: Item availability filters
        :param skip_deleted_nm: Skip deleted items
        :param limit: Number of items in response (max 1000)
        :param offset: Offset for pagination
        :param nm_ids: List of WB article numbers for filtering
        :param subject_id: Subject ID filter
        :param brand_name: Brand filter
        :param tag_id: Tag ID filter
        :return: List of :class:`ProductDataItem`
        """
        call = GetProductData(
            current_period=Period(start=date_from, end=date_to),
            stock_type=stock_type,
            skip_deleted_nm=skip_deleted_nm,
            order_by=OrderBy(field=order_by_field, mode=order_by_mode),
            availability_filters=availability_filters,
            limit=limit,
            offset=offset,
            nm_ids=nm_ids,
            subject_id=subject_id,
            brand_name=brand_name,
            tag_id=tag_id,
        )
        return await self(call)

    async def get_product_cards_statistics_per_period(
        self,
        date_from: str,
        date_to: str,
        past_date_from: str | None = None,
        past_date_to: str | None = None,
        order_by_field: SalesFunnelOrderField = SalesFunnelOrderField.OPEN_CARD,
        order_by_mode: ProductDataOrderMode = ProductDataOrderMode.DESC,
        limit: int = 50,
        offset: int = 0,
        nm_ids: list[int] | None = None,
        brand_names: list[str] | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
        skip_deleted_nm: bool | None = None,
    ) -> list[ProductCardStatistics]:
        """
        Generates a report on products by comparing key metrics for current and past periods.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/operation/postSalesFunnelProducts

        :param date_from: Selected period start date (YYYY-MM-DD)
        :param date_to: Selected period end date (YYYY-MM-DD)
        :param past_date_from: Past period start date for comparison (YYYY-MM-DD)
        :param past_date_to: Past period end date for comparison (YYYY-MM-DD)
        :param order_by_field: Field to sort by
        :param order_by_mode: Sort order (asc/desc)
        :param limit: Number of product cards in response (max 1000)
        :param offset: How many results to skip
        :param nm_ids: WB articles to include (empty = all products)
        :param brand_names: Brand filter
        :param subject_ids: Subject ID filter
        :param tag_ids: Tag ID filter
        :param skip_deleted_nm: Skip deleted items
        :return: List of :class:`ProductCardStatistics`
        """
        past_period = (
            SalesFunnelPeriod(start=past_date_from, end=past_date_to)
            if past_date_from and past_date_to
            else None
        )
        call = GetProductCardsStatistics(
            selected_period=SalesFunnelPeriod(start=date_from, end=date_to),
            past_period=past_period,
            order_by=SalesFunnelOrderBy(field=order_by_field, mode=order_by_mode),
            limit=limit,
            offset=offset,
            nm_ids=nm_ids,
            brand_names=brand_names,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
            skip_deleted_nm=skip_deleted_nm,
        )
        return await self(call)

    async def get_product_cards_list(
        self,
        with_photo: int = -1,
        locale: str | None = None,
        text_search: str | None = None,
        tag_ids: list[int] | None = None,
        object_ids: list[int] | None = None,
        brands: list[str] | None = None,
        imt_id: int | None = None,
        ascending: bool = False,
        limit: int = 100,
        updated_at: str | None = None,
        nm_id: int | None = None,
    ) -> list[ProductCard]:
        """
        Returns the list of created product cards.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post
        """
        call = GetProductCardsList(
            locale=locale,
            settings=CardListSettings(
                sort=CardListSort(ascending=ascending),
                filter=CardListFilter(
                    with_photo=with_photo,
                    text_search=text_search,
                    tag_ids=tag_ids,
                    object_ids=object_ids,
                    brands=brands,
                    imt_id=imt_id,
                ),
                cursor=CardListCursor(
                    limit=limit,
                    updated_at=updated_at,
                    nm_id=nm_id,
                ),
            ),
        )
        return await self(call)

    async def get_campaigns_lists(self) -> CampaignsList:
        """
        Returns campaigns lists grouped by type and status.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns/paths/~1adv~1v1~1promotion~1count/get

        :return: :class:`CampaignsList`
        """
        call = GetCampaignsLists()
        return await self(call)

    async def get_campaigns_statistics(
        self,
        ids: list[int],
        begin_date: str,
        end_date: str,
    ) -> list[CampaignStatistics]:
        """
        Generates statistics for campaigns regardless of their type.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v3~1fullstats/get

        :param ids: Campaign IDs (max 50)
        :param begin_date: Start date (YYYY-MM-DD)
        :param end_date: End date (YYYY-MM-DD)
        :return: List of :class:`CampaignStatistics`
        """
        call = GetCampaignsStatistics(ids=ids, begin_date=begin_date, end_date=end_date)
        return await self(call)

    @unofficial
    async def get_product_detail(
        self,
        nm: int,
        dest: int,
        spp: int | None = None,
        rate: int | None = None,
    ) -> list[ProductDetail]:
        """
        Returns product detail by WB article. No official documentation available.

        :param nm: WB article (nmID)
        :param dest: Destination region ID
        :param spp: SPP discount
        :param rate: Rate
        :return: List of :class:`ProductDetail`
        """
        call = GetProductDetail(nm=nm, dest=dest, spp=spp, rate=rate)
        return await self(call)
