from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    BufferGoodsTask,
    BufferTasks,
    ContentV1Brands,
    ContentV1RecommendationsList,
    ContentV1RecommendationsSetUpdate,
    ContentV2BarcodesCreate,
    ContentV2CardsDeleteTrashCreate,
    ContentV2CardsErrorList,
    ContentV2CardsLimits,
    ContentV2CardsMoveNmCreate,
    ContentV2CardsRecoverCreate,
    ContentV2CardsUpdateCreate,
    ContentV2CardsUploadAddCreate,
    ContentV2CardsUploadCreate,
    ContentV2DirectoryColors,
    ContentV2DirectoryCountries,
    ContentV2DirectoryKinds,
    ContentV2DirectorySeasons,
    ContentV2DirectoryTnved,
    ContentV2DirectoryVat,
    ContentV2GetCardsList,
    ContentV2GetCardsTrash,
    ContentV2ObjectAll,
    ContentV2ObjectCharcsSubjectId,
    ContentV2ObjectParentAll,
    ContentV2TagCreate,
    ContentV2TagIdDelete,
    ContentV2TagIdUpdate,
    ContentV2TagNomenclatureLinkCreate,
    ContentV2Tags,
    ContentV3MediaFileCreate,
    ContentV3MediaSaveCreate,
    DbwWarehousesWarehouseIdContacts,
    DbwWarehousesWarehouseIdContactsUpdate,
    DiscountsPricesV1UploadTaskB2bWholesaleUpdate,
    HistoryGoodsTask,
    HistoryTasks,
    ListGoodsFilterGet,
    ListGoodsFilterPost,
    ListGoodsSizeNm,
    Offices,
    QuarantineGoods,
    StocksWarehouseId,
    StocksWarehouseIdDelete,
    StocksWarehouseIdUpdate,
    UploadTaskClubDiscountUpdate,
    UploadTaskSizeUpdate,
    UploadTaskUpdate,
    Warehouses,
    WarehousesCreate,
    WarehousesWarehouseIdDelete,
    WarehousesWarehouseIdUpdate,
)
from .models import (
    BrandsResponse,
    ContentV1RecommendationsSetUpdateRecListItem,
    ContentV2BarcodesCreateResponse,
    ContentV2CardsDeleteTrashCreateResponse,
    ContentV2CardsLimitsResponse,
    ContentV2CardsRecoverCreateResponse,
    ContentV2CardsUploadAddCreateCardsToAddItem,
    ContentV2DirectoryColorsResponse,
    ContentV2DirectoryCountriesResponse,
    ContentV2DirectoryKindsResponse,
    ContentV2DirectorySeasonsResponse,
    ContentV2DirectoryTnvedResponse,
    ContentV2DirectoryVatResponse,
    ContentV2GetCardsListResponse,
    ContentV2GetCardsListSettings,
    ContentV2GetCardsTrashResponse,
    ContentV2GetCardsTrashSettings,
    ContentV2ObjectAllResponse,
    ContentV2ObjectCharcsSubjectIdResponse,
    ContentV2ObjectParentAllResponse,
    ContentV2TagsResponse,
    ContentV3MediaFileCreateResponse,
    ContentV3MediaSaveCreateResponse,
    DbwWarehousesWarehouseIdContactsResponse,
    DbwWarehousesWarehouseIdContactsUpdateContactsItem,
    GetRecomRes,
    Office,
    ResponseContentError,
    ResponseItemList,
    ResponsePublicViewerPublicErrorsTableListV2,
    SetRecomRes,
    StocksWarehouseIdResponse,
    StocksWarehouseIdUpdateStocksItem,
    SwaggerPublicErrorsCursorInput,
    SwaggerPublicErrorsOrderV2,
    Warehouse,
    WarehousesCreateResponse,
)


