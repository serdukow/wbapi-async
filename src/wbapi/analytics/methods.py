from __future__ import annotations

from typing import Any

from ..client.method import WBMethod
from ..utils.token import Scope
from .models import (
    CommonItemFilters,
    CommonReportFilters,
    CommonResponseProperties,
    CommonShippingOfficeFilters,
    CommonSizeFilters,
    GetItemRatingResponse,
    GetOrderFeedPagination,
    GetOrderFeedResponse,
    GetOrderFeedSelectedPeriod,
    GetSalesFunnelGroupedHistoryResponse,
    GetSalesFunnelProductsHistoryResponseItem,
    GetSalesFunnelProductsResponse,
    GetStocksReportOfficesResponse,
    GetStocksReportProductsGroupsResponse,
    GetStocksReportProductsResponse,
    GetStocksReportProductsSizesResponse,
    GetStocksReportWbWarehousesResponse,
    NmReportCreateReportResponse,
    NmReportGetReportsResponse,
    NmReportRetryReportResponse,
    OrderBy,
    OrderByGrTe,
    OrderByItemRating,
    OrderByMainAndDetails,
    PastPeriod,
    PastPeriodItemRating,
    Period,
    PeriodItemRating,
    PeriodOrdersRequest,
    SalesFunnelItemReq,
)


class CreateNmReportDownload(WBMethod[NmReportCreateReportResponse]):
    """Создать отчёт

    POST /api/v2/nm-report/downloads
    """

    __path__ = "/api/v2/nm-report/downloads"
    __http_method__ = "POST"
    __returns__ = NmReportCreateReportResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }
    __items__ = "data"

    body: SalesFunnelItemReq | list[Any] | dict[str, Any]


class CreateNmReportDownloadsRetry(WBMethod[NmReportRetryReportResponse]):
    """Сгенерировать отчёт повторно

    POST /api/v2/nm-report/downloads/retry
    """

    __path__ = "/api/v2/nm-report/downloads/retry"
    __http_method__ = "POST"
    __returns__ = NmReportRetryReportResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"download_id": "downloadId"}

    download_id: str | None = None
    """ID отчёта"""


class GetItemRating(WBMethod[GetItemRatingResponse]):
    """Получить отчёт

    POST /api/analytics/v2/item-rating
    """

    __path__ = "/api/analytics/v2/item-rating"
    __http_method__ = "POST"
    __returns__ = GetItemRatingResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {"all": (20000, 3)}
    __paginate__ = "offset_body"
    __items__ = "data"
    __body_fields__ = {
        "current_period": "currentPeriod",
        "past_period": "pastPeriod",
        "nm_ids": "nmIds",
        "subject_ids": "subjectIds",
        "brand_names": "brandNames",
        "tag_ids": "tagIds",
        "is_not_include_nms_without_sales": "isNotIncludeNmsWithoutSales",
        "only_shadowed_nms": "onlyShadowedNms",
        "order_by": "orderBy",
        "limit": "limit",
        "offset": "offset",
    }

    current_period: PeriodItemRating
    offset: int
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
    order_by: OrderByItemRating
    brand_names: list[str] | None = None
    """Список брендов для фильтрации"""
    is_not_include_nms_without_sales: bool | None = None
    """Не возвращать товары без продаж:   - `true` — да, возвращаются только товары с продажами за
    период, указанный в объекте `currentPeriod` …
    """
    limit: int | None = None
    """Количество товаров в ответе"""
    nm_ids: list[int] | None = None
    """Список артикулов WB для фильтрации"""
    only_shadowed_nms: bool | None = None
    """Возвращаются ли в ответе только скрытые товары:   - `true` — да, возвращаются только скрытые
    из каталога товары …
    """
    past_period: PastPeriodItemRating | None = None
    subject_ids: list[int] | None = None
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = None
    """Список ID ярлыков для фильтрации"""


class GetNmReportDownloads(WBMethod[NmReportGetReportsResponse]):
    """Получить список отчётов

    GET /api/v2/nm-report/downloads
    """

    __path__ = "/api/v2/nm-report/downloads"
    __http_method__ = "GET"
    __returns__ = NmReportGetReportsResponse
    __query_params__ = {"filter_download_ids": "filter[downloadIds]"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }
    __items__ = "data"

    filter_download_ids: list[str] | None = None
    """ID отчёта"""


