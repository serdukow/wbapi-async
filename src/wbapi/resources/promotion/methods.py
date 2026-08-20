from __future__ import annotations

from typing import Any

from ...client.method import WBMethod
from ...utils.token import Scope
from .models import (
    AdvertV1BidsMinCreateResponse,
    AdvertV1BidsUpdateBidsItem,
    AdvertV1BidsUpdateResponse,
    AdvV0AuctionNmsUpdateNmsItem,
    AdvV0AuctionNmsUpdateResponse,
    AdvV0AuctionPlacementsUpdatePlacementsItem,
    AdvV0NormqueryStatsCreateItemsItem,
    AdvV1AdvertResponse,
    AdvV1AdvertsResponseItem,
    AdvV1BalanceResponse,
    AdvV1BudgetResponse,
    AdvV1CountResponse,
    AdvV1NormqueryStatsCreateItemsItem,
    AdvV1PaymentsResponseItem,
    AdvV1PromotionCountResponse,
    AdvV1SupplierSubjectsResponseItem,
    AdvV1UpdResponseItem,
    AdvV2SupplierNmsCreateResponseItem,
    FullStatsItem,
    GetAdverts,
    RequestWithDate,
    ResponseWithReturn,
    StatInterval,
    V0BidsRecommendationsCpmResponse,
    V0DeleteNormQueryBidsRequestItem,
    V0GetNormQueryBidsRequestItem,
    V0GetNormQueryBidsResponse,
    V0GetNormQueryListRequestItem,
    V0GetNormQueryListResponse,
    V0GetNormQueryMinusRequestItem,
    V0GetNormQueryMinusResponse,
    V0GetNormQueryStatsResponse,
    V0SetNormQueryBidsRequestItem,
    V1GetNormQueryStatsResponse,
    V1SetNormQueryBidsRequestItem,
    V1SetNormQueryBidsResponse,
    V2GetConfigResponse,
)


class AdvV0AuctionNmsUpdate(WBMethod[AdvV0AuctionNmsUpdateResponse]):
    """Изменение списка карточек товаров в кампаниях

    PATCH /adv/v0/auction/nms
    """

    __path__ = "/adv/v0/auction/nms"
    __http_method__ = "PATCH"
    __returns__ = AdvV0AuctionNmsUpdateResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 1),
        "service": (1000, 1),
        "basic_secret": (1000, 1),
        "basic": (1800000, 1),
    }
    __body_fields__ = {"nms": "nms"}

    nms: list[AdvV0AuctionNmsUpdateNmsItem]
    """Карточки товаров в кампаниях"""


class AdvV0AuctionPlacementsUpdate(WBMethod[None]):
    """Изменение мест размещения в кампаниях с ручной ставкой

    PUT /adv/v0/auction/placements
    """

    __path__ = "/adv/v0/auction/placements"
    __http_method__ = "PUT"
    __returns__ = None
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 1),
        "service": (1000, 1),
        "basic_secret": (1000, 1),
        "basic": (1800000, 1),
    }
    __body_fields__ = {"placements": "placements"}

    placements: list[AdvV0AuctionPlacementsUpdatePlacementsItem]
    """Места размещения в кампаниях"""


class AdvV0Delete(WBMethod[None]):
    """Удаление кампании

    GET /adv/v0/delete
    """

    __path__ = "/adv/v0/delete"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 5),
        "service": (200, 5),
        "basic_secret": (200, 5),
        "basic": (720000, 1),
    }

    id_: int
    """ID кампании"""


class AdvV0NormqueryBidsDelete(WBMethod[None]):
    """Удалить ставки поисковых кластеров

    DELETE /adv/v0/normquery/bids
    """

    __path__ = "/adv/v0/normquery/bids"
    __http_method__ = "DELETE"
    __returns__ = None
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 10),
        "service": (200, 10),
        "basic_secret": (200, 10),
        "basic": (720000, 1),
    }
    __body_fields__ = {"bids": "bids"}

    bids: list[V0DeleteNormQueryBidsRequestItem]


class AdvV0NormqueryBidsUpdate(WBMethod[None]):
    """Установить ставки для поисковых кластеров

    POST /adv/v0/normquery/bids
    """

    __path__ = "/adv/v0/normquery/bids"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (500, 4),
        "service": (500, 4),
        "basic_secret": (500, 4),
        "basic": (720000, 1),
    }
    __body_fields__ = {"bids": "bids"}

    bids: list[V0SetNormQueryBidsRequestItem]


