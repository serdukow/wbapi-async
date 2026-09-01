# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from msgspec import field as _field

from ..client.model import WBModel


class CommonInfo(WBModel):
    """Общая информация"""

    advertised_products: CommonInfoAdvertisedProducts | None = _field(default=None, name="advertisedProducts")
    """Количество товаров в рекламе"""
    supplier_rating: CommonInfoSupplierRating | None = _field(default=None, name="supplierRating")
    """Рейтинг продавца"""
    total_products: int | None = _field(default=None, name="totalProducts")
    """Общее количество товаров"""


class CommonInfoAdvertisedProducts(WBModel):
    """Количество товаров в рекламе"""

    current: int | None = _field(default=None)
    """Текущее количество товаров в рекламе"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class CommonInfoSupplierRating(WBModel):
    """Рейтинг продавца"""

    current: float | None = _field(default=None)
    """Текущий рейтинг продавца"""
    dynamics: float | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class DistributionTableItem(WBModel):
    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    disqualified: int | None = _field(default=None)
    """Отзывы, исключённые из рейтинга"""
    feedback_count: DistributionTableItemFeedbackCount | None = _field(default=None, name="feedbackCount")
    """Все отзывы за период"""
    feedback_rating: DistributionTableItemFeedbackRating | None = _field(default=None, name="feedbackRating")
    """Рейтинг товара по отзывам"""
    five_star: DistributionTableItemFiveStar | None = _field(default=None, name="fiveStar")
    """Отзывы 5 звёзд"""
    four_star: DistributionTableItemFourStar | None = _field(default=None, name="fourStar")
    """Отзывы 4 звезды"""
    is_shadowed: bool | None = _field(default=None, name="isShadowed")
    """Является ли товар скрытым из каталога:   - `true` — товар скрыт из каталога   - `false` —
    товар не скрыт из каталога
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    one_star: DistributionTableItemOneStar | None = _field(default=None, name="oneStar")
    """Отзывы 1 звезда"""
    pinned_feedback: bool | None = _field(default=None, name="pinnedFeedback")
    """Отзыв закреплён"""
    rating: float | None = _field(default=None)
    """Рейтинг карточки товара"""
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    tag_id: int | None = _field(default=None, name="tagId")
    """ID ярлыка"""
    tag_name: str | None = _field(default=None, name="tagName")
    """Название ярлыка"""
    three_star: DistributionTableItemThreeStar | None = _field(default=None, name="threeStar")
    """Отзывы 3 звезды"""
    title: str | None = _field(default=None)
    """Название товара"""
    two_star: DistributionTableItemTwoStar | None = _field(default=None, name="twoStar")
    """Отзывы 2 звезды"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class DistributionTableItemFeedbackCount(WBModel):
    """Все отзывы за период"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class DistributionTableItemFeedbackRating(WBModel):
    """Рейтинг товара по отзывам"""

    current: float | None = _field(default=None)
    """Текущий рейтинг"""
    dynamics: float | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    percentile: float | None = _field(default=None)
    """Сколько процентов товаров этого предмета у других продавцов имеют рейтинг ниже, чем у этого
    товара
    """


class DistributionTableItemFiveStar(WBModel):
    """Отзывы 5 звёзд"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class DistributionTableItemFourStar(WBModel):
    """Отзывы 4 звезды"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class DistributionTableItemOneStar(WBModel):
    """Отзывы 1 звезда"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class DistributionTableItemThreeStar(WBModel):
    """Отзывы 3 звезды"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class DistributionTableItemTwoStar(WBModel):
    """Отзывы 2 звезды"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


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

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: int | None = _field(default=None)
    """Всего оценок"""


class FeedbacksIncreaseItemFourStar(WBModel):
    """Отзывы 4 звезды"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: int | None = _field(default=None)
    """Всего оценок"""


class FeedbacksIncreaseItemOneStar(WBModel):
    """Отзывы 1 звезда"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: int | None = _field(default=None)
    """Всего оценок"""


class FeedbacksIncreaseItemThreeStar(WBModel):
    """Отзывы 3 звезды"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: int | None = _field(default=None)
    """Всего оценок"""


class FeedbacksIncreaseItemTwoStar(WBModel):
    """Отзывы 2 звезды"""

    current: int | None = _field(default=None)
    """Прирост оценок за период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
    total: int | None = _field(default=None)
    """Всего оценок"""


class FloatGraphByPeriodItem(WBModel):
    """Среднее количество заказов за месяц"""

    end: str | None = _field(default=None)
    """Конец месяца"""
    start: str | None = _field(default=None)
    """Начало месяца"""
    value: float | None = _field(default=None)
    """Среднее количество заказов"""


class GetItemRatingResponse(WBModel):
    data: ItemRatingResponse | None = _field(default=None)
    """Данные ответа"""


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
    """Данные ответа"""


class GetOrderFeedSelectedPeriod(WBModel):
    """Запрашиваемый период. По дате текущего статуса заказа"""

    end: str | None = _field(default=None)
    """Дата и время конца периода. Не ранее 31 суток от текущей даты"""
    start: str | None = _field(default=None)
    """Дата и время начала периода. Не ранее 31 суток от текущей даты и не позднее `end`"""


class GetSalesFunnelGroupedHistoryResponse(WBModel):
    data: list[GetSalesFunnelGroupedHistoryResponseDataItem] | None = _field(default=None)
    """Статистика"""


class GetSalesFunnelGroupedHistoryResponseDataItem(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    history: list[History] | None = _field(default=None)
    """Статистика за период"""
    product: GetSalesFunnelGroupedHistoryResponseDataItemProduct | None = _field(default=None)
    """Карточка товара"""


class GetSalesFunnelGroupedHistoryResponseDataItemProduct(WBModel):
    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    title: str | None = _field(default=None)
    """Название карточки товара"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class GetSalesFunnelGroupedHistorySelectedPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class GetSalesFunnelProductsHistoryResponseItem(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    history: list[History] | None = _field(default=None)
    """Статистика за период"""
    product: GetSalesFunnelProductsHistoryResponseItemProduct | None = _field(default=None)
    """Карточка товара"""