class GetNmReportDownloadsFile(WBMethod[None]):
    """Получить отчёт

    GET /api/v2/nm-report/downloads/file/{downloadId}
    """

    __path__ = "/api/v2/nm-report/downloads/file/{downloadId}"
    __http_method__ = "GET"
    __returns__ = None
    __path_params__ = ("downloadId",)
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }

    download_id: str | int
    """ID отчёта"""


class GetOrderFeed(WBMethod[GetOrderFeedResponse]):
    """Получить отчёт

    POST /api/analytics/v1/order-feed
    """

    __path__ = "/api/analytics/v1/order-feed"
    __http_method__ = "POST"
    __returns__ = GetOrderFeedResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (10800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {
        "selected_period": "selectedPeriod",
        "nm_ids": "nmIds",
        "subject_ids": "subjectIds",
        "brand_names": "brandNames",
        "tag_ids": "tagIds",
        "pagination": "pagination",
    }

    selected_period: GetOrderFeedSelectedPeriod
    """Запрашиваемый период. По дате текущего статуса заказа"""
    brand_names: list[str] | None = None
    """Список брендов для фильтрации"""
    nm_ids: list[int] | None = None
    """Список артикулов WB для фильтрации"""
    pagination: GetOrderFeedPagination | None = None
    """Пагинация"""
    subject_ids: list[int] | None = None
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = None
    """Список ID ярлыков для фильтрации"""


class GetSalesFunnelGroupedHistory(WBMethod[GetSalesFunnelGroupedHistoryResponse]):
    """Статистика групп карточек товаров по дням

    POST /api/analytics/v3/sales-funnel/grouped/history
    """

    __path__ = "/api/analytics/v3/sales-funnel/grouped/history"
    __http_method__ = "POST"
    __returns__ = GetSalesFunnelGroupedHistoryResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {
        "selected_period": "selectedPeriod",
        "brand_names": "brandNames",
        "subject_ids": "subjectIds",
        "tag_ids": "tagIds",
        "skip_deleted_nm": "skipDeletedNm",
        "aggregation_level": "aggregationLevel",
    }

    selected_period: dict[str, Any]
    aggregation_level: str | None = None
    brand_names: list[str] | None = None
    """Список брендов для фильтрации"""
    skip_deleted_nm: bool | None = None
    """Скрыть удалённые товары"""
    subject_ids: list[int] | None = None
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = None
    """Список ID ярлыков для фильтрации"""


class GetSalesFunnelProducts(WBMethod[GetSalesFunnelProductsResponse]):
    """Статистика карточек товаров за период

    POST /api/analytics/v3/sales-funnel/products
    """

    __path__ = "/api/analytics/v3/sales-funnel/products"
    __http_method__ = "POST"
    __returns__ = GetSalesFunnelProductsResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (1800000, 1),
    }
    __paginate__ = "offset_body"
    __items__ = "data"
    __body_fields__ = {
        "selected_period": "selectedPeriod",
        "past_period": "pastPeriod",
        "nm_ids": "nmIds",
        "brand_names": "brandNames",
        "subject_ids": "subjectIds",
        "tag_ids": "tagIds",
        "skip_deleted_nm": "skipDeletedNm",
        "order_by": "orderBy",
        "limit": "limit",
        "offset": "offset",
    }

    selected_period: dict[str, Any]
    brand_names: list[str] | None = None
    """Список брендов для фильтрации"""
    limit: int | None = None
    """Количество карточек товара в ответе"""
    nm_ids: list[int] | None = None
    """Артикулы WB, по которым нужно составить отчёт. Оставьте пустым, чтобы получить отчёт обо
    всех товарах
    """
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
    order_by: OrderBy | None = None
    past_period: dict[str, Any] | None = None
    skip_deleted_nm: bool | None = None
    """Скрыть удалённые товары"""
    subject_ids: list[int] | None = None
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = None
    """Список ID ярлыков для фильтрации"""


class GetSalesFunnelProductsHistory(WBMethod[list[GetSalesFunnelProductsHistoryResponseItem]]):
    """Статистика карточек товаров по дням

    POST /api/analytics/v3/sales-funnel/products/history
    """

    __path__ = "/api/analytics/v3/sales-funnel/products/history"
    __http_method__ = "POST"
    __returns__ = list[GetSalesFunnelProductsHistoryResponseItem]
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (1800000, 1),
    }
    __body_fields__ = {
        "selected_period": "selectedPeriod",
        "nm_ids": "nmIds",
        "skip_deleted_nm": "skipDeletedNm",
        "aggregation_level": "aggregationLevel",
    }

    nm_ids: list[int]
    """Артикулы WB, по которым нужно составить отчёт"""
    selected_period: dict[str, Any]
    aggregation_level: str | None = None
    skip_deleted_nm: bool | None = None
    """Скрыть удалённые товары"""


