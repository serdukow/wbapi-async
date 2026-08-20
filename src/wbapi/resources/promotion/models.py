from __future__ import annotations

from typing import Any

from msgspec import field as _field

from ...client.model import WBModel


class AdvV0AuctionNmsUpdateBody(WBModel):
    nms: list[AdvV0AuctionNmsUpdateBodyNmsItem] | None = _field(default=None)
    """Карточки товаров в кампаниях"""


class AdvV0AuctionNmsUpdateBodyNmsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nms: AdvV0AuctionNmsUpdateBodyNmsItemNms | None = _field(default=None)
    """Карточки товаров. Максимум 50 товаров для одной кампании"""


class AdvV0AuctionNmsUpdateBodyNmsItemNms(WBModel):
    """Карточки товаров. Максимум 50 товаров для одной кампании"""

    add: Any | None = _field(default=None)
    """Карточки товаров, которые необходимо добавить"""
    delete: Any | None = _field(default=None)
    """Карточки товаров, которые необходимо удалить"""


class AdvV0AuctionNmsUpdateNmsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nms: AdvV0AuctionNmsUpdateNmsItemNms | None = _field(default=None)
    """Карточки товаров. Максимум 50 товаров для одной кампании"""


class AdvV0AuctionNmsUpdateNmsItemNms(WBModel):
    """Карточки товаров. Максимум 50 товаров для одной кампании"""

    add: Any | None = _field(default=None)
    """Карточки товаров, которые необходимо добавить"""
    delete: list[int] | None = _field(default=None)
    """Карточки товаров, которые необходимо удалить"""


class AdvV0AuctionNmsUpdateResponse(WBModel):
    nms: list[AdvV0AuctionNmsUpdateResponseNmsItem] | None = _field(default=None)
    """Результат отработки запроса"""


class AdvV0AuctionNmsUpdateResponseNmsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nms: AdvV0AuctionNmsUpdateResponseNmsItemNms | None = _field(default=None)
    """Карточки товаров"""


class AdvV0AuctionNmsUpdateResponseNmsItemNms(WBModel):
    """Карточки товаров"""

    added: Any | None = _field(default=None)
    """Добавленные карточки товаров"""
    deleted: Any | None = _field(default=None)
    """Удалённые карточки товаров"""


class AdvV0AuctionPlacementsUpdateBody(WBModel):
    placements: list[AdvV0AuctionPlacementsUpdateBodyPlacementsItem] | None = _field(default=None)
    """Места размещения в кампаниях"""


class AdvV0AuctionPlacementsUpdateBodyPlacementsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    placements: AdvV0AuctionPlacementsUpdateBodyPlacementsItemPlacements | None = _field(default=None)
    """Места размещения"""


class AdvV0AuctionPlacementsUpdateBodyPlacementsItemPlacements(WBModel):
    """Места размещения"""

    recommendations: Any | None = _field(default=None)
    """Размещение в рекомендациях:   - `false` — отключено   - `true` — включено"""
    search: Any | None = _field(default=None)
    """Размещение в поиске:   - `false` — отключено   - `true` — включено"""


class AdvV0AuctionPlacementsUpdatePlacementsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    placements: AdvV0AuctionPlacementsUpdatePlacementsItemPlacements | None = _field(default=None)
    """Места размещения"""


class AdvV0AuctionPlacementsUpdatePlacementsItemPlacements(WBModel):
    """Места размещения"""

    recommendations: bool | None = _field(default=None)
    """Размещение в рекомендациях:   - `false` — отключено   - `true` — включено"""
    search: bool | None = _field(default=None)
    """Размещение в поиске:   - `false` — отключено   - `true` — включено"""


class AdvV0NormqueryStatsCreateItemsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""


