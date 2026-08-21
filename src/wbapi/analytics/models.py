from __future__ import annotations

from typing import Any

from msgspec import field as _field

from ..client.model import WBModel


class CommonItemFilters(WBModel):
    """Общие фильтры по товару"""

    availability_filters: list[str] | None = _field(default=None, name="availabilityFilters")
    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    current_period: PeriodInv | None = _field(default=None, name="currentPeriod")
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Список артикулов WB для фильтрации"""
    order_by: TableOrderBy | None = _field(default=None, name="orderBy")
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    stock_type: str | None = _field(default=None, name="stockType")
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    tag_id: int | None = _field(default=None, name="tagID")
    """ID ярлыка"""


class CommonReportFilters(WBModel):
    """Общие фильтры по отчёту"""

    availability_filters: list[str] | None = _field(default=None, name="availabilityFilters")
    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: PeriodInv | None = _field(default=None, name="currentPeriod")
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Список артикулов WB для фильтрации"""
    order_by: TableOrderBy | None = _field(default=None, name="orderBy")
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    stock_type: str | None = _field(default=None, name="stockType")
    subject_ids: list[int] | None = _field(default=None, name="subjectIDs")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIDs")
    """Список ID ярлыков для фильтрации"""


class CommonResponseProperties(WBModel):
    data: dict[str, Any] | None = _field(default=None)
    """Данные ответа"""


class CommonShippingOfficeFilters(WBModel):
    """Общие фильтры по регионам отгрузки"""

    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: PeriodInv | None = _field(default=None, name="currentPeriod")
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Список артикулов WB для фильтрации"""
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    stock_type: str | None = _field(default=None, name="stockType")
    subject_ids: list[int] | None = _field(default=None, name="subjectIDs")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIDs")
    """Список ID ярлыков для фильтрации"""


class CommonSizeFilters(WBModel):
    """Общие фильтры по размеру"""

    current_period: PeriodInv | None = _field(default=None, name="currentPeriod")
    include_office: bool | None = _field(default=None, name="includeOffice")
    """Включить детализацию по складам"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    order_by: TableOrderBy | None = _field(default=None, name="orderBy")
    stock_type: str | None = _field(default=None, name="stockType")