class AdvV0NormqueryGetBids(WBMethod[V0GetNormQueryBidsResponse]):
    """Список ставок поисковых кластеров

    POST /adv/v0/normquery/get-bids
    """

    __path__ = "/adv/v0/normquery/get-bids"
    __http_method__ = "POST"
    __returns__ = V0GetNormQueryBidsResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 10),
        "service": (200, 10),
        "basic_secret": (200, 10),
        "basic": (720000, 1),
    }
    __body_fields__ = {"items": "items"}

    items: list[V0GetNormQueryBidsRequestItem]


class AdvV0NormqueryGetMinus(WBMethod[V0GetNormQueryMinusResponse]):
    """Список минус-фраз кампаний

    POST /adv/v0/normquery/get-minus
    """

    __path__ = "/adv/v0/normquery/get-minus"
    __http_method__ = "POST"
    __returns__ = V0GetNormQueryMinusResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 10),
        "service": (200, 10),
        "basic_secret": (200, 10),
        "basic": (720000, 1),
    }
    __items__ = "items"
    __body_fields__ = {"items": "items"}

    items: list[V0GetNormQueryMinusRequestItem]


class AdvV0NormqueryListCreate(WBMethod[V0GetNormQueryListResponse]):
    """Списки активных и неактивных поисковых кластеров

    POST /adv/v0/normquery/list
    """

    __path__ = "/adv/v0/normquery/list"
    __http_method__ = "POST"
    __returns__ = V0GetNormQueryListResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 10),
        "service": (200, 10),
        "basic_secret": (200, 10),
        "basic": (720000, 1),
    }
    __items__ = "items"
    __body_fields__ = {"items": "items"}

    items: list[V0GetNormQueryListRequestItem]


class AdvV0NormquerySetMinusCreate(WBMethod[None]):
    """Установка и удаление минус-фраз

    POST /adv/v0/normquery/set-minus
    """

    __path__ = "/adv/v0/normquery/set-minus"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 10),
        "service": (200, 10),
        "basic_secret": (200, 10),
        "basic": (720000, 1),
    }
    __body_fields__ = {"advert_id": "advert_id", "nm_id": "nm_id", "norm_queries": "norm_queries"}

    advert_id: int
    """ID кампании"""
    nm_id: int
    """Артикул WB"""
    norm_queries: list[str]


class AdvV0NormqueryStatsCreate(WBMethod[V0GetNormQueryStatsResponse]):
    """Статистика поисковых кластеров

    POST /adv/v0/normquery/stats
    """

    __path__ = "/adv/v0/normquery/stats"
    __http_method__ = "POST"
    __returns__ = V0GetNormQueryStatsResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (6000, 20),
        "service": (6000, 20),
        "basic_secret": (6000, 20),
        "basic": (720000, 1),
    }
    __body_fields__ = {"from_": "from", "to": "to", "items": "items"}

    from_: str
    """Дата начала периода"""
    items: list[AdvV0NormqueryStatsCreateItemsItem]
    to: str
    """Дата окончания периода"""


class AdvV0Pause(WBMethod[None]):
    """Пауза кампании

    GET /adv/v0/pause
    """

    __path__ = "/adv/v0/pause"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 5),
        "service": (200, 5),
        "basic_secret": (200, 5),
        "basic": (720000, 1),
    }

    id_: int
    """ID кампании"""


class AdvV0RenameCreate(WBMethod[None]):
    """Переименование кампании

    POST /adv/v0/rename
    """

    __path__ = "/adv/v0/rename"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 5),
        "service": (200, 5),
        "basic_secret": (200, 5),
        "basic": (1800000, 1),
    }
    __body_fields__ = {"advert_id": "advertId", "name": "name"}

    advert_id: int
    """ID кампании, в которой меняется название"""
    name: str
    """Новое название (максимум 100 символов)"""


class AdvV0Start(WBMethod[None]):
    """Запуск кампании

    GET /adv/v0/start
    """

    __path__ = "/adv/v0/start"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 5),
        "service": (200, 5),
        "basic_secret": (200, 5),
        "basic": (720000, 1),
    }

    id_: int
    """ID кампании"""


