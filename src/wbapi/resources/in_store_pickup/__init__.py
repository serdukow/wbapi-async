from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    ClickCollectOrders,
    ClickCollectOrdersClient,
    ClickCollectOrdersClientIdentity,
    ClickCollectOrdersFinalPrice,
    ClickCollectOrdersMetaCustomsDeclarationUpdate,
    ClickCollectOrdersMetaDelete,
    ClickCollectOrdersMetaDetails,
    ClickCollectOrdersMetaGtinUpdate,
    ClickCollectOrdersMetaImeiUpdate,
    ClickCollectOrdersMetaSgtinUpdate,
    ClickCollectOrdersMetaUinUpdate,
    ClickCollectOrdersNew,
    ClickCollectOrdersStatusCancel,
    ClickCollectOrdersStatusConfirmUpdate,
    ClickCollectOrdersStatusInfo,
    ClickCollectOrdersStatusPrepareCreate,
    ClickCollectOrdersStatusReceiveCreate,
    ClickCollectOrdersStatusRejectCreate,
)
from .models import (
    ApiCheckedIdentity,
    ApiCustomsDeclarationSetResponse,
    ApiGTIN,
    ApiIMEI,
    ApiMetaDetailsResponse,
    ApiMetaSetResponses,
    ApiNewOrders,
    ApiOrderClientInfoResp,
    ApiOrders,
    ApiOrdersFinalPriceResponse,
    ApiOrdersMetaDetailsResponse,
    ApiOrdersResponses,
    ApiOrderStatusesV2,
    ApiSGTINs,
    ApiStatusSetResponses,
    ApiUIN,
    ClickCollectOrdersMetaCustomsDeclarationUpdateOrdersItem,
)


if TYPE_CHECKING:
    from ...client import WBApi