class DistributionTableItem(WBModel):
    brand_name: Any | None = _field(default=None, name="brandName")
    """Бренд"""
    disqualified: Any | None = _field(default=None)
    """Отзывы, исключённые из рейтинга"""
    feedback_count: Any | None = _field(default=None, name="feedbackCount")
    """Все отзывы за период"""
    feedback_rating: Any | None = _field(default=None, name="feedbackRating")
    """Рейтинг товара по отзывам"""
    five_star: Any | None = _field(default=None, name="fiveStar")
    """Отзывы 5 звёзд"""
    four_star: Any | None = _field(default=None, name="fourStar")
    """Отзывы 4 звезды"""
    is_shadowed: Any | None = _field(default=None, name="isShadowed")
    """Является ли товар скрытым из каталога:   - `true` — товар скрыт из каталога   - `false` —
    товар не скрыт из каталога
    """
    nm_id: Any | None = _field(default=None, name="nmId")
    """Артикул WB"""
    one_star: Any | None = _field(default=None, name="oneStar")
    """Отзывы 1 звезда"""
    pinned_feedback: Any | None = _field(default=None, name="pinnedFeedback")
    """Отзыв закреплён"""
    rating: Any | None = _field(default=None)
    """Рейтинг карточки товара"""
    subject_id: Any | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: Any | None = _field(default=None, name="subjectName")
    """Название предмета"""
    tag_id: Any | None = _field(default=None, name="tagId")
    """ID ярлыка"""
    tag_name: Any | None = _field(default=None, name="tagName")
    """Название ярлыка"""
    three_star: Any | None = _field(default=None, name="threeStar")
    """Отзывы 3 звезды"""
    title: Any | None = _field(default=None)
    """Название товара"""
    two_star: Any | None = _field(default=None, name="twoStar")
    """Отзывы 2 звезды"""
    vendor_code: Any | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class FeedbacksIncreaseItem(WBModel):
    """Прирост оценок"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    five_star: FeedbacksIncreaseItemFiveStar | None = _field(default=None, name="fiveStar")
    """Отзывы 5 звёзд"""
    four_star: FeedbacksIncreaseItemFourStar | None = _field(default=None, name="fourStar")
    """Отзывы 4 звезды"""
    one_star: FeedbacksIncreaseItemOneStar | None = _field(default=None, name="oneStar")
    """Отзывы 1 звезда"""
    three_star: FeedbacksIncreaseItemThreeStar | None = _field(default=None, name="threeStar")
    """Отзывы 3 звезды"""
    total: int | None = _field(default=None)
    """Всего оценок"""
    two_star: FeedbacksIncreaseItemTwoStar | None = _field(default=None, name="twoStar")
    """Отзывы 2 звезды"""


class FeedbacksIncreaseItemFiveStar(WBModel):
    """Отзывы 5 звёзд"""

    current: Any | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: Any | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: Any | None = _field(default=None)
    """Всего оценок"""


class FeedbacksIncreaseItemFourStar(WBModel):
    """Отзывы 4 звезды"""

    current: Any | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: Any | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: Any | None = _field(default=None)
    """Всего оценок"""


class FeedbacksIncreaseItemOneStar(WBModel):
    """Отзывы 1 звезда"""

    current: Any | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: Any | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: Any | None = _field(default=None)
    """Всего оценок"""


class FeedbacksIncreaseItemThreeStar(WBModel):
    """Отзывы 3 звезды"""

    current: Any | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: Any | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: Any | None = _field(default=None)
    """Всего оценок"""


class FeedbacksIncreaseItemTwoStar(WBModel):
    """Отзывы 2 звезды"""

    current: Any | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: Any | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: Any | None = _field(default=None)
    """Всего оценок"""


class GetItemRatingResponse(WBModel):
    data: ItemRatingResponse | None = _field(default=None)


class GetOrderFeedPagination(WBModel):
    """Пагинация"""

    limit: int | None = _field(default=None)
    """Количество заказов в ответе"""
    offset: int | None = _field(default=None)
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
    snapshot_time: str | None = _field(default=None, name="snapshotTime")
    """Метка снимка данных, в рамках которого выполняется пагинация.Данные отчёта обновляются
    асинхронно. Чтобы не пропускать и не дублировать заказы, запросы одной вы …
    """


class GetOrderFeedResponse(WBModel):
    data: OrderFeedResponse | None = _field(default=None)


class GetOrderFeedSelectedPeriod(WBModel):
    """Запрашиваемый период. По дате текущего статуса заказа"""

    end: str | None = _field(default=None)
    """Дата и время конца периода. Не ранее 31 суток от текущей даты"""
    start: str | None = _field(default=None)
    """Дата и время начала периода. Не ранее 31 суток от текущей даты и не позднее `end`"""


class GetSalesFunnelGroupedHistoryResponse(WBModel):
    data: list[GetSalesFunnelGroupedHistoryResponseDataItem] | None = _field(default=None)


class GetSalesFunnelGroupedHistoryResponseDataItem(WBModel):
    currency: Any | None = _field(default=None)
    history: list[Any] | None = _field(default=None)
    """Статистика за период"""
    product: Any | None = _field(default=None)


class GetSalesFunnelProductsHistoryResponseItem(WBModel):
    currency: str | None = _field(default=None)
    history: list[History] | None = _field(default=None)
    """Статистика за период"""
    product: dict[str, Any] | None = _field(default=None)


class GetSalesFunnelProductsResponse(WBModel):
    data: dict[str, Any] | None = _field(default=None)


class GetStocksReportOfficesResponse(WBModel):
    data: TableShippingOfficeResponse | None = _field(default=None)


class GetStocksReportProductsGroupsResponse(WBModel):
    data: TableGroupResponseSt | None = _field(default=None)


class GetStocksReportProductsResponse(WBModel):
    data: TableItemResponse | None = _field(default=None)


class GetStocksReportProductsSizesResponse(WBModel):
    data: TableSizeResponse | None = _field(default=None)


class GetStocksReportWbWarehousesResponse(WBModel):
    data: InventoryWbResponse | None = _field(default=None)


class GroupedHistoryRequest(WBModel):
    aggregation_level: str | None = _field(default=None, name="aggregationLevel")
    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    selected_period: dict[str, Any] | None = _field(default=None, name="selectedPeriod")
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class History(WBModel):
    add_to_cart_conversion: Any | None = _field(default=None, name="addToCartConversion")
    """Конверсия в корзину. Какой процент посетителей, открывших карточку товара, добавили товар в
    корзину, %
    """
    add_to_wishlist_count: Any | None = _field(default=None, name="addToWishlistCount")
    """Количество добавлений товара в **Отложенные**"""
    buyout_count: Any | None = _field(default=None, name="buyoutCount")
    """Выкупили товаров, шт."""
    buyout_percent: Any | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа"""
    buyout_sum: Any | None = _field(default=None, name="buyoutSum")
    """Выкупили на сумму"""
    cart_count: Any | None = _field(default=None, name="cartCount")
    """Положили в корзину, шт."""
    cart_to_order_conversion: Any | None = _field(default=None, name="cartToOrderConversion")
    """Конверсия в заказ. Какой процент посетителей, добавивших товар в корзину, сделали заказ
    """
    date: Any | None = _field(default=None)
    """Дата сбора статистики"""
    open_count: Any | None = _field(default=None, name="openCount")
    """Количество переходов в карточку товара"""
    order_count: Any | None = _field(default=None, name="orderCount")
    """Заказали товаров, шт."""
    order_sum: Any | None = _field(default=None, name="orderSum")
    """Заказали на сумму"""


