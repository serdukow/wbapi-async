from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    GroupsInfo,
    Orders,
    OrdersB2bInfo,
    OrdersClient,
    OrdersDeliveryDate,
    OrdersFinalPrice,
    OrdersMetaCustomsDeclarationUpdate,
    OrdersMetaDelete,
    OrdersMetaDetails,
    OrdersMetaGtinUpdate,
    OrdersMetaImeiUpdate,
    OrdersMetaSgtinUpdate,
    OrdersMetaUinUpdate,
    OrdersNew,
    OrdersStatusCancel,
    OrdersStatusConfirmUpdate,
    OrdersStatusDeliverUpdate,
    OrdersStatusInfo,
    OrdersStatusReceiveCreate,
    OrdersStatusRejectCreate,
    OrdersStickers,
)
from .models import (
    ApiB2bClientInfoResponses,
    ApiGTIN,
    ApiIMEI,
    ApiOrderCodeRequest,
    ApiOrdersFinalPriceResponse,
    ApiOrdersMetaDetailsResponse,
    ApiOrderStatusesV2,
    ApiSGTINs,
    ApiStatusSetDeliverResponses,
    ApiStatusSetResponses,
    ApiUIN,
    DbsOnlyClientInfoResp,
    DeliveryDatesInfoResp,
    GroupsInfoResponseItem,
    OrdersMetaCustomsDeclarationUpdateOrdersItem,
    OrdersNewResponse,
    OrdersResponse,
    OrdersStatusReceiveCreateResponse,
    OrdersStickersResponse,
)


if TYPE_CHECKING:
    from ...client import WBApi