class GetSalesFunnelProductsHistoryResponseItemProduct(WBModel):
    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    title: str | None = _field(default=None)
    """Название карточки товара"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class GetSalesFunnelProductsHistorySelectedPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class GetSalesFunnelProductsPastPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class GetSalesFunnelProductsResponse(WBModel):
    data: GetSalesFunnelProductsResponseData | None = _field(default=None)
    """Статистика"""


class GetSalesFunnelProductsResponseData(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    products: list[GetSalesFunnelProductsResponseDataProductsItem] | None = _field(default=None)
    """Список карточек товаров"""


class GetSalesFunnelProductsResponseDataProductsItem(WBModel):
    product: GetSalesFunnelProductsResponseDataProductsItemProduct | None = _field(default=None)
    """Карточка товара"""
    statistic: GetSalesFunnelProductsResponseDataProductsItemStatistic | None = _field(default=None)
    """Статистика"""


class GetSalesFunnelProductsResponseDataProductsItemProduct(WBModel):
    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    feedback_rating: float | None = _field(default=None, name="feedbackRating")
    """Оценка пользователей"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    product_rating: float | None = _field(default=None, name="productRating")
    """Оценка карточки"""
    stocks: GetSalesFunnelProductsResponseDataProductsItemProductStocks | None = _field(default=None)
    """Остатки"""
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    tags: list[Tag] | None = _field(default=None)
    """Ярлыки"""
    title: str | None = _field(default=None)
    """Название карточки товара"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class GetSalesFunnelProductsResponseDataProductsItemProductStocks(WBModel):
    """Остатки"""

    balance_sum: int | None = _field(default=None, name="balanceSum")
    """Сумма остатков на складах на текущий день, шт."""
    mp: int | None = _field(default=None)
    """Общее количество остатков на складах продавца на текущий день, шт."""
    wb: int | None = _field(default=None)
    """Общее количество остатков на складах WB на текущий день, шт."""


class GetSalesFunnelProductsResponseDataProductsItemStatistic(WBModel):
    comparison: GetSalesFunnelProductsResponseDataProductsItemStatisticComparison | None = _field(
        default=None
    )
    """Сравнение"""
    past: GetSalesFunnelProductsResponseDataProductsItemStatisticPast | None = _field(default=None)
    """Период для сравнения"""
    selected: GetSalesFunnelProductsResponseDataProductsItemStatisticSelected | None = _field(default=None)
    """Запрашиваемый период"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticComparison(WBModel):
    add_to_wishlist_dynamic: int | None = _field(default=None, name="addToWishlistDynamic")
    """Динамика добавлений товара в избранное"""
    avg_orders_count_per_day_dynamic: int | None = _field(default=None, name="avgOrdersCountPerDayDynamic")
    """Динамика среднего количества заказов в день"""
    avg_price_dynamic: int | None = _field(default=None, name="avgPriceDynamic")
    """Динамика средней цены на товары. Учитываются скидки для акций"""
    buyout_count_dynamic: int | None = _field(default=None, name="buyoutCountDynamic")
    """Динамика выкупов"""
    buyout_sum_dynamic: int | None = _field(default=None, name="buyoutSumDynamic")
    """Динамика суммы выкупов"""
    cancel_count_dynamic: int | None = _field(default=None, name="cancelCountDynamic")
    """Динамика отмен и возвратов товаров"""
    cancel_sum_dynamic: int | None = _field(default=None, name="cancelSumDynamic")
    """Динамика сумм отмен и возвратов товаров"""
    cart_count_dynamic: int | None = _field(default=None, name="cartCountDynamic")
    """Динамика добавлений в корзину"""
    conversions: GetSalesFunnelProductsResponseDataProductsItemStatisticComparisonConversions | None = _field(
        default=None
    )
    """Конверсии"""
    localization_percent_dynamic: int | None = _field(default=None, name="localizationPercentDynamic")
    """Динамика локальных заказов в рамках одного региона. На данный момент может быть только `0`
    """
    open_count_dynamic: int | None = _field(default=None, name="openCountDynamic")
    """Динамика переходов в карточку товара"""
    order_count_dynamic: int | None = _field(default=None, name="orderCountDynamic")
    """Динамика количества заказов"""
    order_sum_dynamic: int | None = _field(default=None, name="orderSumDynamic")
    """Динамика суммы заказов"""
    share_order_percent_dynamic: int | None = _field(default=None, name="shareOrderPercentDynamic")
    """Динамика доли в выручке"""
    time_to_ready_dynamic: (
        GetSalesFunnelProductsResponseDataProductsItemStatisticComparisonTimeToReadyDynamic | None
    ) = _field(default=None, name="timeToReadyDynamic")
    """Динамика среднего времени доставки"""
    wb_club_dynamic: GetSalesFunnelProductsResponseDataProductsItemStatisticComparisonWbClubDynamic | None = (
        _field(default=None, name="wbClubDynamic")
    )
    """Динамика заказов с WB Клубом"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticComparisonConversions(WBModel):
    add_to_cart_percent: int | None = _field(default=None, name="addToCartPercent")
    """Конверсия в корзину. Какой процент посетителей, открывших карточку товара, добавили товар в
    корзину, %
    """
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа. Какой процент посетителей, заказавших товар, его выкупили. Без учёта
    товаров, которые еще доставляются покупателю, %
    """
    cart_to_order_percent: int | None = _field(default=None, name="cartToOrderPercent")
    """Конверсия в заказ. Какой процент посетителей, добавивших товар в корзину, сделали заказ, %
    """


class GetSalesFunnelProductsResponseDataProductsItemStatisticComparisonTimeToReadyDynamic(WBModel):
    days: int | None = _field(default=None)
    """Дни"""
    hours: int | None = _field(default=None)
    """Часы"""
    mins: int | None = _field(default=None)
    """Минуты"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticComparisonWbClubDynamic(WBModel):
    avg_order_count_per_day: float | None = _field(default=None, name="avgOrderCountPerDay")
    """Динамика среднего количества заказов с WB Клубом в день"""
    avg_price: int | None = _field(default=None, name="avgPrice")
    """Динамика средней цены на товары с WB Клубом"""
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Динамика выкупов с WB Клубом"""
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Динамика процента выкупа с WB Клубом"""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Динамика суммы выкупов с WB Клубом"""
    cancel_count: int | None = _field(default=None, name="cancelCount")
    """Динамика отмен и возвратов товаров с WB Клубом"""
    cancel_sum: int | None = _field(default=None, name="cancelSum")
    """Динамика сумм отмен и возвратов товаров с WB Клубом"""
    order_count: int | None = _field(default=None, name="orderCount")
    """Динамика количества заказов с WB Клубом"""
    order_sum: int | None = _field(default=None, name="orderSum")
    """Динамика суммы заказов с WB Клубом"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticPast(WBModel):
    add_to_wishlist: int | None = _field(default=None, name="addToWishlist")
    """Добавили в **Отложенные**"""
    avg_orders_count_per_day: float | None = _field(default=None, name="avgOrdersCountPerDay")
    """Среднее количество заказов в день, шт."""
    avg_price: int | None = _field(default=None, name="avgPrice")
    """Средняя цена"""
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупили товаров, шт."""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупили на сумму"""
    cancel_count: int | None = _field(default=None, name="cancelCount")
    """Отменили и вернули товаров, шт."""
    cancel_sum: int | None = _field(default=None, name="cancelSum")
    """Отменили и вернули на сумму"""
    cart_count: int | None = _field(default=None, name="cartCount")
    """Положили в корзину, шт."""
    conversions: GetSalesFunnelProductsResponseDataProductsItemStatisticPastConversions | None = _field(
        default=None
    )
    """Конверсии"""
    localization_percent: int | None = _field(default=None, name="localizationPercent")
    """Локальные заказы в рамках одного региона. На данный момент может быть только `100`"""
    open_count: int | None = _field(default=None, name="openCount")
    """Количество переходов в карточку товара"""
    order_count: int | None = _field(default=None, name="orderCount")
    """Заказали товаров, шт."""
    order_sum: int | None = _field(default=None, name="orderSum")
    """Заказали на сумму"""
    period: GetSalesFunnelProductsResponseDataProductsItemStatisticPastPeriod | None = _field(default=None)
    """Даты периода"""
    share_order_percent: float | None = _field(default=None, name="shareOrderPercent")
    """Доля в выручке"""
    time_to_ready: GetSalesFunnelProductsResponseDataProductsItemStatisticPastTimeToReady | None = _field(
        default=None, name="timeToReady"
    )
    """Среднее время доставки"""
    wb_club: GetSalesFunnelProductsResponseDataProductsItemStatisticPastWbClub | None = _field(
        default=None, name="wbClub"
    )
    """Статистика WB Клуба"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticPastConversions(WBModel):
    add_to_cart_percent: int | None = _field(default=None, name="addToCartPercent")
    """Конверсия в корзину. Какой процент посетителей, открывших карточку товара, добавили товар в
    корзину, %
    """
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа. Какой процент посетителей, заказавших товар, его выкупили. Без учёта
    товаров, которые еще доставляются покупателю, %
    """
    cart_to_order_percent: int | None = _field(default=None, name="cartToOrderPercent")
    """Конверсия в заказ. Какой процент посетителей, добавивших товар в корзину, сделали заказ, %
    """


class GetSalesFunnelProductsResponseDataProductsItemStatisticPastPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticPastTimeToReady(WBModel):
    days: int | None = _field(default=None)
    """Дни"""
    hours: int | None = _field(default=None)
    """Часы"""
    mins: int | None = _field(default=None)
    """Минуты"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticPastWbClub(WBModel):
    avg_order_count_per_day: float | None = _field(default=None, name="avgOrderCountPerDay")
    """Среднее количество заказов с WB Клубом в день, шт."""
    avg_price: int | None = _field(default=None, name="avgPrice")
    """Средняя цена с WB Клубом"""
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупили товаров с WB Клубом, шт."""
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа с WB Клубом"""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупили с WB Клубом на сумму"""
    cancel_count: int | None = _field(default=None, name="cancelCount")
    """Отменили и вернули товаров с WB Клубом, шт."""
    cancel_sum: int | None = _field(default=None, name="cancelSum")
    """Отменили и вернули с WB Клубом на сумму"""
    order_count: int | None = _field(default=None, name="orderCount")
    """Заказали товаров с WB Клубом, шт."""
    order_sum: int | None = _field(default=None, name="orderSum")
    """Заказали с WB Клубом на сумму"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticSelected(WBModel):
    add_to_wishlist: int | None = _field(default=None, name="addToWishlist")
    """Добавили в **Отложенные**"""
    avg_orders_count_per_day: float | None = _field(default=None, name="avgOrdersCountPerDay")
    """Среднее количество заказов в день, шт."""
    avg_price: int | None = _field(default=None, name="avgPrice")
    """Средняя цена"""
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупили товаров, шт."""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупили на сумму"""
    cancel_count: int | None = _field(default=None, name="cancelCount")
    """Отменили и вернули товаров, шт."""
    cancel_sum: int | None = _field(default=None, name="cancelSum")
    """Отменили и вернули на сумму"""
    cart_count: int | None = _field(default=None, name="cartCount")
    """Положили в корзину, шт."""
    conversions: GetSalesFunnelProductsResponseDataProductsItemStatisticSelectedConversions | None = _field(
        default=None
    )
    """Конверсии"""
    localization_percent: int | None = _field(default=None, name="localizationPercent")
    """Локальные заказы в рамках одного региона. На данный момент может быть только `100`"""
    open_count: int | None = _field(default=None, name="openCount")
    """Количество переходов в карточку товара"""
    order_count: int | None = _field(default=None, name="orderCount")
    """Заказали товаров, шт."""
    order_sum: int | None = _field(default=None, name="orderSum")
    """Заказали на сумму"""
    period: GetSalesFunnelProductsResponseDataProductsItemStatisticSelectedPeriod | None = _field(
        default=None
    )
    """Даты периода"""
    share_order_percent: float | None = _field(default=None, name="shareOrderPercent")
    """Доля в выручке"""
    time_to_ready: GetSalesFunnelProductsResponseDataProductsItemStatisticSelectedTimeToReady | None = _field(
        default=None, name="timeToReady"
    )
    """Среднее время доставки"""
    wb_club: GetSalesFunnelProductsResponseDataProductsItemStatisticSelectedWbClub | None = _field(
        default=None, name="wbClub"
    )
    """Статистика WB Клуба"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticSelectedConversions(WBModel):
    add_to_cart_percent: int | None = _field(default=None, name="addToCartPercent")
    """Конверсия в корзину. Какой процент посетителей, открывших карточку товара, добавили товар в
    корзину, %
    """
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа. Какой процент посетителей, заказавших товар, его выкупили. Без учёта
    товаров, которые еще доставляются покупателю, %
    """
    cart_to_order_percent: int | None = _field(default=None, name="cartToOrderPercent")
    """Конверсия в заказ. Какой процент посетителей, добавивших товар в корзину, сделали заказ, %
    """