class InventoryRequest(WBModel):
    """Параметры запроса текущих остатков на складах WB"""

    chrt_ids: list[int] | None = _field(default=None, name="chrtIds")
    """ID размеров. Используется только для указанных в массиве `nmIds` артикулов"""
    limit: int | None = _field(default=None)
    """Количество строк в ответе"""
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Артикулы WB"""
    offset: int | None = _field(default=None)
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""


class InventoryWbResponse(WBModel):
    """Текущие остатки товаров на складах WB"""

    items: list[InventoryWbResponseItemsItem] | None = _field(default=None)
    """Остатки товаров на складах WB по размерам"""


class InventoryWbResponseItemsItem(WBModel):
    chrt_id: Any | None = _field(default=None, name="chrtId")
    """ID размера"""
    in_way_from_client: Any | None = _field(default=None, name="inWayFromClient")
    """В пути от клиента"""
    in_way_to_client: Any | None = _field(default=None, name="inWayToClient")
    """В пути к клиенту"""
    nm_id: Any | None = _field(default=None, name="nmId")
    """Артикул WB"""
    quantity: Any | None = _field(default=None)
    """Количество товара на складе, доступное клиентам для добавления в корзину"""
    region_name: Any | None = _field(default=None, name="regionName")
    """Регион отгрузки. На данный момент может быть только `Склад WB`"""
    warehouse_id: Any | None = _field(default=None, name="warehouseId")
    """ID склада. На данный момент может быть только `-999999`"""
    warehouse_name: Any | None = _field(default=None, name="warehouseName")
    """Название склада. На данный момент может быть только `Склад WB`"""


class ItemHistoryRequest(WBModel):
    aggregation_level: str | None = _field(default=None, name="aggregationLevel")
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Артикулы WB, по которым нужно составить отчёт"""
    selected_period: dict[str, Any] | None = _field(default=None, name="selectedPeriod")
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""


