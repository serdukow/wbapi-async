# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    CancelOrder,
    CreatePasses,
    CreateSuppliesTrbx,
    CreateSupply,
    DeleteOrdersMeta,
    DeletePasses,
    DeleteSuppliesTrbx,
    DeleteSupply,
    GetOrders,
    GetOrdersArchive,
    GetOrdersClient,
    GetOrdersMeta,
    GetOrdersNew,
    GetOrdersStatus,
    GetOrdersStickers,
    GetPasses,
    GetPassesOffices,
    GetSettingsAutoreturns,
    GetSettingsAutoreturnsItems,
    GetSettingsAutoreturnsSubcategoriesRestricted,
    GetStatusHistory,
    GetStickersCrossBorder,
    GetSupplies,
    GetSuppliesBarcode,
    GetSuppliesById,
    GetSuppliesOrderIds,
    GetSuppliesOrdersReshipment,
    GetSuppliesTrbx,
    GetSuppliesTrbxStickers,
    SetMetaCustomsDeclaration,
    SetMetaExpiration,
    SetMetaGtin,
    SetMetaImei,
    SetMetaSgtin,
    SetMetaUin,
    UpdatePasses,
    UpdateSettingsAutoreturn,
    UpdateSettingsAutoreturnsItem,
    UpdateSuppliesDeliver,
    UpdateSuppliesOrder,
)
from .models import (
    CreatePassesResponse,
    CreateSuppliesTrbxResponse,
    CreateSupplyResponse,
    CrossborderTurkeyClientInfoResp,
    GetOrdersNewResponse,
    GetOrdersResponse,
    GetOrdersStatusResponse,
    GetOrdersStickersResponse,
    GetSettingsAutoreturnsItemsResponse,
    GetSettingsAutoreturnsResponse,
    GetSettingsAutoreturnsSubcategoriesRestrictedResponse,
    GetStatusHistoryResponse,
    GetStickersCrossBorderResponse,
    GetSuppliesBarcodeResponse,
    GetSuppliesOrdersReshipmentResponse,
    GetSuppliesResponse,
    GetSuppliesTrbxResponse,
    GetSuppliesTrbxStickersResponse,
    Pass,
    PassOffice,
    Supply,
    UpdateSettingsAutoreturnsItemResponse,
    V3ArchiveOrders,
    V3OrdersMetaAPI,
    V3SupplyOrderIDsAPI,
)


if TYPE_CHECKING:
    from ..client import WBApi