class AdvV0RenameCreateBody(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании, в которой меняется название"""
    name: str | None = _field(default=None)
    """Новое название (максимум 100 символов)"""


class AdvV1AdvertResponse(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID медиакампании"""
    brand: str | None = _field(default=None)
    """Название бренда"""
    create_time: str | None = _field(default=None, name="createTime")
    """Время создания медиакампании"""
    extended: AdvV1AdvertResponseExtended | None = _field(default=None)
    items: list[AdvV1AdvertResponseItemsItem] | None = _field(default=None)
    """Информация о баннере.  Наличие в ответе тех или иных полей зависит от конфигурации
    медиакампании.
    """
    name: str | None = _field(default=None)
    """Название медиакампании"""
    status: int | None = _field(default=None)
    """Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с
    возможностью вернуть на модерацию)   - `4` — готова к запуску …
    """
    type: int | None = _field(default=None)
    """Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам"""


class AdvV1AdvertResponseExtended(WBModel):
    budget: int | None = _field(default=None)
    """Остаток бюджета для типа `2`"""
    contract_id: int | None = _field(default=None)
    """ID контракта, для продавцов на контракте"""
    expenses: int | None = _field(default=None)
    """Затраты"""
    from_: str | None = _field(default=None, name="from")
    """Дата и время начала показа медиакампании"""
    operation: int | None = _field(default=None)
    """Источник списания:   - `1` — баланс   - `2` — счёт"""
    price: int | None = _field(default=None)
    """Стоимость размещения по дням для типа `1`"""
    reason: str | None = _field(default=None)
    """Комментарий модератора"""
    to: str | None = _field(default=None)
    """Дата и время окончания показа медиакампании"""
    updated_at: str | None = _field(default=None)
    """Дата и время изменения кампании"""


class AdvV1AdvertResponseItemsItem(WBModel):
    erid: str | None = _field(default=None, name="Erid")
    """Уникальный ID медиакампании для работы с ОРД"""
    action_name: str | None = _field(default=None)
    """Название акции"""
    additional_settings: int | None = _field(default=None, name="additionalSettings")
    """Дополнительные настройки.  Формат почтовой рассылки: - `1` — общий - `2` — частичный - `3` —
    уникальный  Социальная сеть: - `1` — VK - `2` — OK (Одноклассники)
    """
    advert_type: int | None = _field(default=None)
    """Тип продвижения: - `1` — баннер - `2` — всплывающее меню - `3` — почтовая рассылка - `4` —
    социальные сети - `5` — push-уведомления в мобильном приложении
    """
    bottom_text1: str | None = _field(default=None, name="bottomText1")
    """Текст под плашкой баннера"""
    bottom_text2: str | None = _field(default=None, name="bottomText2")
    """2-я строка с текстом под плашкой баннера"""
    budget: int | None = _field(default=None)
    """Бюджет"""
    category_name: str | None = _field(default=None)
    """Название категории размещения"""
    cpm: int | None = _field(default=None)
    """Ставка"""
    created_at: str | None = _field(default=None)
    """Дата создания баннера"""
    daily_limit: int | None = _field(default=None)
    """Дневной лимит (для баннеров по показам)"""
    date_from: str | None = _field(default=None)
    """Дата начала работы баннера"""
    date_to: str | None = _field(default=None)
    """Дата завершения работы баннера"""
    id: int | None = _field(default=None)
    """ID баннера"""
    message: str | None = _field(default=None)
    """Текст push-уведомления или рассылки"""
    name: str | None = _field(default=None)
    """Бренд"""
    nms: list[int] | None = _field(default=None)
    """Подборка артикулов WB"""
    place: int | None = _field(default=None)
    """Позиция на странице размещения"""
    receivers_count: int | None = _field(default=None, name="receiversCount")
    """Кол-во получателей push-уведомлений"""
    show_hours: list[AdvV1AdvertResponseItemsItemShowHoursItem] | None = _field(default=None)
    """Часы показа"""
    status: int | None = _field(default=None)
    """Статус (такой же как у медиакампании)"""
    subject_id: int | None = _field(default=None)
    """ID родительской категории товара"""
    subject_name: str | None = _field(default=None)
    """Название родительской категории товара"""
    updated_at: str | None = _field(default=None)
    """Дата и время обновления баннера"""
    url: str | None = _field(default=None)
    """URL страницы, на которую попадает пользователь при клике по баннеру"""


class AdvV1AdvertResponseItemsItemShowHoursItem(WBModel):
    from_: Any | None = _field(default=None, name="From")
    """Начало показа"""
    to: Any | None = _field(default=None, name="To")
    """Конец показа"""


class AdvV1AdvertsResponseItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID медиакампании"""
    brand: str | None = _field(default=None)
    """Название бренда"""
    create_time: str | None = _field(default=None, name="createTime")
    """Время создания медиакампании"""
    end_time: str | None = _field(default=None, name="endTime")
    """Время завершения медиакампании"""
    name: str | None = _field(default=None)
    """Название медиакампании"""
    status: int | None = _field(default=None)
    """Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с
    возможностью вернуть на модерацию)   - `4` — готова к запуску …
    """
    type: int | None = _field(default=None)
    """Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам"""


class AdvV1BalanceResponse(WBModel):
    balance: int | None = _field(default=None)
    """Счёт в базовых единицах валюты аккаунта продавца"""
    bonus: int | None = _field(default=None)
    """Бонусы в базовых единицах валюты аккаунта продавца"""
    cashbacks: list[AdvV1BalanceResponseCashbacksItem] | None = _field(default=None)
    """Промо-бонусы"""
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    net: int | None = _field(default=None)
    """Баланс в базовых единицах валюты аккаунта продавца"""


class AdvV1BalanceResponseCashbacksItem(WBModel):
    expiration_date: str | None = _field(default=None)
    """Дата окончания действия промо-бонусов"""
    percent: int | None = _field(default=None)
    """Процент от суммы пополнения бюджета кампании, который можно оплатить промо-бонусами за один
    раз
    """
    sum: int | None = _field(default=None)
    """Промо-бонусы в базовых единицах валюты аккаунта продавца"""


class AdvV1BudgetDepositCreateBody(WBModel):
    cashback_percent: int | None = _field(default=None)
    """Процент от суммы пополнения, который можно пополнить промо-бонусами. Нужно указать значение
    поля percent из ответа метода получения баланса …
    """
    cashback_sum: int | None = _field(default=None)
    """Сумма пополнения бюджета промо-бонусами. …"""
    return_: bool | None = _field(default=None, name="return")
    """Флаг возврата ответа (`true` — в ответе вернется обновлённый размер бюджета кампании,
    `false` или не указать параметр вообще — не вернётся.)
    """
    sum: int | None = _field(default=None)
    """Общая сумма пополнения бюджета в базовых единицах валюты аккаунта продавца"""
    type: int | None = _field(default=None)
    """Тип источника пополнения: - `0` — Счёт - `1` — Баланс - `3` — Бонусы"""


class AdvV1BudgetResponse(WBModel):
    cash: int | None = _field(default=None)
    """Поле не используется. Значение всегда 0."""
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    netting: int | None = _field(default=None)
    """Поле не используется. Значение всегда 0."""
    total: int | None = _field(default=None)
    """Бюджет кампании в базовых единицах валюты аккаунта продавца"""


class AdvV1CountResponse(WBModel):
    adverts: AdvV1CountResponseAdverts | None = _field(default=None)
    all: int | None = _field(default=None)
    """Общее количество медиакампаний всех статусов и типов"""


class AdvV1CountResponseAdverts(WBModel):
    count: int | None = _field(default=None)
    """Количество медиакампаний"""
    status: int | None = _field(default=None)
    """Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с
    возможностью вернуть на модерацию)   - `4` — готова к запуску …
    """
    type: int | None = _field(default=None)
    """Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам"""


class AdvV1NormqueryStatsCreateItemsItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""


class AdvV1PaymentsResponseItem(WBModel):
    card_status: str | None = _field(default=None, name="cardStatus")
    """Статус операции при оплате картой: - `success` — успех - `fail` — неуспех - `pending` — в
    ожидании ответа - `unknown` — неизвестно
    """
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    date: str | None = _field(default=None)
    """Дата платежа"""
    id: int | None = _field(default=None)
    """ID платежа"""
    status_id: int | None = _field(default=None, name="statusId")
    """Статус: - `0` — ошибка - `1` — обработано"""
    sum: int | None = _field(default=None)
    """Сумма платежа"""
    type: int | None = _field(default=None)
    """Тип источника списания: - `0` — Счёт - `1` — Баланс - `3` — Картой"""


class AdvV1PromotionCountResponse(WBModel):
    adverts: list[AdvV1PromotionCountResponseAdvertsItem] | None = _field(default=None)
    """Данные по кампаниям"""
    all: int | None = _field(default=None)
    """Общее количество кампаний всех статусов и типов"""


class AdvV1PromotionCountResponseAdvertsItem(WBModel):
    advert_list: list[AdvV1PromotionCountResponseAdvertsItemAdvertListItem] | None = _field(default=None)
    """Список кампаний"""
    count: int | None = _field(default=None)
    """Количество кампаний"""
    status: int | None = _field(default=None)
    """Статус кампании"""
    type: int | None = _field(default=None)
    """Тип кампании:   - `8` — кампания с единой ставкой (**устаревший тип**) …"""


class AdvV1PromotionCountResponseAdvertsItemAdvertListItem(WBModel):
    advert_id: Any | None = _field(default=None, name="advertId")
    """ID кампании"""
    change_time: Any | None = _field(default=None, name="changeTime")
    """Дата и время последнего изменения кампании"""


class AdvV1SupplierSubjectsResponseItem(WBModel):
    count: int | None = _field(default=None)
    """Количество Артикулов WB (`nmId`) с таким предметом."""
    id: int | None = _field(default=None)
    """ID предмета"""
    name: str | None = _field(default=None)
    """Предмет"""


class AdvV1UpdResponseItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    advert_status: int | None = _field(default=None, name="advertStatus")
    """Статус кампании: - `-1` — удалена, процесс удаления будет завершён в течение 10 минут - `4`
    — готова к запуску - `7` — завершена - `8` — отменена …
    """
    advert_type: int | None = _field(default=None, name="advertType")
    """Тип кампании"""
    camp_name: str | None = _field(default=None, name="campName")
    """Название кампании"""
    payment_type: str | None = _field(default=None, name="paymentType")
    """Источник списания:  - `Баланс`  - `Бонусы`  - `Счёт`  - `Кэшбэк`"""
    upd_num: int | None = _field(default=None, name="updNum")
    """Номер выставленного документа"""
    upd_sum: int | None = _field(default=None, name="updSum")
    """Выставленная сумма в базовых единицах валюты аккаунта продавца"""
    upd_time: str | None = _field(default=None, name="updTime")
    """Время списания"""


class AdvV2SeacatSaveAdCreateBody(WBModel):
    bid_type: str | None = _field(default=None)
    """Тип ставки:   - `manual` — ручная   - `unified` — единая"""
    name: str | None = _field(default=None)
    """Название кампании"""
    nms: list[int] | None = _field(default=None)
    """Карточки товаров для кампании. Доступные карточки товаров можно получить с помощью метода
    Карточки товаров для кампаний. Максимум 50 товаров (`nm`)
    """
    payment_type: str | None = _field(default=None)
    """Тип оплаты: - `cpm` — за показы - `cpc` — за клик. При создании с этим типом оплаты в
    кампании автоматически устанавливается минимальная ставка
    """
    placement_types: list[str] | None = _field(default=None)
    """Места размещения:   - `search` — в поиске   - `recommendations` — в рекомендациях  Укажите
    только для кампании с ручной ставкой
    """


class AdvV2SupplierNmsCreateResponseItem(WBModel):
    nm: int | None = _field(default=None)
    """Артикул WB"""
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    title: str | None = _field(default=None)
    """Название товара"""


class AdvertNMsSettings(WBModel):
    bids_kopecks: Any | None = _field(default=None)
    nm_id: Any | None = _field(default=None)
    """Артикул WB"""
    subject: Any | None = _field(default=None)


class AdvertSettings(WBModel):
    """Настройки кампании"""

    name: Any | None = _field(default=None)
    """Название кампании"""
    payment_type: Any | None = _field(default=None)
    """Тип оплаты: - `cpm` — за показы - `cpc` — за клик"""
    placements: Any | None = _field(default=None)
    """Места размещения"""


class AdvertV1BidsMinCreateBody(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_ids: list[int] | None = _field(default=None)
    """Список артикулов WB"""
    payment_type: str | None = _field(default=None)
    """Тип оплаты:       - `cpm` — за показы       - `cpc` — за клик"""
    placement_types: list[str] | None = _field(default=None)
    """Места размещения:   - `search` — поиск   - `recommendation` — рекомендации   - `combined` —
    поиск и рекомендации
    """


class AdvertV1BidsMinCreateResponse(WBModel):
    bids: list[AdvertV1BidsMinCreateResponseBidsItem] | None = _field(default=None)
    """Список карточек товаров со ставками"""


class AdvertV1BidsMinCreateResponseBidsItem(WBModel):
    bids: list[AdvertV1BidsMinCreateResponseBidsItemBidsItem] | None = _field(default=None)
    """Список ставок по местам размещения"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""