class ItemOrdersRequest(WBModel):
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    period: PeriodOrdersRequest | None = _field(default=None)
    search_texts: list[str] | None = _field(default=None, name="searchTexts")
    """Поисковые запросы. Для тарифов Джема **Продвинутый** и **Премиальный** максимум — 100"""


class ItemRatingRequest(WBModel):
    """Параметры запроса"""

    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: PeriodItemRating | None = _field(default=None, name="currentPeriod")
    is_not_include_nms_without_sales: bool | None = _field(default=None, name="isNotIncludeNmsWithoutSales")
    """Не возвращать товары без продаж:   - `true` — да, возвращаются только товары с продажами за
    период, указанный в объекте `currentPeriod` …
    """
    limit: int | None = _field(default=None)
    """Количество товаров в ответе"""
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Список артикулов WB для фильтрации"""
    offset: int | None = _field(default=None)
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
    only_shadowed_nms: bool | None = _field(default=None, name="onlyShadowedNms")
    """Возвращаются ли в ответе только скрытые товары:   - `true` — да, возвращаются только скрытые
    из каталога товары …
    """
    order_by: OrderByItemRating | None = _field(default=None, name="orderBy")
    past_period: PastPeriodItemRating | None = _field(default=None, name="pastPeriod")
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class ItemRatingResponse(WBModel):
    """Данные ответа"""

    feedback_increase: FeedbacksIncreaseItem | None = _field(default=None, name="feedbackIncrease")
    items: list[DistributionTableItem] | None = _field(default=None)
    """Данные по товарам"""
    seller_rating: TableItemFloat | None = _field(default=None, name="sellerRating")


class ItemSearchTextsRequest(WBModel):
    """Параметры для запроса по рейтингу поисковых запросов:"""

    current_period: Period | None = _field(default=None, name="currentPeriod")
    include_search_texts: bool | None = _field(default=None, name="includeSearchTexts")
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = _field(default=None, name="includeSubstitutedSKUs")
    """Показать данные по прямым запросам с подменным артикулом"""
    limit: int | None = _field(default=None)
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Список артикулов WB"""
    order_by: OrderByGrTe | None = _field(default=None, name="orderBy")
    past_period: PastPeriod | None = _field(default=None, name="pastPeriod")
    top_order_by: str | None = _field(default=None, name="topOrderBy")
    """Фильтрация по поисковым запросам, по которым больше всего:   - `openCard` — перешли в
    карточку   - `addToCart` — добавили в корзину …
    """


class ItemsRequest(WBModel):
    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    limit: int | None = _field(default=None)
    """Количество карточек товара в ответе"""
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Артикулы WB, по которым нужно составить отчёт. Оставьте пустым, чтобы получить отчёт обо
    всех товарах
    """
    offset: int | None = _field(default=None)
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
    order_by: OrderBy | None = _field(default=None, name="orderBy")
    past_period: dict[str, Any] | None = _field(default=None, name="pastPeriod")
    selected_period: dict[str, Any] | None = _field(default=None, name="selectedPeriod")
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class MainRequest(WBModel):
    """Параметры запроса для формирования главной страницы:"""

    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: Period | None = _field(default=None, name="currentPeriod")
    include_search_texts: bool | None = _field(default=None, name="includeSearchTexts")
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = _field(default=None, name="includeSubstitutedSKUs")
    """Показать данные по прямым запросам с подменным артикулом"""
    limit: int | None = _field(default=None)
    """Количество групп товаров в ответе"""
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Список артикулов WB для фильтрации"""
    offset: int | None = _field(default=None)
    """После какого элемента выдавать данные"""
    order_by: OrderByMainAndDetails | None = _field(default=None, name="orderBy")
    past_period: PastPeriod | None = _field(default=None, name="pastPeriod")
    position_cluster: str | None = _field(default=None, name="positionCluster")
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class NmReportCreateReportResponse(WBModel):
    data: str | None = _field(default=None)
    """Уведомление, что началась генерация отчёта"""


