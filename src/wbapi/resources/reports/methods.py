from __future__ import annotations

from ...client.method import WBMethod
from ...utils.token import Scope
from .models import (
    WHM,
    AcceptanceReportTasksTaskIdDownloadResponseItem,
    AnalyticsBannedProductsBlockedResponse,
    AnalyticsGoodsReturnResponse,
    CreateTaskResponse,
    ExciseReportResponse,
    GetTasksResponse,
    MeasurementPenalties,
    OrdersItem,
    PaidStorageTasksTaskIdDownloadResponseItem,
    SalesItem,
    WarehouseRemainsTasksTaskIdDownloadResponseItem,
)


class AcceptanceReportCreate(WBMethod[CreateTaskResponse]):
    """Создать отчёт

    GET /api/v1/acceptance_report
    """

    __path__ = "/api/v1/acceptance_report"
    __http_method__ = "GET"
    __returns__ = CreateTaskResponse
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (10800000, 1),
    }
    __items__ = "data"

    date_from: str
    """Начало отчётного периода, `ГГГГ-ММ-ДД`"""
    date_to: str
    """Конец отчётного периода, `ГГГГ-ММ-ДД`"""


class AcceptanceReportTasksTaskIdDownload(WBMethod[list[AcceptanceReportTasksTaskIdDownloadResponseItem]]):
    """Получить отчёт

    GET /api/v1/acceptance_report/tasks/{task_id}/download
    """

    __path__ = "/api/v1/acceptance_report/tasks/{task_id}/download"
    __http_method__ = "GET"
    __returns__ = list[AcceptanceReportTasksTaskIdDownloadResponseItem]
    __path_params__ = ("task_id",)
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (1800000, 1),
    }

    task_id: str | int
    """ID задания на генерацию"""


class AcceptanceReportTasksTaskIdStatus(WBMethod[GetTasksResponse]):
    """Проверить статус

    GET /api/v1/acceptance_report/tasks/{task_id}/status
    """

    __path__ = "/api/v1/acceptance_report/tasks/{task_id}/status"
    __http_method__ = "GET"
    __returns__ = GetTasksResponse
    __path_params__ = ("task_id",)
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (5000, 1),
        "service": (5000, 1),
        "basic_secret": (5000, 1),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    task_id: str | int
    """ID задания на генерацию"""


class AnalyticsAntifraudDetails(WBMethod[None]):
    """Самовыкупы

    GET /api/v1/analytics/antifraud-details
    """

    __path__ = "/api/v1/analytics/antifraud-details"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"date": "date"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (600000, 10),
        "service": (600000, 10),
        "basic_secret": (600000, 10),
        "basic": (3600000, 1),
    }

    date: str | None = None
    """Дата, которая входит в отчётный период, `ГГГГ-ММ-ДД`.  Чтобы получить данные за всё время с
    августа 2023,  не указывайте этот параметр
    """


class AnalyticsBannedProductsBlocked(WBMethod[AnalyticsBannedProductsBlockedResponse]):
    """Получить отчёт

    GET /api/v1/analytics/banned-products/blocked
    """

    __path__ = "/api/v1/analytics/banned-products/blocked"
    __http_method__ = "GET"
    __returns__ = AnalyticsBannedProductsBlockedResponse
    __query_params__ = {"sort": "sort", "order": "order"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (10000, 6),
        "service": (10000, 6),
        "basic_secret": (10000, 6),
        "basic": (3600000, 1),
    }

    order: str
    """Порядок выдачи - `desc` — от наибольшего числового значения к наименьшему, от последнего по
    алфавиту значения к первому …
    """
    sort: str
    """Сортировка - `brand` — по бренду - `nmId` — по артикулу WB - `title` — по наименованию
    товара - `vendorCode` — по артикулу продавца …
    """


class AnalyticsBrandShare(WBMethod[None]):
    """Получить отчёт

    GET /api/v1/analytics/brand-share
    """

    __path__ = "/api/v1/analytics/brand-share"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {
        "parent_id": "parentId",
        "brand": "brand",
        "date_from": "dateFrom",
        "date_to": "dateTo",
    }
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (5000, 20),
        "service": (5000, 20),
        "basic_secret": (5000, 20),
        "basic": (3600000, 1),
    }

    brand: str
    """Бренд"""
    date_from: str
    """Начало отчётного периода, `ГГГГ-ММ-ДД`"""
    date_to: str
    """Конец отчётного периода, `ГГГГ-ММ-ДД`"""
    parent_id: int
    """ID родительской категории"""