if TYPE_CHECKING:
    from ...client import WBApi


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

    async def buffer_goods_task(
        self, *, limit: int, upload_id: int, offset: int | None = None, auto_paginate: bool = False
    ) -> None | list[Any]:
        """Детализация необработанной загрузки

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param upload_id: ID загрузки
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = BufferGoodsTask(limit=limit, upload_id=upload_id, offset=offset)
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_buffer_goods_task(
        self, *, limit: int, upload_id: int, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Детализация необработанной загрузки — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param upload_id: ID загрузки
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in BufferGoodsTask(limit=limit, upload_id=upload_id, offset=offset).stream(self._api):
            yield item

    async def buffer_tasks(self, *, upload_id: int) -> None:
        """Состояние необработанной загрузки

        :param upload_id: ID загрузки
        """
        await BufferTasks(upload_id=upload_id).emit(self._api)

    async def content_v1_brands(
        self, *, subject_id: int, next_: int | None = None, auto_paginate: bool = False
    ) -> BrandsResponse | list[Any]:
        """Бренды

        :param subject_id: ID предмета
        :param next_: Параметр пагинации. Используйте значение `next` из ответа, чтобы получить следующий
            пакет данных
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = ContentV1Brands(subject_id=subject_id, next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_content_v1_brands(
        self, *, subject_id: int, next_: int | None = None
    ) -> AsyncIterator[Any]:
        """Бренды — постранично, по одной записи.

        :param subject_id: ID предмета
        :param next_: Параметр пагинации. Используйте значение `next` из ответа, чтобы получить следующий
            пакет данных
        """
        async for item in ContentV1Brands(subject_id=subject_id, next_=next_).stream(self._api):
            yield item

    async def content_v1_recommendations_list(
        self,
        *,
        brand_names: list[str] | None = None,
        limit: int | None = None,
        next_: int | None = None,
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
        call = ContentV1RecommendationsList(
            brand_names=brand_names, limit=limit, next_=next_, search=search, subject_ids=subject_ids
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_content_v1_recommendations_list(
        self,
        *,
        brand_names: list[str] | None = None,
        limit: int | None = None,
        next_: int | None = None,
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
        async for item in ContentV1RecommendationsList(
            brand_names=brand_names, limit=limit, next_=next_, search=search, subject_ids=subject_ids
        ).stream(self._api):
            yield item

    async def content_v1_recommendations_set_update(
        self, *, rec_list: list[ContentV1RecommendationsSetUpdateRecListItem], replace: bool | None = None
    ) -> SetRecomRes:
        """Установить рекомендации для товаров

        :param rec_list: Список рекомендаций для товаров
        :param replace: Действие в запросе:   - `false` — добавить новые рекомендации к существующим   -
            `true` — заменить существующие рекомендации новыми
        """
        return await ContentV1RecommendationsSetUpdate(rec_list=rec_list, replace=replace).emit(self._api)

    async def content_v2_barcodes_create(
        self, *, count: int | None = None
    ) -> ContentV2BarcodesCreateResponse:
        """Генерация баркодов

        :param count: Кол-во баркодов которые надо сгенерировать, максимальное доступное количество баркодов
            для генерации - `5 000`
        """
        return await ContentV2BarcodesCreate(count=count).emit(self._api)

    async def content_v2_cards_delete_trash_create(
        self, *, nm_ids: list[int] | None = None
    ) -> ContentV2CardsDeleteTrashCreateResponse:
        """Перенос карточек товаров в корзину

        :param nm_ids: Артикулы WB
        """
        return await ContentV2CardsDeleteTrashCreate(nm_ids=nm_ids).emit(self._api)

    async def content_v2_cards_error_list(
        self,
        *,
        cursor: SwaggerPublicErrorsCursorInput | None = None,
        locale: str | None = None,
        order: SwaggerPublicErrorsOrderV2 | None = None,
        auto_paginate: bool = False,
    ) -> ResponsePublicViewerPublicErrorsTableListV2 | list[Any]:
        """Список несозданных карточек товаров с ошибками

        :param locale: Язык названий предметов:   - `ru` — русский   - `en` — английский   - `zh` —
            китайский  Не используется в песочнице
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = ContentV2CardsErrorList(cursor=cursor, locale=locale, order=order)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_content_v2_cards_error_list(
        self,
        *,
        cursor: SwaggerPublicErrorsCursorInput | None = None,
        locale: str | None = None,
        order: SwaggerPublicErrorsOrderV2 | None = None,
    ) -> AsyncIterator[Any]:
        """Список несозданных карточек товаров с ошибками — постранично, по одной записи.

        :param locale: Язык названий предметов:   - `ru` — русский   - `en` — английский   - `zh` —
            китайский  Не используется в песочнице
        """
        async for item in ContentV2CardsErrorList(cursor=cursor, locale=locale, order=order).stream(
            self._api
        ):
            yield item

    async def content_v2_cards_limits(self) -> ContentV2CardsLimitsResponse:
        """Лимиты карточек товаров"""
        return await ContentV2CardsLimits().emit(self._api)

    async def content_v2_cards_move_nm_create(self, *, body: Any) -> ResponseItemList:
        """Объединение и разъединение карточек товаров"""
        return await ContentV2CardsMoveNmCreate(body=body).emit(self._api)

    async def content_v2_cards_recover_create(
        self, *, nm_ids: list[int] | None = None
    ) -> ContentV2CardsRecoverCreateResponse:
        """Восстановление карточек товаров из корзины

        :param nm_ids: Артикулы WB
        """
        return await ContentV2CardsRecoverCreate(nm_ids=nm_ids).emit(self._api)

    async def content_v2_cards_update_create(self, *, body: Any) -> ResponseItemList:
        """Редактирование карточек товаров"""
        return await ContentV2CardsUpdateCreate(body=body).emit(self._api)

    async def content_v2_cards_upload_add_create(
        self,
        *,
        cards_to_add: list[ContentV2CardsUploadAddCreateCardsToAddItem] | None = None,
        imt_id: int | None = None,
    ) -> ResponseItemList:
        """Создание карточек товаров с присоединением

        :param cards_to_add: Добавляемые карточки товаров
        :param imt_id: `imtID` отдельной карточки товара или группы объединённых карточек товаров, к которой
            присоединяются создаваемые карточки
        """
        return await ContentV2CardsUploadAddCreate(cards_to_add=cards_to_add, imt_id=imt_id).emit(self._api)

    async def content_v2_cards_upload_create(self, *, body: Any) -> ResponseItemList:
        """Создание карточек товаров"""
        return await ContentV2CardsUploadCreate(body=body).emit(self._api)

    async def content_v2_directory_colors(
        self, *, locale: str | None = None
    ) -> ContentV2DirectoryColorsResponse:
        """Цвет

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await ContentV2DirectoryColors(locale=locale).emit(self._api)

    async def content_v2_directory_countries(
        self, *, locale: str | None = None
    ) -> ContentV2DirectoryCountriesResponse:
        """Страна производства

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await ContentV2DirectoryCountries(locale=locale).emit(self._api)

    async def content_v2_directory_kinds(
        self, *, locale: str | None = None
    ) -> ContentV2DirectoryKindsResponse:
        """Пол

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await ContentV2DirectoryKinds(locale=locale).emit(self._api)

    async def content_v2_directory_seasons(
        self, *, locale: str | None = None
    ) -> ContentV2DirectorySeasonsResponse:
        """Сезон

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await ContentV2DirectorySeasons(locale=locale).emit(self._api)

    async def content_v2_directory_tnved(
        self, *, subject_id: int, locale: str | None = None, search: int | None = None
    ) -> ContentV2DirectoryTnvedResponse:
        """ТНВЭД-код

        :param subject_id: ID предмета
        :param locale: Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский …
        :param search: Поиск по ТНВЭД-коду. Работает только в паре с `subjectID`
        """
        return await ContentV2DirectoryTnved(subject_id=subject_id, locale=locale, search=search).emit(
            self._api
        )

    async def content_v2_directory_vat(self, *, locale: str | None = None) -> ContentV2DirectoryVatResponse:
        """Ставка НДС

        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await ContentV2DirectoryVat(locale=locale).emit(self._api)

    async def content_v2_get_cards_list(
        self,
        *,
        locale: str | None = None,
        settings: ContentV2GetCardsListSettings | None = None,
        auto_paginate: bool = False,
    ) -> ContentV2GetCardsListResponse | list[Any]:
        """Список карточек товаров

        :param locale: Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский …
        :param settings: Настройки
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = ContentV2GetCardsList(locale=locale, settings=settings)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_content_v2_get_cards_list(
        self, *, locale: str | None = None, settings: ContentV2GetCardsListSettings | None = None
    ) -> AsyncIterator[Any]:
        """Список карточек товаров — постранично, по одной записи.

        :param locale: Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский …
        :param settings: Настройки
        """
        async for item in ContentV2GetCardsList(locale=locale, settings=settings).stream(self._api):
            yield item

    async def content_v2_get_cards_trash(
        self,
        *,
        locale: str | None = None,
        settings: ContentV2GetCardsTrashSettings | None = None,
        auto_paginate: bool = False,
    ) -> ContentV2GetCardsTrashResponse | list[Any]:
        """Список карточек товаров в корзине

        :param locale: Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский …
        :param settings: Настройки
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = ContentV2GetCardsTrash(locale=locale, settings=settings)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_content_v2_get_cards_trash(
        self, *, locale: str | None = None, settings: ContentV2GetCardsTrashSettings | None = None
    ) -> AsyncIterator[Any]:
        """Список карточек товаров в корзине — постранично, по одной записи.

        :param locale: Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` —
            английский   - `zh` — китайский …
        :param settings: Настройки
        """
        async for item in ContentV2GetCardsTrash(locale=locale, settings=settings).stream(self._api):
            yield item

    async def content_v2_object_all(
        self,
        *,
        limit: int | None = None,
        locale: str | None = None,
        name: str | None = None,
        offset: int | None = None,
        parent_id: int | None = None,
        auto_paginate: bool = False,
    ) -> ContentV2ObjectAllResponse | list[Any]:
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
        call = ContentV2ObjectAll(limit=limit, locale=locale, name=name, offset=offset, parent_id=parent_id)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_content_v2_object_all(
        self,
        *,
        limit: int | None = None,
        locale: str | None = None,
        name: str | None = None,
        offset: int | None = None,
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
        async for item in ContentV2ObjectAll(
            limit=limit, locale=locale, name=name, offset=offset, parent_id=parent_id
        ).stream(self._api):
            yield item

    async def content_v2_object_charcs_subject_id(
        self, *, subject_id: str | int, locale: str | None = None
    ) -> ContentV2ObjectCharcsSubjectIdResponse:
        """Характеристики предмета

        :param subject_id: ID предмета
        :param locale: Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский
            - `zh` — китайский …
        """
        return await ContentV2ObjectCharcsSubjectId(subject_id=subject_id, locale=locale).emit(self._api)

    async def content_v2_object_parent_all(
        self, *, locale: str | None = None
    ) -> ContentV2ObjectParentAllResponse:
        """Родительские категории товаров

        :param locale: Язык поля ответа `name`:   - `ru` — русский   - `en` — английский   - `zh` —
            китайский …
        """
        return await ContentV2ObjectParentAll(locale=locale).emit(self._api)

    async def content_v2_tag_create(
        self, *, color: str | None = None, name: str | None = None
    ) -> ResponseContentError:
        """Создание ярлыка

        :param color: Цвет ярлыка.  Доступные цвета:   - `D1CFD7` — серый   - `FEE0E0` — красный   -
            `ECDAFF` — фиолетовый   - `E4EAFF` — синий   - `DEF1DD` — зеленый …
        :param name: Имя ярлыка
        """
        return await ContentV2TagCreate(color=color, name=name).emit(self._api)

    async def content_v2_tag_id_delete(self, *, id_: str | int) -> ResponseContentError:
        """Удаление ярлыка

        :param id_: Числовой ID ярлыка
        """
        return await ContentV2TagIdDelete(id_=id_).emit(self._api)

    async def content_v2_tag_id_update(
        self, *, id_: str | int, color: str | None = None, name: str | None = None
    ) -> ResponseContentError:
        """Изменение ярлыка

        :param id_: Числовой ID ярлыка
        :param color: Цвет ярлыка
        :param name: Имя ярлыка
        """
        return await ContentV2TagIdUpdate(id_=id_, color=color, name=name).emit(self._api)

    async def content_v2_tag_nomenclature_link_create(
        self, *, nm_id: int | None = None, tags_ids: list[int] | None = None
    ) -> ResponseContentError:
        """Управление ярлыками в карточке товара

        :param nm_id: Артикул WB
        :param tags_ids: Массив числовых ID ярлыков. Что бы снять ярлыки с карточки товара, необходимо
            передать пустой массив. …
        """
        return await ContentV2TagNomenclatureLinkCreate(nm_id=nm_id, tags_ids=tags_ids).emit(self._api)

    async def content_v2_tags(self) -> ContentV2TagsResponse:
        """Список ярлыков"""
        return await ContentV2Tags().emit(self._api)

    async def content_v3_media_file_create(self) -> ContentV3MediaFileCreateResponse:
        """Загрузить медиафайл"""
        return await ContentV3MediaFileCreate().emit(self._api)

    async def content_v3_media_save_create(
        self, *, data: list[str] | None = None, nm_id: int | None = None
    ) -> ContentV3MediaSaveCreateResponse:
        """Загрузить медиафайлы по ссылкам

        :param data: Ссылки на изображения в том порядке, в котором они будут в карточке товара, и на видео,
            на любой позиции массива
        :param nm_id: Артикул WB
        """
        return await ContentV3MediaSaveCreate(data=data, nm_id=nm_id).emit(self._api)

    async def dbw_warehouses_warehouse_id_contacts(
        self, *, warehouse_id: str | int
    ) -> DbwWarehousesWarehouseIdContactsResponse:
        """Список контактов

        :param warehouse_id: ID склада продавца
        """
        return await DbwWarehousesWarehouseIdContacts(warehouse_id=warehouse_id).emit(self._api)

    async def dbw_warehouses_warehouse_id_contacts_update(
        self,
        *,
        warehouse_id: str | int,
        contacts: list[DbwWarehousesWarehouseIdContactsUpdateContactsItem] | None = None,
    ) -> None:
        """Обновить список контактов

        :param warehouse_id: ID склада продавца
        """
        await DbwWarehousesWarehouseIdContactsUpdate(warehouse_id=warehouse_id, contacts=contacts).emit(
            self._api
        )

    async def discounts_prices_v1_upload_task_b2b_wholesale_update(self) -> None:
        """Установить оптовые скидки для B2B-продаж"""
        await DiscountsPricesV1UploadTaskB2bWholesaleUpdate().emit(self._api)

    async def history_goods_task(
        self, *, limit: int, upload_id: int, offset: int | None = None, auto_paginate: bool = False
    ) -> None | list[Any]:
        """Детализация обработанной загрузки

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param upload_id: ID загрузки
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = HistoryGoodsTask(limit=limit, upload_id=upload_id, offset=offset)
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_history_goods_task(
        self, *, limit: int, upload_id: int, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Детализация обработанной загрузки — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param upload_id: ID загрузки
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in HistoryGoodsTask(limit=limit, upload_id=upload_id, offset=offset).stream(self._api):
            yield item

    async def history_tasks(self, *, upload_id: int) -> None:
        """Состояние обработанной загрузки

        :param upload_id: ID загрузки
        """
        await HistoryTasks(upload_id=upload_id).emit(self._api)

    async def list_goods_filter_get(
        self,
        *,
        limit: int,
        filter_nm_id: int | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> None | list[Any]:
        """Получить товары с ценами

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param filter_nm_id: Артикул WB для поиска товара
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = ListGoodsFilterGet(limit=limit, filter_nm_id=filter_nm_id, offset=offset)
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_list_goods_filter_get(
        self, *, limit: int, filter_nm_id: int | None = None, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Получить товары с ценами — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param filter_nm_id: Артикул WB для поиска товара
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in ListGoodsFilterGet(limit=limit, filter_nm_id=filter_nm_id, offset=offset).stream(
            self._api
        ):
            yield item

    async def list_goods_filter_post(self) -> None:
        """Получить товары с ценами по артикулам"""
        await ListGoodsFilterPost().emit(self._api)

    async def list_goods_size_nm(
        self, *, limit: int, nm_id: int, offset: int | None = None, auto_paginate: bool = False
    ) -> None | list[Any]:
        """Получить размеры товара с ценами

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param nm_id: Артикул WB
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = ListGoodsSizeNm(limit=limit, nm_id=nm_id, offset=offset)
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_list_goods_size_nm(
        self, *, limit: int, nm_id: int, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Получить размеры товара с ценами — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param nm_id: Артикул WB
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in ListGoodsSizeNm(limit=limit, nm_id=nm_id, offset=offset).stream(self._api):
            yield item

    async def offices(self) -> list[Office]:
        """Получить список складов WB"""
        return await Offices().emit(self._api)

    async def quarantine_goods(
        self, *, limit: int, offset: int | None = None, auto_paginate: bool = False
    ) -> None | list[Any]:
        """Получить товары в карантине

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = QuarantineGoods(limit=limit, offset=offset)
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_quarantine_goods(self, *, limit: int, offset: int | None = None) -> AsyncIterator[Any]:
        """Получить товары в карантине — постранично, по одной записи.

        :param limit: Сколько элементов вывести на одной странице (пагинация)
        :param offset: Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11
            элемента
        """
        async for item in QuarantineGoods(limit=limit, offset=offset).stream(self._api):
            yield item

    async def stocks_warehouse_id(
        self, *, chrt_ids: list[int], warehouse_id: str | int
    ) -> StocksWarehouseIdResponse:
        """Получить остатки товаров

        :param chrt_ids: Массив ID размеров товаров
        :param warehouse_id: ID склада продавца
        """
        return await StocksWarehouseId(chrt_ids=chrt_ids, warehouse_id=warehouse_id).emit(self._api)

    async def stocks_warehouse_id_delete(self, *, chrt_ids: list[int], warehouse_id: str | int) -> None:
        """Удалить остатки товаров

        :param chrt_ids: Массив ID размеров товаров
        :param warehouse_id: ID склада продавца
        """
        await StocksWarehouseIdDelete(chrt_ids=chrt_ids, warehouse_id=warehouse_id).emit(self._api)

    async def stocks_warehouse_id_update(
        self, *, stocks: list[StocksWarehouseIdUpdateStocksItem], warehouse_id: str | int
    ) -> None:
        """Обновить остатки товаров

        :param stocks: Массив ID размеров товаров и их остатков
        :param warehouse_id: ID склада продавца
        """
        await StocksWarehouseIdUpdate(stocks=stocks, warehouse_id=warehouse_id).emit(self._api)

    async def upload_task_club_discount_update(self) -> None:
        """Установить скидки WB Клуба"""
        await UploadTaskClubDiscountUpdate().emit(self._api)

    async def upload_task_size_update(self) -> None:
        """Установить цены для размеров"""
        await UploadTaskSizeUpdate().emit(self._api)

    async def upload_task_update(self) -> None:
        """Установить цены и скидки"""
        await UploadTaskUpdate().emit(self._api)

    async def warehouses(self) -> list[Warehouse]:
        """Получить список складов продавца"""
        return await Warehouses().emit(self._api)

    async def warehouses_create(self, *, name: str, office_id: int) -> WarehousesCreateResponse:
        """Создать склад продавца

        :param name: Имя склада продавца
        :param office_id: ID склада WB.Нельзя привязывать склад WB, который уже используется
        """
        return await WarehousesCreate(name=name, office_id=office_id).emit(self._api)

    async def warehouses_warehouse_id_delete(self, *, warehouse_id: str | int) -> None:
        """Удалить склад продавца

        :param warehouse_id: ID склада продавца
        """
        await WarehousesWarehouseIdDelete(warehouse_id=warehouse_id).emit(self._api)

    async def warehouses_warehouse_id_update(
        self, *, name: str, office_id: int, warehouse_id: str | int
    ) -> None:
        """Обновить склад продавца

        :param name: Имя склада продавца
        :param office_id: ID склада WB.Нельзя привязывать склад WB, который уже используется.Можно менять не
            чаще одного раза в сутки
        :param warehouse_id: ID склада продавца
        """
        await WarehousesWarehouseIdUpdate(name=name, office_id=office_id, warehouse_id=warehouse_id).emit(
            self._api
        )