class NmReportGetReportsResponse(WBModel):
    data: list[NmReportGetReportsResponseDataItem] | None = _field(default=None)


class NmReportGetReportsResponseDataItem(WBModel):
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата и время завершения генерации"""
    end_date: str | None = _field(default=None, name="endDate")
    """Конец периода"""
    id: str | None = _field(default=None)
    """ID отчёта"""
    name: str | None = _field(default=None)
    """Название отчёта"""
    size: int | None = _field(default=None)
    """Размер отчёта, Б"""
    start_date: str | None = _field(default=None, name="startDate")
    """Начало периода"""
    status: str | None = _field(default=None)
    """Статус отчёта:  * `WAITING` — в очереди на обработку * `PROCESSING` — генерируется *
    `SUCCESS —` готов * `RETRY` — ожидает повторной обработки …
    """


class NmReportRetryReportRequest(WBModel):
    download_id: str | None = _field(default=None, name="downloadId")
    """ID отчёта"""


class NmReportRetryReportResponse(WBModel):
    data: str | None = _field(default=None)
    """Уведомление, что началась повторная генерация отчёта"""


class Order(WBModel):
    """Заказ"""

    cancel_type: Any | None = _field(default=None, name="cancelType")
    """Тип отмены (при `"status":"cancel"`):   - `app` — отказ до получения   - `receipt` — отказ
    при получении   - `expire` — истёк срок получения …
    """
    chrt_id: Any | None = _field(default=None, name="chrtId")
    """ID размера"""
    created_at: Any | None = _field(default=None, name="createdAt")
    """Дата и время оформления заказа"""
    destination_city: Any | None = _field(default=None, name="destinationCity")
    """Населённый пункт доставки"""
    destination_district: Any | None = _field(default=None, name="destinationDistrict")
    """Федеральный округ доставки. Если доставка не по России, возвращается страна"""
    is_b2b: Any | None = _field(default=None, name="isB2b")
    """Тип продажи:   - `true` — B2B   - `false` — B2C"""
    is_mp: Any | None = _field(default=None, name="isMp")
    """Тип склада:   - `true` — склад продавца   - `false` — склад WB"""
    nm_id: Any | None = _field(default=None, name="nmId")
    """Артикул WB"""
    seller_price: Any | None = _field(default=None, name="sellerPrice")
    """Цена продавца со скидкой продавца (без учёта скидки WB Клуба и оптовой скидки для
    B2B-продаж)
    """
    srid: Any | None = _field(default=None)
    """ID заказа"""
    status: Any | None = _field(default=None)
    """Статус заказа:   - `created` — оформлен   - `buyout` — продан   - `cancel` — отменён   -
    `return` — возвращён   - `returnDefective` — возвращён по причине брака
    """
    updated_at: Any | None = _field(default=None, name="updatedAt")
    """Дата и время текущего статуса. При `"status":"created"` возвращается значение поля
    `createdAt`
    """
    warehouse_name: Any | None = _field(default=None, name="warehouseName")
    """Название склада. На данный момент для складов WB может быть только `Склад WB`"""
    warehouse_region: Any | None = _field(default=None, name="warehouseRegion")
    """Федеральный округ склада. Если склад не в России, возвращается страна. На данный момент для
    складов WB может быть только `""`
    """


class OrderBy(WBModel):
    """Параметры сортировки"""

    field: str | None = _field(default=None)
    """Поле для сортировки:   - `openCard` — Перешли в карточку   - `addToCart` — Положили в
    корзину   - `orderCount` — Заказали товаров, шт …
    """
    mode: str | None = _field(default=None)
    """Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию"""


class OrderByGrTe(WBModel):
    """Параметры сортировки"""

    field: str | None = _field(default=None)
    """Поле для сортировки:   - `avgPosition` — по средней позиции   - `addToCart` — по добавлениям
    в корзину …
    """
    mode: str | None = _field(default=None)
    """Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию"""


class OrderByItemRating(WBModel):
    """Параметры сортировки"""

    field: str | None = _field(default=None)
    """Поле для сортировки:   - `feedbackRating` — Рейтинг товара по отзывам   - `feedbackCount` —
    Все отзывы за период   - `fiveStar` — Отзывы 5 звёзд …
    """
    mode: str | None = _field(default=None)
    """Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию"""


class OrderByMainAndDetails(WBModel):
    """Параметры сортировки"""

    field: str | None = _field(default=None)
    """Поле для сортировки:   - `avgPosition` — по средней позиции   - `addToCart` — по добавлениям
    в корзину …
    """
    mode: str | None = _field(default=None)
    """Порядок сортировки:   - `asc` — по возрастанию   - `desc` — по убыванию"""


class OrderFeedRequest(WBModel):
    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Список артикулов WB для фильтрации"""
    pagination: OrderFeedRequestPagination | None = _field(default=None)
    """Пагинация"""
    selected_period: OrderFeedRequestSelectedPeriod | None = _field(default=None, name="selectedPeriod")
    """Запрашиваемый период. По дате текущего статуса заказа"""
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class OrderFeedRequestPagination(WBModel):
    """Пагинация"""

    limit: int | None = _field(default=None)
    """Количество заказов в ответе"""
    offset: int | None = _field(default=None)
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
    snapshot_time: str | None = _field(default=None, name="snapshotTime")
    """Метка снимка данных, в рамках которого выполняется пагинация.Данные отчёта обновляются
    асинхронно. Чтобы не пропускать и не дублировать заказы, запросы одной вы …
    """