class GetSalesFunnelProductsResponseDataProductsItemStatisticSelectedPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticSelectedTimeToReady(WBModel):
    days: int | None = _field(default=None)
    """Дни"""
    hours: int | None = _field(default=None)
    """Часы"""
    mins: int | None = _field(default=None)
    """Минуты"""


class GetSalesFunnelProductsResponseDataProductsItemStatisticSelectedWbClub(WBModel):
    avg_order_count_per_day: float | None = _field(default=None, name="avgOrderCountPerDay")
    """Среднее количество заказов с WB Клубом в день, шт."""
    avg_price: int | None = _field(default=None, name="avgPrice")
    """Средняя цена с WB Клубом"""
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупили товаров с WB Клубом, шт."""
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа с WB Клубом"""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупили с WB Клубом на сумму"""
    cancel_count: int | None = _field(default=None, name="cancelCount")
    """Отменили и вернули товаров с WB Клубом, шт."""
    cancel_sum: int | None = _field(default=None, name="cancelSum")
    """Отменили и вернули с WB Клубом на сумму"""
    order_count: int | None = _field(default=None, name="orderCount")
    """Заказали товаров с WB Клубом, шт."""
    order_sum: int | None = _field(default=None, name="orderSum")
    """Заказали с WB Клубом на сумму"""


class GetSalesFunnelProductsSelectedPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class GetSearchReportProductOrdersResponse(WBModel):
    data: ItemOrdersResponse | None = _field(default=None)


class GetSearchReportProductSearchTextsResponse(WBModel):
    data: ItemSearchTextsResponse | None = _field(default=None)


class GetSearchReportResponse(WBModel):
    data: MainResponse | None = _field(default=None)


class GetSearchReportTableDetailsResponse(WBModel):
    data: TableDetailsResponse | None = _field(default=None)


class GetSearchReportTableGroupsResponse(WBModel):
    data: TableGroupResponse | None = _field(default=None)


class GetStocksReportOfficesBody(WBModel):
    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: PeriodInv | None = _field(default=None, name="currentPeriod")
    """Период"""
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Список артикулов WB для фильтрации"""
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    stock_type: str | None = _field(default=None, name="stockType")
    """Тип складов хранения товаров:   - `""` — все   - `wb` — склады WB   - `mp` — склады продавца
    """
    subject_ids: list[int] | None = _field(default=None, name="subjectIDs")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIDs")
    """Список ID ярлыков для фильтрации"""


class GetStocksReportOfficesResponse(WBModel):
    data: TableShippingOfficeResponse | None = _field(default=None)


class GetStocksReportProductsBody(WBModel):
    availability_filters: list[str] | None = _field(default=None, name="availabilityFilters")
    """Доступность товара:   - `deficient` — Дефицит   - `actual` — Актуальный   - `balanced` —
    Баланс   - `nonActual` — Неактуальный   - `nonLiquid` — Неликвид …
    """
    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    current_period: PeriodInv | None = _field(default=None, name="currentPeriod")
    """Период"""
    limit: int | None = _field(default=None)
    """Количество товаров в ответе"""
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Список артикулов WB для фильтрации"""
    offset: int | None = _field(default=None)
    """После какого элемента выдавать данные"""
    order_by: TableOrderBy | None = _field(default=None, name="orderBy")
    """Вид сортировки данных"""
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    stock_type: str | None = _field(default=None, name="stockType")
    """Тип складов хранения товаров:   - `""` — все   - `wb` — склады WB   - `mp` — склады продавца
    """
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    tag_id: int | None = _field(default=None, name="tagID")
    """ID ярлыка"""


class GetStocksReportProductsGroupsBody(WBModel):
    availability_filters: list[str] | None = _field(default=None, name="availabilityFilters")
    """Доступность товара:   - `deficient` — Дефицит   - `actual` — Актуальный   - `balanced` —
    Баланс   - `nonActual` — Неактуальный   - `nonLiquid` — Неликвид …
    """
    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: PeriodInv | None = _field(default=None, name="currentPeriod")
    """Период"""
    limit: int | None = _field(default=None)
    """Количество групп в ответе"""
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Список артикулов WB для фильтрации"""
    offset: int | None = _field(default=None)
    """После какого элемента выдавать данные"""
    order_by: TableOrderBy | None = _field(default=None, name="orderBy")
    """Вид сортировки данных"""
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    stock_type: str | None = _field(default=None, name="stockType")
    """Тип складов хранения товаров:   - `""` — все   - `wb` — склады WB   - `mp` — склады продавца
    """
    subject_ids: list[int] | None = _field(default=None, name="subjectIDs")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIDs")
    """Список ID ярлыков для фильтрации"""


