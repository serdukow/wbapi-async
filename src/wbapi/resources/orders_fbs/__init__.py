from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    Orders,
    OrdersArchive,
    OrdersClientCreate,
    OrdersMeta,
    OrdersNew,
    OrdersOrderIdCancel,
    OrdersOrderIdMetaCustomsDeclarationUpdate,
    OrdersOrderIdMetaDelete,
    OrdersOrderIdMetaExpirationUpdate,
    OrdersOrderIdMetaGtinUpdate,
    OrdersOrderIdMetaImeiUpdate,
    OrdersOrderIdMetaSgtinUpdate,
    OrdersOrderIdMetaUinUpdate,
    OrdersStatus,
    OrdersStatusHistory,
    OrdersStickers,
    OrdersStickersCrossBorder,
    Passes,
    PassesCreate,
    PassesOffices,
    PassesPassIdDelete,
    PassesPassIdUpdate,
    SettingsAutoreturns,
    SettingsAutoreturnsItems,
    SettingsAutoreturnsItemsUpdate,
    SettingsAutoreturnsSubcategoriesRestricted,
    SettingsAutoreturnsUpdate,
    Supplies,
    SuppliesCreate,
    SuppliesOrdersReshipment,
    SuppliesSupplyId,
    SuppliesSupplyIdBarcode,
    SuppliesSupplyIdDelete,
    SuppliesSupplyIdDeliverUpdate,
    SuppliesSupplyIdOrderIds,
    SuppliesSupplyIdOrdersCreate,
    SuppliesSupplyIdTrbx,
    SuppliesSupplyIdTrbxCreate,
    SuppliesSupplyIdTrbxDelete,
    SuppliesSupplyIdTrbxStickers,
)
from .models import (
    CrossborderTurkeyClientInfoResp,
    OrdersNewResponse,
    OrdersResponse,
    OrdersStatusHistoryResponse,
    OrdersStatusResponse,
    OrdersStickersCrossBorderResponse,
    OrdersStickersResponse,
    Pass,
    PassesCreateResponse,
    PassOffice,
    SettingsAutoreturnsItemsResponse,
    SettingsAutoreturnsItemsUpdateResponse,
    SettingsAutoreturnsResponse,
    SettingsAutoreturnsSubcategoriesRestrictedResponse,
    SuppliesCreateResponse,
    SuppliesOrdersReshipmentResponse,
    SuppliesResponse,
    SuppliesSupplyIdBarcodeResponse,
    SuppliesSupplyIdTrbxCreateResponse,
    SuppliesSupplyIdTrbxResponse,
    SuppliesSupplyIdTrbxStickersResponse,
    Supply,
    V3ArchiveOrders,
    V3OrdersMetaAPI,
    V3SupplyOrderIDsAPI,
)