class OrderFeedRequestSelectedPeriod(WBModel):
    """Запрашиваемый период. По дате текущего статуса заказа"""

    end: str | None = _field(default=None)
    """Дата и время конца периода. Не ранее 31 суток от текущей даты"""
    start: str | None = _field(default=None)
    """Дата и время начала периода. Не ранее 31 суток от текущей даты и не позднее `end`"""


class OrderFeedResponse(WBModel):
    """Данные ответа"""

    currency: str | None = _field(default=None)
    orders: list[Order] | None = _field(default=None)
    """Заказы"""
    snapshot_time: str | None = _field(default=None, name="snapshotTime")
    """Метка снимка данных, в рамках которого выполняется пагинация"""


class PastPeriod(WBModel):
    """Прошлый период для сравнения. Количество дней — меньше или равно `currentPeriod`"""

    end: str | None = _field(default=None)
    """Дата окончания периода. Не позднее даты перед датой начала `currentPeriod`. Не ранее 365
    суток от сегодня
    """
    start: str | None = _field(default=None)
    """Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня"""


class PastPeriodItemRating(WBModel):
    """Прошлый период для сравнения. Количество дней — меньше или равно `currentPeriod`"""

    end: str | None = _field(default=None)
    """Дата окончания периода. Не ранее 364 суток от вчерашнего дня и не позднее даты перед началом
    `currentPeriod`.
    """
    start: str | None = _field(default=None)
    """Дата начала периода. Не ранее 364 суток от вчерашнего дня и не позднее `end`"""


class Period(WBModel):
    """Текущий период"""

    end: str | None = _field(default=None)
    """Дата окончания периода. Не ранее 365 суток от сегодня"""
    start: str | None = _field(default=None)
    """Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня"""


class PeriodInv(WBModel):
    """Период"""

    end: str | None = _field(default=None)
    """Дата окончания периода. Не ранее 3 месяцев от текущей даты"""
    start: str | None = _field(default=None)
    """Дата начала периода. Не позднее `end`. Не ранее 3 месяцев от текущей даты"""