class AdvertV1BidsMinCreateResponseBidsItemBidsItem(WBModel):
    currency: Any | None = _field(default=None)
    """Валюта аккаунта продавца"""
    type: Any | None = _field(default=None)
    value: Any | None = _field(default=None)
    """Минимальная ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""


class AdvertV1BidsUpdateBidsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_bids: list[AdvertV1BidsUpdateBidsItemNmBidsItem] | None = _field(default=None)
    """Ставки"""


class AdvertV1BidsUpdateBidsItemNmBidsItem(WBModel):
    bid_kopecks: int | None = _field(default=None)
    """Ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""
    placement: str | None = _field(default=None)
    """Место размещения:   - `search` — в поиске (для кампаний с ручной ставкой)   -
    `recommendations`— в рекомендациях (для кампаний с ручной ставкой) …
    """


class AdvertV1BidsUpdateBody(WBModel):
    bids: list[AdvertV1BidsUpdateBodyBidsItem] | None = _field(default=None)
    """Ставки в кампаниях"""


class AdvertV1BidsUpdateBodyBidsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_bids: list[AdvertV1BidsUpdateBodyBidsItemNmBidsItem] | None = _field(default=None)
    """Ставки"""


class AdvertV1BidsUpdateBodyBidsItemNmBidsItem(WBModel):
    bid_kopecks: Any | None = _field(default=None)
    """Ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""
    nm_id: Any | None = _field(default=None)
    """Артикул WB"""
    placement: Any | None = _field(default=None)
    """Место размещения:   - `search` — в поиске (для кампаний с ручной ставкой)   -
    `recommendations`— в рекомендациях (для кампаний с ручной ставкой) …
    """


class AdvertV1BidsUpdateResponse(WBModel):
    bids: list[AdvertV1BidsUpdateResponseBidsItem] | None = _field(default=None)
    """Результат отработки запроса"""
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""


class AdvertV1BidsUpdateResponseBidsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_bids: list[AdvertV1BidsUpdateResponseBidsItemNmBidsItem] | None = _field(default=None)
    """Ставки"""


class AdvertV1BidsUpdateResponseBidsItemNmBidsItem(WBModel):
    bid_kopecks: Any | None = _field(default=None)
    """Ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""
    nm_id: Any | None = _field(default=None)
    """Артикул WB"""
    placement: Any | None = _field(default=None)
    """Место размещения:   - `search` — в поиске   - `recommendations`— в рекомендациях"""


