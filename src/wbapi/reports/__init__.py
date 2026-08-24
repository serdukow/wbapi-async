from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    CreateAcceptanceReport,
    CreatePaidStorage,
    CreateWarehouseRemain,
    GetAcceptanceReportTasksDownload,
    GetAcceptanceReportTasksStatus,
    GetAnalyticsAntifraudDetails,
    GetAnalyticsBannedProductsBlocked,
    GetAnalyticsBrandShare,
    GetAnalyticsBrandShareBrands,
    GetAnalyticsBrandShareParentSubjects,
    GetAnalyticsDeductions,
    GetAnalyticsExciseReport,
    GetAnalyticsGoodsLabeling,
    GetAnalyticsGoodsReturns,
    GetAnalyticsMeasurementPenalties,
    GetAnalyticsRegionSale,
    GetAnalyticsWarehouseMeasurements,
    GetPaidStorageTasksDownload,
    GetPaidStorageTasksStatus,
    GetSupplierOrders,
    GetSupplierSales,
    GetWarehouseRemainsTasksDownload,
    GetWarehouseRemainsTasksStatus,
)
from .models import (
    WHM,
    CreateTaskResponse,
    ExciseReportResponse,
    GetAcceptanceReportTasksDownloadResponseItem,
    GetAnalyticsBannedProductsBlockedResponse,
    GetAnalyticsGoodsReturnsResponse,
    GetPaidStorageTasksDownloadResponseItem,
    GetTasksResponse,
    GetWarehouseRemainsTasksDownloadResponseItem,
    MeasurementPenalties,
    OrdersItem,
    SalesItem,
)


if TYPE_CHECKING:
    from ..client import WBApi