class PeriodItemRating(WBModel):
    """Текущий период"""

    end: str | None = _field(default=None)
    """Дата окончания периода. Не ранее 364 суток от вчерашнего дня"""
    start: str | None = _field(default=None)
    """Дата начала периода. Не ранее 364 суток от вчерашнего дня и не позднее `end`"""


class PeriodOrdersRequest(WBModel):
    """Текущий период. Максимум 7 суток"""

    end: str | None = _field(default=None)
    """Дата окончания периода. Не ранее 365 суток от сегодня"""
    start: str | None = _field(default=None)
    """Дата начала периода. Не позднее `end`. Не ранее 365 суток от сегодня"""


class SalesFunnelItemReq(WBModel):
    id: str | None = _field(default=None)
    """ID отчёта в UUID-формате. Генерируется продавцом самостоятельно"""
    params: SalesFunnelItemReqParams | None = _field(default=None)
    """Параметры отчёта"""
    report_type: str | None = _field(default=None, name="reportType")
    """Тип отчёта `DETAIL_HISTORY_REPORT` — Воронка продаж. По артикулам WB"""
    user_report_name: str | None = _field(default=None, name="userReportName")
    """Название отчёта. Если не указано, сформируется автоматически"""


class SalesFunnelItemReqParams(WBModel):
    """Параметры отчёта"""

    aggregation_level: str | None = _field(default=None, name="aggregationLevel")
    """Как сгруппировать данные (по умолчанию по дням):    * `day` — по дням   * `week` — по
    неделям   * `month` — по месяцам
    """
    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    end_date: str | None = _field(default=None, name="endDate")
    """Конец периода"""
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Артикулы WB, по которым составить отчёт. Оставьте пустым, чтобы получить отчёт обо всех
    товарах
    """
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    start_date: str | None = _field(default=None, name="startDate")
    """Начало периода"""
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""
    timezone: str | None = _field(default=None)
    """Временная зона по формату IANA"""


class TableDetailsRequest(WBModel):
    """Параметры запроса для пагинации по товарам в группе:"""

    brand_name: str | None = _field(default=None, name="brandName")
    """Название товара"""
    current_period: Period | None = _field(default=None, name="currentPeriod")
    include_search_texts: bool | None = _field(default=None, name="includeSearchTexts")
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = _field(default=None, name="includeSubstitutedSKUs")
    """Показать данные по прямым запросам с подменным артикулом"""
    limit: int | None = _field(default=None)
    """Количество товаров в ответе"""
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Список артикулов WB"""
    offset: int | None = _field(default=None)
    """После какого элемента выдавать данные"""
    order_by: OrderByMainAndDetails | None = _field(default=None, name="orderBy")
    past_period: PastPeriod | None = _field(default=None, name="pastPeriod")
    position_cluster: str | None = _field(default=None, name="positionCluster")
    """Товары с какой средней позицией в поиске показывать в отчёте:   - `all` — все   -
    `firstHundred` — от 1 до 100   - `secondHundred` — от 101 до 200 …
    """
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    tag_id: int | None = _field(default=None, name="tagId")
    """ID ярлыка"""


class TableGroupItemSt(WBModel):
    """Данные по группе"""

    brand_name: Any | None = _field(default=None, name="brandName")
    """Бренд"""
    items: Any | None = _field(default=None)
    """Товары группы"""
    metrics: Any | None = _field(default=None)
    """Метрики группы"""
    subject_id: Any | None = _field(default=None, name="subjectID")
    """ID предмета"""
    subject_name: Any | None = _field(default=None, name="subjectName")
    """Название предмета"""
    tag_id: Any | None = _field(default=None, name="tagID")
    """ID ярлыка"""
    tag_name: Any | None = _field(default=None, name="tagName")
    """Название ярлыка"""