class GetStocksReportProductsGroupsResponse(WBModel):
    data: TableGroupResponseSt | None = _field(default=None)


class GetStocksReportProductsResponse(WBModel):
    data: TableItemResponse | None = _field(default=None)


class GetStocksReportProductsSizesBody(WBModel):
    current_period: PeriodInv | None = _field(default=None, name="currentPeriod")
    """Период"""
    include_office: bool | None = _field(default=None, name="includeOffice")
    """Включить детализацию по складам"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    order_by: TableOrderBy | None = _field(default=None, name="orderBy")
    """Вид сортировки данных"""
    stock_type: str | None = _field(default=None, name="stockType")
    """Тип складов хранения товаров:   - `""` — все   - `wb` — склады WB   - `mp` — склады продавца
    """


class GetStocksReportProductsSizesResponse(WBModel):
    data: TableSizeResponse | None = _field(default=None)


class GetStocksReportWbWarehousesResponse(WBModel):
    data: InventoryWbResponse | None = _field(default=None)
    """Текущие остатки товаров на складах WB"""


class GroupedHistoryRequest(WBModel):
    aggregation_level: str | None = _field(default=None, name="aggregationLevel")
    """Тип агрегации. Если не указано, то по умолчанию используется агрегация по дням.  Доступные
    уровни агрегации `day`, `week`
    """
    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    selected_period: GroupedHistoryRequestSelectedPeriod | None = _field(default=None, name="selectedPeriod")
    """Запрашиваемый период"""
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class GroupedHistoryRequestSelectedPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class History(WBModel):
    add_to_cart_conversion: int | None = _field(default=None, name="addToCartConversion")
    """Конверсия в корзину. Какой процент посетителей, открывших карточку товара, добавили товар в
    корзину, %
    """
    add_to_wishlist_count: int | None = _field(default=None, name="addToWishlistCount")
    """Количество добавлений товара в **Отложенные**"""
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупили товаров, шт."""
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа"""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупили на сумму"""
    cart_count: int | None = _field(default=None, name="cartCount")
    """Положили в корзину, шт."""
    cart_to_order_conversion: int | None = _field(default=None, name="cartToOrderConversion")
    """Конверсия в заказ. Какой процент посетителей, добавивших товар в корзину, сделали заказ
    """
    date: str | None = _field(default=None)
    """Дата сбора статистики"""
    open_count: int | None = _field(default=None, name="openCount")
    """Количество переходов в карточку товара"""
    order_count: int | None = _field(default=None, name="orderCount")
    """Заказали товаров, шт."""
    order_sum: int | None = _field(default=None, name="orderSum")
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
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера"""
    in_way_from_client: int | None = _field(default=None, name="inWayFromClient")
    """В пути от клиента"""
    in_way_to_client: int | None = _field(default=None, name="inWayToClient")
    """В пути к клиенту"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    quantity: int | None = _field(default=None)
    """Количество товара на складе, доступное клиентам для добавления в корзину"""
    region_name: str | None = _field(default=None, name="regionName")
    """Регион отгрузки. На данный момент может быть только `Склад WB`"""
    warehouse_id: int | None = _field(default=None, name="warehouseId")
    """ID склада. На данный момент может быть только `-999999`"""
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Название склада. На данный момент может быть только `Склад WB`"""


class ItemHistoryRequest(WBModel):
    aggregation_level: str | None = _field(default=None, name="aggregationLevel")
    """Тип агрегации. Если не указано, то по умолчанию используется агрегация по дням.  Доступные
    уровни агрегации `day`, `week`
    """
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Артикулы WB, по которым нужно составить отчёт"""
    selected_period: ItemHistoryRequestSelectedPeriod | None = _field(default=None, name="selectedPeriod")
    """Запрашиваемый период"""
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""


class ItemHistoryRequestSelectedPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class ItemOrdersMetrics(WBModel):
    avg_position: int | None = _field(default=None, name="avgPosition")
    """Средняя позиция товара в результатах поиска"""
    dt: str | None = _field(default=None)
    """Дата сбора статистики"""
    orders: int | None = _field(default=None)
    """Сколько раз товары из поиска заказали"""


class ItemOrdersRequest(WBModel):
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    period: PeriodOrdersRequest | None = _field(default=None)
    """Текущий период. Максимум 7 суток"""
    search_texts: list[str] | None = _field(default=None, name="searchTexts")
    """Поисковые запросы. Для тарифов Джема **Продвинутый** и **Премиальный** максимум — 100"""


class ItemOrdersResponse(WBModel):
    items: list[ItemOrdersTextItem] | None = _field(default=None)
    """Элементы таблицы"""
    total: list[ItemOrdersMetrics] | None = _field(default=None)
    """Итог по товарам"""


class ItemOrdersTextItem(WBModel):
    date_items: list[ItemOrdersMetrics] | None = _field(default=None, name="dateItems")
    """Статистика по датам"""
    frequency: int | None = _field(default=None)
    """Количество обращений с поисковым запросом"""
    text: str | None = _field(default=None)
    """Текст поискового запроса"""


class ItemRatingRequest(WBModel):
    """Параметры запроса"""

    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: PeriodItemRating | None = _field(default=None, name="currentPeriod")
    """Текущий период"""
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
    """Параметры сортировки"""
    past_period: PastPeriodItemRating | None = _field(default=None, name="pastPeriod")
    """Прошлый период для сравнения. Количество дней — меньше или равно `currentPeriod`"""
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class ItemRatingResponse(WBModel):
    """Данные ответа"""

    feedback_increase: FeedbacksIncreaseItem | None = _field(default=None, name="feedbackIncrease")
    """Прирост оценок"""
    items: list[DistributionTableItem] | None = _field(default=None)
    """Данные по товарам"""
    seller_rating: TableItemFloat | None = _field(default=None, name="sellerRating")
    """Рейтинг продавца"""


class ItemSearchTextsRequest(WBModel):
    """Параметры для запроса по рейтингу поисковых запросов:"""

    current_period: Period | None = _field(default=None, name="currentPeriod")
    """Текущий период"""
    include_search_texts: bool | None = _field(default=None, name="includeSearchTexts")
    """Показать данные по поисковым запросам без учёта подменного артикула"""
    include_substituted_skus: bool | None = _field(default=None, name="includeSubstitutedSKUs")
    """Показать данные по прямым запросам с подменным артикулом"""
    limit: int | None = _field(default=None)
    nm_ids: list[int] | None = _field(default=None, name="nmIds")
    """Список артикулов WB"""
    order_by: OrderByGrTe | None = _field(default=None, name="orderBy")
    """Параметры сортировки"""
    past_period: PastPeriod | None = _field(default=None, name="pastPeriod")
    """Прошлый период для сравнения. Количество дней — меньше или равно `currentPeriod`"""
    top_order_by: str | None = _field(default=None, name="topOrderBy")
    """Фильтрация по поисковым запросам, по которым больше всего:   - `openCard` — перешли в
    карточку   - `addToCart` — добавили в корзину …
    """