class AnalyticsBrandShareBrands(WBMethod[None]):
    """Бренды продавца

    GET /api/v1/analytics/brand-share/brands
    """

    __path__ = "/api/v1/analytics/brand-share/brands"
    __http_method__ = "GET"
    __returns__ = None
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 10),
        "service": (60000, 10),
        "basic_secret": (60000, 10),
        "basic": (3600000, 1),
    }


class AnalyticsBrandShareParentSubjects(WBMethod[None]):
    """Родительские категории бренда

    GET /api/v1/analytics/brand-share/parent-subjects
    """

    __path__ = "/api/v1/analytics/brand-share/parent-subjects"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"locale": "locale", "brand": "brand", "date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (5000, 20),
        "service": (5000, 20),
        "basic_secret": (5000, 20),
        "basic": (3600000, 1),
    }

    brand: str
    """Бренд"""
    date_from: str
    """Начало отчётного периода, `ГГГГ-ММ-ДД`"""
    date_to: str
    """Конец отчётного периода, `ГГГГ-ММ-ДД`"""
    locale: str | None = None
    """Язык поля ответа `parentName`:   - `ru` — русский   - `en` — английский   - `zh` — китайский
    """


class AnalyticsExciseReport(WBMethod[ExciseReportResponse]):
    """Получить отчёт

    POST /api/v1/analytics/excise-report
    """

    __path__ = "/api/v1/analytics/excise-report"
    __http_method__ = "POST"
    __returns__ = ExciseReportResponse
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1800000, 10),
        "service": (1800000, 10),
        "basic_secret": (1800000, 10),
        "basic": (43200000, 1),
    }
    __body_fields__ = {"countries": "countries"}

    date_from: str
    """Начало отчётного периода, `ГГГГ-ММ-ДД`"""
    date_to: str
    """Конец отчётного периода, `ГГГГ-ММ-ДД`"""
    countries: list[str] | None = None
    """Код стран по стандарту ISO 3166-2. Чтобы получить данные по всем странам, оставьте параметр
    пустым
    """


class AnalyticsGoodsLabeling(WBMethod[None]):
    """Маркировка товара

    GET /api/v1/analytics/goods-labeling
    """

    __path__ = "/api/v1/analytics/goods-labeling"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 10),
        "service": (60000, 10),
        "basic_secret": (60000, 10),
        "basic": (3600000, 1),
    }

    date_from: str
    """Начало отчётного периода, `ГГГГ-ММ-ДД`"""
    date_to: str
    """Конец отчётного периода, `ГГГГ-ММ-ДД`"""


class AnalyticsGoodsReturn(WBMethod[AnalyticsGoodsReturnResponse]):
    """Получить отчёт

    GET /api/v1/analytics/goods-return
    """

    __path__ = "/api/v1/analytics/goods-return"
    __http_method__ = "GET"
    __returns__ = AnalyticsGoodsReturnResponse
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 10),
        "service": (60000, 10),
        "basic_secret": (60000, 10),
        "basic": (1800000, 1),
    }

    date_from: str
    """Дата начала отчётного периода"""
    date_to: str
    """Дата окончания отчётного периода"""


class AnalyticsRegionSale(WBMethod[None]):
    """Получить отчёт

    GET /api/v1/analytics/region-sale
    """

    __path__ = "/api/v1/analytics/region-sale"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (10000, 5),
        "service": (10000, 5),
        "basic_secret": (10000, 5),
        "basic": (3600000, 1),
    }

    date_from: str
    """Начало отчётного периода, `ГГГГ-ММ-ДД`"""
    date_to: str
    """Конец отчётного периода, `ГГГГ-ММ-ДД`"""


class AnalyticsV1Deductions(WBMethod[None]):
    """Подмены и неверные вложения

    GET /api/analytics/v1/deductions
    """

    __path__ = "/api/analytics/v1/deductions"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {
        "date_from": "dateFrom",
        "date_to": "dateTo",
        "sort": "sort",
        "order": "order",
        "limit": "limit",
        "offset": "offset",
    }
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"

    date_to: str
    """Конец отчётного периода"""
    limit: int
    """Количество удержаний в ответе"""
    date_from: str | None = None
    """Начало отчётного периода. По умолчанию используются дата и время, когда были впервые
    получены данные для отчёта
    """
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
    order: str | None = None
    """Порядок выдачи: - `desc` — по убыванию - `asc` — по возрастанию"""
    sort: str | None = None
    """Сортировка: - `nmId` — по артикулу WB - `dtBonus` — по дате и времени удержания -
    `bonusSumm` — по сумме удержания
    """