class TableGroupRequest(WBModel):
    """Параметры запроса для пагинации по группам:"""

    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: Period | None = _field(default=None, name="currentPeriod")
    include_search_texts: bool | None = _field(default=None, name="includeSearchTexts")
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = _field(default=None, name="includeSubstitutedSKUs")
    """Показать данные по прямым запросам с подменным артикулом"""
    limit: int | None = _field(default=None)
    """Количество групп товаров в ответе"""
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Список артикулов WB для фильтрации"""
    offset: int | None = _field(default=None)
    """После какого элемента выдавать данные"""
    order_by: OrderByGrTe | None = _field(default=None, name="orderBy")
    past_period: PastPeriod | None = _field(default=None, name="pastPeriod")
    position_cluster: str | None = _field(default=None, name="positionCluster")
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class TableGroupResponseSt(WBModel):
    currency: str | None = _field(default=None)
    groups: list[TableGroupItemSt] | None = _field(default=None)


class TableItemFloat(WBModel):
    """Рейтинг продавца"""

    current: float | None = _field(default=None)
    """Текущий рейтинг"""
    dynamics: float | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableItemItemSt(WBModel):
    """Данные по товару"""

    brand_name: Any | None = _field(default=None, name="brandName")
    """Бренд"""
    has_sizes: Any | None = _field(default=None, name="hasSizes")
    """Является ли товар размерным. Неразмерный товар имеет единственный размер, с `"techSize":"0"`
    """
    is_deleted: Any | None = _field(default=None, name="isDeleted")
    """Является ли товар удалённым"""
    main_photo: Any | None = _field(default=None, name="mainPhoto")
    """Ссылка на главное фото"""
    metrics: Any | None = _field(default=None)
    """Метрики товара"""
    name: Any | None = _field(default=None)
    """Название товара"""
    nm_id: Any | None = _field(default=None, name="nmID")
    """Артикул WB"""
    subject_name: Any | None = _field(default=None, name="subjectName")
    """Название предмета"""
    vendor_code: Any | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class TableItemResponse(WBModel):
    currency: str | None = _field(default=None)
    items: list[TableItemItemSt] | None = _field(default=None)
    """Множество данных по товарам"""


class TableOfficeItem(WBModel):
    """Данные по складу"""

    metrics: Any | None = _field(default=None)
    """Метрики склада"""
    office_id: Any | None = _field(default=None, name="officeID")
    """ID склада. На данный момент для складов WB может быть только `-999999`"""
    office_name: Any | None = _field(default=None, name="officeName")
    """Название склада. На данный момент для складов WB может быть только `""`"""
    region_name: Any | None = _field(default=None, name="regionName")
    """Регион отгрузки. На данный момент для складов WB может быть только `Склад WB`"""


class TableOrderBy(WBModel):
    """Вид сортировки данных"""

    field: Any | None = _field(default=None)
    mode: Any | None = _field(default=None)


class TableShippingOfficeItem(WBModel):
    """Данные по региону отгрузки"""

    metrics: Any | None = _field(default=None)
    """Метрики по региону"""
    offices: Any | None = _field(default=None)
    """Данные по складам. На данный момент может быть только `[]`"""
    region_name: Any | None = _field(default=None, name="regionName")
    """Регион отгрузки. На данный момент для складов WB может быть только `Склад WB`"""


class TableShippingOfficeResponse(WBModel):
    currency: str | None = _field(default=None)
    regions: list[TableShippingOfficeItem] | None = _field(default=None)
    """Множество данных по регионам отгрузки"""


class TableSizeResponse(WBModel):
    currency: str | None = _field(default=None)
    offices: list[TableOfficeItem] | None = _field(default=None)
    """Множество данных по складам"""
    sizes: list[TableSizeResponseSizesItem] | None = _field(default=None)
    """Множество данных по размерам товара"""


class TableSizeResponseSizesItem(WBModel):
    chrt_id: Any | None = _field(default=None, name="chrtID")
    """ID размера"""
    metrics: Any | None = _field(default=None)
    """Метрики размера"""
    name: Any | None = _field(default=None)
    """Название размера"""
    offices: Any | None = _field(default=None)
    """Склады"""