class AdvV0Stop(WBMethod[None]):
    """Завершение кампании

    GET /adv/v0/stop
    """

    __path__ = "/adv/v0/stop"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 5),
        "service": (200, 5),
        "basic_secret": (200, 5),
        "basic": (720000, 1),
    }

    id_: int
    """ID кампании"""


class AdvV1Advert(WBMethod[AdvV1AdvertResponse]):
    """Информация о медиакампании

    GET /adv/v1/advert
    """

    __path__ = "/adv/v1/advert"
    __http_method__ = "GET"
    __returns__ = AdvV1AdvertResponse
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-media-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (100, 10),
        "service": (100, 10),
        "basic_secret": (100, 10),
        "basic": (720000, 1),
    }
    __items__ = "items"

    id_: int
    """ID медиакампании"""


class AdvV1Adverts(WBMethod[list[AdvV1AdvertsResponseItem]]):
    """Список медиакампаний

    GET /adv/v1/adverts
    """

    __path__ = "/adv/v1/adverts"
    __http_method__ = "GET"
    __returns__ = list[AdvV1AdvertsResponseItem]
    __query_params__ = {
        "status": "status",
        "type_": "type",
        "limit": "limit",
        "offset": "offset",
        "order": "order",
        "direction": "direction",
    }
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-media-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (100, 10),
        "service": (100, 10),
        "basic_secret": (100, 10),
        "basic": (3600000, 1),
    }
    __paginate__ = "offset_query"

    direction: str | None = None
    """Порядок сортировки: - `desc` — от большего к меньшему - `asc` — от меньшего к большему"""
    limit: int | None = None
    """Количество кампаний в ответе"""
    offset: int | None = None
    """Смещение относительно первой медиакампании"""
    order: str | None = None
    """Порядок вывода ответа: - `create` — по времени создания медиакампании - `id` — по ID
    медиакампании
    """
    status: str | None = None
    """Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с
    возможностью вернуть на модерацию)   - `4` — готова к запуску …
    """
    type_: int | None = None
    """Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам"""


class AdvV1Balance(WBMethod[AdvV1BalanceResponse]):
    """Баланс

    GET /adv/v1/balance
    """

    __path__ = "/adv/v1/balance"
    __http_method__ = "GET"
    __returns__ = AdvV1BalanceResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 5),
        "service": (1000, 5),
        "basic_secret": (1000, 5),
        "basic": (1800000, 1),
    }


class AdvV1Budget(WBMethod[AdvV1BudgetResponse]):
    """Бюджет кампании

    GET /adv/v1/budget
    """

    __path__ = "/adv/v1/budget"
    __http_method__ = "GET"
    __returns__ = AdvV1BudgetResponse
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (250, 4),
        "service": (250, 4),
        "basic_secret": (250, 4),
        "basic": (900000, 1),
    }

    id_: int
    """ID кампании"""


class AdvV1BudgetDepositCreate(WBMethod[ResponseWithReturn]):
    """Пополнение бюджета кампании

    POST /adv/v1/budget/deposit
    """

    __path__ = "/adv/v1/budget/deposit"
    __http_method__ = "POST"
    __returns__ = ResponseWithReturn
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 5),
        "service": (1000, 5),
        "basic_secret": (1000, 5),
        "basic": (720000, 1),
    }
    __body_fields__ = {
        "sum": "sum",
        "cashback_sum": "cashback_sum",
        "cashback_percent": "cashback_percent",
        "type_": "type",
        "return_": "return",
    }

    id_: int
    """ID кампании"""
    cashback_percent: int | None = None
    """Процент от суммы пополнения, который можно пополнить промо-бонусами. Нужно указать значение
    поля percent из ответа метода получения баланса …
    """
    cashback_sum: int | None = None
    """Сумма пополнения бюджета промо-бонусами. …"""
    return_: bool | None = None
    """Флаг возврата ответа (`true` — в ответе вернется обновлённый размер бюджета кампании,
    `false` или не указать параметр вообще — не вернётся.)
    """
    sum: int | None = None
    """Общая сумма пополнения бюджета в базовых единицах валюты аккаунта продавца"""
    type_: int | None = None
    """Тип источника пополнения: - `0` — Счёт - `1` — Баланс - `3` — Бонусы"""