class FullStatsItem(WBModel):
    """Статистика по одной кампании за период, указанный в запросе. По всем артикулам WB и плат"""

    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    atbs: int | None = _field(default=None)
    """Количество добавлений товаров в корзину"""
    booster_stats: list[Any] | None = _field(default=None, name="boosterStats")
    canceled: int | None = _field(default=None)
    """Отмены, шт."""
    clicks: int | None = _field(default=None)
    """Количество кликов"""
    cpc: float | None = _field(default=None)
    """Средняя стоимость клика в базовых единицах валюты аккаунта продавца"""
    cr: float | None = _field(default=None)
    """CR (conversion rate) — отношение количества заказов к общему количеству кликов"""
    ctr: float | None = _field(default=None)
    """CTR (click-through rate) — отношение числа кликов к количеству показов в процентах"""
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    days: list[Any] | None = _field(default=None)
    orders: int | None = _field(default=None)
    """Количество заказов"""
    shks: int | None = _field(default=None)
    """Количество заказанных товаров, шт."""
    sum: float | None = _field(default=None)
    """Затраты в базовых единицах валюты аккаунта продавца"""
    sum_price: float | None = _field(default=None)
    """Сумма заказов в базовых единицах валюты аккаунта продавца"""
    views: int | None = _field(default=None)
    """Количество просмотров"""