class OrdersFbs:
    """Заказы FBS.

    С помощью методов раздела Заказы FBS (Fulfillment by Seller) вы можете:
      - получать информацию о сборочных заданиях и их статусах, отменять сборочные задания, получать
      стикеры
      - добавлять, редактировать и удалять идентификаторы маркировки сборочных заданий
      - управлять поставками
      - создавать, редактировать и удалять пропуска на склады WB

    Вы можете протестировать методы заказов FBS в песочнице. Также в песочнице доступны специальные
    методы для эмуляции действий пользователя

      Узнать, как использовать методы в бизнес-кейсах, можно в инструкции по работе с заказами FBS

      Узнать больше о заказах FBS можно в справочном центре
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def cancel_order(self, *, order_id: str | int) -> None:
        """Отменить сборочное задание

        :param order_id: ID сборочного задания
        """
        await CancelOrder(order_id=order_id).emit(self._api)

    async def create_passes(
        self, *, car_model: str, car_number: str, first_name: str, last_name: str, office_id: int
    ) -> CreatePassesResponse:
        """Создать пропуск

        :param car_model: Марка машины
        :param car_number: Номер машины
        :param first_name: Имя водителя
        :param last_name: Фамилия водителя
        :param office_id: ID склада
        """
        return await CreatePasses(
            car_model=car_model,
            car_number=car_number,
            first_name=first_name,
            last_name=last_name,
            office_id=office_id,
        ).emit(self._api)

    async def create_supplies_trbx(self, *, amount: int, supply_id: str | int) -> CreateSuppliesTrbxResponse:
        """Добавить грузоместа к поставке

        :param amount: Количество грузомест, которые необходимо добавить к поставке
        :param supply_id: ID поставки
        """
        return await CreateSuppliesTrbx(amount=amount, supply_id=supply_id).emit(self._api)

    async def create_supply(self, *, name: str | None = None) -> CreateSupplyResponse:
        """Создать новую поставку

        :param name: Наименование поставки
        """
        return await CreateSupply(name=name).emit(self._api)

    async def delete_orders_meta(self, *, key: str, order_id: str | int) -> None:
        """Удалить идентификаторы маркировки сборочного задания

        :param key: Название идентификаторов маркировки для удаления. Передаётся только одно значение.
        :param order_id: ID сборочного задания
        """
        await DeleteOrdersMeta(key=key, order_id=order_id).emit(self._api)

    async def delete_passes(self, *, pass_id: str | int) -> None:
        """Удалить пропуск

        :param pass_id: ID пропуска
        """
        await DeletePasses(pass_id=pass_id).emit(self._api)

    async def delete_supplies_trbx(self, *, supply_id: str | int, trbx_ids: list[str]) -> None:
        """Удалить грузоместа из поставки

        :param supply_id: ID поставки
        :param trbx_ids: Список ID грузомест, которые необходимо удалить
        """
        await DeleteSuppliesTrbx(supply_id=supply_id, trbx_ids=trbx_ids).emit(self._api)

    async def delete_supply(self, *, supply_id: str | int) -> None:
        """Удалить поставку

        :param supply_id: ID поставки
        """
        await DeleteSupply(supply_id=supply_id).emit(self._api)

    async def get_orders(
        self,
        *,
        limit: int,
        next_: int,
        date_from: int | None = None,
        date_to: int | None = None,
        auto_paginate: bool = False,
    ) -> GetOrdersResponse | list[Any]:
        """Получить информацию о сборочных заданиях

        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param date_from: Дата начала периода в формате Unix timestamp. По умолчанию — дата за 30 дней до
            запроса. Часовой пояс — UTC
        :param date_to: Дата конца периода в формате Unix timestamp. Часовой пояс — UTC
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetOrders(limit=limit, next_=next_, date_from=date_from, date_to=date_to)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_orders(
        self, *, limit: int, next_: int, date_from: int | None = None, date_to: int | None = None
    ) -> AsyncIterator[Any]:
        """Получить информацию о сборочных заданиях — постранично, по одной записи.

        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param date_from: Дата начала периода в формате Unix timestamp. По умолчанию — дата за 30 дней до
            запроса. Часовой пояс — UTC
        :param date_to: Дата конца периода в формате Unix timestamp. Часовой пояс — UTC
        """
        async for item in GetOrders(limit=limit, next_=next_, date_from=date_from, date_to=date_to).stream(
            self._api
        ):
            yield item

    async def get_orders_archive(
        self, *, limit: int, month: int, next_: int, year: int, auto_paginate: bool = False
    ) -> V3ArchiveOrders | list[Any]:
        """Получить список архивных сборочных заданий

        :param limit: Количество сборочных заданий в ответе
        :param month: Месяц создания заказа
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param year: Год создания заказа
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetOrdersArchive(limit=limit, month=month, next_=next_, year=year)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_orders_archive(
        self, *, limit: int, month: int, next_: int, year: int
    ) -> AsyncIterator[Any]:
        """Получить список архивных сборочных заданий — постранично, по одной записи.

        :param limit: Количество сборочных заданий в ответе
        :param month: Месяц создания заказа
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param year: Год создания заказа
        """
        async for item in GetOrdersArchive(limit=limit, month=month, next_=next_, year=year).stream(
            self._api
        ):
            yield item

    async def get_orders_client(self, *, orders: list[int] | None = None) -> CrossborderTurkeyClientInfoResp:
        """Заказы с информацией по клиенту

        :param orders: Список заказов
        """
        return await GetOrdersClient(orders=orders).emit(self._api)

    async def get_orders_meta(self, *, orders: list[int]) -> V3OrdersMetaAPI:
        """Получить идентификаторы маркировки сборочных заданий

        :param orders: Не более 100 элементов
        """
        return await GetOrdersMeta(orders=orders).emit(self._api)

    async def get_orders_new(self) -> GetOrdersNewResponse:
        """Получить список новых сборочных заданий"""
        return await GetOrdersNew().emit(self._api)

    async def get_orders_status(self, *, orders: list[int]) -> GetOrdersStatusResponse:
        """Получить статусы сборочных заданий

        :param orders: Список ID сборочных заданий
        """
        return await GetOrdersStatus(orders=orders).emit(self._api)

    async def get_orders_stickers(
        self, *, height: int, type_: str, width: int, orders: list[int] | None = None
    ) -> GetOrdersStickersResponse:
        """Получить стикеры сборочных заданий

        :param height: Высота стикера
        :param type_: Тип стикера
        :param width: Ширина стикера
        :param orders: Список ID сборочных заданий
        """
        return await GetOrdersStickers(height=height, type_=type_, width=width, orders=orders).emit(self._api)

    async def get_passes(self) -> list[Pass]:
        """Получить список пропусков"""
        return await GetPasses().emit(self._api)

    async def get_passes_offices(self) -> list[PassOffice]:
        """Получить список складов, для которых требуется пропуск"""
        return await GetPassesOffices().emit(self._api)

    async def get_settings_autoreturns(self) -> GetSettingsAutoreturnsResponse:
        """Получить настройки автовозврата продавца"""
        return await GetSettingsAutoreturns().emit(self._api)

    async def get_settings_autoreturns_items(
        self, *, chrt_ids: list[int]
    ) -> GetSettingsAutoreturnsItemsResponse:
        """Получить настройки автовозврата товаров

        :param chrt_ids: Список ID размеров товаров в системе WB
        """
        return await GetSettingsAutoreturnsItems(chrt_ids=chrt_ids).emit(self._api)

    async def get_settings_autoreturns_subcategories_restricted(
        self, *, limit: int, next_: int, auto_paginate: bool = False
    ) -> GetSettingsAutoreturnsSubcategoriesRestrictedResponse | list[Any]:
        """Получить предметы, которые не хранятся на складах WB

        :param limit: Количество предметов в ответе
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetSettingsAutoreturnsSubcategoriesRestricted(limit=limit, next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_settings_autoreturns_subcategories_restricted(
        self, *, limit: int, next_: int
    ) -> AsyncIterator[Any]:
        """Получить предметы, которые не хранятся на складах WB — постранично, по одной записи.

        :param limit: Количество предметов в ответе
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        """
        async for item in GetSettingsAutoreturnsSubcategoriesRestricted(limit=limit, next_=next_).stream(
            self._api
        ):
            yield item

    async def get_status_history(self, *, orders: list[int] | None = None) -> GetStatusHistoryResponse:
        """История статусов для сборочных заданий трансграничных поставок

        :param orders: ID сборочных заданий
        """
        return await GetStatusHistory(orders=orders).emit(self._api)

    async def get_stickers_cross_border(
        self, *, orders: list[int] | None = None
    ) -> GetStickersCrossBorderResponse:
        """Получить стикеры сборочных заданий трансграничных поставок

        :param orders: Список ID сборочных заданий
        """
        return await GetStickersCrossBorder(orders=orders).emit(self._api)

    async def get_supplies(
        self, *, limit: int, next_: int, auto_paginate: bool = False
    ) -> GetSuppliesResponse | list[Any]:
        """Получить список поставок

        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetSupplies(limit=limit, next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_supplies(self, *, limit: int, next_: int) -> AsyncIterator[Any]:
        """Получить список поставок — постранично, по одной записи.

        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        """
        async for item in GetSupplies(limit=limit, next_=next_).stream(self._api):
            yield item

    async def get_supplies_barcode(self, *, supply_id: str | int, type_: str) -> GetSuppliesBarcodeResponse:
        """Получить QR-код поставки

        :param supply_id: ID поставки
        :param type_: Тип стикера
        """
        return await GetSuppliesBarcode(supply_id=supply_id, type_=type_).emit(self._api)

    async def get_supplies_by_id(self, *, supply_id: str | int) -> Supply:
        """Получить информацию о поставке

        :param supply_id: ID поставки
        """
        return await GetSuppliesById(supply_id=supply_id).emit(self._api)

    async def get_supplies_order_ids(self, *, supply_id: str | int) -> V3SupplyOrderIDsAPI:
        """Получить ID сборочных заданий поставки

        :param supply_id: ID поставки
        """
        return await GetSuppliesOrderIds(supply_id=supply_id).emit(self._api)

    async def get_supplies_orders_reshipment(self) -> GetSuppliesOrdersReshipmentResponse:
        """Получить все сборочные задания для повторной отгрузки"""
        return await GetSuppliesOrdersReshipment().emit(self._api)

    async def get_supplies_trbx(self, *, supply_id: str | int) -> GetSuppliesTrbxResponse:
        """Получить список грузомест поставки

        :param supply_id: ID поставки
        """
        return await GetSuppliesTrbx(supply_id=supply_id).emit(self._api)

    async def get_supplies_trbx_stickers(
        self, *, supply_id: str | int, trbx_ids: list[str], type_: str
    ) -> GetSuppliesTrbxStickersResponse:
        """Получить стикеры грузомест поставки

        :param supply_id: ID поставки
        :param trbx_ids: Список ID грузомест, по которым необходимо вернуть стикеры
        :param type_: Тип стикера
        """
        return await GetSuppliesTrbxStickers(supply_id=supply_id, trbx_ids=trbx_ids, type_=type_).emit(
            self._api
        )

    async def set_meta_customs_declaration(self, *, customs_declaration: str, order_id: str | int) -> None:
        """Закрепить номер ДТ за сборочным заданием

        :param customs_declaration: Номер ДТ
        :param order_id: ID сборочного задания
        """
        await SetMetaCustomsDeclaration(customs_declaration=customs_declaration, order_id=order_id).emit(
            self._api
        )

    async def set_meta_expiration(self, *, expiration: str, order_id: str | int) -> None:
        """Закрепить за сборочным заданием срок годности товара

        :param expiration: Дата, до которой годен товар. Не менее 30 дней с текущей даты
        :param order_id: ID сборочного задания
        """
        await SetMetaExpiration(expiration=expiration, order_id=order_id).emit(self._api)

    async def set_meta_gtin(self, *, gtin: str, order_id: str | int) -> None:
        """Закрепить GTIN за сборочным заданием

        :param gtin: GTIN
        :param order_id: ID сборочного задания
        """
        await SetMetaGtin(gtin=gtin, order_id=order_id).emit(self._api)

    async def set_meta_imei(self, *, imei: str, order_id: str | int) -> None:
        """Закрепить IMEI за сборочным заданием

        :param imei: IMEI
        :param order_id: ID сборочного задания
        """
        await SetMetaImei(imei=imei, order_id=order_id).emit(self._api)

    async def set_meta_sgtin(self, *, order_id: str | int, sgtins: list[str]) -> None:
        """Закрепить код маркировки Честного знака за сборочным заданием

        :param order_id: ID сборочного задания
        :param sgtins: Массив кодов маркировки Честного знака. Вы можете передать коды маркировки:   -
            полностью — с GS-разделителями и кодом проверки подлинности (криптохвостом) …
        """
        await SetMetaSgtin(order_id=order_id, sgtins=sgtins).emit(self._api)

    async def set_meta_uin(self, *, order_id: str | int, uin: str) -> None:
        """Закрепить УИН за сборочным заданием

        :param order_id: ID сборочного задания
        :param uin: УИН
        """
        await SetMetaUin(order_id=order_id, uin=uin).emit(self._api)

    async def update_passes(
        self,
        *,
        car_model: str,
        car_number: str,
        first_name: str,
        last_name: str,
        office_id: int,
        pass_id: str | int,
    ) -> None:
        """Обновить пропуск

        :param car_model: Марка машины
        :param car_number: Номер машины
        :param first_name: Имя водителя
        :param last_name: Фамилия водителя
        :param office_id: ID склада
        :param pass_id: ID пропуска
        """
        await UpdatePasses(
            car_model=car_model,
            car_number=car_number,
            first_name=first_name,
            last_name=last_name,
            office_id=office_id,
            pass_id=pass_id,
        ).emit(self._api)

    async def update_settings_autoreturn(self, *, type_: str) -> None:
        """Обновить настройки автовозврата продавца

        :param type_: Тип автовозврата малогабаритных товаров: …
        """
        await UpdateSettingsAutoreturn(type_=type_).emit(self._api)

    async def update_settings_autoreturns_item(
        self, *, chrt_ids: list[int], type_: str
    ) -> UpdateSettingsAutoreturnsItemResponse:
        """Обновить настройки автовозврата товаров

        :param chrt_ids: Список ID размеров товаров в системе WB
        :param type_: Тип автовозврата малогабаритных товаров:   - `byWarehouse` — все товары отправляются
            на склад WB …
        """
        return await UpdateSettingsAutoreturnsItem(chrt_ids=chrt_ids, type_=type_).emit(self._api)

    async def update_supplies_deliver(self, *, supply_id: str | int) -> None:
        """Передать поставку в доставку

        :param supply_id: ID поставки
        """
        await UpdateSuppliesDeliver(supply_id=supply_id).emit(self._api)

    async def update_supplies_order(self, *, supply_id: str | int, orders: list[int] | None = None) -> None:
        """Добавить сборочные задания к поставке

        :param supply_id: ID поставки
        :param orders: ID сборочных заданий
        """
        await UpdateSuppliesOrder(supply_id=supply_id, orders=orders).emit(self._api)
