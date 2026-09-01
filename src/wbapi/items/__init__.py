# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    CreateBarcode,
    CreateCardsUpload,
    CreateCardsUploadAdd,
    CreateTag,
    CreateTagNomenclatureLink,
    CreateWarehouse,
    DeleteStock,
    DeleteTag,
    DeleteWarehouse,
    GetBrands,
    GetBufferGoodsTask,
    GetBufferTasks,
    GetCardsErrorList,
    GetCardsLimits,
    GetCardsList,
    GetCardsTrash,
    GetDbwWarehousesContacts,
    GetDirectoryColors,
    GetDirectoryCountries,
    GetDirectoryKinds,
    GetDirectorySeasons,
    GetDirectoryTnved,
    GetDirectoryVat,
    GetGoodsFilterGet,
    GetGoodsFilterPost,
    GetGoodsSizeNm,
    GetHistoryGoodsTask,
    GetHistoryTasks,
    GetObjectAll,
    GetObjectCharcs,
    GetObjectParentAll,
    GetOffices,
    GetQuarantineGoods,
    GetRecommendationsList,
    GetStocks,
    GetTags,
    GetWarehouses,
    SetDiscountsPricesUploadTaskB2bWholesale,
    SetRecommendation,
    SetUploadTask,
    SetUploadTaskClubDiscount,
    SetUploadTaskSize,
    UpdateCard,
    UpdateCardsDeleteTrash,
    UpdateCardsMoveNm,
    UpdateCardsRecover,
    UpdateDbwWarehousesContact,
    UpdateStock,
    UpdateTag,
    UpdateWarehouse,
    UploadMediaFile,
    UploadMediaSave,
)
from .models import (
    BrandsResponse,
    CreateBarcodeResponse,
    CreateCardsUploadAddCardsToAddItem,
    CreateWarehouseResponse,
    GetBufferGoodsTaskResponse,
    GetBufferTasksResponse,
    GetCardsLimitsResponse,
    GetCardsListResponse,
    GetCardsListSettings,
    GetCardsTrashResponse,
    GetCardsTrashSettings,
    GetDbwWarehousesContactsResponse,
    GetDirectoryColorsResponse,
    GetDirectoryCountriesResponse,
    GetDirectoryKindsResponse,
    GetDirectorySeasonsResponse,
    GetDirectoryTnvedResponse,
    GetDirectoryVatResponse,
    GetGoodsFilterResponse,
    GetGoodsSizeNmResponse,
    GetHistoryGoodsTaskResponse,
    GetHistoryTasksResponse,
    GetObjectAllResponse,
    GetObjectCharcsResponse,
    GetObjectParentAllResponse,
    GetQuarantineGoodsResponse,
    GetRecomRes,
    GetStocksResponse,
    GetTagsResponse,
    Office,
    ResponseContentError,
    ResponseItemList,
    ResponsePublicViewerPublicErrorsTableListV2,
    SetDiscountsPricesUploadTaskB2bWholesaleResponse,
    SetRecommendationRecListItem,
    SetRecomRes,
    SwaggerPublicErrorsCursorInput,
    SwaggerPublicErrorsOrderV2,
    TaskCreated,
    UpdateCardsDeleteTrashResponse,
    UpdateCardsRecoverResponse,
    UpdateDbwWarehousesContactContactsItem,
    UpdateStockStocksItem,
    UploadMediaFileResponse,
    UploadMediaSaveResponse,
    Warehouse,
)


if TYPE_CHECKING:
    from ..client import WBApi