class GetAdverts(WBModel):
    adverts: list[GetAdvertsAdvertsItem] | None = _field(default=None)
    """Кампании"""


class GetAdvertsAdvertsItem(WBModel):
    bid_type: str | None = _field(default=None)
    """Тип ставки:   - `unified` — единая ставка   - `manual` — ручная ставка"""
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    id: int | None = _field(default=None)
    """ID кампании"""
    nm_settings: list[AdvertNMsSettings] | None = _field(default=None)
    """Настройки товаров"""
    restrictions: GetAdvertsAdvertsItemRestrictions | None = _field(default=None)
    """Ограничения кампании"""
    settings: AdvertSettings | None = _field(default=None)
    status: int | None = _field(default=None)
    """Статус кампании: - `-1` — удалена, процесс удаления будет завершён в течение 10 минут - `4`
    — готова к запуску - `7` — завершена - `8` — отменена …
    """
    timestamps: Timestamps | None = _field(default=None)


class GetAdvertsAdvertsItemRestrictions(WBModel):
    """Ограничения кампании"""

    can_change_nms: Any | None = _field(default=None)
    """Можно ли изменять список товаров кампании:   - `true` — да   - `false` — нет"""


class NormQueryBidFailResponseItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    norm_query: str | None = _field(default=None, name="normQuery")
    """Поисковый кластер — это группа похожих поисковых запросов, по которым покупатели находят
    товары
    """
    reason: str | None = _field(default=None)
    """Описание причины ошибки"""


class RequestWithDate(WBModel):
    dates: list[str] | None = _field(default=None)
    """Даты, за которые нужно получить информацию"""
    id: int | None = _field(default=None)
    """ID кампании"""


class ResponseWithReturn(WBModel):
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    total: int | None = _field(default=None)
    """Размер обновлённого бюджета"""


