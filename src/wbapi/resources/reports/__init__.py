from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    AcceptanceReportCreate,
    AcceptanceReportTasksTaskIdDownload,
    AcceptanceReportTasksTaskIdStatus,
    AnalyticsAntifraudDetails,
    AnalyticsBannedProductsBlocked,
    AnalyticsBrandShare,
    AnalyticsBrandShareBrands,
    AnalyticsBrandShareParentSubjects,
    AnalyticsExciseReport,
    AnalyticsGoodsLabeling,
    AnalyticsGoodsReturn,
    AnalyticsRegionSale,
    AnalyticsV1Deductions,
    AnalyticsV1MeasurementPenalties,
    AnalyticsV1WarehouseMeasurements,
    PaidStorageCreate,
    PaidStorageTasksTaskIdDownload,
    PaidStorageTasksTaskIdStatus,
    SupplierOrders,
    SupplierSales,
    WarehouseRemainsCreate,
    WarehouseRemainsTasksTaskIdDownload,
    WarehouseRemainsTasksTaskIdStatus,
)
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


if TYPE_CHECKING:
    from ...client import WBApi


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

    async def acceptance_report_create(self, *, date_from: str, date_to: str) -> CreateTaskResponse:
        """Создать отчёт

        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        """
        return await AcceptanceReportCreate(date_from=date_from, date_to=date_to).emit(self._api)

    async def acceptance_report_tasks_task_id_download(
        self, *, task_id: str | int
    ) -> list[AcceptanceReportTasksTaskIdDownloadResponseItem]:
        """Получить отчёт

        :param task_id: ID задания на генерацию
        """
        return await AcceptanceReportTasksTaskIdDownload(task_id=task_id).emit(self._api)

    async def acceptance_report_tasks_task_id_status(self, *, task_id: str | int) -> GetTasksResponse:
        """Проверить статус

        :param task_id: ID задания на генерацию
        """
        return await AcceptanceReportTasksTaskIdStatus(task_id=task_id).emit(self._api)

    async def analytics_antifraud_details(self, *, date: str | None = None) -> None:
        """Самовыкупы

        :param date: Дата, которая входит в отчётный период, `ГГГГ-ММ-ДД`.  Чтобы получить данные за всё
            время с августа 2023,  не указывайте этот параметр
        """
        await AnalyticsAntifraudDetails(date=date).emit(self._api)

    async def analytics_banned_products_blocked(
        self, *, order: str, sort: str
    ) -> AnalyticsBannedProductsBlockedResponse:
        """Получить отчёт

        :param order: Порядок выдачи - `desc` — от наибольшего числового значения к наименьшему, от
            последнего по алфавиту значения к первому …
        :param sort: Сортировка - `brand` — по бренду - `nmId` — по артикулу WB - `title` — по наименованию
            товара - `vendorCode` — по артикулу продавца …
        """
        return await AnalyticsBannedProductsBlocked(order=order, sort=sort).emit(self._api)

    async def analytics_brand_share(
        self, *, brand: str, date_from: str, date_to: str, parent_id: int
    ) -> None:
        """Получить отчёт

        :param brand: Бренд
        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        :param parent_id: ID родительской категории
        """
        await AnalyticsBrandShare(
            brand=brand, date_from=date_from, date_to=date_to, parent_id=parent_id
        ).emit(self._api)

    async def analytics_brand_share_brands(self) -> None:
        """Бренды продавца"""
        await AnalyticsBrandShareBrands().emit(self._api)

    async def analytics_brand_share_parent_subjects(
        self, *, brand: str, date_from: str, date_to: str, locale: str | None = None
    ) -> None:
        """Родительские категории бренда

        :param brand: Бренд
        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        :param locale: Язык поля ответа `parentName`:   - `ru` — русский   - `en` — английский   - `zh` —
            китайский
        """
        await AnalyticsBrandShareParentSubjects(
            brand=brand, date_from=date_from, date_to=date_to, locale=locale
        ).emit(self._api)

    async def analytics_excise_report(
        self, *, date_from: str, date_to: str, countries: list[str] | None = None
    ) -> ExciseReportResponse:
        """Получить отчёт

        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        :param countries: Код стран по стандарту ISO 3166-2. Чтобы получить данные по всем странам, оставьте
            параметр пустым
        """
        return await AnalyticsExciseReport(date_from=date_from, date_to=date_to, countries=countries).emit(
            self._api
        )

    async def analytics_goods_labeling(self, *, date_from: str, date_to: str) -> None:
        """Маркировка товара

        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        """
        await AnalyticsGoodsLabeling(date_from=date_from, date_to=date_to).emit(self._api)

    async def analytics_goods_return(self, *, date_from: str, date_to: str) -> AnalyticsGoodsReturnResponse:
        """Получить отчёт

        :param date_from: Дата начала отчётного периода
        :param date_to: Дата окончания отчётного периода
        """
        return await AnalyticsGoodsReturn(date_from=date_from, date_to=date_to).emit(self._api)

    async def analytics_region_sale(self, *, date_from: str, date_to: str) -> None:
        """Получить отчёт

        :param date_from: Начало отчётного периода, `ГГГГ-ММ-ДД`
        :param date_to: Конец отчётного периода, `ГГГГ-ММ-ДД`
        """
        await AnalyticsRegionSale(date_from=date_from, date_to=date_to).emit(self._api)

    async def analytics_v1_deductions(
        self,
        *,
        date_to: str,
        limit: int,
        date_from: str | None = None,
        offset: int | None = None,
        order: str | None = None,
        sort: str | None = None,
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
        call = AnalyticsV1Deductions(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset, order=order, sort=sort
        )
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_analytics_v1_deductions(
        self,
        *,
        date_to: str,
        limit: int,
        date_from: str | None = None,
        offset: int | None = None,
        order: str | None = None,
        sort: str | None = None,
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
        async for item in AnalyticsV1Deductions(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset, order=order, sort=sort
        ).stream(self._api):
            yield item

    async def analytics_v1_measurement_penalties(
        self,
        *,
        date_to: str,
        limit: int,
        date_from: str | None = None,
        offset: int | None = None,
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
        call = AnalyticsV1MeasurementPenalties(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_analytics_v1_measurement_penalties(
        self, *, date_to: str, limit: int, date_from: str | None = None, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Удержания за занижение габаритов упаковки — постранично, по одной записи.

        :param date_to: Конец отчётного периода
        :param limit: Количество удержаний в ответе
        :param date_from: Начало отчётного периода. По умолчанию используется дата, когда были впервые
            получены данные для отчёта
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        """
        async for item in AnalyticsV1MeasurementPenalties(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset
        ).stream(self._api):
            yield item

    async def analytics_v1_warehouse_measurements(
        self,
        *,
        date_to: str,
        limit: int,
        date_from: str | None = None,
        offset: int | None = None,
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
        call = AnalyticsV1WarehouseMeasurements(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_analytics_v1_warehouse_measurements(
        self, *, date_to: str, limit: int, date_from: str | None = None, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Замеры склада — постранично, по одной записи.

        :param date_to: Конец отчётного периода
        :param limit: Количество замеров в ответе
        :param date_from: Начало отчётного периода. По умолчанию используется дата, когда были впервые
            получены данные для отчёта
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        """
        async for item in AnalyticsV1WarehouseMeasurements(
            date_to=date_to, limit=limit, date_from=date_from, offset=offset
        ).stream(self._api):
            yield item

    async def paid_storage_create(self, *, date_from: str, date_to: str) -> CreateTaskResponse:
        """Создать отчёт

        :param date_from: Начало отчётного периода в формате RFC3339. Можно передать дату или дату со
            временем. Примеры:    * `2019-06-20`   * `2019-06-20T23:59:59` …
        :param date_to: Конец отчётного периода в формате RFC3339. Можно передать дату или дату со временем.
            Примеры:    * `2019-06-20`   * `2019-06-20T23:59:59` …
        """
        return await PaidStorageCreate(date_from=date_from, date_to=date_to).emit(self._api)

    async def paid_storage_tasks_task_id_download(
        self, *, task_id: str | int
    ) -> list[PaidStorageTasksTaskIdDownloadResponseItem]:
        """Получить отчёт

        :param task_id: ID задания на генерацию
        """
        return await PaidStorageTasksTaskIdDownload(task_id=task_id).emit(self._api)

    async def paid_storage_tasks_task_id_status(self, *, task_id: str | int) -> GetTasksResponse:
        """Проверить статус

        :param task_id: ID задания на генерацию
        """
        return await PaidStorageTasksTaskIdStatus(task_id=task_id).emit(self._api)

    async def supplier_orders(self, *, date_from: str, flag: int | None = None) -> list[OrdersItem]:
        """Заказы

        :param date_from: Дата и время последнего изменения по заказу. Дата в формате RFC3339. Можно
            передать дату или дату со временем. …
        :param flag: Если параметр `flag=0` (или не указан в строке запроса), при вызове API возвращаются
            данные, …
        """
        return await SupplierOrders(date_from=date_from, flag=flag).emit(self._api)

    async def supplier_sales(self, *, date_from: str, flag: int | None = None) -> list[SalesItem]:
        """Продажи

        :param date_from: Дата и время последнего изменения по продаже/возврату. Дата в формате RFC3339.
            Можно передать дату или дату со временем. …
        :param flag: Если параметр `flag=0` (или не указан в строке запроса), при вызове API возвращаются
            данные, …
        """
        return await SupplierSales(date_from=date_from, flag=flag).emit(self._api)

    async def warehouse_remains_create(
        self,
        *,
        filter_pics: int | None = None,
        filter_volume: int | None = None,
        group_by_barcode: bool | None = None,
        group_by_brand: bool | None = None,
        group_by_nm: bool | None = None,
        group_by_sa: bool | None = None,
        group_by_size: bool | None = None,
        group_by_subject: bool | None = None,
        locale: str | None = None,
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
        return await WarehouseRemainsCreate(
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

    async def warehouse_remains_tasks_task_id_download(
        self, *, task_id: str | int
    ) -> list[WarehouseRemainsTasksTaskIdDownloadResponseItem]:
        """Получить отчёт

        :param task_id: ID задания на генерацию
        """
        return await WarehouseRemainsTasksTaskIdDownload(task_id=task_id).emit(self._api)

    async def warehouse_remains_tasks_task_id_status(self, *, task_id: str | int) -> GetTasksResponse:
        """Проверить статус

        :param task_id: ID задания на генерацию
        """
        return await WarehouseRemainsTasksTaskIdStatus(task_id=task_id).emit(self._api)
