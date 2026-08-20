from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    Orders,
    OrdersClient,
    OrdersCourier,
    OrdersDeliveryDate,
    OrdersMetaDelete,
    OrdersMetaDetails,
    OrdersMetaSgtinUpdate,
    OrdersNew,
    OrdersOrderIdCancel,
    OrdersOrderIdConfirmUpdate,
    OrdersOrderIdMetaGtinUpdate,
    OrdersOrderIdMetaImeiUpdate,
    OrdersOrderIdMetaUinUpdate,
    OrdersStatus,
    OrdersStatusDeliverUpdate,
    OrdersStickers,
)
from .models import (
    ApiMetaDeleteResponses,
    ApiOrdersMetaDetailsResponse,
    ApiSGTINs,
    ApiStatusSetResponses,
    ClientInfoResp,
    DeliveryDatesInfoResp,
    OrderCourierInfoResp,
    OrdersNewResponse,
    OrdersResponse,
    OrdersStatusResponse,
    OrdersStickersResponse,
)


if TYPE_CHECKING:
    from ...client import WBApi


class OrdersDbw:
    """Заказы DBW.

    С помощью методов Заказы DBW (Доставка курьером WB) вы можете:
      - получать информацию о сборочных заданиях, управлять статусами и отменять сборочные задания
      - получать, добавлять, редактировать и удалять метаданные сборочных заданий

      Узнать, как использовать методы в бизнес-кейсах, можно в инструкции по работе с заказами DBW
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def orders(
        self, *, date_from: int, date_to: int, limit: int, next_: int, auto_paginate: bool = False
    ) -> OrdersResponse | list[Any]:
        """Получить информацию о завершенных сборочных заданиях

        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных
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
        :param limit: Параметр пагинации. Устанавливает предельное количество возвращаемых данных
        :param next_: Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет
            данных. Для получения полного списка данных должен быть равен `0` в первом …
        """
        async for item in Orders(date_from=date_from, date_to=date_to, limit=limit, next_=next_).stream(
            self._api
        ):
            yield item

    async def orders_client(self, *, orders: list[int] | None = None) -> ClientInfoResp:
        """Информация о покупателе

        :param orders: Список ID сборочных заданий
        """
        return await OrdersClient(orders=orders).emit(self._api)

    async def orders_courier(self, *, orders: list[int] | None = None) -> OrderCourierInfoResp:
        """Информация о курьере

        :param orders: Список ID сборочных заданий
        """
        return await OrdersCourier(orders=orders).emit(self._api)

    async def orders_delivery_date(self, *, orders: list[int] | None = None) -> DeliveryDatesInfoResp:
        """Получить дату и время доставки

        :param orders: Список ID сборочных заданий
        """
        return await OrdersDeliveryDate(orders=orders).emit(self._api)

    async def orders_meta_delete(self, *, key: str, orders_ids: list[int]) -> ApiMetaDeleteResponses:
        """Удалить идентификаторы маркировки сборочных заданий

        :param key: Название идентификатора маркировки для удаления. Передаётся только одно значение
        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersMetaDelete(key=key, orders_ids=orders_ids).emit(self._api)

    async def orders_meta_details(self, *, orders_ids: list[int]) -> ApiOrdersMetaDetailsResponse:
        """Получить идентификаторы маркировки сборочных заданий

        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersMetaDetails(orders_ids=orders_ids).emit(self._api)

    async def orders_meta_sgtin_update(self, *, orders: list[ApiSGTINs]) -> ApiStatusSetResponses:
        """Закрепить коды маркировки Честного знака за сборочными заданиями"""
        return await OrdersMetaSgtinUpdate(orders=orders).emit(self._api)

    async def orders_new(self) -> OrdersNewResponse:
        """Получить список новых сборочных заданий"""
        return await OrdersNew().emit(self._api)

    async def orders_order_id_cancel(self, *, order_id: str | int) -> None:
        """Отменить сборочное задание

        :param order_id: ID сборочного задания
        """
        await OrdersOrderIdCancel(order_id=order_id).emit(self._api)

    async def orders_order_id_confirm_update(self, *, order_id: str | int) -> None:
        """Перевести на сборку

        :param order_id: ID сборочного задания
        """
        await OrdersOrderIdConfirmUpdate(order_id=order_id).emit(self._api)

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

    async def orders_status_deliver_update(self, *, orders_ids: list[int]) -> ApiStatusSetResponses:
        """Перевести сборочные задания в доставку

        :param orders_ids: Список ID сборочных заданий
        """
        return await OrdersStatusDeliverUpdate(orders_ids=orders_ids).emit(self._api)

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