class StatInterval(WBModel):
    interval: StatIntervalInterval | None = _field(default=None)
    """Период"""
    stats: list[StatsBlok1] | None = _field(default=None)
    """Блок статистики"""


class StatIntervalInterval(WBModel):
    """Период"""

    begin: str | None = _field(default=None)
    """Начало периода"""
    end: str | None = _field(default=None)
    """Конец периода"""


class StatsBlok1(WBModel):
    advert_type: Any | None = _field(default=None)
    """Тип медиакампании:   - `1` — размещение по дням   - `2` — размещение по просмотрам"""
    atbs: Any | None = _field(default=None)
    """Количество добавлений товаров в корзину"""
    category_name: Any | None = _field(default=None)
    """Название категории"""
    clicks: Any | None = _field(default=None)
    """Количество кликов"""
    cpc: Any | None = _field(default=None)
    """(cost per click) — цена клика по продвигаемому товару"""
    cr: Any | None = _field(default=None)
    """CR(conversion rate) — это отношение количества заказов к общему количеству посещений
    медиакампании
    """
    cr1: Any | None = _field(default=None)
    """Отношение количества добавлений в корзину к количеству кликов"""
    cr2: Any | None = _field(default=None)
    """Отношение количества заказов к количеству добавлений в корзину"""
    ctr: Any | None = _field(default=None)
    """CTR (click-through rate) — показатель кликабельности, отношение числа кликов к количеству
    показов в рамках медиакампании
    """
    daily_stats: Any | None = _field(default=None)
    date_from: Any | None = _field(default=None)
    """Время начала размещения"""
    date_to: Any | None = _field(default=None)
    """Время завершения размещения"""
    expenses: Any | None = _field(default=None)
    """Стоимость размещения баннера"""
    item_id: Any | None = _field(default=None)
    """ID баннера"""
    item_name: Any | None = _field(default=None)
    """Бренд"""
    orders: Any | None = _field(default=None)
    """Количество заказов"""
    place: Any | None = _field(default=None)
    """Место на странице"""
    price: Any | None = _field(default=None)
    """Стоимость размещения"""
    status: Any | None = _field(default=None)
    """Статус медиакампании"""
    subject_name: Any | None = _field(default=None)
    """Родительская категория предмета"""
    views: Any | None = _field(default=None)
    """Количество просмотров"""


class Timestamps(WBModel):
    """Временные отметки"""

    created: Any | None = _field(default=None)
    """Время создания кампании"""
    deleted: Any | None = _field(default=None)
    """Время удаления кампании. Если кампания не удалена, время указывается в будущем"""
    started: Any | None = _field(default=None)
    """Время последнего запуска кампании"""
    updated: Any | None = _field(default=None)
    """Время последнего изменения кампании"""


class V0BidRecommendationBase(WBModel):
    """Рекомендуемые ставки для карточек товаров"""

    competitive_bid: V0BidRecommendationBaseBidCompetitiveBid | None = _field(
        default=None, name="competitiveBid"
    )
    leaders_bid: V0BidRecommendationBaseBidLeadersBid | None = _field(default=None, name="leadersBid")
    top2: V0BidRecommendationBaseBidTop2 | None = _field(default=None)


class V0BidRecommendationBaseBidCompetitiveBid(WBModel):
    """Конкурентная ставка — расчётная средняя ставка других продавцов, продающих аналогичные т"""

    bid_kopecks: Any | None = _field(default=None, name="bidKopecks")
    """Рекомендуемая ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""


class V0BidRecommendationBaseBidLeadersBid(WBModel):
    """Лидерская ставка — средняя ставка с которой товары занимают лидирующие позиции в вашей к"""

    bid_kopecks: Any | None = _field(default=None, name="bidKopecks")
    """Рекомендуемая ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""


class V0BidRecommendationBaseBidTop2(WBModel):
    """Топ-ставка"""

    bid_kopecks: Any | None = _field(default=None, name="bidKopecks")
    """Рекомендуемая ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца. Если
    `0`, для данного предмета топ-ставка не используется
    """


class V0BidRecommendationNormQuery(WBModel):
    norm_query: str | None = _field(default=None, name="normQuery")
    """Поисковый кластер"""
    reach_max: V0BidRecommendationReachMax | None = _field(default=None, name="reachMax")
    reach_medium: V0BidRecommendationReachMedium | None = _field(default=None, name="reachMedium")
    reach_min: V0BidRecommendationReachMin | None = _field(default=None, name="reachMin")


class V0BidRecommendationReachMax(WBModel):
    """Максимальный охват: 76-100%"""

    bid_kopecks: Any | None = _field(default=None, name="bidKopecks")
    """Рекомендуемая ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца."""
    bid_kopecks_min: Any | None = _field(default=None, name="bidKopecksMin")
    """Минимальная ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца."""