class AdvV1Count(WBMethod[AdvV1CountResponse]):
    """Количество медиакампаний

    GET /adv/v1/count
    """

    __path__ = "/adv/v1/count"
    __http_method__ = "GET"
    __returns__ = AdvV1CountResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-media-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (100, 10),
        "service": (100, 10),
        "basic_secret": (100, 10),
        "basic": (3600000, 1),
    }


class AdvV1NormqueryStatsCreate(WBMethod[V1GetNormQueryStatsResponse]):
    """Статистика по поисковым кластерам с детализацией по дням

    POST /adv/v1/normquery/stats
    """

    __path__ = "/adv/v1/normquery/stats"
    __http_method__ = "POST"
    __returns__ = V1GetNormQueryStatsResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (6000, 20),
        "service": (6000, 20),
        "basic_secret": (6000, 20),
        "basic": (1800000, 1),
    }
    __items__ = "items"
    __body_fields__ = {"from_": "from", "to": "to", "items": "items"}

    from_: str
    """Дата начала периода"""
    items: list[AdvV1NormqueryStatsCreateItemsItem]
    to: str
    """Дата окончания периода периода"""


class AdvV1Payments(WBMethod[list[AdvV1PaymentsResponseItem]]):
    """Получение истории пополнений счёта

    GET /adv/v1/payments
    """

    __path__ = "/adv/v1/payments"
    __http_method__ = "GET"
    __returns__ = list[AdvV1PaymentsResponseItem]
    __query_params__ = {"from_": "from", "to": "to"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 5),
        "service": (1000, 5),
        "basic_secret": (1000, 5),
        "basic": (3600000, 1),
    }

    from_: str | None = None
    """Начало интервала"""
    to: str | None = None
    """Конец интервала. (Минимальный интервал 1 день, максимальный 31)"""


class AdvV1PromotionCount(WBMethod[AdvV1PromotionCountResponse]):
    """Списки кампаний

    GET /adv/v1/promotion/count
    """

    __path__ = "/adv/v1/promotion/count"
    __http_method__ = "GET"
    __returns__ = AdvV1PromotionCountResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 5),
        "service": (200, 5),
        "basic_secret": (200, 5),
        "basic": (900000, 1),
    }


class AdvV1StatsCreate(WBMethod[list[StatInterval]]):
    """Статистика медиакампаний

    POST /adv/v1/stats
    """

    __path__ = "/adv/v1/stats"
    __http_method__ = "POST"
    __returns__ = list[StatInterval]
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-media-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (100, 10),
        "service": (100, 10),
        "basic_secret": (100, 10),
        "basic": (3600000, 1),
    }

    body: list[RequestWithDate] | list[Any] | dict[str, Any]


class AdvV1SupplierSubjects(WBMethod[list[AdvV1SupplierSubjectsResponseItem]]):
    """Предметы для кампаний

    GET /adv/v1/supplier/subjects
    """

    __path__ = "/adv/v1/supplier/subjects"
    __http_method__ = "GET"
    __returns__ = list[AdvV1SupplierSubjectsResponseItem]
    __query_params__ = {"payment_type": "payment_type"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (12000, 5),
        "service": (12000, 5),
        "basic_secret": (12000, 5),
        "basic": (1800000, 1),
    }

    payment_type: str | None = None
    """Тип оплаты: - `cpm` — за показы - `cpc` — за клик"""


class AdvV1Upd(WBMethod[list[AdvV1UpdResponseItem]]):
    """Получение истории затрат

    GET /adv/v1/upd
    """

    __path__ = "/adv/v1/upd"
    __http_method__ = "GET"
    __returns__ = list[AdvV1UpdResponseItem]
    __query_params__ = {"from_": "from", "to": "to"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 5),
        "service": (1000, 5),
        "basic_secret": (1000, 5),
        "basic": (3600000, 1),
    }

    from_: str
    """Начало интервала"""
    to: str
    """Конец интервала. (Минимальный интервал 1 день, максимальный 31)"""