class AnalyticsV1MeasurementPenalties(WBMethod[MeasurementPenalties]):
    """Удержания за занижение габаритов упаковки

    GET /api/analytics/v1/measurement-penalties
    """

    __path__ = "/api/analytics/v1/measurement-penalties"
    __http_method__ = "GET"
    __returns__ = MeasurementPenalties
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo", "limit": "limit", "offset": "offset"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (21600000, 1),
    }
    __paginate__ = "offset_query"
    __items__ = "data"

    date_to: str
    """Конец отчётного периода"""
    limit: int
    """Количество удержаний в ответе"""
    date_from: str | None = None
    """Начало отчётного периода. По умолчанию используется дата, когда были впервые получены данные
    для отчёта
    """
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""


class AnalyticsV1WarehouseMeasurements(WBMethod[WHM]):
    """Замеры склада

    GET /api/analytics/v1/warehouse-measurements
    """

    __path__ = "/api/analytics/v1/warehouse-measurements"
    __http_method__ = "GET"
    __returns__ = WHM
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo", "limit": "limit", "offset": "offset"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (21600000, 1),
    }
    __paginate__ = "offset_query"
    __items__ = "data"

    date_to: str
    """Конец отчётного периода"""
    limit: int
    """Количество замеров в ответе"""
    date_from: str | None = None
    """Начало отчётного периода. По умолчанию используется дата, когда были впервые получены данные
    для отчёта
    """
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""


class PaidStorageCreate(WBMethod[CreateTaskResponse]):
    """Создать отчёт

    GET /api/v1/paid_storage
    """

    __path__ = "/api/v1/paid_storage"
    __http_method__ = "GET"
    __returns__ = CreateTaskResponse
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 5),
        "service": (60000, 5),
        "basic_secret": (60000, 5),
        "basic": (3600000, 1),
    }
    __items__ = "data"

    date_from: str
    """Начало отчётного периода в формате RFC3339. Можно передать дату или дату со временем.
    Примеры:    * `2019-06-20`   * `2019-06-20T23:59:59` …
    """
    date_to: str
    """Конец отчётного периода в формате RFC3339. Можно передать дату или дату со временем.
    Примеры:    * `2019-06-20`   * `2019-06-20T23:59:59` …
    """


class PaidStorageTasksTaskIdDownload(WBMethod[list[PaidStorageTasksTaskIdDownloadResponseItem]]):
    """Получить отчёт

    GET /api/v1/paid_storage/tasks/{task_id}/download
    """

    __path__ = "/api/v1/paid_storage/tasks/{task_id}/download"
    __http_method__ = "GET"
    __returns__ = list[PaidStorageTasksTaskIdDownloadResponseItem]
    __path_params__ = ("task_id",)
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (1800000, 1),
    }

    task_id: str | int
    """ID задания на генерацию"""


class PaidStorageTasksTaskIdStatus(WBMethod[GetTasksResponse]):
    """Проверить статус

    GET /api/v1/paid_storage/tasks/{task_id}/status
    """

    __path__ = "/api/v1/paid_storage/tasks/{task_id}/status"
    __http_method__ = "GET"
    __returns__ = GetTasksResponse
    __path_params__ = ("task_id",)
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (5000, 5),
        "service": (5000, 5),
        "basic_secret": (5000, 5),
        "basic": (1800000, 2),
    }
    __items__ = "data"

    task_id: str | int
    """ID задания на генерацию"""


class SupplierOrders(WBMethod[list[OrdersItem]]):
    """Заказы

    GET /api/v1/supplier/orders
    """

    __path__ = "/api/v1/supplier/orders"
    __http_method__ = "GET"
    __returns__ = list[OrdersItem]
    __query_params__ = {"date_from": "dateFrom", "flag": "flag"}
    __scope__ = Scope.STATISTICS
    __host__ = "https://statistics-api.wildberries.ru"
    __sandbox_host__ = "https://statistics-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 10),
        "service": (60000, 10),
        "basic_secret": (60000, 10),
        "basic": (10800000, 1),
    }

    date_from: str
    """Дата и время последнего изменения по заказу. Дата в формате RFC3339. Можно передать дату или
    дату со временем. …
    """
    flag: int | None = None
    """Если параметр `flag=0` (или не указан в строке запроса), при вызове API возвращаются данные,
    …
    """


