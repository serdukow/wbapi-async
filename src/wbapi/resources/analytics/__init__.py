from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    NmReportDownloads,
    NmReportDownloadsCreate,
    NmReportDownloadsFileDownloadId,
    NmReportDownloadsRetryCreate,
    SearchReportProductOrdersCreate,
    SearchReportProductSearchTextsCreate,
    SearchReportReportCreate,
    SearchReportTableDetailsCreate,
    SearchReportTableGroupsCreate,
    StocksReportOfficesCreate,
    StocksReportProductsGroupsCreate,
    StocksReportProductsProductsCreate,
    StocksReportProductsSizesCreate,
    V1OrderFeed,
    V1StocksReportWbWarehousesCreate,
    V2ItemRating,
    V3SalesFunnelGroupedHistoryCreate,
    V3SalesFunnelProductsCreate,
    V3SalesFunnelProductsHistoryCreate,
)
from .models import (
    CommonResponseProperties,
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
    StocksReportOfficesCreateResponse,
    StocksReportProductsGroupsCreateResponse,
    StocksReportProductsProductsCreateResponse,
    StocksReportProductsSizesCreateResponse,
    V1OrderFeedPagination,
    V1OrderFeedResponse,
    V1OrderFeedSelectedPeriod,
    V1StocksReportWbWarehousesCreateResponse,
    V2ItemRatingResponse,
    V3SalesFunnelGroupedHistoryCreateResponse,
    V3SalesFunnelProductsCreateResponse,
    V3SalesFunnelProductsHistoryCreateResponseItem,
)


if TYPE_CHECKING:
    from ...client import WBApi