class AdvV2SeacatSaveAdCreate(WBMethod[int]):
    """Создать кампанию

    POST /adv/v2/seacat/save-ad
    """

    __path__ = "/adv/v2/seacat/save-ad"
    __http_method__ = "POST"
    __returns__ = int
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (12000, 5),
        "service": (12000, 5),
        "basic_secret": (12000, 5),
        "basic": (720000, 1),
    }
    __body_fields__ = {
        "name": "name",
        "nms": "nms",
        "bid_type": "bid_type",
        "payment_type": "payment_type",
        "placement_types": "placement_types",
    }

    name: str
    """Название кампании"""
    bid_type: str | None = None
    """Тип ставки:   - `manual` — ручная   - `unified` — единая"""
    nms: list[int] | None = None
    """Карточки товаров для кампании. Доступные карточки товаров можно получить с помощью метода
    Карточки товаров для кампаний. Максимум 50 товаров (`nm`)
    """
    payment_type: str | None = None
    """Тип оплаты: - `cpm` — за показы - `cpc` — за клик. При создании с этим типом оплаты в
    кампании автоматически устанавливается минимальная ставка
    """
    placement_types: list[str] | None = None
    """Места размещения:   - `search` — в поиске   - `recommendations` — в рекомендациях  Укажите
    только для кампании с ручной ставкой
    """


class AdvV2SupplierNmsCreate(WBMethod[list[AdvV2SupplierNmsCreateResponseItem]]):
    """Карточки товаров для кампаний

    POST /adv/v2/supplier/nms
    """

    __path__ = "/adv/v2/supplier/nms"
    __http_method__ = "POST"
    __returns__ = list[AdvV2SupplierNmsCreateResponseItem]
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __sandbox_host__ = "https://advert-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (12000, 5),
        "service": (12000, 5),
        "basic_secret": (12000, 5),
        "basic": (1800000, 1),
    }

    body: list[int] | list[Any] | dict[str, Any]


class AdvV3Fullstats(WBMethod[list[FullStatsItem]]):
    """Статистика кампаний

    GET /adv/v3/fullstats
    """

    __path__ = "/adv/v3/fullstats"
    __http_method__ = "GET"
    __returns__ = list[FullStatsItem]
    __query_params__ = {"ids": "ids", "begin_date": "beginDate", "end_date": "endDate"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 1),
        "service": (20000, 1),
        "basic_secret": (20000, 1),
        "basic": (3600000, 1),
    }

    begin_date: str
    """Дата начала интервала"""
    end_date: str
    """Дата окончания интервала"""
    ids: str
    """ID кампаний, максимум 50 значений"""


class AdvertV0BidsRecommendations(WBMethod[V0BidsRecommendationsCpmResponse]):
    """Рекомендуемые ставки для карточек товаров и поисковых кластеров

    GET /api/advert/v0/bids/recommendations
    """

    __path__ = "/api/advert/v0/bids/recommendations"
    __http_method__ = "GET"
    __returns__ = V0BidsRecommendationsCpmResponse
    __query_params__ = {"nm_id": "nmId", "advert_id": "advertId"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (12000, 5),
        "service": (12000, 5),
        "basic_secret": (12000, 5),
        "basic": (180000, 1),
    }

    advert_id: int
    """ID кампании"""
    nm_id: int
    """Артикул WB"""


class AdvertV1BidsMinCreate(WBMethod[AdvertV1BidsMinCreateResponse]):
    """Минимальные ставки для карточек товаров

    POST /api/advert/v1/bids/min
    """

    __path__ = "/api/advert/v1/bids/min"
    __http_method__ = "POST"
    __returns__ = AdvertV1BidsMinCreateResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (720000, 1),
    }
    __body_fields__ = {
        "advert_id": "advert_id",
        "nm_ids": "nm_ids",
        "payment_type": "payment_type",
        "placement_types": "placement_types",
    }

    advert_id: int
    """ID кампании"""
    nm_ids: list[int]
    """Список артикулов WB"""
    payment_type: str
    """Тип оплаты:       - `cpm` — за показы       - `cpc` — за клик"""
    placement_types: list[str]
    """Места размещения:   - `search` — поиск   - `recommendation` — рекомендации   - `combined` —
    поиск и рекомендации
    """


class AdvertV1BidsUpdate(WBMethod[AdvertV1BidsUpdateResponse]):
    """Изменение ставок в кампаниях

    PATCH /api/advert/v1/bids
    """

    __path__ = "/api/advert/v1/bids"
    __http_method__ = "PATCH"
    __returns__ = AdvertV1BidsUpdateResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 5),
        "service": (200, 5),
        "basic_secret": (200, 5),
        "basic": (1800000, 1),
    }
    __body_fields__ = {"bids": "bids"}

    bids: list[AdvertV1BidsUpdateBidsItem]
    """Ставки в кампаниях"""


