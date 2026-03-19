from pydantic import Field

from ..enums.product_data_order_mode import ProductDataOrderMode
from ..enums.sales_funnel_order_field import SalesFunnelOrderField
from ..types.base import BaseType
from ..types.product_cards_statistics import ProductCardStatistics
from ..types.request_limit import RequestLimit
from .base import WbMethod


class SalesFunnelPeriod(BaseType):
    start: str = Field(alias="start")
    end: str = Field(alias="end")


class SalesFunnelOrderBy(BaseType):
    field: SalesFunnelOrderField = Field(SalesFunnelOrderField.OPEN_CARD, alias="field")
    mode: ProductDataOrderMode = Field(ProductDataOrderMode.DESC, alias="mode")


class GetProductCardsStatisticsPerPeriod(WbMethod):
    """
    Generates a report on products by comparing key metrics for the current period with a past one.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/operation/postSalesFunnelProducts
    """

    __return__ = ProductCardStatistics
    __api__ = "seller-analytics-api"
    __method__ = "api/analytics/v3/sales-funnel/products"
    __http_method__ = "POST"
    __data_key__ = "data.products"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20000, burst=3)

    selected_period: SalesFunnelPeriod = Field(alias="selectedPeriod")
    limit: int | None = Field(50, alias="limit")
    offset: int = Field(0, alias="offset")

    past_period: SalesFunnelPeriod | None = Field(None, alias="pastPeriod")
    nm_ids: list[int] | None = Field(None, alias="nmIds")
    brand_names: list[str] | None = Field(None, alias="brandNames")
    subject_ids: list[int] | None = Field(None, alias="subjectIds")
    tag_ids: list[int] | None = Field(None, alias="tagIds")
    skip_deleted_nm: bool | None = Field(None, alias="skipDeletedNm")
    order_by: SalesFunnelOrderBy | None = Field(None, alias="orderBy")