class V0BidRecommendationReachMedium(WBModel):
    """Средний охват: 61-75%"""

    bid_kopecks: Any | None = _field(default=None, name="bidKopecks")
    """Рекомендуемая ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""
    bid_kopecks_min: Any | None = _field(default=None, name="bidKopecksMin")
    """Минимальная ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""


class V0BidRecommendationReachMin(WBModel):
    """Минимальный охват: 50-60%"""

    bid_kopecks: Any | None = _field(default=None, name="bidKopecks")
    """Рекомендуемая ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""
    bid_kopecks_min: Any | None = _field(default=None, name="bidKopecksMin")
    """Минимальная ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца"""


class V0BidsRecommendationsCpmResponse(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    base: V0BidRecommendationBase | None = _field(default=None)
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    norm_queries: list[V0BidRecommendationNormQuery] | None = _field(default=None, name="normQueries")
    """Рекомендуемые ставки для поисковых кластеров"""
    payment_type: str | None = _field(default=None, name="paymentType")
    """Тип оплаты:   - `cpm` — за показы"""


class V0DeleteNormQueryBidsRequest(WBModel):
    bids: list[V0DeleteNormQueryBidsRequestItem] | None = _field(default=None)


class V0DeleteNormQueryBidsRequestItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""
    norm_query: str | None = _field(default=None)
    """Поисковый кластер"""


class V0GetNormQueryBidsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    bid: int | None = _field(default=None)
    """Текущая ставка в базовых единицах валюты аккаунта продавца за тысячу показов"""
    bid_kopecks: int | None = _field(default=None)
    """Текущая ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца за тысячу
    показов
    """
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""
    norm_query: str | None = _field(default=None)
    """Поисковый кластер"""


class V0GetNormQueryBidsRequest(WBModel):
    items: list[V0GetNormQueryBidsRequestItem] | None = _field(default=None)


class V0GetNormQueryBidsRequestItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""


class V0GetNormQueryBidsResponse(WBModel):
    bids: list[V0GetNormQueryBidsItem] | None = _field(default=None)


class V0GetNormQueryListRequest(WBModel):
    items: list[V0GetNormQueryListRequestItem] | None = _field(default=None)


class V0GetNormQueryListRequestItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""


class V0GetNormQueryListResponse(WBModel):
    items: list[V0GetNormQueryListResponseItem] | None = _field(default=None)


class V0GetNormQueryListResponseItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    norm_queries: V0GetNormQueryListResponseItemNormQueries | None = _field(default=None, name="normQueries")


class V0GetNormQueryListResponseItemNormQueries(WBModel):
    """Поисковые кластеры"""

    active: Any | None = _field(default=None)
    """Активные поисковые кластеры"""
    archived: Any | None = _field(default=None)
    """Архивные поисковые кластеры"""
    excluded: Any | None = _field(default=None)
    """Неактивные поисковые кластеры"""


class V0GetNormQueryMinusRequest(WBModel):
    items: list[V0GetNormQueryMinusRequestItem] | None = _field(default=None)


class V0GetNormQueryMinusRequestItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""


class V0GetNormQueryMinusResponse(WBModel):
    items: list[V0GetNormQueryMinusResponseItem] | None = _field(default=None)


class V0GetNormQueryMinusResponseItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""
    norm_queries: list[str] | None = _field(default=None)
    """Список минус-фраз"""


class V0GetNormQueryStatsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""
    stats: list[V0GetNormQueryStatsItemStat] | None = _field(default=None)


class V0GetNormQueryStatsItemStat(WBModel):
    atbs: Any | None = _field(default=None)
    """Количество добавлений товаров в корзину"""
    avg_pos: Any | None = _field(default=None)
    """Средняя позиция товара на страницах поисковой выдачи"""
    clicks: Any | None = _field(default=None)
    """Количество кликов"""
    cpc: Any | None = _field(default=None)
    """Стоимость одного клика в базовых единицах валюты аккаунта продавца"""
    cpm: Any | None = _field(default=None)
    """Средняя стоимость за тысячу показов в базовых единицах валюты аккаунта продавца.  Для
    кампаний с типом оплаты `cpc` — за клики — значение будет `null`
    """
    ctr: Any | None = _field(default=None)
    """Кликабельность — отношение числа кликов к количеству показов, %.  Для кампаний с типом
    оплаты `cpc` — за клики — значение будет `null`
    """
    currency: Any | None = _field(default=None)
    """Валюта аккаунта продавца"""
    norm_query: Any | None = _field(default=None)
    """Поисковый кластер"""
    orders: Any | None = _field(default=None)
    """Количество заказов"""
    shks: Any | None = _field(default=None)
    """Количество заказанных товаров, шт."""
    spend: Any | None = _field(default=None)
    """Затраты на продвижение товаров в конкретном поисковом кластере кампании"""
    views: Any | None = _field(default=None)
    """Количество просмотров.  Для кампаний с типом оплаты `cpc` — за клики — значение будет `null`
    """


class V0GetNormQueryStatsRequest(WBModel):
    from_: str | None = _field(default=None, name="from")
    """Дата начала периода"""
    items: list[V0GetNormQueryStatsRequestItemsItem] | None = _field(default=None)
    to: str | None = _field(default=None)
    """Дата окончания периода"""


class V0GetNormQueryStatsRequestItemsItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""


class V0GetNormQueryStatsResponse(WBModel):
    """Статистика по поисковым кластерам"""

    stats: list[V0GetNormQueryStatsItem] | None = _field(default=None)


class V0SetMinusNormQueryRequest(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""
    norm_queries: list[str] | None = _field(default=None)


class V0SetNormQueryBidsRequest(WBModel):
    bids: list[V0SetNormQueryBidsRequestItem] | None = _field(default=None)


class V0SetNormQueryBidsRequestItem(WBModel):
    advert_id: int | None = _field(default=None)
    """ID кампании"""
    bid: int | None = _field(default=None)
    """Ставка за тысячу показов в базовых единицах валюты аккаунта продавца"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""
    norm_query: str | None = _field(default=None)
    """Поисковый кластер"""