class AdvertV1Config(WBMethod[V2GetConfigResponse]):
    """Конфигурационные значения продвижения

    GET /api/advert/v1/config
    """

    __path__ = "/api/advert/v1/config"
    __http_method__ = "GET"
    __returns__ = V2GetConfigResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {"all": (60000, 10)}


class AdvertV1NormqueryBidsUpdate(WBMethod[V1SetNormQueryBidsResponse]):
    """Установить ставки для поисковых кластеров в валюте аккаунта продавца

    POST /api/advert/v1/normquery/bids
    """

    __path__ = "/api/advert/v1/normquery/bids"
    __http_method__ = "POST"
    __returns__ = V1SetNormQueryBidsResponse
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {"personal": (500, 4), "service": (500, 4)}
    __body_fields__ = {"bids": "bids"}

    bids: list[V1SetNormQueryBidsRequestItem]


class AdvertV2Adverts(WBMethod[GetAdverts]):
    """Информация о кампаниях

    GET /api/advert/v2/adverts
    """

    __path__ = "/api/advert/v2/adverts"
    __http_method__ = "GET"
    __returns__ = GetAdverts
    __query_params__ = {"ids": "ids", "statuses": "statuses", "payment_type": "payment_type"}
    __scope__ = Scope.PROMOTION
    __host__ = "https://advert-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 5),
        "service": (200, 5),
        "basic_secret": (200, 5),
        "basic": (3600000, 1),
    }

    ids: str | None = None
    """ID кампаний, максимум 50"""
    payment_type: str | None = None
    """Тип оплаты: - `cpm` — за показы - `cpc` — за клик"""
    statuses: str | None = None
    """Статусы кампаний: - `-1` — удалена, процесс удаления будет завершён в течение 10 минут - `4`
    — готова к запуску - `7` — завершена - `8` — отменена …
    """


class CalendarPromotions(WBMethod[None]):
    """Список акций

    GET /api/v1/calendar/promotions
    """

    __path__ = "/api/v1/calendar/promotions"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {
        "start_date_time": "startDateTime",
        "end_date_time": "endDateTime",
        "all_promo": "allPromo",
        "limit": "limit",
        "offset": "offset",
    }
    __scope__ = Scope.PRICES
    __host__ = "https://dp-calendar-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (3600000, 1),
    }
    __paginate__ = "offset_query"

    all_promo: bool
    """Показать акции:   - `false` — доступные для участия   - `true` — все акции"""
    end_date_time: str
    """Конец периода, формат `YYYY-MM-DDTHH:MM:SSZ`"""
    start_date_time: str
    """Начало периода, формат `YYYY-MM-DDTHH:MM:SSZ`"""
    limit: int | None = None
    """Количество запрашиваемых акций"""
    offset: int | None = None
    """После какого элемента выдавать данные"""


class CalendarPromotionsDetails(WBMethod[None]):
    """Детальная информация об акциях

    GET /api/v1/calendar/promotions/details
    """

    __path__ = "/api/v1/calendar/promotions/details"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"promotion_ids": "promotionIDs"}
    __scope__ = Scope.PRICES
    __host__ = "https://dp-calendar-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (3600000, 1),
    }

    promotion_ids: list[int]
    """ID акций, по которым нужно вернуть информацию"""


class CalendarPromotionsNomenclatures(WBMethod[None]):
    """Список товаров для участия в акции

    GET /api/v1/calendar/promotions/nomenclatures
    """

    __path__ = "/api/v1/calendar/promotions/nomenclatures"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {
        "promotion_id": "promotionID",
        "in_action": "inAction",
        "limit": "limit",
        "offset": "offset",
    }
    __scope__ = Scope.PRICES
    __host__ = "https://dp-calendar-api.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __paginate__ = "offset_query"

    in_action: bool
    """Участвует в акции:   - `true` — да   - `false` — нет"""
    promotion_id: int
    """ID акции"""
    limit: int | None = None
    """Количество запрашиваемых товаров"""
    offset: int | None = None
    """После какого элемента выдавать данные"""


class CalendarPromotionsUploadCreate(WBMethod[None]):
    """Добавить товар в акцию

    POST /api/v1/calendar/promotions/upload
    """

    __path__ = "/api/v1/calendar/promotions/upload"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PRICES
    __host__ = "https://dp-calendar-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (3600000, 1),
    }