class SupplierSales(WBMethod[list[SalesItem]]):
    """Продажи

    GET /api/v1/supplier/sales
    """

    __path__ = "/api/v1/supplier/sales"
    __http_method__ = "GET"
    __returns__ = list[SalesItem]
    __query_params__ = {"date_from": "dateFrom", "flag": "flag"}
    __scope__ = Scope.STATISTICS
    __host__ = "https://statistics-api.wildberries.ru"
    __sandbox_host__ = "https://statistics-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (7200000, 1),
    }

    date_from: str
    """Дата и время последнего изменения по продаже/возврату. Дата в формате RFC3339. Можно
    передать дату или дату со временем. …
    """
    flag: int | None = None
    """Если параметр `flag=0` (или не указан в строке запроса), при вызове API возвращаются данные,
    …
    """


class WarehouseRemainsCreate(WBMethod[CreateTaskResponse]):
    """Создать отчёт

    GET /api/v1/warehouse_remains
    """

    __path__ = "/api/v1/warehouse_remains"
    __http_method__ = "GET"
    __returns__ = CreateTaskResponse
    __query_params__ = {
        "locale": "locale",
        "group_by_brand": "groupByBrand",
        "group_by_subject": "groupBySubject",
        "group_by_sa": "groupBySa",
        "group_by_nm": "groupByNm",
        "group_by_barcode": "groupByBarcode",
        "group_by_size": "groupBySize",
        "filter_pics": "filterPics",
        "filter_volume": "filterVolume",
    }
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 5),
        "service": (60000, 5),
        "basic_secret": (60000, 5),
        "basic": (900000, 1),
    }
    __items__ = "data"

    filter_pics: int | None = None
    """Фильтр по фото:   - `-1` — без фото   - `0` — не применять фильтр   - `1` — с фото"""
    filter_volume: int | None = None
    """Фильтр по объёму:   - `-1` — без габаритов   - `0` — не применять фильтр   - `3` — свыше
    трёх литров
    """
    group_by_barcode: bool | None = None
    """Разбивка по баркодам"""
    group_by_brand: bool | None = None
    """Разбивка по брендам"""
    group_by_nm: bool | None = None
    """Разбивка по артикулам WB. Если `groupByNm=true`, в ответе будет поле `volume`"""
    group_by_sa: bool | None = None
    """Разбивка по артикулам продавца"""
    group_by_size: bool | None = None
    """Разбивка по размерам"""
    group_by_subject: bool | None = None
    """Разбивка по предметам"""
    locale: str | None = None
    """Язык полей ответа `subjectName` и `warehouseName`:   - `ru` — русский   - `en` — английский
    - `zh` — китайский. Значения `warehouseName` на английском
    """


class WarehouseRemainsTasksTaskIdDownload(WBMethod[list[WarehouseRemainsTasksTaskIdDownloadResponseItem]]):
    """Получить отчёт

    GET /api/v1/warehouse_remains/tasks/{task_id}/download
    """

    __path__ = "/api/v1/warehouse_remains/tasks/{task_id}/download"
    __http_method__ = "GET"
    __returns__ = list[WarehouseRemainsTasksTaskIdDownloadResponseItem]
    __path_params__ = ("task_id",)
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 1),
        "service": (60000, 1),
        "basic_secret": (60000, 1),
        "basic": (900000, 1),
    }

    task_id: str | int
    """ID задания на генерацию"""


class WarehouseRemainsTasksTaskIdStatus(WBMethod[GetTasksResponse]):
    """Проверить статус

    GET /api/v1/warehouse_remains/tasks/{task_id}/status
    """

    __path__ = "/api/v1/warehouse_remains/tasks/{task_id}/status"
    __http_method__ = "GET"
    __returns__ = GetTasksResponse
    __path_params__ = ("task_id",)
    __scope__ = Scope.ANALYTICS
    __host__ = "https://seller-analytics-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (5000, 5),
        "service": (5000, 5),
        "basic_secret": (5000, 5),
        "basic": (900000, 1),
    }
    __items__ = "data"

    task_id: str | int
    """ID задания на генерацию"""