if TYPE_CHECKING:
    from ...client import WBApi


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

    async def orders(
        self,
        *,
        limit: int,
        next_: int,
        date_from: int | None = None,
        date_to: int | None = None,
        auto_paginate: bool = False,
    ) -> OrdersResponse | list[Any]:
        """Получить информацию о сборочных заданиях

        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param date_from: Дата начала периода в формате Unix timestamp. По умолчанию — дата за 30 дней до
            запроса. Часовой пояс — UTC
        :param date_to: Дата конца периода в формате Unix timestamp. Часовой пояс — UTC
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = Orders(limit=limit, next_=next_, date_from=date_from, date_to=date_to)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_orders(
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
        async for item in Orders(limit=limit, next_=next_, date_from=date_from, date_to=date_to).stream(
            self._api
        ):
            yield item

    async def orders_archive(
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
        call = OrdersArchive(limit=limit, month=month, next_=next_, year=year)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_orders_archive(
        self, *, limit: int, month: int, next_: int, year: int
    ) -> AsyncIterator[Any]:
        """Получить список архивных сборочных заданий — постранично, по одной записи.

        :param limit: Количество сборочных заданий в ответе
        :param month: Месяц создания заказа
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param year: Год создания заказа
        """
        async for item in OrdersArchive(limit=limit, month=month, next_=next_, year=year).stream(self._api):
            yield item

    async def orders_client_create(
        self, *, orders: list[int] | None = None
    ) -> CrossborderTurkeyClientInfoResp:
        """Заказы с информацией по клиенту

        :param orders: Список заказов
        """
        return await OrdersClientCreate(orders=orders).emit(self._api)

    async def orders_meta(self, *, orders: list[int]) -> V3OrdersMetaAPI:
        """Получить идентификаторы маркировки сборочных заданий"""
        return await OrdersMeta(orders=orders).emit(self._api)

    async def orders_new(self) -> OrdersNewResponse:
        """Получить список новых сборочных заданий"""
        return await OrdersNew().emit(self._api)

    async def orders_order_id_cancel(self, *, order_id: str | int) -> None:
        """Отменить сборочное задание

        :param order_id: ID сборочного задания
        """
        await OrdersOrderIdCancel(order_id=order_id).emit(self._api)

    async def orders_order_id_meta_customs_declaration_update(
        self, *, customs_declaration: str, order_id: str | int
    ) -> None:
        """Закрепить номер ДТ за сборочным заданием

        :param customs_declaration: Номер ДТ
        :param order_id: ID сборочного задания
        """
        await OrdersOrderIdMetaCustomsDeclarationUpdate(
            customs_declaration=customs_declaration, order_id=order_id
        ).emit(self._api)

    async def orders_order_id_meta_delete(self, *, key: str, order_id: str | int) -> None:
        """Удалить идентификаторы маркировки сборочного задания

        :param key: Название идентификаторов маркировки для удаления. Передаётся только одно значение.
        :param order_id: ID сборочного задания
        """
        await OrdersOrderIdMetaDelete(key=key, order_id=order_id).emit(self._api)

    async def orders_order_id_meta_expiration_update(self, *, expiration: str, order_id: str | int) -> None:
        """Закрепить за сборочным заданием срок годности товара

        :param expiration: Дата, до которой годен товар. Не менее 30 дней с текущей даты
        :param order_id: ID сборочного задания
        """
        await OrdersOrderIdMetaExpirationUpdate(expiration=expiration, order_id=order_id).emit(self._api)

    async def orders_order_id_meta_gtin_update(self, *, gtin: str, order_id: str | int) -> None:
        """Закрепить GTIN за сборочным заданием

        :param gtin: GTIN
        :param order_id: ID сборочного задания
        """
        await OrdersOrderIdMetaGtinUpdate(gtin=gtin, order_id=order_id).emit(self._api)

    async def orders_order_id_meta_imei_update(self, *, imei: str, order_id: str | int) -> None:
        """Закрепить IMEI за сборочным заданием

        :param imei: IMEI
        :param order_id: ID сборочного задания
        """
        await OrdersOrderIdMetaImeiUpdate(imei=imei, order_id=order_id).emit(self._api)

    async def orders_order_id_meta_sgtin_update(self, *, order_id: str | int, sgtins: list[str]) -> None:
        """Закрепить код маркировки Честного знака за сборочным заданием

        :param order_id: ID сборочного задания
        :param sgtins: Массив кодов маркировки Честного знака. Вы можете передать коды маркировки:   -
            полностью — с GS-разделителями и кодом проверки подлинности (криптохвостом) …
        """
        await OrdersOrderIdMetaSgtinUpdate(order_id=order_id, sgtins=sgtins).emit(self._api)

    async def orders_order_id_meta_uin_update(self, *, order_id: str | int, uin: str) -> None:
        """Закрепить УИН за сборочным заданием

        :param order_id: ID сборочного задания
        :param uin: УИН
        """
        await OrdersOrderIdMetaUinUpdate(order_id=order_id, uin=uin).emit(self._api)

    async def orders_status(self, *, orders: list[int]) -> OrdersStatusResponse:
        """Получить статусы сборочных заданий

        :param orders: Список ID сборочных заданий
        """
        return await OrdersStatus(orders=orders).emit(self._api)

    async def orders_status_history(self, *, orders: list[int] | None = None) -> OrdersStatusHistoryResponse:
        """История статусов для сборочных заданий трансграничных поставок

        :param orders: ID сборочных заданий
        """
        return await OrdersStatusHistory(orders=orders).emit(self._api)

    async def orders_stickers(
        self, *, height: int, type_: str, width: int, orders: list[int] | None = None
    ) -> OrdersStickersResponse:
        """Получить стикеры сборочных заданий

        :param height: Высота стикера
        :param type_: Тип стикера
        :param width: Ширина стикера
        :param orders: Список ID сборочных заданий
        """
        return await OrdersStickers(height=height, type_=type_, width=width, orders=orders).emit(self._api)

    async def orders_stickers_cross_border(
        self, *, orders: list[int] | None = None
    ) -> OrdersStickersCrossBorderResponse:
        """Получить стикеры сборочных заданий трансграничных поставок

        :param orders: Список ID сборочных заданий
        """
        return await OrdersStickersCrossBorder(orders=orders).emit(self._api)

    async def passes(self) -> list[Pass]:
        """Получить список пропусков"""
        return await Passes().emit(self._api)

    async def passes_create(
        self, *, car_model: str, car_number: str, first_name: str, last_name: str, office_id: int
    ) -> PassesCreateResponse:
        """Создать пропуск

        :param car_model: Марка машины
        :param car_number: Номер машины
        :param first_name: Имя водителя
        :param last_name: Фамилия водителя
        :param office_id: ID склада
        """
        return await PassesCreate(
            car_model=car_model,
            car_number=car_number,
            first_name=first_name,
            last_name=last_name,
            office_id=office_id,
        ).emit(self._api)

    async def passes_offices(self) -> list[PassOffice]:
        """Получить список складов, для которых требуется пропуск"""
        return await PassesOffices().emit(self._api)

    async def passes_pass_id_delete(self, *, pass_id: str | int) -> None:
        """Удалить пропуск

        :param pass_id: ID пропуска
        """
        await PassesPassIdDelete(pass_id=pass_id).emit(self._api)

    async def passes_pass_id_update(
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
        await PassesPassIdUpdate(
            car_model=car_model,
            car_number=car_number,
            first_name=first_name,
            last_name=last_name,
            office_id=office_id,
            pass_id=pass_id,
        ).emit(self._api)

    async def settings_autoreturns(self) -> SettingsAutoreturnsResponse:
        """Получить настройки автовозврата продавца"""
        return await SettingsAutoreturns().emit(self._api)

    async def settings_autoreturns_items(self, *, chrt_ids: list[int]) -> SettingsAutoreturnsItemsResponse:
        """Получить настройки автовозврата товаров

        :param chrt_ids: Список ID размеров товаров в системе WB
        """
        return await SettingsAutoreturnsItems(chrt_ids=chrt_ids).emit(self._api)

    async def settings_autoreturns_items_update(
        self, *, chrt_ids: list[int], type_: str
    ) -> SettingsAutoreturnsItemsUpdateResponse:
        """Обновить настройки автовозврата товаров

        :param chrt_ids: Список ID размеров товаров в системе WB
        :param type_: Тип автовозврата малогабаритных товаров:   - `byWarehouse` — все товары отправляются
            на склад WB …
        """
        return await SettingsAutoreturnsItemsUpdate(chrt_ids=chrt_ids, type_=type_).emit(self._api)

    async def settings_autoreturns_subcategories_restricted(
        self, *, limit: int, next_: int, auto_paginate: bool = False
    ) -> SettingsAutoreturnsSubcategoriesRestrictedResponse | list[Any]:
        """Получить предметы, которые не хранятся на складах WB

        :param limit: Количество предметов в ответе
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = SettingsAutoreturnsSubcategoriesRestricted(limit=limit, next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_settings_autoreturns_subcategories_restricted(
        self, *, limit: int, next_: int
    ) -> AsyncIterator[Any]:
        """Получить предметы, которые не хранятся на складах WB — постранично, по одной записи.

        :param limit: Количество предметов в ответе
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        """
        async for item in SettingsAutoreturnsSubcategoriesRestricted(limit=limit, next_=next_).stream(
            self._api
        ):
            yield item

    async def settings_autoreturns_update(self, *, type_: str) -> None:
        """Обновить настройки автовозврата продавца

        :param type_: Тип автовозврата малогабаритных товаров: …
        """
        await SettingsAutoreturnsUpdate(type_=type_).emit(self._api)

    async def supplies(
        self, *, limit: int, next_: int, auto_paginate: bool = False
    ) -> SuppliesResponse | list[Any]:
        """Получить список поставок

        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = Supplies(limit=limit, next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_supplies(self, *, limit: int, next_: int) -> AsyncIterator[Any]:
        """Получить список поставок — постранично, по одной записи.

        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        """
        async for item in Supplies(limit=limit, next_=next_).stream(self._api):
            yield item

    async def supplies_create(self, *, name: str | None = None) -> SuppliesCreateResponse:
        """Создать новую поставку

        :param name: Наименование поставки
        """
        return await SuppliesCreate(name=name).emit(self._api)

    async def supplies_orders_reshipment(self) -> SuppliesOrdersReshipmentResponse:
        """Получить все сборочные задания для повторной отгрузки"""
        return await SuppliesOrdersReshipment().emit(self._api)

    async def supplies_supply_id(self, *, supply_id: str | int) -> Supply:
        """Получить информацию о поставке

        :param supply_id: ID поставки
        """
        return await SuppliesSupplyId(supply_id=supply_id).emit(self._api)

    async def supplies_supply_id_barcode(
        self, *, supply_id: str | int, type_: str
    ) -> SuppliesSupplyIdBarcodeResponse:
        """Получить QR-код поставки

        :param supply_id: ID поставки
        :param type_: Тип стикера
        """
        return await SuppliesSupplyIdBarcode(supply_id=supply_id, type_=type_).emit(self._api)

    async def supplies_supply_id_delete(self, *, supply_id: str | int) -> None:
        """Удалить поставку

        :param supply_id: ID поставки
        """
        await SuppliesSupplyIdDelete(supply_id=supply_id).emit(self._api)

    async def supplies_supply_id_deliver_update(self, *, supply_id: str | int) -> None:
        """Передать поставку в доставку

        :param supply_id: ID поставки
        """
        await SuppliesSupplyIdDeliverUpdate(supply_id=supply_id).emit(self._api)

    async def supplies_supply_id_order_ids(self, *, supply_id: str | int) -> V3SupplyOrderIDsAPI:
        """Получить ID сборочных заданий поставки

        :param supply_id: ID поставки
        """
        return await SuppliesSupplyIdOrderIds(supply_id=supply_id).emit(self._api)

    async def supplies_supply_id_orders_create(
        self, *, supply_id: str | int, orders: list[int] | None = None
    ) -> None:
        """Добавить сборочные задания к поставке

        :param supply_id: ID поставки
        :param orders: ID сборочных заданий
        """
        await SuppliesSupplyIdOrdersCreate(supply_id=supply_id, orders=orders).emit(self._api)

    async def supplies_supply_id_trbx(self, *, supply_id: str | int) -> SuppliesSupplyIdTrbxResponse:
        """Получить список грузомест поставки

        :param supply_id: ID поставки
        """
        return await SuppliesSupplyIdTrbx(supply_id=supply_id).emit(self._api)

    async def supplies_supply_id_trbx_create(
        self, *, amount: int, supply_id: str | int
    ) -> SuppliesSupplyIdTrbxCreateResponse:
        """Добавить грузоместа к поставке

        :param amount: Количество грузомест, которые необходимо добавить к поставке
        :param supply_id: ID поставки
        """
        return await SuppliesSupplyIdTrbxCreate(amount=amount, supply_id=supply_id).emit(self._api)

    async def supplies_supply_id_trbx_delete(self, *, supply_id: str | int, trbx_ids: list[str]) -> None:
        """Удалить грузоместа из поставки

        :param supply_id: ID поставки
        :param trbx_ids: Список ID грузомест, которые необходимо удалить
        """
        await SuppliesSupplyIdTrbxDelete(supply_id=supply_id, trbx_ids=trbx_ids).emit(self._api)

    async def supplies_supply_id_trbx_stickers(
        self, *, supply_id: str | int, trbx_ids: list[str], type_: str
    ) -> SuppliesSupplyIdTrbxStickersResponse:
        """Получить стикеры грузомест поставки

        :param supply_id: ID поставки
        :param trbx_ids: Список ID грузомест, по которым необходимо вернуть стикеры
        :param type_: Тип стикера
        """
        return await SuppliesSupplyIdTrbxStickers(supply_id=supply_id, trbx_ids=trbx_ids, type_=type_).emit(
            self._api
        )
