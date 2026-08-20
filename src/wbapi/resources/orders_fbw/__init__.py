from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    AcceptanceOptionsCreate,
    Supplies,
    SuppliesId,
    SuppliesIdGoods,
    SuppliesIdPackage,
    TransitTariffs,
    Warehouses,
)
from .models import (
    ModelsBox,
    ModelsDateFilterRequest,
    ModelsGoodInSupply,
    ModelsOptionsResultModel,
    ModelsSupply,
    ModelsSupplyDetails,
    ModelsTransitTariff,
    ModelsWarehousesResultItems,
)


if TYPE_CHECKING:
    from ...client import WBApi


class OrdersFbw:
    """Поставки FBW.

    Узнать больше о поставках FBW можно в справочном центре

    В разделе описаны методы получения:
      - информации для формирования поставок
      - информации о поставках

    Вы можете создавать карточки товара в песочнице Контента, а потом использовать баркоды товаров в
    песочнице Поставок
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def acceptance_options_create(
        self, *, body: Any, warehouse_id: int | None = None
    ) -> ModelsOptionsResultModel:
        """Опции приёмки

        :param warehouse_id: ID склада.  Если параметр не указан, возвращаются данные по всем складам.
            **Максимум одно значение**
        """
        return await AcceptanceOptionsCreate(body=body, warehouse_id=warehouse_id).emit(self._api)

    async def supplies(
        self,
        *,
        dates: list[ModelsDateFilterRequest] | None = None,
        limit: int | None = None,
        offset: int | None = None,
        status_ids: list[int] | None = None,
        auto_paginate: bool = False,
    ) -> list[ModelsSupply] | list[Any]:
        """Список поставок

        :param dates: Фильтр по датам
        :param limit: Количество записей в ответе
        :param offset: После какого элемента выдавать данные
        :param status_ids: Фильтр поставок по статусам. Возможные значения:   - `1` — Не запланировано   -
            `2` — Запланировано   - `3` — Отгрузка разрешена   - `4` — Идёт приёмка …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = Supplies(dates=dates, limit=limit, offset=offset, status_ids=status_ids)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_supplies(
        self,
        *,
        dates: list[ModelsDateFilterRequest] | None = None,
        limit: int | None = None,
        offset: int | None = None,
        status_ids: list[int] | None = None,
    ) -> AsyncIterator[Any]:
        """Список поставок — постранично, по одной записи.

        :param dates: Фильтр по датам
        :param limit: Количество записей в ответе
        :param offset: После какого элемента выдавать данные
        :param status_ids: Фильтр поставок по статусам. Возможные значения:   - `1` — Не запланировано   -
            `2` — Запланировано   - `3` — Отгрузка разрешена   - `4` — Идёт приёмка …
        """
        async for item in Supplies(dates=dates, limit=limit, offset=offset, status_ids=status_ids).stream(
            self._api
        ):
            yield item

    async def supplies_id(self, *, id_: str | int, is_preorder_id: bool | None = None) -> ModelsSupplyDetails:
        """Детали поставки

        :param id_: ID поставки или заказа
        :param is_preorder_id: Поиск по:   - `true` — ID заказа, если в `ID` передаёте ID заказа   - `false`
            — ID поставки, если в `ID` передаёте ID поставки
        """
        return await SuppliesId(id_=id_, is_preorder_id=is_preorder_id).emit(self._api)

    async def supplies_id_goods(
        self,
        *,
        id_: str | int,
        is_preorder_id: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> list[ModelsGoodInSupply] | list[Any]:
        """Товары поставки

        :param id_: ID поставки или заказа
        :param is_preorder_id: Поиск по:   - `true` — ID заказа, если в `ID` передаёте ID заказа   - `false`
            — ID поставки, если в `ID` передаёте ID поставки
        :param limit: Количество записей в ответе
        :param offset: После какого элемента выдавать данные
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = SuppliesIdGoods(id_=id_, is_preorder_id=is_preorder_id, limit=limit, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_supplies_id_goods(
        self,
        *,
        id_: str | int,
        is_preorder_id: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> AsyncIterator[Any]:
        """Товары поставки — постранично, по одной записи.

        :param id_: ID поставки или заказа
        :param is_preorder_id: Поиск по:   - `true` — ID заказа, если в `ID` передаёте ID заказа   - `false`
            — ID поставки, если в `ID` передаёте ID поставки
        :param limit: Количество записей в ответе
        :param offset: После какого элемента выдавать данные
        """
        async for item in SuppliesIdGoods(
            id_=id_, is_preorder_id=is_preorder_id, limit=limit, offset=offset
        ).stream(self._api):
            yield item

    async def supplies_id_package(self, *, id_: str | int) -> list[ModelsBox]:
        """Упаковка поставки

        :param id_: ID поставки
        """
        return await SuppliesIdPackage(id_=id_).emit(self._api)

    async def transit_tariffs(self) -> list[ModelsTransitTariff]:
        """Транзитные направления"""
        return await TransitTariffs().emit(self._api)

    async def warehouses(self) -> list[ModelsWarehousesResultItems]:
        """Список складов"""
        return await Warehouses().emit(self._api)