class V1GetNormQueryStatsRequest(WBModel):
    from_: str | None = _field(default=None, name="from")
    """Дата начала периода"""
    items: list[V1GetNormQueryStatsRequestItemsItem] | None = _field(default=None)
    to: str | None = _field(default=None)
    """Дата окончания периода периода"""


class V1GetNormQueryStatsRequestItemsItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""


class V1GetNormQueryStatsResponse(WBModel):
    items: list[V1GetNormQueryStatsResponseItem] | None = _field(default=None)


class V1GetNormQueryStatsResponseItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    daily_stats: list[V1GetNormQueryStatsResponseItemDailyStat] | None = _field(
        default=None, name="dailyStats"
    )
    """Статистика с детализацией по дням"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""


class V1GetNormQueryStatsResponseItemDailyStat(WBModel):
    date: Any | None = _field(default=None)
    """Дата"""
    stat: Any | None = _field(default=None)


class V1SetNormQueryBidsRequest(WBModel):
    bids: list[V1SetNormQueryBidsRequestItem] | None = _field(default=None)


class V1SetNormQueryBidsRequestItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    bid_minor_units: int | None = _field(default=None, name="bidMinorUnits")
    """Ставка в разменных единицах — 0,01 от базовой валюты аккаунта продавца. Допустимый шаг
    ставки указан в ответе метода GET /api/advert/v1/config
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    norm_query: str | None = _field(default=None, name="normQuery")
    """Поисковый кластер"""


class V1SetNormQueryBidsResponse(WBModel):
    failed: list[NormQueryBidFailResponseItem] | None = _field(default=None)
    success: list[V1SetNormQueryBidsSuccessResponseItem] | None = _field(default=None)


class V1SetNormQueryBidsSuccessResponseItem(WBModel):
    advert_id: int | None = _field(default=None, name="advertId")
    """ID кампании"""
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    norm_query: str | None = _field(default=None, name="normQuery")
    """Поисковый кластер — это группа похожих поисковых запросов, по которым покупатели находят
    товары
    """


class V2GetConfigResponse(WBModel):
    cpc_step: int | None = _field(default=None, name="cpcStep")
    """Шаг ставки в разменных единицах — 0,01 от базовой валюты аккаунта продавца для кампаний CPC
    """
    cpm_step: int | None = _field(default=None, name="cpmStep")
    """Шаг ставки в разменных единицах — 0,01 от базовой валюты аккаунта продавца для CPM-кампаний
    """
    currency: str | None = _field(default=None)
    """Валюта аккаунта продавца"""
    currency_code: int | None = _field(default=None, name="currencyCode")
    """Код валюты аккаунта продавца"""
    min_top_up: int | None = _field(default=None, name="minTopUp")
    """Минимальная сумма пополнения бюджета кампании в разменных единицах — 0,01 от базовой валюты
    аккаунта продавца. …
    """