class Reports:
    """Отчёты.

    Узнать больше об отчётах можно в справочном центре

    С помощью этих методов вы можете получать основные отчёты и отчёты о:
      1. Остатках на складах
      2. Товарах с обязательной маркировкой
      3. Удержаниях
      4. Операциях при приёмке
      5. Платном хранении
      6. Продажах по регионам
      7. Доле бренда в продажах
      8. Заблокированных карточках
      9. Возвратах и перемещении товаров
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def create_acceptance_report(self, *, date_from: str, date_to: str) -> CreateTaskResponse:
        """Создать отчёт

        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        """
        return await CreateAcceptanceReport(date_from=date_from, date_to=date_to).emit(self._api)

    async def create_paid_storage(self, *, date_from: str, date_to: str) -> CreateTaskResponse:
        """Создать отчёт

        :param date_from: Начало отчётного периода в формате RFC3339. Можно передать дату или дату со
            временем. Примеры:    * `2019-06-20`   * `2019-06-20T23:59:59` …
        :param date_to: Конец отчётного периода в формате RFC3339. Можно передать дату или дату со временем.
            Примеры:    * `2019-06-20`   * `2019-06-20T23:59:59` …
        """
        return await CreatePaidStorage(date_from=date_from, date_to=date_to).emit(self._api)

    async def create_warehouse_remain(
        self,
        *,
        filter_pics: int | None = 0,
        filter_volume: int | None = 0,
        group_by_barcode: bool | None = False,
        group_by_brand: bool | None = False,
        group_by_nm: bool | None = False,
        group_by_sa: bool | None = False,
        group_by_size: bool | None = False,
        group_by_subject: bool | None = False,
        locale: str | None = "ru",
    ) -> CreateTaskResponse:
        """Создать отчёт

        :param filter_pics: Фильтр по фото:   - `-1` — без фото   - `0` — не применять фильтр   - `1` — с
            фото
        :param filter_volume: Фильтр по объёму:   - `-1` — без габаритов   - `0` — не применять фильтр   -
            `3` — свыше трёх литров
        :param group_by_barcode: Разбивка по баркодам
        :param group_by_brand: Разбивка по брендам
        :param group_by_nm: Разбивка по артикулам WB. Если `groupByNm=true`, в ответе будет поле `volume`
        :param group_by_sa: Разбивка по артикулам продавца
        :param group_by_size: Разбивка по размерам
        :param group_by_subject: Разбивка по предметам
        :param locale: Язык полей ответа `subjectName` и `warehouseName`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский. Значения `warehouseName` на английском
        """
        return await CreateWarehouseRemain(
            filter_pics=filter_pics,
            filter_volume=filter_volume,
            group_by_barcode=group_by_barcode,
            group_by_brand=group_by_brand,
            group_by_nm=group_by_nm,
            group_by_sa=group_by_sa,
            group_by_size=group_by_size,
            group_by_subject=group_by_subject,
            locale=locale,
        ).emit(self._api)

    async def get_acceptance_report_tasks_download(
        self, *, task_id: str | int
    ) -> list[GetAcceptanceReportTasksDownloadResponseItem]:
        """Получить отчёт

        :param task_id: ID задания на генерацию
        """
        return await GetAcceptanceReportTasksDownload(task_id=task_id).emit(self._api)

    async def get_acceptance_report_tasks_status(self, *, task_id: str | int) -> GetTasksResponse:
        """Проверить статус

        :param task_id: ID задания на генерацию
        """
        return await GetAcceptanceReportTasksStatus(task_id=task_id).emit(self._api)

    async def get_analytics_antifraud_details(self, *, date: str | None = None) -> None:
        """Самовыкупы

        :param date: Дата, которая входит в отчётный период, `ГГГГ-ММ-ДД`.  Чтобы получить данные за всё
            время с августа 2023,  не указывайте этот параметр
        """
        await GetAnalyticsAntifraudDetails(date=date).emit(self._api)

    async def get_analytics_banned_products_blocked(
        self, *, order: str, sort: str
    ) -> GetAnalyticsBannedProductsBlockedResponse:
        """Получить отчёт

        :param order: Порядок выдачи - `desc` — от наибольшего числового значения к наименьшему, от
            последнего по алфавиту значения к первому …
        :param sort: Сортировка - `brand` — по бренду - `nmId` — по артикулу WB - `title` — по наименованию
            товара - `vendorCode` — по артикулу продавца …
        """
        return await GetAnalyticsBannedProductsBlocked(order=order, sort=sort).emit(self._api)

    async def get_analytics_brand_share(
        self, *, brand: str, date_from: str, date_to: str, parent_id: int
    ) -> None:
        """Получить отчёт

        :param brand: Бренд
        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        :param parent_id: ID родительской категории
        """
        await GetAnalyticsBrandShare(
            brand=brand, date_from=date_from, date_to=date_to, parent_id=parent_id
        ).emit(self._api)

    async def get_analytics_brand_share_brands(self) -> None:
        """Бренды продавца"""
        await GetAnalyticsBrandShareBrands().emit(self._api)

    async def get_analytics_brand_share_parent_subjects(
        self, *, brand: str, date_from: str, date_to: str, locale: str | None = "ru"
    ) -> None:
        """Родительские категории бренда

        :param brand: Бренд
        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        :param locale: Язык поля ответа `parentName`:   - `ru` — русский   - `en` — английский   - `zh` —
            китайский
        """
        await GetAnalyticsBrandShareParentSubjects(
            brand=brand, date_from=date_from, date_to=date_to, locale=locale
        ).emit(self._api)

    async def get_analytics_deductions(
        self,
        *,
        date_to: str,
        limit: int,
        date_from: str | None = None,
        offset: int | None = 0,
        order: str | None = "desc",
        sort: str | None = "dtBonus",
        auto_paginate: bool = False,
    ) -> None | list[Any]:
        """Подмены и неверные вложения

        :param date_to: Конец отчётного периода
        :param limit: Количество удержаний в ответе
        :param date_from: Начало отчётного периода. По умолчанию используются дата и время, когда были
            впервые получены данные для отчёта
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param order: Порядок выдачи: - `desc` — по убыванию - `asc` — по возрастанию
        :param sort: Сортировка: - `nmId` — по артикулу WB - `dtBonus` — по дате и времени удержания -
            `bonusSumm` — по сумме удержания
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetAnalyticsDeductions(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset, order=order, sort=sort
        )
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_get_analytics_deductions(
        self,
        *,
        date_to: str,
        limit: int,
        date_from: str | None = None,
        offset: int | None = 0,
        order: str | None = "desc",
        sort: str | None = "dtBonus",
    ) -> AsyncIterator[Any]:
        """Подмены и неверные вложения — постранично, по одной записи.

        :param date_to: Конец отчётного периода
        :param limit: Количество удержаний в ответе
        :param date_from: Начало отчётного периода. По умолчанию используются дата и время, когда были
            впервые получены данные для отчёта
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param order: Порядок выдачи: - `desc` — по убыванию - `asc` — по возрастанию
        :param sort: Сортировка: - `nmId` — по артикулу WB - `dtBonus` — по дате и времени удержания -
            `bonusSumm` — по сумме удержания
        """
        async for item in GetAnalyticsDeductions(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset, order=order, sort=sort
        ).stream(self._api):
            yield item

    async def get_analytics_excise_report(
        self, *, date_from: str, date_to: str, countries: list[str] | None = None
    ) -> ExciseReportResponse:
        """Получить отчёт

        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        :param countries: Код стран по стандарту ISO 3166-2. Чтобы получить данные по всем странам, оставьте
            параметр пустым
        """
        return await GetAnalyticsExciseReport(date_from=date_from, date_to=date_to, countries=countries).emit(
            self._api
        )

    async def get_analytics_goods_labeling(self, *, date_from: str, date_to: str) -> None:
        """Маркировка товара

        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        """
        await GetAnalyticsGoodsLabeling(date_from=date_from, date_to=date_to).emit(self._api)

    async def get_analytics_goods_returns(
        self, *, date_from: str, date_to: str
    ) -> GetAnalyticsGoodsReturnsResponse:
        """Получить отчёт

        :param date_from: Дата начала отчётного периода
        :param date_to: Дата окончания отчётного периода
        """
        return await GetAnalyticsGoodsReturns(date_from=date_from, date_to=date_to).emit(self._api)

    async def get_analytics_measurement_penalties(
        self,
        *,
        date_to: str,
        limit: int,
        date_from: str | None = None,
        offset: int | None = 0,
        auto_paginate: bool = False,
    ) -> MeasurementPenalties | list[Any]:
        """Удержания за занижение габаритов упаковки

        :param date_to: Конец отчётного периода
        :param limit: Количество удержаний в ответе
        :param date_from: Начало отчётного периода. По умолчанию используется дата, когда были впервые
            получены данные для отчёта
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetAnalyticsMeasurementPenalties(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_analytics_measurement_penalties(
        self, *, date_to: str, limit: int, date_from: str | None = None, offset: int | None = 0
    ) -> AsyncIterator[Any]:
        """Удержания за занижение габаритов упаковки — постранично, по одной записи.

        :param date_to: Конец отчётного периода
        :param limit: Количество удержаний в ответе
        :param date_from: Начало отчётного периода. По умолчанию используется дата, когда были впервые
            получены данные для отчёта
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        """
        async for item in GetAnalyticsMeasurementPenalties(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset
        ).stream(self._api):
            yield item

    async def get_analytics_region_sale(self, *, date_from: str, date_to: str) -> None:
        """Получить отчёт

        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        """
        await GetAnalyticsRegionSale(date_from=date_from, date_to=date_to).emit(self._api)

    async def get_analytics_warehouse_measurements(
        self,
        *,
        date_to: str,
        limit: int,
        date_from: str | None = None,
        offset: int | None = 0,
        auto_paginate: bool = False,
    ) -> WHM | list[Any]:
        """Замеры склада

        :param date_to: Конец отчётного периода
        :param limit: Количество замеров в ответе
        :param date_from: Начало отчётного периода. По умолчанию используется дата, когда были впервые
            получены данные для отчёта
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetAnalyticsWarehouseMeasurements(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_analytics_warehouse_measurements(
        self, *, date_to: str, limit: int, date_from: str | None = None, offset: int | None = 0
    ) -> AsyncIterator[Any]:
        """Замеры склада — постранично, по одной записи.

        :param date_to: Конец отчётного периода
        :param limit: Количество замеров в ответе
        :param date_from: Начало отчётного периода. По умолчанию используется дата, когда были впервые
            получены данные для отчёта
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        """
        async for item in GetAnalyticsWarehouseMeasurements(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset
        ).stream(self._api):
            yield item

    async def get_paid_storage_tasks_download(
        self, *, task_id: str | int
    ) -> list[GetPaidStorageTasksDownloadResponseItem]:
        """Получить отчёт

        :param task_id: ID задания на генерацию
        """
        return await GetPaidStorageTasksDownload(task_id=task_id).emit(self._api)

    async def get_paid_storage_tasks_status(self, *, task_id: str | int) -> GetTasksResponse:
        """Проверить статус

        :param task_id: ID задания на генерацию
        """
        return await GetPaidStorageTasksStatus(task_id=task_id).emit(self._api)

    async def get_supplier_orders(self, *, date_from: str, flag: int | None = 0) -> list[OrdersItem]:
        """Заказы

        :param date_from: Дата и время последнего изменения по заказу. Дата в формате RFC3339. Можно
            передать дату или дату со временем. …
        :param flag: Если параметр `flag=0` (или не указан в строке запроса), при вызове API возвращаются
            данные, …
        """
        return await GetSupplierOrders(date_from=date_from, flag=flag).emit(self._api)

    async def get_supplier_sales(self, *, date_from: str, flag: int | None = 0) -> list[SalesItem]:
        """Продажи

        :param date_from: Дата и время последнего изменения по продаже/возврату. Дата в формате RFC3339.
            Можно передать дату или дату со временем. …
        :param flag: Если параметр `flag=0` (или не указан в строке запроса), при вызове API возвращаются
            данные, …
        """
        return await GetSupplierSales(date_from=date_from, flag=flag).emit(self._api)

    async def get_warehouse_remains_tasks_download(
        self, *, task_id: str | int
    ) -> list[GetWarehouseRemainsTasksDownloadResponseItem]:
        """Получить отчёт

        :param task_id: ID задания на генерацию
        """
        return await GetWarehouseRemainsTasksDownload(task_id=task_id).emit(self._api)

    async def get_warehouse_remains_tasks_status(self, *, task_id: str | int) -> GetTasksResponse:
        """Проверить статус

        :param task_id: ID задания на генерацию
        """
        return await GetWarehouseRemainsTasksStatus(task_id=task_id).emit(self._api)
