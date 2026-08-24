from __future__ import annotations

from typing import Any

from ..client.method import WBMethod
from ..utils.token import Scope
from .models import (
    ModelsBox,
    ModelsDateFilterRequest,
    ModelsGood,
    ModelsGoodInSupply,
    ModelsOptionsResultModel,
    ModelsSupply,
    ModelsSupplyDetails,
    ModelsTransitTariff,
    ModelsWarehousesResultItems,
)


class CreateAcceptanceOption(WBMethod[ModelsOptionsResultModel]):
    """Опции приёмки

    POST /api/v1/acceptance/options
    """

    __path__ = "/api/v1/acceptance/options"
    __http_method__ = "POST"
    __returns__ = ModelsOptionsResultModel
    __query_params__ = {"warehouse_id": "warehouseID"}
    __scope__ = Scope.SUPPLIES
    __host__ = "https://supplies-api.wildberries.ru"
    __sandbox_host__ = "https://supplies-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 6),
        "service": (60000, 6),
        "basic_secret": (60000, 6),
        "basic": (1800000, 1),
    }
    __items__ = "result"

    body: list[ModelsGood] | list[Any] | dict[str, Any]
    warehouse_id: int | None = None
    """ID склада.  Если параметр не указан, возвращаются данные по всем складам. **Максимум одно
    значение**
    """


class GetSupplies(WBMethod[list[ModelsSupply]]):
    """Список поставок

    POST /api/v1/supplies
    """

    __path__ = "/api/v1/supplies"
    __http_method__ = "POST"
    __returns__ = list[ModelsSupply]
    __query_params__ = {"limit": "limit", "offset": "offset"}
    __scope__ = Scope.SUPPLIES
    __host__ = "https://supplies-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 10),
        "service": (20000, 10),
        "basic_secret": (20000, 10),
        "basic": (1800000, 1),
    }
    __paginate__ = "offset_query"
    __body_fields__ = {"dates": "dates", "status_ids": "statusIDs"}

    dates: list[ModelsDateFilterRequest] | None = None
    """Фильтр по датам"""
    limit: int | None = 1000
    """Количество записей в ответе"""
    offset: int | None = 0
    """После какого элемента выдавать данные"""
    status_ids: list[int] | None = None
    """Фильтр поставок по статусам. Возможные значения:   - `1` — Не запланировано   - `2` —
    Запланировано   - `3` — Отгрузка разрешена   - `4` — Идёт приёмка …
    """


class GetSuppliesById(WBMethod[ModelsSupplyDetails]):
    """Детали поставки

    GET /api/v1/supplies/{ID}
    """

    __path__ = "/api/v1/supplies/{ID}"
    __http_method__ = "GET"
    __returns__ = ModelsSupplyDetails
    __path_params__ = ("ID",)
    __query_params__ = {"is_preorder_id": "isPreorderID"}
    __scope__ = Scope.SUPPLIES
    __host__ = "https://supplies-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 10),
        "service": (20000, 10),
        "basic_secret": (20000, 10),
        "basic": (1800000, 1),
    }

    id_: str | int
    """ID поставки или заказа"""
    is_preorder_id: bool | None = False
    """Поиск по:   - `true` — ID заказа, если в `ID` передаёте ID заказа   - `false` — ID поставки,
    если в `ID` передаёте ID поставки
    """


class GetSuppliesGoods(WBMethod[list[ModelsGoodInSupply]]):
    """Товары поставки

    GET /api/v1/supplies/{ID}/goods
    """

    __path__ = "/api/v1/supplies/{ID}/goods"
    __http_method__ = "GET"
    __returns__ = list[ModelsGoodInSupply]
    __path_params__ = ("ID",)
    __query_params__ = {"limit": "limit", "offset": "offset", "is_preorder_id": "isPreorderID"}
    __scope__ = Scope.SUPPLIES
    __host__ = "https://supplies-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 10),
        "service": (20000, 10),
        "basic_secret": (20000, 10),
        "basic": (1800000, 1),
    }
    __paginate__ = "offset_query"

    id_: str | int
    """ID поставки или заказа"""
    is_preorder_id: bool | None = False
    """Поиск по:   - `true` — ID заказа, если в `ID` передаёте ID заказа   - `false` — ID поставки,
    если в `ID` передаёте ID поставки
    """
    limit: int | None = 100
    """Количество записей в ответе"""
    offset: int | None = 0
    """После какого элемента выдавать данные"""


class GetSuppliesPackage(WBMethod[list[ModelsBox]]):
    """Упаковка поставки

    GET /api/v1/supplies/{ID}/package
    """

    __path__ = "/api/v1/supplies/{ID}/package"
    __http_method__ = "GET"
    __returns__ = list[ModelsBox]
    __path_params__ = ("ID",)
    __scope__ = Scope.SUPPLIES
    __host__ = "https://supplies-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 10),
        "service": (20000, 10),
        "basic_secret": (20000, 10),
        "basic": (1800000, 1),
    }

    id_: str | int
    """ID поставки"""


class GetTransitTariffs(WBMethod[list[ModelsTransitTariff]]):
    """Транзитные направления

    GET /api/v1/transit-tariffs
    """

    __path__ = "/api/v1/transit-tariffs"
    __http_method__ = "GET"
    __returns__ = list[ModelsTransitTariff]
    __scope__ = Scope.SUPPLIES
    __host__ = "https://supplies-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (100000, 10),
        "service": (100000, 10),
        "basic_secret": (100000, 10),
        "basic": (43200000, 1),
    }


class GetWarehouses(WBMethod[list[ModelsWarehousesResultItems]]):
    """Список складов

    GET /api/v1/warehouses
    """

    __path__ = "/api/v1/warehouses"
    __http_method__ = "GET"
    __returns__ = list[ModelsWarehousesResultItems]
    __scope__ = Scope.SUPPLIES
    __host__ = "https://supplies-api.wildberries.ru"
    __sandbox_host__ = "https://supplies-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (60000, 6),
        "service": (60000, 6),
        "basic_secret": (60000, 6),
        "basic": (43200000, 1),
    }