class GetSearchReport(WBMethod[CommonResponseProperties]):
    """Основная страница

    POST /api/v2/search-report/report
    """

    __path__ = "/api/v2/search-report/report"
    __http_method__ = "POST"
    __returns__ = CommonResponseProperties
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }
    __paginate__ = "offset_body"
    __body_fields__ = {
        "current_period": "currentPeriod",
        "past_period": "pastPeriod",
        "nm_ids": "nmIds",
        "subject_ids": "subjectIds",
        "brand_names": "brandNames",
        "tag_ids": "tagIds",
        "position_cluster": "positionCluster",
        "order_by": "orderBy",
        "include_substituted_skus": "includeSubstitutedSKUs",
        "include_search_texts": "includeSearchTexts",
        "limit": "limit",
        "offset": "offset",
    }

    current_period: Period
    limit: int
    """Количество групп товаров в ответе"""
    offset: int
    """После какого элемента выдавать данные"""
    order_by: OrderByMainAndDetails
    position_cluster: str
    brand_names: list[str] | None = None
    """Список брендов для фильтрации"""
    include_search_texts: bool | None = None
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = None
    """Показать данные по прямым запросам с подменным артикулом"""
    nm_ids: list[int] | None = None
    """Список артикулов WB для фильтрации"""
    past_period: PastPeriod | None = None
    subject_ids: list[int] | None = None
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = None
    """Список ID ярлыков для фильтрации"""


class GetSearchReportProductOrders(WBMethod[CommonResponseProperties]):
    """Заказы и позиции по поисковым запросам товара

    POST /api/v2/search-report/product/orders
    """

    __path__ = "/api/v2/search-report/product/orders"
    __http_method__ = "POST"
    __returns__ = CommonResponseProperties
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }
    __body_fields__ = {"period": "period", "nm_id": "nmId", "search_texts": "searchTexts"}

    nm_id: int
    """Артикул WB"""
    period: PeriodOrdersRequest
    search_texts: list[str]
    """Поисковые запросы. Для тарифов Джема **Продвинутый** и **Премиальный** максимум — 100"""


class GetSearchReportProductSearchTexts(WBMethod[CommonResponseProperties]):
    """Поисковые запросы по товару

    POST /api/v2/search-report/product/search-texts
    """

    __path__ = "/api/v2/search-report/product/search-texts"
    __http_method__ = "POST"
    __returns__ = CommonResponseProperties
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }
    __body_fields__ = {
        "current_period": "currentPeriod",
        "past_period": "pastPeriod",
        "nm_ids": "nmIds",
        "top_order_by": "topOrderBy",
        "include_substituted_skus": "includeSubstitutedSKUs",
        "include_search_texts": "includeSearchTexts",
        "order_by": "orderBy",
        "limit": "limit",
    }

    current_period: Period
    limit: int
    nm_ids: list[int]
    """Список артикулов WB"""
    order_by: OrderByGrTe
    top_order_by: str
    """Фильтрация по поисковым запросам, по которым больше всего:   - `openCard` — перешли в
    карточку   - `addToCart` — добавили в корзину …
    """
    include_search_texts: bool | None = None
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = None
    """Показать данные по прямым запросам с подменным артикулом"""
    past_period: PastPeriod | None = None


class GetSearchReportTableDetails(WBMethod[CommonResponseProperties]):
    """Пагинация по товарам в группе

    POST /api/v2/search-report/table/details
    """

    __path__ = "/api/v2/search-report/table/details"
    __http_method__ = "POST"
    __returns__ = CommonResponseProperties
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }
    __paginate__ = "offset_body"
    __body_fields__ = {
        "current_period": "currentPeriod",
        "past_period": "pastPeriod",
        "subject_id": "subjectId",
        "brand_name": "brandName",
        "tag_id": "tagId",
        "nm_ids": "nmIds",
        "order_by": "orderBy",
        "position_cluster": "positionCluster",
        "include_substituted_skus": "includeSubstitutedSKUs",
        "include_search_texts": "includeSearchTexts",
        "limit": "limit",
        "offset": "offset",
    }

    current_period: Period
    limit: int
    """Количество товаров в ответе"""
    offset: int
    """После какого элемента выдавать данные"""
    order_by: OrderByMainAndDetails
    position_cluster: str
    """Товары с какой средней позицией в поиске показывать в отчёте:   - `all` — все   -
    `firstHundred` — от 1 до 100   - `secondHundred` — от 101 до 200 …
    """
    brand_name: str | None = None
    """Название товара"""
    include_search_texts: bool | None = None
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = None
    """Показать данные по прямым запросам с подменным артикулом"""
    nm_ids: list[int] | None = None
    """Список артикулов WB"""
    past_period: PastPeriod | None = None
    subject_id: int | None = None
    """ID предмета"""
    tag_id: int | None = None
    """ID ярлыка"""