class Items:
    """Работа с товарами.

    С помощью методов этого раздела вы можете:
      - создавать и редактировать карточки товаров
      - получать категории, предметы, характеристики и бренды товаров
      - загружать медиафайлы в карточки товаров
      - настраивать ярлыки для поиска товаров
      - работать с рекомендациями для товаров
      - устанавливать цены и скидки
      - управлять остатками товаров и складами, если вы работаете по модели продаж со склада продавца

    Вы можете протестировать методы работы с товарами в песочнице. Также в песочнице доступны
    специальные методы для управления карточками товаров

      Узнать, как использовать методы в бизнес-кейсах, можно в инструкции по работе с товарами
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def create_barcode(self, *, count: int | None = None) -> CreateBarcodeResponse:
        """Генерация баркодов

        :param count: Кол-во баркодов которые надо сгенерировать, максимальное доступное количество баркодов
            для генерации - `5 000`
        """
        return await CreateBarcode(count=count).emit(self._api)

    async def create_cards_upload(self, *, body: Any) -> ResponseItemList:
        """Создание карточек товаров"""
        return await CreateCardsUpload(body=body).emit(self._api)

    async def create_cards_upload_add(
        self,
        *,
        cards_to_add: list[CreateCardsUploadAddCardsToAddItem] | None = None,
        imt_id: int | None = None,
    ) -> ResponseItemList:
        """Создание карточек товаров с присоединением

        :param cards_to_add: Добавляемые карточки товаров
        :param imt_id: `imtID` отдельной карточки товара или группы объединённых карточек товаров, к которой
            присоединяются создаваемые карточки
        """
        return await CreateCardsUploadAdd(cards_to_add=cards_to_add, imt_id=imt_id).emit(self._api)

    async def create_tag(self, *, color: str | None = None, name: str | None = None) -> ResponseContentError:
        """Создание ярлыка

        :param color: Цвет ярлыка.  Доступные цвета:   - `D1CFD7` — серый   - `FEE0E0` — красный   -
            `ECDAFF` — фиолетовый   - `E4EAFF` — синий   - `DEF1DD` — зеленый …
        :param name: Имя ярлыка
        """
        return await CreateTag(color=color, name=name).emit(self._api)

    async def create_tag_nomenclature_link(
        self, *, nm_id: int | None = None, tags_ids: list[int] | None = None
    ) -> ResponseContentError:
        """Управление ярлыками в карточке товара

        :param nm_id: Артикул WB
        :param tags_ids: Массив числовых ID ярлыков. Что бы снять ярлыки с карточки товара, необходимо
            передать пустой массив. …
        """
        return await CreateTagNomenclatureLink(nm_id=nm_id, tags_ids=tags_ids).emit(self._api)

    async def create_warehouse(self, *, name: str, office_id: int) -> CreateWarehouseResponse:
        """Создать склад продавца

        :param name: Имя склада продавца
        :param office_id: ID склада WB.Нельзя привязывать склад WB, который уже используется
        """
        return await CreateWarehouse(name=name, office_id=office_id).emit(self._api)

    async def delete_stock(self, *, chrt_ids: list[int], warehouse_id: str | int) -> None:
        """Удалить остатки товаров

        :param chrt_ids: Массив ID размеров товаров
        :param warehouse_id: ID склада продавца
        """
        await DeleteStock(chrt_ids=chrt_ids, warehouse_id=warehouse_id).emit(self._api)

    async def delete_tag(self, *, id_: str | int) -> ResponseContentError:
        """Удаление ярлыка

        :param id_: Числовой ID ярлыка
        """
        return await DeleteTag(id_=id_).emit(self._api)

    async def delete_warehouse(self, *, warehouse_id: str | int) -> None:
        """Удалить склад продавца

        :param warehouse_id: ID склада продавца
        """
        await DeleteWarehouse(warehouse_id=warehouse_id).emit(self._api)

    async def get_brands(
        self, *, subject_id: int, next_: int | None = None, auto_paginate: bool = False
    ) -> BrandsResponse | list[Any]:
        """Бренды

        :param subject_id: ID предмета
        :param next_: Параметр пагинации. Используйте значение `next` из ответа, чтобы получить следующий
            пакет данных
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetBrands(subject_id=subject_id, next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_brands(self, *, subject_id: int, next_: int | None = None) -> AsyncIterator[Any]:
        """Бренды — постранично, по одной записи.

        :param subject_id: ID предмета
        :param next_: Параметр пагинации. Используйте значение `next` из ответа, чтобы получить следующий
            пакет данных
        """
        async for item in GetBrands(subject_id=subject_id, next_=next_).stream(self._api):
            yield item

    async def get_buffer_goods_task(
        self, *, limit: int, upload_id: int, offset: int | None = None, auto_paginate: bool = False
    ) -> GetBufferGoodsTaskResponse | list[Any]:
        """Детализация необработанной загрузки

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param upload_id: ID загрузки
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetBufferGoodsTask(limit=limit, upload_id=upload_id, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_buffer_goods_task(
        self, *, limit: int, upload_id: int, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Детализация необработанной загрузки — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param upload_id: ID загрузки
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in GetBufferGoodsTask(limit=limit, upload_id=upload_id, offset=offset).stream(
            self._api
        ):
            yield item

    async def get_buffer_tasks(self, *, upload_id: int) -> GetBufferTasksResponse:
        """Состояние необработанной загрузки

        :param upload_id: ID загрузки
        """
        return await GetBufferTasks(upload_id=upload_id).emit(self._api)

    async def get_cards_error_list(
        self,
        *,
        cursor: SwaggerPublicErrorsCursorInput | None = None,
        locale: str | None = None,
        order: SwaggerPublicErrorsOrderV2 | None = None,
        auto_paginate: bool = False,
    ) -> ResponsePublicViewerPublicErrorsTableListV2 | list[Any]:
        """Список несозданных карточек товаров с ошибками

        :param cursor: Пагинатор
        :param locale: Язык названий предметов:   - `ru` — русский   - `en` — английский   - `zh` —
            китайский  Не используется в песочнице
        :param order: Порядок выдачи пакетов
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetCardsErrorList(cursor=cursor, locale=locale, order=order)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_cards_error_list(
        self,
        *,
        cursor: SwaggerPublicErrorsCursorInput | None = None,
        locale: str | None = None,
        order: SwaggerPublicErrorsOrderV2 | None = None,
    ) -> AsyncIterator[Any]:
        """Список несозданных карточек товаров с ошибками — постранично, по одной записи.

        :param cursor: Пагинатор
        :param locale: Язык названий предметов:   - `ru` — русский   - `en` — английский   - `zh` —
            китайский  Не используется в песочнице
        :param order: Порядок выдачи пакетов
        """
        async for item in GetCardsErrorList(cursor=cursor, locale=locale, order=order).stream(self._api):
            yield item

    async def get_cards_limits(self) -> GetCardsLimitsResponse:
        """Лимиты карточек товаров"""
        return await GetCardsLimits().emit(self._api)

    async def get_cards_list(
        self,
        *,
        locale: str | None = None,
        settings: GetCardsListSettings | None = None,
        auto_paginate: bool = False,
    ) -> GetCardsListResponse | list[Any]:
        """Список карточек товаров

        :param locale: Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский …
        :param settings: Настройки
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetCardsList(locale=locale, settings=settings)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_cards_list(
        self, *, locale: str | None = None, settings: GetCardsListSettings | None = None
    ) -> AsyncIterator[Any]:
        """Список карточек товаров — постранично, по одной записи.

        :param locale: Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский …
        :param settings: Настройки
        """
        async for item in GetCardsList(locale=locale, settings=settings).stream(self._api):
            yield item

    async def get_cards_trash(
        self,
        *,
        locale: str | None = None,
        settings: GetCardsTrashSettings | None = None,
        auto_paginate: bool = False,
    ) -> GetCardsTrashResponse | list[Any]:
        """Список карточек товаров в корзине

        :param locale: Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский …
        :param settings: Настройки
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetCardsTrash(locale=locale, settings=settings)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_cards_trash(
        self, *, locale: str | None = None, settings: GetCardsTrashSettings | None = None
    ) -> AsyncIterator[Any]:
        """Список карточек товаров в корзине — постранично, по одной записи.

        :param locale: Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский …
        :param settings: Настройки
        """
        async for item in GetCardsTrash(locale=locale, settings=settings).stream(self._api):
            yield item

    async def get_dbw_warehouses_contacts(
        self, *, warehouse_id: str | int
    ) -> GetDbwWarehousesContactsResponse:
        """Список контактов

        :param warehouse_id: ID склада продавца
        """
        return await GetDbwWarehousesContacts(warehouse_id=warehouse_id).emit(self._api)

    async def get_directory_colors(self, *, locale: str | None = None) -> GetDirectoryColorsResponse:
        """Цвет

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await GetDirectoryColors(locale=locale).emit(self._api)

    async def get_directory_countries(self, *, locale: str | None = None) -> GetDirectoryCountriesResponse:
        """Страна производства

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await GetDirectoryCountries(locale=locale).emit(self._api)

    async def get_directory_kinds(self, *, locale: str | None = None) -> GetDirectoryKindsResponse:
        """Пол

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await GetDirectoryKinds(locale=locale).emit(self._api)

    async def get_directory_seasons(self, *, locale: str | None = None) -> GetDirectorySeasonsResponse:
        """Сезон

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await GetDirectorySeasons(locale=locale).emit(self._api)

    async def get_directory_tnved(
        self, *, subject_id: int, locale: str | None = None, search: int | None = None
    ) -> GetDirectoryTnvedResponse:
        """ТНВЭД-код

        :param subject_id: ID предмета
        :param locale: Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский …
        :param search: Поиск по ТНВЭД-коду. Работает только в паре с `subjectID`
        """
        return await GetDirectoryTnved(subject_id=subject_id, locale=locale, search=search).emit(self._api)

    async def get_directory_vat(self, *, locale: str | None = None) -> GetDirectoryVatResponse:
        """Ставка НДС

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await GetDirectoryVat(locale=locale).emit(self._api)

    async def get_goods_filter_get(
        self,
        *,
        limit: int,
        filter_nm_id: int | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> GetGoodsFilterResponse | list[Any]:
        """Получить товары с ценами

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param filter_nm_id: Артикул WB для поиска товара
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetGoodsFilterGet(limit=limit, filter_nm_id=filter_nm_id, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_goods_filter_get(
        self, *, limit: int, filter_nm_id: int | None = None, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Получить товары с ценами — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param filter_nm_id: Артикул WB для поиска товара
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in GetGoodsFilterGet(limit=limit, filter_nm_id=filter_nm_id, offset=offset).stream(
            self._api
        ):
            yield item

    async def get_goods_filter_post(self) -> GetGoodsFilterResponse:
        """Получить товары с ценами по артикулам"""
        return await GetGoodsFilterPost().emit(self._api)

    async def get_goods_size_nm(
        self, *, limit: int, nm_id: int, offset: int | None = None, auto_paginate: bool = False
    ) -> GetGoodsSizeNmResponse | list[Any]:
        """Получить размеры товара с ценами

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param nm_id: Артикул WB
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetGoodsSizeNm(limit=limit, nm_id=nm_id, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_goods_size_nm(
        self, *, limit: int, nm_id: int, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Получить размеры товара с ценами — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param nm_id: Артикул WB
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in GetGoodsSizeNm(limit=limit, nm_id=nm_id, offset=offset).stream(self._api):
            yield item

    async def get_history_goods_task(
        self, *, limit: int, upload_id: int, offset: int | None = None, auto_paginate: bool = False
    ) -> GetHistoryGoodsTaskResponse | list[Any]:
        """Детализация обработанной загрузки

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param upload_id: ID загрузки
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetHistoryGoodsTask(limit=limit, upload_id=upload_id, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_history_goods_task(
        self, *, limit: int, upload_id: int, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Детализация обработанной загрузки — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param upload_id: ID загрузки
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in GetHistoryGoodsTask(limit=limit, upload_id=upload_id, offset=offset).stream(
            self._api
        ):
            yield item

    async def get_history_tasks(self, *, upload_id: int) -> GetHistoryTasksResponse:
        """Состояние обработанной загрузки

        :param upload_id: ID загрузки
        """
        return await GetHistoryTasks(upload_id=upload_id).emit(self._api)

    async def get_object_all(
        self,
        *,
        limit: int | None = 30,
        locale: str | None = None,
        name: str | None = None,
        offset: int | None = 0,
        parent_id: int | None = None,
        auto_paginate: bool = False,
    ) -> GetObjectAllResponse | list[Any]:
        """Список предметов

        :param limit: Количество предметов, максимум 1000
        :param locale: Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский …
        :param name: Поиск по названию предмета (Носки), поиск работает по подстроке, искать можно на любом
            из поддерживаемых языков
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param parent_id: ID родительской категории предмета
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetObjectAll(limit=limit, locale=locale, name=name, offset=offset, parent_id=parent_id)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_object_all(
        self,
        *,
        limit: int | None = 30,
        locale: str | None = None,
        name: str | None = None,
        offset: int | None = 0,
        parent_id: int | None = None,
    ) -> AsyncIterator[Any]:
        """Список предметов — постранично, по одной записи.

        :param limit: Количество предметов, максимум 1000
        :param locale: Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский …
        :param name: Поиск по названию предмета (Носки), поиск работает по подстроке, искать можно на любом
            из поддерживаемых языков
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param parent_id: ID родительской категории предмета
        """
        async for item in GetObjectAll(
            limit=limit, locale=locale, name=name, offset=offset, parent_id=parent_id
        ).stream(self._api):
            yield item

    async def get_object_charcs(
        self, *, subject_id: str | int, locale: str | None = None
    ) -> GetObjectCharcsResponse:
        """Характеристики предмета

        :param subject_id: ID предмета
        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await GetObjectCharcs(subject_id=subject_id, locale=locale).emit(self._api)

    async def get_object_parent_all(self, *, locale: str | None = None) -> GetObjectParentAllResponse:
        """Родительские категории товаров

        :param locale: Язык поля ответа `name`:   - `ru` — русский   - `en` — английский   - `zh` —
            китайский …
        """
        return await GetObjectParentAll(locale=locale).emit(self._api)

    async def get_offices(self) -> list[Office]:
        """Получить список складов WB"""
        return await GetOffices().emit(self._api)

    async def get_quarantine_goods(
        self, *, limit: int, offset: int | None = None, auto_paginate: bool = False
    ) -> GetQuarantineGoodsResponse | list[Any]:
        """Получить товары в карантине

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetQuarantineGoods(limit=limit, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_quarantine_goods(self, *, limit: int, offset: int | None = None) -> AsyncIterator[Any]:
        """Получить товары в карантине — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in GetQuarantineGoods(limit=limit, offset=offset).stream(self._api):
            yield item

    async def get_recommendations_list(
        self,
        *,
        brand_names: list[str] | None = None,
        limit: int | None = 20,
        next_: int | None = 0,
        search: str | None = None,
        subject_ids: list[int] | None = None,
        auto_paginate: bool = False,
    ) -> GetRecomRes | list[Any]:
        """Список рекомендаций в карточках товаров

        :param brand_names: Бренды
        :param limit: Количество товаров в ответе
        :param next_: Курсор. Последний `nmId` в ответе
        :param search: Поиск:   - по артикулу WB `nmId` — полное совпадение   - по артикулу продавца
            `vendorCode` — частичное совпадение
        :param subject_ids: ID предметов
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetRecommendationsList(
            brand_names=brand_names, limit=limit, next_=next_, search=search, subject_ids=subject_ids
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_recommendations_list(
        self,
        *,
        brand_names: list[str] | None = None,
        limit: int | None = 20,
        next_: int | None = 0,
        search: str | None = None,
        subject_ids: list[int] | None = None,
    ) -> AsyncIterator[Any]:
        """Список рекомендаций в карточках товаров — постранично, по одной записи.

        :param brand_names: Бренды
        :param limit: Количество товаров в ответе
        :param next_: Курсор. Последний `nmId` в ответе
        :param search: Поиск:   - по артикулу WB `nmId` — полное совпадение   - по артикулу продавца
            `vendorCode` — частичное совпадение
        :param subject_ids: ID предметов
        """
        async for item in GetRecommendationsList(
            brand_names=brand_names, limit=limit, next_=next_, search=search, subject_ids=subject_ids
        ).stream(self._api):
            yield item

    async def get_stocks(self, *, chrt_ids: list[int], warehouse_id: str | int) -> GetStocksResponse:
        """Получить остатки товаров

        :param chrt_ids: Массив ID размеров товаров
        :param warehouse_id: ID склада продавца
        """
        return await GetStocks(chrt_ids=chrt_ids, warehouse_id=warehouse_id).emit(self._api)

    async def get_tags(self) -> GetTagsResponse:
        """Список ярлыков"""
        return await GetTags().emit(self._api)

    async def get_warehouses(self) -> list[Warehouse]:
        """Получить список складов продавца"""
        return await GetWarehouses().emit(self._api)

    async def set_discounts_prices_upload_task_b2b_wholesale(
        self,
    ) -> SetDiscountsPricesUploadTaskB2bWholesaleResponse:
        """Установить оптовые скидки для B2B-продаж"""
        return await SetDiscountsPricesUploadTaskB2bWholesale().emit(self._api)

    async def set_recommendation(
        self, *, rec_list: list[SetRecommendationRecListItem], replace: bool | None = False
    ) -> SetRecomRes:
        """Установить рекомендации для товаров

        :param rec_list: Список рекомендаций для товаров
        :param replace: Действие в запросе:   - `false` — добавить новые рекомендации к существующим   -
            `true` — заменить существующие рекомендации новыми
        """
        return await SetRecommendation(rec_list=rec_list, replace=replace).emit(self._api)

    async def set_upload_task(self) -> TaskCreated:
        """Установить цены и скидки"""
        return await SetUploadTask().emit(self._api)

    async def set_upload_task_club_discount(self) -> TaskCreated:
        """Установить скидки WB Клуба"""
        return await SetUploadTaskClubDiscount().emit(self._api)

    async def set_upload_task_size(self) -> TaskCreated:
        """Установить цены для размеров"""
        return await SetUploadTaskSize().emit(self._api)

    async def update_card(self, *, body: Any) -> ResponseItemList:
        """Редактирование карточек товаров"""
        return await UpdateCard(body=body).emit(self._api)

    async def update_cards_delete_trash(
        self, *, nm_ids: list[int] | None = None
    ) -> UpdateCardsDeleteTrashResponse:
        """Перенос карточек товаров в корзину

        :param nm_ids: Артикулы WB
        """
        return await UpdateCardsDeleteTrash(nm_ids=nm_ids).emit(self._api)

    async def update_cards_move_nm(self, *, body: Any) -> ResponseItemList:
        """Объединение и разъединение карточек товаров"""
        return await UpdateCardsMoveNm(body=body).emit(self._api)

    async def update_cards_recover(self, *, nm_ids: list[int] | None = None) -> UpdateCardsRecoverResponse:
        """Восстановление карточек товаров из корзины

        :param nm_ids: Артикулы WB
        """
        return await UpdateCardsRecover(nm_ids=nm_ids).emit(self._api)

    async def update_dbw_warehouses_contact(
        self, *, warehouse_id: str | int, contacts: list[UpdateDbwWarehousesContactContactsItem] | None = None
    ) -> None:
        """Обновить список контактов

        :param warehouse_id: ID склада продавца
        :param contacts: Не более 5 элементов
        """
        await UpdateDbwWarehousesContact(warehouse_id=warehouse_id, contacts=contacts).emit(self._api)

    async def update_stock(self, *, stocks: list[UpdateStockStocksItem], warehouse_id: str | int) -> None:
        """Обновить остатки товаров

        :param stocks: Массив ID размеров товаров и их остатков
        :param warehouse_id: ID склада продавца
        """
        await UpdateStock(stocks=stocks, warehouse_id=warehouse_id).emit(self._api)

    async def update_tag(
        self, *, id_: str | int, color: str | None = None, name: str | None = None
    ) -> ResponseContentError:
        """Изменение ярлыка

        :param id_: Числовой ID ярлыка
        :param color: Цвет ярлыка
        :param name: Имя ярлыка
        """
        return await UpdateTag(id_=id_, color=color, name=name).emit(self._api)

    async def update_warehouse(self, *, name: str, office_id: int, warehouse_id: str | int) -> None:
        """Обновить склад продавца

        :param name: Имя склада продавца
        :param office_id: ID склада WB.Нельзя привязывать склад WB, который уже используется.Можно менять не
            чаще одного раза в сутки
        :param warehouse_id: ID склада продавца
        """
        await UpdateWarehouse(name=name, office_id=office_id, warehouse_id=warehouse_id).emit(self._api)

    async def upload_media_file(self) -> UploadMediaFileResponse:
        """Загрузить медиафайл"""
        return await UploadMediaFile().emit(self._api)

    async def upload_media_save(
        self, *, data: list[str] | None = None, nm_id: int | None = None
    ) -> UploadMediaSaveResponse:
        """Загрузить медиафайлы по ссылкам

        :param data: Ссылки на изображения в том порядке, в котором они будут в карточке товара, и на видео,
            на любой позиции массива
        :param nm_id: Артикул WB
        """
        return await UploadMediaSave(data=data, nm_id=nm_id).emit(self._api)