class ItemSearchTextsResponse(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    items: list[TableSearchTextItem] | None = _field(default=None)
    """Элементы таблицы"""


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
    """Параметры сортировки"""
    past_period: ItemsRequestPastPeriod | None = _field(default=None, name="pastPeriod")
    """Период для сравнения"""
    selected_period: ItemsRequestSelectedPeriod | None = _field(default=None, name="selectedPeriod")
    """Запрашиваемый период"""
    skip_deleted_nm: bool | None = _field(default=None, name="skipDeletedNm")
    """Скрыть удалённые товары"""
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class ItemsRequestPastPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class ItemsRequestSelectedPeriod(WBModel):
    end: str | None = _field(default=None)
    """Конец периода"""
    start: str | None = _field(default=None)
    """Начало периода"""


class MainRequest(WBModel):
    """Параметры запроса для формирования главной страницы:"""

    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: Period | None = _field(default=None, name="currentPeriod")
    """Текущий период"""
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
    """Параметры сортировки"""
    past_period: PastPeriod | None = _field(default=None, name="pastPeriod")
    """Прошлый период для сравнения. Количество дней — меньше или равно `currentPeriod`"""
    position_cluster: str | None = _field(default=None, name="positionCluster")
    """Товары с какой средней позицией в поиске показывать в отчёте:   - `all` — все   -
    `firstHundred` — от 1 до 100   - `secondHundred` — от 101 до 200 …
    """
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class MainResponse(WBModel):
    common_info: CommonInfo | None = _field(default=None, name="commonInfo")
    """Общая информация"""
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    groups: list[TableGroupItem] | None = _field(default=None)
    """Список элементов таблицы"""
    position_info: PositionInfo | None = _field(default=None, name="positionInfo")
    """Информация о позиции товара"""
    visibility_info: VisibilityInfo | None = _field(default=None, name="visibilityInfo")
    """Видимость карточек и переходы в карточки. По дням, неделям, месяцам"""


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

    cancel_type: str | None = _field(default=None, name="cancelType")
    """Тип отмены (при `"status":"cancel"`):   - `app` — отказ до получения   - `receipt` — отказ
    при получении   - `expire` — истёк срок получения …
    """
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера"""
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата и время оформления заказа"""
    destination_city: str | None = _field(default=None, name="destinationCity")
    """Населённый пункт доставки"""
    destination_district: str | None = _field(default=None, name="destinationDistrict")
    """Федеральный округ доставки. Если доставка не по России, возвращается страна"""
    is_b2b: bool | None = _field(default=None, name="isB2b")
    """Тип продажи:   - `true` — B2B   - `false` — B2C"""
    is_mp: bool | None = _field(default=None, name="isMp")
    """Тип склада:   - `true` — склад продавца   - `false` — склад WB"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    seller_price: float | None = _field(default=None, name="sellerPrice")
    """Цена продавца со скидкой продавца (без учёта скидки WB Клуба и оптовой скидки для
    B2B-продаж)
    """
    srid: str | None = _field(default=None)
    """ID заказа"""
    status: str | None = _field(default=None)
    """Статус заказа:   - `created` — оформлен   - `buyout` — продан   - `cancel` — отменён   -
    `return` — возвращён   - `returnDefective` — возвращён по причине брака
    """
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время текущего статуса. При `"status":"created"` возвращается значение поля
    `createdAt`
    """
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Название склада. На данный момент для складов WB может быть только `Склад WB`"""
    warehouse_region: str | None = _field(default=None, name="warehouseRegion")
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
    """Валюта отчёта"""
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


class PositionInfo(WBModel):
    """Информация о позиции товара"""

    average: PositionInfoAverage | None = _field(default=None)
    """Средняя позиция товара в результатах поиска"""
    chart_items: list[SearchReportPositionChartItem] | None = _field(default=None, name="chartItems")
    """Данные для чарта по средней и медианной позиции товара в результатах поиска"""
    clusters: SearchReportPositionClusters | None = _field(default=None)
    """Количество товаров со средней позицией в поиске:   - `firstHundred` — от 1 до 100   -
    `secondHundred` — от 101 до 200   - `below` — от 201 и ниже
    """
    median: PositionInfoMedian | None = _field(default=None)
    """Медианная позиция товара в результатах поиска"""


class PositionInfoAverage(WBModel):
    """Средняя позиция товара в результатах поиска"""

    current: int | None = _field(default=None)
    """Текущая средняя позиция товара"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class PositionInfoMedian(WBModel):
    """Медианная позиция товара в результатах поиска"""

    current: int | None = _field(default=None)
    """Текущая медианная позиция товара"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


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


class SearchReportPositionChartItem(WBModel):
    average: int | None = _field(default=None)
    """Средняя позиция товара в результатах поиска"""
    dt: str | None = _field(default=None)
    """Дата"""
    median: int | None = _field(default=None)
    """Медианная позиция товара в результатах поиска"""


class SearchReportPositionClusters(WBModel):
    """Количество товаров со средней позицией в поиске:"""

    below: SearchReportPositionClustersBelow | None = _field(default=None)
    """от 201 и ниже"""
    first_hundred: SearchReportPositionClustersFirstHundred | None = _field(default=None, name="firstHundred")
    """от 1 до 100"""
    second_hundred: SearchReportPositionClustersSecondHundred | None = _field(
        default=None, name="secondHundred"
    )
    """от 101 до 200"""


class SearchReportPositionClustersBelow(WBModel):
    """от 201 и ниже"""

    current: int | None = _field(default=None)
    """Текущее количество товаров"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class SearchReportPositionClustersFirstHundred(WBModel):
    """от 1 до 100"""

    current: int | None = _field(default=None)
    """Текущее количество товаров"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class SearchReportPositionClustersSecondHundred(WBModel):
    """от 101 до 200"""

    current: int | None = _field(default=None)
    """Текущее количество товаров"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableDetailsRequest(WBModel):
    """Параметры запроса для пагинации по товарам в группе:"""

    brand_name: str | None = _field(default=None, name="brandName")
    """Название товара"""
    current_period: Period | None = _field(default=None, name="currentPeriod")
    """Текущий период"""
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
    """Параметры сортировки"""
    past_period: PastPeriod | None = _field(default=None, name="pastPeriod")
    """Прошлый период для сравнения. Количество дней — меньше или равно `currentPeriod`"""
    position_cluster: str | None = _field(default=None, name="positionCluster")
    """Товары с какой средней позицией в поиске показывать в отчёте:   - `all` — все   -
    `firstHundred` — от 1 до 100   - `secondHundred` — от 101 до 200 …
    """
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    tag_id: int | None = _field(default=None, name="tagId")
    """ID ярлыка"""


class TableDetailsResponse(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    products: list[TableItemItem] | None = _field(default=None)
    """Список товаров в группе по фильтру"""


class TableGroupItem(WBModel):
    """К группе товаров относятся все карточки, подходящие хотя бы по одному из параметров:"""

    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    items: list[TableItemItem] | None = _field(default=None)
    """Массив товаров группы"""
    metrics: TableGroupItemMetrics | None = _field(default=None)
    """Метрики товара в таблице"""
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    tag_id: int | None = _field(default=None, name="tagId")
    """ID ярлыка"""
    tag_name: str | None = _field(default=None, name="tagName")
    """Название ярлыка"""


class TableGroupItemMetrics(WBModel):
    """Метрики товара в таблице"""

    add_to_cart: TableGroupItemMetricsAddToCart | None = _field(default=None, name="addToCart")
    """Сколько раз товар из поиска добавили в корзину"""
    avg_position: TableGroupItemMetricsAvgPosition | None = _field(default=None, name="avgPosition")
    """Средняя позиция товара в результатах поиска"""
    cart_to_order: TableGroupItemMetricsCartToOrder | None = _field(default=None, name="cartToOrder")
    """Конверсия в заказ из поиска — доля заказов товара по отношению ко всем добавлениям товара из
    поиска в корзину
    """
    open_card: TableGroupItemMetricsOpenCard | None = _field(default=None, name="openCard")
    """Количество переходов в карточку товара из поиска"""
    open_to_cart: TableGroupItemMetricsOpenToCart | None = _field(default=None, name="openToCart")
    """Конверсия в корзину из поиска — доля добавлений товара в корзину по отношению ко всем
    переходам в карточку товара из поиска
    """
    orders: TableGroupItemMetricsOrders | None = _field(default=None)
    """Сколько раз товары из поиска заказали"""
    visibility: TableGroupItemMetricsVisibility | None = _field(default=None)
    """Процент видимости товара в результатах поиска"""


class TableGroupItemMetricsAddToCart(WBModel):
    """Сколько раз товар из поиска добавили в корзину"""

    current: int | None = _field(default=None)
    """Текущее количество"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableGroupItemMetricsAvgPosition(WBModel):
    """Средняя позиция товара в результатах поиска"""

    current: int | None = _field(default=None)
    """Текущая средняя позиция"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableGroupItemMetricsCartToOrder(WBModel):
    """Конверсия в заказ из поиска — доля заказов товара по отношению ко всем добавлениям товар"""

    current: int | None = _field(default=None)
    """Текущая конверсия"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableGroupItemMetricsOpenCard(WBModel):
    """Количество переходов в карточку товара из поиска"""

    current: int | None = _field(default=None)
    """Текущее количество переходов"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableGroupItemMetricsOpenToCart(WBModel):
    """Конверсия в корзину из поиска — доля добавлений товара в корзину по отношению ко всем пе"""

    current: int | None = _field(default=None)
    """Текущая конверсия"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableGroupItemMetricsOrders(WBModel):
    """Сколько раз товары из поиска заказали"""

    current: int | None = _field(default=None)
    """Текущее количество"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableGroupItemMetricsVisibility(WBModel):
    """Процент видимости товара в результатах поиска"""

    current: int | None = _field(default=None)
    """Текущий процент видимости"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableGroupItemSt(WBModel):
    """Данные по группе"""

    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    items: list[TableItemItemSt] | None = _field(default=None)
    """Товары группы"""
    metrics: TableGroupItemStMetrics | None = _field(default=None)
    """Метрики группы"""
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    tag_id: int | None = _field(default=None, name="tagID")
    """ID ярлыка"""
    tag_name: str | None = _field(default=None, name="tagName")
    """Название ярлыка"""


class TableGroupItemStMetrics(WBModel):
    avg_orders: float | None = _field(default=None, name="avgOrders")
    """Среднее количество заказов в день"""
    avg_orders_by_month: list[FloatGraphByPeriodItem] | None = _field(default=None, name="avgOrdersByMonth")
    """Среднее количество заказов по месяцам"""
    avg_stock_turnover: TableGroupItemStMetricsAvgStockTurnover | None = _field(
        default=None, name="avgStockTurnover"
    )
    """Оборачиваемость средних остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупы, шт."""
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа"""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупы, сумма"""
    from_client_count: int | None = _field(default=None, name="fromClientCount")
    """В пути от клиента, шт."""
    lost_buyouts_count: float | None = _field(default=None, name="lostBuyoutsCount")
    """Упущенные выкупы, шт. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение не
    рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_buyouts_sum: float | None = _field(default=None, name="lostBuyoutsSum")
    """Упущенные выкупы, сумма. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение
    не рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_orders_count: float | None = _field(default=None, name="lostOrdersCount")
    """Упущенные заказы, шт. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение не
    рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_orders_sum: float | None = _field(default=None, name="lostOrdersSum")
    """Упущенные заказы, сумма. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение
    не рассчитано   2. Значение `-2` — нулевое значение
    """
    office_missing_time: TableGroupItemStMetricsOfficeMissingTime | None = _field(
        default=None, name="officeMissingTime"
    )
    """Время отсутствия товара на складе. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    orders_count: int | None = _field(default=None, name="ordersCount")
    """Заказы, шт."""
    orders_sum: int | None = _field(default=None, name="ordersSum")
    """Заказы, сумма"""
    sale_rate: TableGroupItemStMetricsSaleRate | None = _field(default=None, name="saleRate")
    """Оборачиваемость текущих остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    stock_count: int | None = _field(default=None, name="stockCount")
    """Остатки на текущий день, шт."""
    stock_sum: int | None = _field(default=None, name="stockSum")
    """Стоимость остатков на текущий день"""
    to_client_count: int | None = _field(default=None, name="toClientCount")
    """В пути к клиенту, шт."""


class TableGroupItemStMetricsAvgStockTurnover(WBModel):
    """Оборачиваемость средних остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableGroupItemStMetricsOfficeMissingTime(WBModel):
    """Время отсутствия товара на складе. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableGroupItemStMetricsSaleRate(WBModel):
    """Оборачиваемость текущих остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableGroupRequest(WBModel):
    """Параметры запроса для пагинации по группам:"""

    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Список брендов для фильтрации"""
    current_period: Period | None = _field(default=None, name="currentPeriod")
    """Текущий период"""
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
    """Параметры сортировки"""
    past_period: PastPeriod | None = _field(default=None, name="pastPeriod")
    """Прошлый период для сравнения. Количество дней — меньше или равно `currentPeriod`"""
    position_cluster: str | None = _field(default=None, name="positionCluster")
    """Товары с какой средней позицией в поиске показывать в отчёте:   - `all` — все   -
    `firstHundred` — от 1 до 100   - `secondHundred` — от 101 до 200 …
    """
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """Список ID предметов для фильтрации"""
    tag_ids: list[int] | None = _field(default=None, name="tagIds")
    """Список ID ярлыков для фильтрации"""


class TableGroupResponse(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    groups: list[TableGroupItem] | None = _field(default=None)
    """Список групп товаров для таблицы"""


class TableGroupResponseSt(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    groups: list[TableGroupItemSt] | None = _field(default=None)
    """Множество данных по группам"""


class TableItemFloat(WBModel):
    """Рейтинг продавца"""

    current: float | None = _field(default=None)
    """Текущий рейтинг"""
    dynamics: float | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class TableItemItem(WBModel):
    pass


class TableItemItemSt(WBModel):
    """Данные по товару"""

    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    has_sizes: bool | None = _field(default=None, name="hasSizes")
    """Является ли товар размерным. Неразмерный товар имеет единственный размер, с `"techSize":"0"`
    """
    is_deleted: bool | None = _field(default=None, name="isDeleted")
    """Является ли товар удалённым"""
    main_photo: str | None = _field(default=None, name="mainPhoto")
    """Ссылка на главное фото"""
    metrics: TableItemItemStMetrics | None = _field(default=None)
    """Метрики товара"""
    name: str | None = _field(default=None)
    """Название товара"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class TableItemItemStMetrics(WBModel):
    availability: str | None = _field(default=None)
    """Доступность товара:   - `deficient` — Дефицит   - `actual` — Актуальный   - `balanced` —
    Баланс   - `nonActual` — Неактуальный   - `nonLiquid` — Неликвид …
    """
    avg_orders: float | None = _field(default=None, name="avgOrders")
    """Среднее количество заказов в день"""
    avg_orders_by_month: list[FloatGraphByPeriodItem] | None = _field(default=None, name="avgOrdersByMonth")
    """Среднее количество заказов по месяцам"""
    avg_stock_turnover: TableItemItemStMetricsAvgStockTurnover | None = _field(
        default=None, name="avgStockTurnover"
    )
    """Оборачиваемость средних остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупы, шт."""
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа"""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупы, сумма"""
    current_price: TableItemItemStMetricsCurrentPrice | None = _field(default=None, name="currentPrice")
    """Текущая цена"""
    from_client_count: int | None = _field(default=None, name="fromClientCount")
    """В пути от клиента, шт."""
    lost_buyouts_count: float | None = _field(default=None, name="lostBuyoutsCount")
    """Упущенные выкупы, шт. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение не
    рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_buyouts_sum: float | None = _field(default=None, name="lostBuyoutsSum")
    """Упущенные выкупы, сумма. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение
    не рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_orders_count: float | None = _field(default=None, name="lostOrdersCount")
    """Упущенные заказы, шт. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение не
    рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_orders_sum: float | None = _field(default=None, name="lostOrdersSum")
    """Упущенные заказы, сумма. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение
    не рассчитано   2. Значение `-2` — нулевое значение
    """
    office_missing_time: TableItemItemStMetricsOfficeMissingTime | None = _field(
        default=None, name="officeMissingTime"
    )
    """Время отсутствия товара на складе. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    orders_count: int | None = _field(default=None, name="ordersCount")
    """Заказы, шт."""
    orders_sum: int | None = _field(default=None, name="ordersSum")
    """Заказы, сумма"""
    sale_rate: TableItemItemStMetricsSaleRate | None = _field(default=None, name="saleRate")
    """Оборачиваемость текущих остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    stock_count: int | None = _field(default=None, name="stockCount")
    """Остатки на текущий день, шт."""
    stock_sum: int | None = _field(default=None, name="stockSum")
    """Стоимость остатков на текущий день"""
    to_client_count: int | None = _field(default=None, name="toClientCount")
    """В пути к клиенту, шт."""


class TableItemItemStMetricsAvgStockTurnover(WBModel):
    """Оборачиваемость средних остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableItemItemStMetricsCurrentPrice(WBModel):
    """Текущая цена"""

    max_price: int | None = _field(default=None, name="maxPrice")
    """Максимальная цена продавца со скидкой продавца (без учёта скидки WB Клуба)"""
    min_price: int | None = _field(default=None, name="minPrice")
    """Минимальная цена продавца со скидкой продавца (без учёта скидки WB Клуба)"""


class TableItemItemStMetricsOfficeMissingTime(WBModel):
    """Время отсутствия товара на складе. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableItemItemStMetricsSaleRate(WBModel):
    """Оборачиваемость текущих остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableItemResponse(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    items: list[TableItemItemSt] | None = _field(default=None)
    """Множество данных по товарам"""


class TableOfficeItem(WBModel):
    """Данные по складу"""

    metrics: TableOfficeItemMetrics | None = _field(default=None)
    """Метрики склада"""
    office_id: int | None = _field(default=None, name="officeID")
    """ID склада. На данный момент для складов WB может быть только `-999999`"""
    office_name: str | None = _field(default=None, name="officeName")
    """Название склада. На данный момент для складов WB может быть только `""`"""
    region_name: str | None = _field(default=None, name="regionName")
    """Регион отгрузки. На данный момент для складов WB может быть только `Склад WB`"""


class TableOfficeItemMetrics(WBModel):
    avg_orders: float | None = _field(default=None, name="avgOrders")
    """Среднее количество заказов в день"""
    avg_orders_by_month: list[FloatGraphByPeriodItem] | None = _field(default=None, name="avgOrdersByMonth")
    """Среднее количество заказов по месяцам"""
    avg_stock_turnover: TableOfficeItemMetricsAvgStockTurnover | None = _field(
        default=None, name="avgStockTurnover"
    )
    """Оборачиваемость средних остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупы, шт."""
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа"""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупы, сумма"""
    from_client_count: int | None = _field(default=None, name="fromClientCount")
    """В пути от клиента, шт."""
    lost_buyouts_count: float | None = _field(default=None, name="lostBuyoutsCount")
    """Упущенные выкупы, шт. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение не
    рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_buyouts_sum: float | None = _field(default=None, name="lostBuyoutsSum")
    """Упущенные выкупы, сумма. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение
    не рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_orders_count: float | None = _field(default=None, name="lostOrdersCount")
    """Упущенные заказы, шт. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение не
    рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_orders_sum: float | None = _field(default=None, name="lostOrdersSum")
    """Упущенные заказы, сумма. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение
    не рассчитано   2. Значение `-2` — нулевое значение
    """
    office_missing_time: TableOfficeItemMetricsOfficeMissingTime | None = _field(
        default=None, name="officeMissingTime"
    )
    """Время отсутствия товара на складе. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    orders_count: int | None = _field(default=None, name="ordersCount")
    """Заказы, шт."""
    orders_sum: int | None = _field(default=None, name="ordersSum")
    """Заказы, сумма"""
    sale_rate: TableOfficeItemMetricsSaleRate | None = _field(default=None, name="saleRate")
    """Оборачиваемость текущих остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    stock_count: int | None = _field(default=None, name="stockCount")
    """Остатки на текущий день, шт."""
    stock_sum: int | None = _field(default=None, name="stockSum")
    """Стоимость остатков на текущий день"""
    to_client_count: int | None = _field(default=None, name="toClientCount")
    """В пути к клиенту, шт."""


class TableOfficeItemMetricsAvgStockTurnover(WBModel):
    """Оборачиваемость средних остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableOfficeItemMetricsOfficeMissingTime(WBModel):
    """Время отсутствия товара на складе. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableOfficeItemMetricsSaleRate(WBModel):
    """Оборачиваемость текущих остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableOrderBy(WBModel):
    """Вид сортировки данных"""

    field: str | None = _field(default=None)
    """Сортировка по полю:   - `ordersCount` — Заказы, шт.   - `ordersSum` — Заказы, сумма   -
    `avgOrders` — Среднее количество заказов в день …
    """
    mode: str | None = _field(default=None)
    """Порядок сортировки: - asc — по возрастанию - desc — по убыванию"""


class TableSearchTextItem(WBModel):
    pass


class TableShippingOfficeItem(WBModel):
    """Данные по региону отгрузки"""

    metrics: TableShippingOfficeItemMetrics | None = _field(default=None)
    """Метрики по региону"""
    offices: list[TableShippingOfficeItemOfficesItem] | None = _field(default=None)
    """Данные по складам. На данный момент может быть только `[]`"""
    region_name: str | None = _field(default=None, name="regionName")
    """Регион отгрузки. На данный момент для складов WB может быть только `Склад WB`"""


class TableShippingOfficeItemMetrics(WBModel):
    from_client_count: int | None = _field(default=None, name="fromClientCount")
    """В пути от клиента, шт."""
    sale_rate: TableShippingOfficeItemMetricsSaleRate | None = _field(default=None, name="saleRate")
    """Оборачиваемость текущих остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    stock_count: int | None = _field(default=None, name="stockCount")
    """Остатки на текущий день, шт."""
    stock_sum: int | None = _field(default=None, name="stockSum")
    """Остатки на текущий день, сумма"""
    to_client_count: int | None = _field(default=None, name="toClientCount")
    """В пути к клиенту, шт."""


class TableShippingOfficeItemMetricsSaleRate(WBModel):
    """Оборачиваемость текущих остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableShippingOfficeItemOfficesItem(WBModel):
    metrics: TableShippingOfficeItemOfficesItemMetrics | None = _field(default=None)
    """Метрики по складу"""
    office_id: int | None = _field(default=None, name="officeID")
    """ID склада"""
    office_name: str | None = _field(default=None, name="officeName")
    """Название склада"""


class TableShippingOfficeItemOfficesItemMetrics(WBModel):
    from_client_count: int | None = _field(default=None, name="fromClientCount")
    """В пути от клиента, шт."""
    sale_rate: TableShippingOfficeItemOfficesItemMetricsSaleRate | None = _field(
        default=None, name="saleRate"
    )
    """Оборачиваемость текущих остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    stock_count: int | None = _field(default=None, name="stockCount")
    """Остатки на текущий день, шт."""
    stock_sum: int | None = _field(default=None, name="stockSum")
    """Остатки на текущий день, сумма"""
    to_client_count: int | None = _field(default=None, name="toClientCount")
    """В пути к клиенту, шт."""


class TableShippingOfficeItemOfficesItemMetricsSaleRate(WBModel):
    """Оборачиваемость текущих остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableShippingOfficeResponse(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    regions: list[TableShippingOfficeItem] | None = _field(default=None)
    """Множество данных по регионам отгрузки"""


class TableSizeResponse(WBModel):
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    offices: list[TableOfficeItem] | None = _field(default=None)
    """Множество данных по складам"""
    sizes: list[TableSizeResponseSizesItem] | None = _field(default=None)
    """Множество данных по размерам товара"""


class TableSizeResponseSizesItem(WBModel):
    chrt_id: int | None = _field(default=None, name="chrtID")
    """ID размера"""
    metrics: TableSizeResponseSizesItemMetrics | None = _field(default=None)
    """Метрики размера"""
    name: str | None = _field(default=None)
    """Название размера"""
    offices: list[TableOfficeItem] | None = _field(default=None)
    """Склады"""


class TableSizeResponseSizesItemMetrics(WBModel):
    avg_orders: float | None = _field(default=None, name="avgOrders")
    """Среднее количество заказов в день"""
    avg_orders_by_month: list[FloatGraphByPeriodItem] | None = _field(default=None, name="avgOrdersByMonth")
    """Среднее количество заказов по месяцам"""
    avg_stock_turnover: TableSizeResponseSizesItemMetricsAvgStockTurnover | None = _field(
        default=None, name="avgStockTurnover"
    )
    """Оборачиваемость средних остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    buyout_count: int | None = _field(default=None, name="buyoutCount")
    """Выкупы, шт."""
    buyout_percent: int | None = _field(default=None, name="buyoutPercent")
    """Процент выкупа"""
    buyout_sum: int | None = _field(default=None, name="buyoutSum")
    """Выкупы, сумма"""
    current_price: TableSizeResponseSizesItemMetricsCurrentPrice | None = _field(
        default=None, name="currentPrice"
    )
    """Текущая цена"""
    from_client_count: int | None = _field(default=None, name="fromClientCount")
    """В пути от клиента, шт."""
    lost_buyouts_count: float | None = _field(default=None, name="lostBuyoutsCount")
    """Упущенные выкупы, шт. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение не
    рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_buyouts_sum: float | None = _field(default=None, name="lostBuyoutsSum")
    """Упущенные выкупы, сумма. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение
    не рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_orders_count: float | None = _field(default=None, name="lostOrdersCount")
    """Упущенные заказы, шт. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение не
    рассчитано   2. Значение `-2` — нулевое значение
    """
    lost_orders_sum: float | None = _field(default=None, name="lostOrdersSum")
    """Упущенные заказы, сумма. Особые случаи:   1. Значение меньше `0` и не равно `-2` — значение
    не рассчитано   2. Значение `-2` — нулевое значение
    """
    office_missing_time: TableSizeResponseSizesItemMetricsOfficeMissingTime | None = _field(
        default=None, name="officeMissingTime"
    )
    """Время отсутствия товара на складе. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    orders_count: int | None = _field(default=None, name="ordersCount")
    """Заказы, шт."""
    orders_sum: int | None = _field(default=None, name="ordersSum")
    """Заказы, сумма"""
    sale_rate: TableSizeResponseSizesItemMetricsSaleRate | None = _field(default=None, name="saleRate")
    """Оборачиваемость текущих остатков. Особые случаи:   1. `"hours":-1` — бесконечная
    длительность   2. `"hours":-2` — нулевая длительность …
    """
    stock_count: int | None = _field(default=None, name="stockCount")
    """Остатки на текущий день, шт."""
    stock_sum: int | None = _field(default=None, name="stockSum")
    """Стоимость остатков на текущий день"""
    to_client_count: int | None = _field(default=None, name="toClientCount")
    """В пути к клиенту, шт."""


class TableSizeResponseSizesItemMetricsAvgStockTurnover(WBModel):
    """Оборачиваемость средних остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableSizeResponseSizesItemMetricsCurrentPrice(WBModel):
    """Текущая цена"""

    max_price: int | None = _field(default=None, name="maxPrice")
    """Максимальная цена продавца со скидкой продавца (без учёта скидки WB Клуба)"""
    min_price: int | None = _field(default=None, name="minPrice")
    """Минимальная цена продавца со скидкой продавца (без учёта скидки WB Клуба)"""


class TableSizeResponseSizesItemMetricsOfficeMissingTime(WBModel):
    """Время отсутствия товара на складе. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class TableSizeResponseSizesItemMetricsSaleRate(WBModel):
    """Оборачиваемость текущих остатков. Особые случаи:"""

    days: int | None = _field(default=None)
    """Количество дней"""
    hours: int | None = _field(default=None)
    """Количество часов"""


class Tag(WBModel):
    """Ярлык"""

    id: int | None = _field(default=None)
    """ID ярлыка"""
    name: str | None = _field(default=None)
    """Название ярлыка"""


class VisibilityInfo(WBModel):
    """Видимость карточек и переходы в карточки. По дням, неделям, месяцам"""

    by_day: list[VisibilityInfoByDayItem] | None = _field(default=None, name="byDay")
    """Данные для отрисовки графика в личном кабинете по видимости и переходам в карточки по дням
    """
    by_month: list[VisibilityInfoByMonthItem] | None = _field(default=None, name="byMonth")
    """Данные для отрисовки графика в личном кабинете по видимости и переходам в карточки по
    месяцам
    """
    by_week: list[VisibilityInfoByWeekItem] | None = _field(default=None, name="byWeek")
    """Данные для отрисовки графика в личном кабинете по видимости и переходам в карточки по
    неделям
    """
    open_card: VisibilityInfoOpenCard | None = _field(default=None, name="openCard")
    """Количество переходов в карточку товара из поиска"""
    visibility: VisibilityInfoVisibility | None = _field(default=None)
    """Видимость — процент вероятности, что пользователь увидит карточку товара. Зависит от средней
    позиции
    """


class VisibilityInfoByDayItem(WBModel):
    dt: str | None = _field(default=None)
    """Дата"""
    open: int | None = _field(default=None)
    """Количество переходов в карточку"""
    visibility: int | None = _field(default=None)
    """Видимость карточки в результатах поиска, %"""


class VisibilityInfoByMonthItem(WBModel):
    dt: str | None = _field(default=None)
    """Дата"""
    open: int | None = _field(default=None)
    """Количество переходов в карточку"""
    visibility: int | None = _field(default=None)
    """Видимость карточки в результатах поиска, %"""


class VisibilityInfoByWeekItem(WBModel):
    dt: str | None = _field(default=None)
    """Дата"""
    open: int | None = _field(default=None)
    """Количество переходов в карточку"""
    visibility: int | None = _field(default=None)
    """Видимость карточки в результатах поиска, %"""


class VisibilityInfoOpenCard(WBModel):
    """Количество переходов в карточку товара из поиска"""

    current: int | None = _field(default=None)
    """Текущее количество переходов"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""


class VisibilityInfoVisibility(WBModel):
    """Видимость — процент вероятности, что пользователь увидит карточку товара. Зависит от сре"""

    current: int | None = _field(default=None)
    """Видимость в текущий период"""
    dynamics: int | None = _field(default=None)
    """Динамика по сравнению с предыдущим периодом, %"""