class OrdersDbs:
    """DBS.

    Узнать больше о модели DBS можно в справочном центре

    Управление сборочными заданиями и идентификаторами маркировки DBS (Delivery by Seller).

    Вы можете протестировать методы DBS в песочнице. Также в песочнице доступны специальные методы для
    эмуляции действий пользователя
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def groups_info(self, *, groups: list[str] | None = None) -> list[GroupsInfoResponseItem]:
        """Получить информацию о платной доставке

        :param groups: Список значений `groupId`. Можно получить из новых и завершенных сборочных заданий
        """
        return await GroupsInfo(groups=groups).emit(self._api)

    async def orders(
        self, *, date_from: int, date_to: int, limit: int, next_: int, auto_paginate: bool = False
    ) -> OrdersResponse | list[Any]:
        """Получить информацию о завершенных сборочных заданиях

        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = Orders(date_from=date_from, date_to=date_to, limit=limit, next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_orders(
        self, *, date_from: int, date_to: int, limit: int, next_: int
    ) -> AsyncIterator[Any]:
        """Получить информацию о завершенных сборочных заданиях — постранично, по одной записи.

        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных.
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        """
        async for item in Orders(date_from=date_from, date_to=date_to, limit=limit, next_=next_).stream(
            self._api
        ):
            yield item

    async def orders_b2b_info(self, *, orders_ids: list[int]) -> ApiB2bClientInfoResponses:
        """Информация о покупателе B2B

        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersB2bInfo(orders_ids=orders_ids).emit(self._api)

    async def orders_client(self, *, orders: list[int] | None = None) -> DbsOnlyClientInfoResp:
        """Информация о покупателе

        :param orders: Список ID сборочных заданий
        """
        return await OrdersClient(orders=orders).emit(self._api)

    async def orders_delivery_date(self, *, orders: list[int] | None = None) -> DeliveryDatesInfoResp:
        """Получить дату и время доставки

        :param orders: Список ID сборочных заданий
        """
        return await OrdersDeliveryDate(orders=orders).emit(self._api)

    async def orders_final_price(self, *, orders: list[int] | None = None) -> ApiOrdersFinalPriceResponse:
        """Получить цены продавца и суммы к оплате

        :param orders: Список ID сборочных заданий
        """
        return await OrdersFinalPrice(orders=orders).emit(self._api)

    async def orders_meta_customs_declaration_update(
        self, *, orders: list[OrdersMetaCustomsDeclarationUpdateOrdersItem]
    ) -> ApiStatusSetResponses:
        """Закрепить номера ДТ за сборочными заданиями"""
        return await OrdersMetaCustomsDeclarationUpdate(orders=orders).emit(self._api)

    async def orders_meta_delete(self, *, key: str, order_ids: list[int]) -> ApiStatusSetResponses:
        """Удалить идентификаторы маркировки сборочных заданий

        :param key: Название идентификатора маркировки для удаления. Передаётся только одно значение
        :param order_ids: Список ID сборочных заданий
        """
        return await OrdersMetaDelete(key=key, order_ids=order_ids).emit(self._api)

    async def orders_meta_details(self, *, orders_ids: list[int]) -> ApiOrdersMetaDetailsResponse:
        """Получить идентификаторы маркировки сборочных заданий

        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersMetaDetails(orders_ids=orders_ids).emit(self._api)

    async def orders_meta_gtin_update(self, *, orders: list[ApiGTIN]) -> ApiStatusSetResponses:
        """Закрепить GTIN за сборочными заданиями"""
        return await OrdersMetaGtinUpdate(orders=orders).emit(self._api)

    async def orders_meta_imei_update(self, *, orders: list[ApiIMEI]) -> ApiStatusSetResponses:
        """Закрепить IMEI за сборочными заданиями"""
        return await OrdersMetaImeiUpdate(orders=orders).emit(self._api)

    async def orders_meta_sgtin_update(self, *, orders: list[ApiSGTINs]) -> ApiStatusSetResponses:
        """Закрепить коды маркировки Честного знака за сборочными заданиями"""
        return await OrdersMetaSgtinUpdate(orders=orders).emit(self._api)

    async def orders_meta_uin_update(self, *, orders: list[ApiUIN]) -> ApiStatusSetResponses:
        """Закрепить УИН за сборочными заданиями"""
        return await OrdersMetaUinUpdate(orders=orders).emit(self._api)

    async def orders_new(self) -> OrdersNewResponse:
        """Получить список новых сборочных заданий"""
        return await OrdersNew().emit(self._api)

    async def orders_status_cancel(self, *, orders_ids: list[int]) -> ApiStatusSetResponses:
        """Отменить сборочные задания

        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersStatusCancel(orders_ids=orders_ids).emit(self._api)

    async def orders_status_confirm_update(self, *, orders_ids: list[int]) -> ApiStatusSetResponses:
        """Перевести сборочные задания на сборку

        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersStatusConfirmUpdate(orders_ids=orders_ids).emit(self._api)

    async def orders_status_deliver_update(self, *, orders_ids: list[int]) -> ApiStatusSetDeliverResponses:
        """Перевести сборочные задания в доставку

        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersStatusDeliverUpdate(orders_ids=orders_ids).emit(self._api)

    async def orders_status_info(self, *, orders_ids: list[int]) -> ApiOrderStatusesV2:
        """Получить статусы сборочных заданий

        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersStatusInfo(orders_ids=orders_ids).emit(self._api)

    async def orders_status_receive_create(
        self, *, orders: list[ApiOrderCodeRequest]
    ) -> OrdersStatusReceiveCreateResponse:
        """Сообщить о получении заказов"""
        return await OrdersStatusReceiveCreate(orders=orders).emit(self._api)

    async def orders_status_reject_create(
        self, *, orders: list[ApiOrderCodeRequest]
    ) -> ApiStatusSetResponses:
        """Сообщить об отказе от заказов"""
        return await OrdersStatusRejectCreate(orders=orders).emit(self._api)

    async def orders_stickers(
        self, *, height: int, orders: list[int], type_: str, width: int
    ) -> OrdersStickersResponse:
        """Получить стикеры для сборочных заданий с доставкой в ПВЗ

        :param height: Высота стикера
        :param orders: Список ID сборочных заданий
        :param type_: Формат стикера
        :param width: Ширина стикера
        """
        return await OrdersStickers(height=height, orders=orders, type_=type_, width=width).emit(self._api)