class Analytics:
    """Аналитика и данные.

    Узнать больше об аналитике и данных можно в справочном центре

    В разделе описаны методы получения:
      1. Воронки продаж
      2. Ленты заказов
      3. Поисковых запросов по вашим товарам
      4. Истории остатков
      5. Оценки товара
      6. Аналитики продавца в формате CSV
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def nm_report_downloads(
        self, *, filter_download_ids: list[str] | None = None
    ) -> NmReportGetReportsResponse:
        """Получить список отчётов

        :param filter_download_ids: ID отчёта
        """
        return await NmReportDownloads(filter_download_ids=filter_download_ids).emit(self._api)

    async def nm_report_downloads_create(self, *, body: Any) -> NmReportCreateReportResponse:
        """Создать отчёт"""
        return await NmReportDownloadsCreate(body=body).emit(self._api)

    async def nm_report_downloads_file_download_id(self, *, download_id: str | int) -> None:
        """Получить отчёт

        :param download_id: ID отчёта
        """
        await NmReportDownloadsFileDownloadId(download_id=download_id).emit(self._api)

    async def nm_report_downloads_retry_create(
        self, *, download_id: str | None = None
    ) -> NmReportRetryReportResponse:
        """Сгенерировать отчёт повторно

        :param download_id: ID отчёта
        """
        return await NmReportDownloadsRetryCreate(download_id=download_id).emit(self._api)

    async def search_report_product_orders_create(
        self, *, nm_id: int, period: PeriodOrdersRequest, search_texts: list[str]
    ) -> CommonResponseProperties:
        """Заказы и позиции по поисковым запросам товара

        :param nm_id: Артикул WB
        :param search_texts: Поисковые запросы. Для тарифов Джема **Продвинутый** и **Премиальный** максимум
            — 100
        """
        return await SearchReportProductOrdersCreate(
            nm_id=nm_id, period=period, search_texts=search_texts
        ).emit(self._api)

    async def search_report_product_search_texts_create(
        self,
        *,
        current_period: Period,
        limit: int,
        nm_ids: list[int],
        order_by: OrderByGrTe,
        top_order_by: str,
        include_search_texts: bool | None = None,
        include_substituted_skus: bool | None = None,
        past_period: PastPeriod | None = None,
    ) -> CommonResponseProperties:
        """Поисковые запросы по товару

        :param nm_ids: Список артикулов WB
        :param top_order_by: Фильтрация по поисковым запросам, по которым больше всего:   - `openCard` —
            перешли в карточку   - `addToCart` — добавили в корзину …
        :param include_search_texts: Показать данные по поисковым запросам без учёта подменного артикула
        :param include_substituted_skus: Показать данные по прямым запросам с подменным артикулом
        """
        return await SearchReportProductSearchTextsCreate(
            current_period=current_period,
            limit=limit,
            nm_ids=nm_ids,
            order_by=order_by,
            top_order_by=top_order_by,
            include_search_texts=include_search_texts,
            include_substituted_skus=include_substituted_skus,
            past_period=past_period,
        ).emit(self._api)

    async def search_report_report_create(
        self,
        *,
        current_period: Period,
        limit: int,
        offset: int,
        order_by: OrderByMainAndDetails,
        position_cluster: str,
        brand_names: list[str] | None = None,
        include_search_texts: bool | None = None,
        include_substituted_skus: bool | None = None,
        nm_ids: list[int] | None = None,
        past_period: PastPeriod | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
        auto_paginate: bool = False,
    ) -> CommonResponseProperties | list[Any]:
        """Основная страница

        :param limit: Количество групп товаров в ответе
        :param offset: После какого элемента выдавать данные
        :param brand_names: Список брендов для фильтрации
        :param include_search_texts: Показать данные по поисковым запросам без учёта подменного артикула
        :param include_substituted_skus: Показать данные по прямым запросам с подменным артикулом
        :param nm_ids: Список артикулов WB для фильтрации
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = SearchReportReportCreate(
            current_period=current_period,
            limit=limit,
            offset=offset,
            order_by=order_by,
            position_cluster=position_cluster,
            brand_names=brand_names,
            include_search_texts=include_search_texts,
            include_substituted_skus=include_substituted_skus,
            nm_ids=nm_ids,
            past_period=past_period,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_search_report_report_create(
        self,
        *,
        current_period: Period,
        limit: int,
        offset: int,
        order_by: OrderByMainAndDetails,
        position_cluster: str,
        brand_names: list[str] | None = None,
        include_search_texts: bool | None = None,
        include_substituted_skus: bool | None = None,
        nm_ids: list[int] | None = None,
        past_period: PastPeriod | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
    ) -> AsyncIterator[Any]:
        """Основная страница — постранично, по одной записи.

        :param limit: Количество групп товаров в ответе
        :param offset: После какого элемента выдавать данные
        :param brand_names: Список брендов для фильтрации
        :param include_search_texts: Показать данные по поисковым запросам без учёта подменного артикула
        :param include_substituted_skus: Показать данные по прямым запросам с подменным артикулом
        :param nm_ids: Список артикулов WB для фильтрации
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        """
        async for item in SearchReportReportCreate(
            current_period=current_period,
            limit=limit,
            offset=offset,
            order_by=order_by,
            position_cluster=position_cluster,
            brand_names=brand_names,
            include_search_texts=include_search_texts,
            include_substituted_skus=include_substituted_skus,
            nm_ids=nm_ids,
            past_period=past_period,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        ).stream(self._api):
            yield item

    async def search_report_table_details_create(
        self,
        *,
        current_period: Period,
        limit: int,
        offset: int,
        order_by: OrderByMainAndDetails,
        position_cluster: str,
        brand_name: str | None = None,
        include_search_texts: bool | None = None,
        include_substituted_skus: bool | None = None,
        nm_ids: list[int] | None = None,
        past_period: PastPeriod | None = None,
        subject_id: int | None = None,
        tag_id: int | None = None,
        auto_paginate: bool = False,
    ) -> CommonResponseProperties | list[Any]:
        """Пагинация по товарам в группе

        :param limit: Количество товаров в ответе
        :param offset: После какого элемента выдавать данные
        :param position_cluster: Товары с какой средней позицией в поиске показывать в отчёте:   - `all` —
            все   - `firstHundred` — от 1 до 100   - `secondHundred` — от 101 до 200 …
        :param brand_name: Название товара
        :param include_search_texts: Показать данные по поисковым запросам без учёта подменного артикула
        :param include_substituted_skus: Показать данные по прямым запросам с подменным артикулом
        :param nm_ids: Список артикулов WB
        :param subject_id: ID предмета
        :param tag_id: ID ярлыка
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = SearchReportTableDetailsCreate(
            current_period=current_period,
            limit=limit,
            offset=offset,
            order_by=order_by,
            position_cluster=position_cluster,
            brand_name=brand_name,
            include_search_texts=include_search_texts,
            include_substituted_skus=include_substituted_skus,
            nm_ids=nm_ids,
            past_period=past_period,
            subject_id=subject_id,
            tag_id=tag_id,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_search_report_table_details_create(
        self,
        *,
        current_period: Period,
        limit: int,
        offset: int,
        order_by: OrderByMainAndDetails,
        position_cluster: str,
        brand_name: str | None = None,
        include_search_texts: bool | None = None,
        include_substituted_skus: bool | None = None,
        nm_ids: list[int] | None = None,
        past_period: PastPeriod | None = None,
        subject_id: int | None = None,
        tag_id: int | None = None,
    ) -> AsyncIterator[Any]:
        """Пагинация по товарам в группе — постранично, по одной записи.

        :param limit: Количество товаров в ответе
        :param offset: После какого элемента выдавать данные
        :param position_cluster: Товары с какой средней позицией в поиске показывать в отчёте:   - `all` —
            все   - `firstHundred` — от 1 до 100   - `secondHundred` — от 101 до 200 …
        :param brand_name: Название товара
        :param include_search_texts: Показать данные по поисковым запросам без учёта подменного артикула
        :param include_substituted_skus: Показать данные по прямым запросам с подменным артикулом
        :param nm_ids: Список артикулов WB
        :param subject_id: ID предмета
        :param tag_id: ID ярлыка
        """
        async for item in SearchReportTableDetailsCreate(
            current_period=current_period,
            limit=limit,
            offset=offset,
            order_by=order_by,
            position_cluster=position_cluster,
            brand_name=brand_name,
            include_search_texts=include_search_texts,
            include_substituted_skus=include_substituted_skus,
            nm_ids=nm_ids,
            past_period=past_period,
            subject_id=subject_id,
            tag_id=tag_id,
        ).stream(self._api):
            yield item

    async def search_report_table_groups_create(
        self,
        *,
        current_period: Period,
        limit: int,
        offset: int,
        order_by: OrderByGrTe,
        position_cluster: str,
        brand_names: list[str] | None = None,
        include_search_texts: bool | None = None,
        include_substituted_skus: bool | None = None,
        nm_ids: list[int] | None = None,
        past_period: PastPeriod | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
        auto_paginate: bool = False,
    ) -> CommonResponseProperties | list[Any]:
        """Пагинация по группам

        :param limit: Количество групп товаров в ответе
        :param offset: После какого элемента выдавать данные
        :param brand_names: Список брендов для фильтрации
        :param include_search_texts: Показать данные по поисковым запросам без учёта подменного артикула
        :param include_substituted_skus: Показать данные по прямым запросам с подменным артикулом
        :param nm_ids: Список артикулов WB для фильтрации
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = SearchReportTableGroupsCreate(
            current_period=current_period,
            limit=limit,
            offset=offset,
            order_by=order_by,
            position_cluster=position_cluster,
            brand_names=brand_names,
            include_search_texts=include_search_texts,
            include_substituted_skus=include_substituted_skus,
            nm_ids=nm_ids,
            past_period=past_period,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_search_report_table_groups_create(
        self,
        *,
        current_period: Period,
        limit: int,
        offset: int,
        order_by: OrderByGrTe,
        position_cluster: str,
        brand_names: list[str] | None = None,
        include_search_texts: bool | None = None,
        include_substituted_skus: bool | None = None,
        nm_ids: list[int] | None = None,
        past_period: PastPeriod | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
    ) -> AsyncIterator[Any]:
        """Пагинация по группам — постранично, по одной записи.

        :param limit: Количество групп товаров в ответе
        :param offset: После какого элемента выдавать данные
        :param brand_names: Список брендов для фильтрации
        :param include_search_texts: Показать данные по поисковым запросам без учёта подменного артикула
        :param include_substituted_skus: Показать данные по прямым запросам с подменным артикулом
        :param nm_ids: Список артикулов WB для фильтрации
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        """
        async for item in SearchReportTableGroupsCreate(
            current_period=current_period,
            limit=limit,
            offset=offset,
            order_by=order_by,
            position_cluster=position_cluster,
            brand_names=brand_names,
            include_search_texts=include_search_texts,
            include_substituted_skus=include_substituted_skus,
            nm_ids=nm_ids,
            past_period=past_period,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        ).stream(self._api):
            yield item

    async def stocks_report_offices_create(self, *, body: Any) -> StocksReportOfficesCreateResponse:
        """Данные по складам"""
        return await StocksReportOfficesCreate(body=body).emit(self._api)

    async def stocks_report_products_groups_create(
        self, *, body: Any
    ) -> StocksReportProductsGroupsCreateResponse:
        """Данные по группам"""
        return await StocksReportProductsGroupsCreate(body=body).emit(self._api)

    async def stocks_report_products_products_create(
        self, *, body: Any
    ) -> StocksReportProductsProductsCreateResponse:
        """Данные по товарам"""
        return await StocksReportProductsProductsCreate(body=body).emit(self._api)

    async def stocks_report_products_sizes_create(
        self, *, body: Any
    ) -> StocksReportProductsSizesCreateResponse:
        """Данные по размерам"""
        return await StocksReportProductsSizesCreate(body=body).emit(self._api)

    async def v1_order_feed(
        self,
        *,
        selected_period: V1OrderFeedSelectedPeriod,
        brand_names: list[str] | None = None,
        nm_ids: list[int] | None = None,
        pagination: V1OrderFeedPagination | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
    ) -> V1OrderFeedResponse:
        """Получить отчёт

        :param selected_period: Запрашиваемый период. По дате текущего статуса заказа
        :param brand_names: Список брендов для фильтрации
        :param nm_ids: Список артикулов WB для фильтрации
        :param pagination: Пагинация
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        """
        return await V1OrderFeed(
            selected_period=selected_period,
            brand_names=brand_names,
            nm_ids=nm_ids,
            pagination=pagination,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        ).emit(self._api)

    async def v1_stocks_report_wb_warehouses_create(
        self,
        *,
        chrt_ids: list[int] | None = None,
        limit: int | None = None,
        nm_ids: list[int] | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> V1StocksReportWbWarehousesCreateResponse | list[Any]:
        """Остатки на складах WB

        :param chrt_ids: ID размеров. Используется только для указанных в массиве `nmIds` артикулов
        :param limit: Количество строк в ответе
        :param nm_ids: Артикулы WB
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = V1StocksReportWbWarehousesCreate(chrt_ids=chrt_ids, limit=limit, nm_ids=nm_ids, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_v1_stocks_report_wb_warehouses_create(
        self,
        *,
        chrt_ids: list[int] | None = None,
        limit: int | None = None,
        nm_ids: list[int] | None = None,
        offset: int | None = None,
    ) -> AsyncIterator[Any]:
        """Остатки на складах WB — постранично, по одной записи.

        :param chrt_ids: ID размеров. Используется только для указанных в массиве `nmIds` артикулов
        :param limit: Количество строк в ответе
        :param nm_ids: Артикулы WB
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        """
        async for item in V1StocksReportWbWarehousesCreate(
            chrt_ids=chrt_ids, limit=limit, nm_ids=nm_ids, offset=offset
        ).stream(self._api):
            yield item

    async def v2_item_rating(
        self,
        *,
        current_period: PeriodItemRating,
        offset: int,
        order_by: OrderByItemRating,
        brand_names: list[str] | None = None,
        is_not_include_nms_without_sales: bool | None = None,
        limit: int | None = None,
        nm_ids: list[int] | None = None,
        only_shadowed_nms: bool | None = None,
        past_period: PastPeriodItemRating | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
        auto_paginate: bool = False,
    ) -> V2ItemRatingResponse | list[Any]:
        """Получить отчёт

        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param brand_names: Список брендов для фильтрации
        :param is_not_include_nms_without_sales: Не возвращать товары без продаж:   - `true` — да,
            возвращаются только товары с продажами за период, указанный
            в объекте `currentPeriod` …
        :param limit: Количество товаров в ответе
        :param nm_ids: Список артикулов WB для фильтрации
        :param only_shadowed_nms: Возвращаются ли в ответе только скрытые товары:   - `true` — да,
            возвращаются только скрытые из каталога товары …
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = V2ItemRating(
            current_period=current_period,
            offset=offset,
            order_by=order_by,
            brand_names=brand_names,
            is_not_include_nms_without_sales=is_not_include_nms_without_sales,
            limit=limit,
            nm_ids=nm_ids,
            only_shadowed_nms=only_shadowed_nms,
            past_period=past_period,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_v2_item_rating(
        self,
        *,
        current_period: PeriodItemRating,
        offset: int,
        order_by: OrderByItemRating,
        brand_names: list[str] | None = None,
        is_not_include_nms_without_sales: bool | None = None,
        limit: int | None = None,
        nm_ids: list[int] | None = None,
        only_shadowed_nms: bool | None = None,
        past_period: PastPeriodItemRating | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
    ) -> AsyncIterator[Any]:
        """Получить отчёт — постранично, по одной записи.

        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param brand_names: Список брендов для фильтрации
        :param is_not_include_nms_without_sales: Не возвращать товары без продаж:   - `true` — да,
            возвращаются только товары с продажами за период, указанный
            в объекте `currentPeriod` …
        :param limit: Количество товаров в ответе
        :param nm_ids: Список артикулов WB для фильтрации
        :param only_shadowed_nms: Возвращаются ли в ответе только скрытые товары:   - `true` — да,
            возвращаются только скрытые из каталога товары …
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        """
        async for item in V2ItemRating(
            current_period=current_period,
            offset=offset,
            order_by=order_by,
            brand_names=brand_names,
            is_not_include_nms_without_sales=is_not_include_nms_without_sales,
            limit=limit,
            nm_ids=nm_ids,
            only_shadowed_nms=only_shadowed_nms,
            past_period=past_period,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        ).stream(self._api):
            yield item

    async def v3_sales_funnel_grouped_history_create(
        self,
        *,
        selected_period: dict[str, Any],
        aggregation_level: str | None = None,
        brand_names: list[str] | None = None,
        skip_deleted_nm: bool | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
    ) -> V3SalesFunnelGroupedHistoryCreateResponse:
        """Статистика групп карточек товаров по дням

        :param brand_names: Список брендов для фильтрации
        :param skip_deleted_nm: Скрыть удалённые товары
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        """
        return await V3SalesFunnelGroupedHistoryCreate(
            selected_period=selected_period,
            aggregation_level=aggregation_level,
            brand_names=brand_names,
            skip_deleted_nm=skip_deleted_nm,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        ).emit(self._api)

    async def v3_sales_funnel_products_create(
        self,
        *,
        selected_period: dict[str, Any],
        brand_names: list[str] | None = None,
        limit: int | None = None,
        nm_ids: list[int] | None = None,
        offset: int | None = None,
        order_by: OrderBy | None = None,
        past_period: dict[str, Any] | None = None,
        skip_deleted_nm: bool | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
        auto_paginate: bool = False,
    ) -> V3SalesFunnelProductsCreateResponse | list[Any]:
        """Статистика карточек товаров за период

        :param brand_names: Список брендов для фильтрации
        :param limit: Количество карточек товара в ответе
        :param nm_ids: Артикулы WB, по которым нужно составить отчёт. Оставьте пустым, чтобы получить отчёт
            обо всех товарах
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param skip_deleted_nm: Скрыть удалённые товары
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = V3SalesFunnelProductsCreate(
            selected_period=selected_period,
            brand_names=brand_names,
            limit=limit,
            nm_ids=nm_ids,
            offset=offset,
            order_by=order_by,
            past_period=past_period,
            skip_deleted_nm=skip_deleted_nm,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_v3_sales_funnel_products_create(
        self,
        *,
        selected_period: dict[str, Any],
        brand_names: list[str] | None = None,
        limit: int | None = None,
        nm_ids: list[int] | None = None,
        offset: int | None = None,
        order_by: OrderBy | None = None,
        past_period: dict[str, Any] | None = None,
        skip_deleted_nm: bool | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
    ) -> AsyncIterator[Any]:
        """Статистика карточек товаров за период — постранично, по одной записи.

        :param brand_names: Список брендов для фильтрации
        :param limit: Количество карточек товара в ответе
        :param nm_ids: Артикулы WB, по которым нужно составить отчёт. Оставьте пустым, чтобы получить отчёт
            обо всех товарах
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11
            элемента
        :param skip_deleted_nm: Скрыть удалённые товары
        :param subject_ids: Список ID предметов для фильтрации
        :param tag_ids: Список ID ярлыков для фильтрации
        """
        async for item in V3SalesFunnelProductsCreate(
            selected_period=selected_period,
            brand_names=brand_names,
            limit=limit,
            nm_ids=nm_ids,
            offset=offset,
            order_by=order_by,
            past_period=past_period,
            skip_deleted_nm=skip_deleted_nm,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
        ).stream(self._api):
            yield item

    async def v3_sales_funnel_products_history_create(
        self,
        *,
        nm_ids: list[int],
        selected_period: dict[str, Any],
        aggregation_level: str | None = None,
        skip_deleted_nm: bool | None = None,
    ) -> list[V3SalesFunnelProductsHistoryCreateResponseItem]:
        """Статистика карточек товаров по дням

        :param nm_ids: Артикулы WB, по которым нужно составить отчёт
        :param skip_deleted_nm: Скрыть удалённые товары
        """
        return await V3SalesFunnelProductsHistoryCreate(
            nm_ids=nm_ids,
            selected_period=selected_period,
            aggregation_level=aggregation_level,
            skip_deleted_nm=skip_deleted_nm,
        ).emit(self._api)