class GetSearchReportTableGroups(WBMethod[CommonResponseProperties]):
    """Пагинация по группам

    POST /api/v2/search-report/table/groups
    """

    __path__ = "/api/v2/search-report/table/groups"
    __http_method__ = "POST"
    __returns__ = CommonResponseProperties
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (3600000, 1),
    }
    __paginate__ = "offset_body"
    __body_fields__ = {
        "current_period": "currentPeriod",
        "past_period": "pastPeriod",
        "nm_ids": "nmIds",
        "subject_ids": "subjectIds",
        "brand_names": "brandNames",
        "tag_ids": "tagIds",
        "order_by": "orderBy",
        "position_cluster": "positionCluster",
        "include_substituted_skus": "includeSubstitutedSKUs",
        "include_search_texts": "includeSearchTexts",
        "limit": "limit",
        "offset": "offset",
    }

    current_period: Period
    limit: int
    """Количество групп товаров в ответе"""
    offset: int
    """После какого элемента выдавать данные"""
    order_by: OrderByGrTe
    position_cluster: str
    brand_names: list[str] | None = None
    """Список брендов для фильтрации"""
    include_search_texts: bool | None = None
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = None
    """Показать данные по прямым запросам с подменным артикулом"""
    nm_ids: list[int] | None = None
    """Список артикулов WB для фильтрации"""
    past_period: PastPeriod | None = None
    subject_ids: list[int] | None = None
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = None
    """Список ID ярлыков для фильтрации"""


class GetStocksReportOffices(WBMethod[GetStocksReportOfficesResponse]):
    """Данные по складам

    POST /api/v2/stocks-report/offices
    """

    __path__ = "/api/v2/stocks-report/offices"
    __http_method__ = "POST"
    __returns__ = GetStocksReportOfficesResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    body: CommonShippingOfficeFilters | list[Any] | dict[str, Any]


class GetStocksReportProducts(WBMethod[GetStocksReportProductsResponse]):
    """Данные по товарам

    POST /api/v2/stocks-report/products/products
    """

    __path__ = "/api/v2/stocks-report/products/products"
    __http_method__ = "POST"
    __returns__ = GetStocksReportProductsResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    body: CommonItemFilters | list[Any] | dict[str, Any]


class GetStocksReportProductsGroups(WBMethod[GetStocksReportProductsGroupsResponse]):
    """Данные по группам

    POST /api/v2/stocks-report/products/groups
    """

    __path__ = "/api/v2/stocks-report/products/groups"
    __http_method__ = "POST"
    __returns__ = GetStocksReportProductsGroupsResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    body: CommonReportFilters | list[Any] | dict[str, Any]


class GetStocksReportProductsSizes(WBMethod[GetStocksReportProductsSizesResponse]):
    """Данные по размерам

    POST /api/v2/stocks-report/products/sizes
    """

    __path__ = "/api/v2/stocks-report/products/sizes"
    __http_method__ = "POST"
    __returns__ = GetStocksReportProductsSizesResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 3),
        "service": (20000, 3),
        "basic_secret": (20000, 3),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    body: CommonSizeFilters | list[Any] | dict[str, Any]


class GetStocksReportWbWarehouses(WBMethod[GetStocksReportWbWarehousesResponse]):
    """Остатки на складах WB

    POST /api/analytics/v1/stocks-report/wb-warehouses
    """

    __path__ = "/api/analytics/v1/stocks-report/wb-warehouses"
    __http_method__ = "POST"
    __returns__ = GetStocksReportWbWarehousesResponse
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {"all": (20000, 1)}
    __paginate__ = "offset_body"
    __items__ = "data"
    __body_fields__ = {"nm_ids": "nmIds", "chrt_ids": "chrtIds", "limit": "limit", "offset": "offset"}

    chrt_ids: list[int] | None = None
    """ID размеров. Используется только для указанных в массиве `nmIds` артикулов"""
    limit: int | None = None
    """Количество строк в ответе"""
    nm_ids: list[int] | None = None
    """Артикулы WB"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