class InStorePickup:
    """Самовывоз.

    Управление сборочными заданиями и идентификаторами маркировки Самовывоза.

    Вы можете протестировать методы Самовывоза в песочнице. Также в песочнице доступны специальные
    методы для эмуляции действий пользователя
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def click_collect_orders(
        self, *, date_from: int, date_to: int, limit: int, next_: int, auto_paginate: bool = False
    ) -> ApiOrders | list[Any]:
        """Получить информацию о завершённых сборочных заданиях

        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param limit: Количество элементов в ответе
        :param next_: Параметр пагинации. Чтобы получить полный список данных, укажите `0` в первом запросе.
            Чтобы получить следующий пакет данных, используйте значение `next` из отв …
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = ClickCollectOrders(date_from=date_from, date_to=date_to, limit=limit, next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_click_collect_orders(
        self, *, date_from: int, date_to: int, limit: int, next_: int
    ) -> AsyncIterator[Any]:
        """Получить информацию о завершённых сборочных заданиях — постранично, по одной записи.

        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param limit: Количество элементов в ответе
        :param next_: Параметр пагинации. Чтобы получить полный список данных, укажите `0` в первом запросе.
            Чтобы получить следующий пакет данных, используйте значение `next` из отв …
        """
        async for item in ClickCollectOrders(
            date_from=date_from, date_to=date_to, limit=limit, next_=next_
        ).stream(self._api):
            yield item

    async def click_collect_orders_client(self, *, orders: list[int] | None = None) -> ApiOrderClientInfoResp:
        """Информация о покупателе

        :param orders: Список ID сборочных заданий
        """
        return await ClickCollectOrdersClient(orders=orders).emit(self._api)

    async def click_collect_orders_client_identity(
        self, *, order_code: str | None = None, passcode: str | None = None
    ) -> ApiCheckedIdentity:
        """Проверить, что заказ принадлежит покупателю

        :param order_code: Уникальный ID заказа покупателя
        :param passcode: Код подтверждения
        """
        return await ClickCollectOrdersClientIdentity(order_code=order_code, passcode=passcode).emit(
            self._api
        )

    async def click_collect_orders_final_price(
        self, *, orders: list[int] | None = None
    ) -> ApiOrdersFinalPriceResponse:
        """Получить цены продавца и суммы к оплате

        :param orders: Список ID сборочных заданий
        """
        return await ClickCollectOrdersFinalPrice(orders=orders).emit(self._api)

    async def click_collect_orders_meta_customs_declaration_update(
        self, *, orders: list[ClickCollectOrdersMetaCustomsDeclarationUpdateOrdersItem]
    ) -> ApiCustomsDeclarationSetResponse:
        """Закрепить номера ДТ за сборочными заданиями"""
        return await ClickCollectOrdersMetaCustomsDeclarationUpdate(orders=orders).emit(self._api)

    async def click_collect_orders_meta_delete(
        self, *, key: str, orders_ids: list[int]
    ) -> ApiOrdersResponses:
        """Удалить идентификаторы маркировки сборочных заданий

        :param key: Тип идентификаторов маркировки для удаления. Передаётся только одно значение
        :param orders_ids: Список ID сборочных заданий
        """
        return await ClickCollectOrdersMetaDelete(key=key, orders_ids=orders_ids).emit(self._api)

    async def click_collect_orders_meta_details(
        self, *, orders_ids: list[int]
    ) -> ApiOrdersMetaDetailsResponse:
        """Получить идентификаторы маркировки сборочных заданий

        :param orders_ids: Список ID сборочных заданий
        """
        return await ClickCollectOrdersMetaDetails(orders_ids=orders_ids).emit(self._api)

    async def click_collect_orders_meta_gtin_update(self, *, orders: list[ApiGTIN]) -> ApiMetaSetResponses:
        """Закрепить GTIN за сборочными заданиями"""
        return await ClickCollectOrdersMetaGtinUpdate(orders=orders).emit(self._api)

    async def click_collect_orders_meta_imei_update(self, *, orders: list[ApiIMEI]) -> ApiMetaSetResponses:
        """Закрепить IMEI за сборочными заданиями"""
        return await ClickCollectOrdersMetaImeiUpdate(orders=orders).emit(self._api)

    async def click_collect_orders_meta_sgtin_update(self, *, orders: list[ApiSGTINs]) -> ApiMetaSetResponses:
        """Закрепить коды маркировки Честного знака за сборочными заданиями"""
        return await ClickCollectOrdersMetaSgtinUpdate(orders=orders).emit(self._api)

    async def click_collect_orders_meta_uin_update(self, *, orders: list[ApiUIN]) -> ApiMetaSetResponses:
        """Закрепить УИН за сборочными заданиями"""
        return await ClickCollectOrdersMetaUinUpdate(orders=orders).emit(self._api)

    async def click_collect_orders_new(self) -> ApiNewOrders:
        """Получить список новых сборочных заданий"""
        return await ClickCollectOrdersNew().emit(self._api)

    async def click_collect_orders_status_cancel(self, *, orders_ids: list[int]) -> ApiStatusSetResponses:
        """Отменить сборочные задания

        :param orders_ids: Список ID сборочных заданий
        """
        return await ClickCollectOrdersStatusCancel(orders_ids=orders_ids).emit(self._api)

    async def click_collect_orders_status_confirm_update(
        self, *, orders_ids: list[int]
    ) -> ApiStatusSetResponses:
        """Перевести сборочные задания на сборку

        :param orders_ids: Список ID сборочных заданий
        """
        return await ClickCollectOrdersStatusConfirmUpdate(orders_ids=orders_ids).emit(self._api)

    async def click_collect_orders_status_info(self, *, orders_ids: list[int]) -> ApiOrderStatusesV2:
        """Получить статусы сборочных заданий

        :param orders_ids: Список ID сборочных заданий
        """
        return await ClickCollectOrdersStatusInfo(orders_ids=orders_ids).emit(self._api)

    async def click_collect_orders_status_prepare_create(
        self, *, orders_ids: list[int]
    ) -> ApiMetaDetailsResponse:
        """Сообщить, что сборочные задания готовы к выдаче

        :param orders_ids: Список ID сборочных заданий
        """
        return await ClickCollectOrdersStatusPrepareCreate(orders_ids=orders_ids).emit(self._api)

    async def click_collect_orders_status_receive_create(
        self, *, orders_ids: list[int]
    ) -> ApiStatusSetResponses:
        """Сообщить, что заказы приняты покупателями

        :param orders_ids: Список ID сборочных заданий
        """
        return await ClickCollectOrdersStatusReceiveCreate(orders_ids=orders_ids).emit(self._api)

    async def click_collect_orders_status_reject_create(
        self, *, orders_ids: list[int]
    ) -> ApiStatusSetResponses:
        """Сообщить об отказе от заказов

        :param orders_ids: Список ID сборочных заданий
        """
        return await ClickCollectOrdersStatusRejectCreate(orders_ids=orders_ids).emit(self._api)
