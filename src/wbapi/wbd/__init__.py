from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    CreateKeysApiKey,
    CreateOffer,
    CreateOffersThumb,
    CreateUploadInit,
    DeleteContent,
    DeleteKeysApiKey,
    GetAuthor,
    GetAuthorById,
    GetCatalog,
    GetDownload,
    GetKeysApiKeysRedeemed,
    GetOfferKeys,
    GetOfferKeysList,
    GetOffers,
    GetOffersAuthor,
    UpdateAuthor,
    UpdateOffer,
    UpdateOfferPrice,
    UpdateOfferStatus,
    UploadChunk,
    UploadGallery,
    UploadIllustration,
)
from .models import (
    ChunkPart,
    Content,
    ContentList,
    ContentMeta,
    GetFullCatalogResponse,
    IllustrationResponse,
    KeysCountResponse,
    KeysDeleteResponse,
    KeysRedeemedResponseList,
    KeysResponseList,
    OfferMetaRequest,
    OfferResponse,
    OfferResponseList,
    UploadChunkResponse,
    UploadGalleryResponse,
    UploadInitResponse,
)


if TYPE_CHECKING:
    from ..client import WBApi


class Wbd:
    """Wildberries Цифровой.

    По вопросам работы с WBD API обращайтесь в техническую поддержку
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def create_keys_api_key(self, *, keys: list[str], offer_id: int) -> None:
        """Добавить ключи активации

        :param keys: Список ключей.  **Ограничения:** - Максимальное количество ключей — **1000** -
            Максимальная длина ключа — **200 символов**
        :param offer_id: ID предложения
        """
        await CreateKeysApiKey(keys=keys, offer_id=offer_id).emit(self._api)

    async def create_offer(self, *, body: Any) -> OfferResponse:
        """Создать новое предложение"""
        return await CreateOffer(body=body).emit(self._api)

    async def create_offers_thumb(self) -> None:
        """Добавить или обновить обложку предложения"""
        await CreateOffersThumb().emit(self._api)

    async def create_upload_init(
        self,
        *,
        catalog_id: int,
        content_type: str,
        description: str,
        meta: ContentMeta,
        parts: list[ChunkPart],
        title: str,
    ) -> UploadInitResponse:
        """Инициализировать новый контент

        :param catalog_id: ID категории контента: - `1` — Видеоконтент - `2` — Аудиоконтент - `4` — Документ
        :param content_type: Тип файла: - Видеоконтент:     - `video/mp4` - Аудиоконтент:     - `audio/mpeg`
            - Документ:     - `application/pdf`     - `application/epub+zip` …
        :param description: Описание контента.Максимальная длина — **1000 символов.**
        :param parts: Для оптимальной скорости загрузки контента следует разбить файл на фреймы по 2 Мб. В
            массиве указываются индекс каждого фрейма и его размер
        :param title: Название контента.Максимальная длина — **500 символов.**
        """
        return await CreateUploadInit(
            catalog_id=catalog_id,
            content_type=content_type,
            description=description,
            meta=meta,
            parts=parts,
            title=title,
        ).emit(self._api)

    async def delete_content(self, *, content_id: int | None = None) -> None:
        """Удалить контент

        :param content_id: ID контента
        """
        await DeleteContent(content_id=content_id).emit(self._api)

    async def delete_keys_api_key(self, *, ids: list[int]) -> KeysDeleteResponse:
        """Удалить ключи активации

        :param ids: Список ID ключей
        """
        return await DeleteKeysApiKey(ids=ids).emit(self._api)

    async def get_author(
        self,
        *,
        category: int | None = None,
        search: str | None = None,
        skip: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        status: int | None = None,
        take: int | None = None,
        auto_paginate: bool = False,
    ) -> ContentList | list[Any]:
        """Получить список своего контента

        :param category: Фильтрация по категории: - `1` — Видеоконтент - `2` — Аудиоконтент - `4` — Документ
        :param search: Поиск по названию контента
        :param skip: Смещение. Количество контента, которые нужно пропустить в результирующем наборе.
        :param sort: Сортировка контента по дате создания или обновления
        :param sort_dir: Направление сортировки: - `asc` — по возрастанию - `desc` — по убыванию
        :param status: Фильтрация по статусу: - `0` — Создан - `1` — Загружено на сервер - `2` — Опубликован
            - `3` — Ошибка в обработке или публикации - `4` — Обрабатывается …
        :param take: Количество контента для получения
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetAuthor(
            category=category,
            search=search,
            skip=skip,
            sort=sort,
            sort_dir=sort_dir,
            status=status,
            take=take,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_author(
        self,
        *,
        category: int | None = None,
        search: str | None = None,
        skip: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        status: int | None = None,
        take: int | None = None,
    ) -> AsyncIterator[Any]:
        """Получить список своего контента — постранично, по одной записи.

        :param category: Фильтрация по категории: - `1` — Видеоконтент - `2` — Аудиоконтент - `4` — Документ
        :param search: Поиск по названию контента
        :param skip: Смещение. Количество контента, которые нужно пропустить в результирующем наборе.
        :param sort: Сортировка контента по дате создания или обновления
        :param sort_dir: Направление сортировки: - `asc` — по возрастанию - `desc` — по убыванию
        :param status: Фильтрация по статусу: - `0` — Создан - `1` — Загружено на сервер - `2` — Опубликован
            - `3` — Ошибка в обработке или публикации - `4` — Обрабатывается …
        :param take: Количество контента для получения
        """
        async for item in GetAuthor(
            category=category,
            search=search,
            skip=skip,
            sort=sort,
            sort_dir=sort_dir,
            status=status,
            take=take,
        ).stream(self._api):
            yield item

    async def get_author_by_id(self, *, content_id: str | int) -> Content:
        """Получить информацию о контенте

        :param content_id: ID контента
        """
        return await GetAuthorById(content_id=content_id).emit(self._api)

    async def get_catalog(self) -> GetFullCatalogResponse:
        """Получить категории и их подкатегории"""
        return await GetCatalog().emit(self._api)

    async def get_download(self, *, uri: str | int) -> None:
        """Скачать контент

        :param uri: URI-адрес контента
        """
        await GetDownload(uri=uri).emit(self._api)

    async def get_keys_api_keys_redeemed(
        self,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        offer_id: int | None = None,
        skip: int | None = None,
        take: int | None = None,
        auto_paginate: bool = False,
    ) -> KeysRedeemedResponseList | list[Any]:
        """Получить купленные ключи

        :param date_from: Фильтрация по дате покупки начиная с указанной даты (включительно).  Формат даты:
            **RFC3339** (`2023-06-17T19:20:30Z`)
        :param date_to: Фильтрация по дате покупки до указанной даты (не включительно).  Формат даты:
            **RFC3339** (`2024-10-18T19:20:30Z`)
        :param offer_id: Фильтрация по ID предложения. Позволяет выбрать ключи, связанные с определенным
            предложением
        :param skip: Смещение. Указывает, сколько записей нужно пропустить в результирующем наборе.
            Используется для пагинации
        :param take: Количество записей для получения. Указывает, сколько ключей должно быть возвращено в
            ответе
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetKeysApiKeysRedeemed(
            date_from=date_from, date_to=date_to, offer_id=offer_id, skip=skip, take=take
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_keys_api_keys_redeemed(
        self,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        offer_id: int | None = None,
        skip: int | None = None,
        take: int | None = None,
    ) -> AsyncIterator[Any]:
        """Получить купленные ключи — постранично, по одной записи.

        :param date_from: Фильтрация по дате покупки начиная с указанной даты (включительно).  Формат даты:
            **RFC3339** (`2023-06-17T19:20:30Z`)
        :param date_to: Фильтрация по дате покупки до указанной даты (не включительно).  Формат даты:
            **RFC3339** (`2024-10-18T19:20:30Z`)
        :param offer_id: Фильтрация по ID предложения. Позволяет выбрать ключи, связанные с определенным
            предложением
        :param skip: Смещение. Указывает, сколько записей нужно пропустить в результирующем наборе.
            Используется для пагинации
        :param take: Количество записей для получения. Указывает, сколько ключей должно быть возвращено в
            ответе
        """
        async for item in GetKeysApiKeysRedeemed(
            date_from=date_from, date_to=date_to, offer_id=offer_id, skip=skip, take=take
        ).stream(self._api):
            yield item

    async def get_offer_keys(self, *, offer_id: str | int) -> KeysCountResponse:
        """Получить количество ключей для предложения

        :param offer_id: ID предложения
        """
        return await GetOfferKeys(offer_id=offer_id).emit(self._api)

    async def get_offer_keys_list(
        self,
        *,
        offer_id: str | int,
        deleted: bool | None = None,
        expired: bool | None = None,
        reserved: bool | None = None,
        skip: int | None = None,
        sold: bool | None = None,
        take: int | None = None,
        auto_paginate: bool = False,
    ) -> KeysResponseList | list[Any]:
        """Получить список ключей

        :param offer_id: ID предложения
        :param deleted: Указывает, будут ли в ответе присутствовать удалённые ключи
        :param expired: Указывает, будут ли в ответе присутствовать ключи с истекшим сроком действия
        :param reserved: Указывает, будут ли в ответе присутствовать зарезервированные ключи
        :param skip: Смещение. Указывает, сколько записей нужно пропустить в результирующем наборе.
            Используется для пагинации
        :param sold: Указывает, будут ли в ответе присутствовать проданные ключи
        :param take: Количество записей для получения. Указывает, сколько ключей должно быть возвращено в
            ответе
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetOfferKeysList(
            offer_id=offer_id,
            deleted=deleted,
            expired=expired,
            reserved=reserved,
            skip=skip,
            sold=sold,
            take=take,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_offer_keys_list(
        self,
        *,
        offer_id: str | int,
        deleted: bool | None = None,
        expired: bool | None = None,
        reserved: bool | None = None,
        skip: int | None = None,
        sold: bool | None = None,
        take: int | None = None,
    ) -> AsyncIterator[Any]:
        """Получить список ключей — постранично, по одной записи.

        :param offer_id: ID предложения
        :param deleted: Указывает, будут ли в ответе присутствовать удалённые ключи
        :param expired: Указывает, будут ли в ответе присутствовать ключи с истекшим сроком действия
        :param reserved: Указывает, будут ли в ответе присутствовать зарезервированные ключи
        :param skip: Смещение. Указывает, сколько записей нужно пропустить в результирующем наборе.
            Используется для пагинации
        :param sold: Указывает, будут ли в ответе присутствовать проданные ключи
        :param take: Количество записей для получения. Указывает, сколько ключей должно быть возвращено в
            ответе
        """
        async for item in GetOfferKeysList(
            offer_id=offer_id,
            deleted=deleted,
            expired=expired,
            reserved=reserved,
            skip=skip,
            sold=sold,
            take=take,
        ).stream(self._api):
            yield item

    async def get_offers(self, *, offer_id: str | int) -> OfferResponse:
        """Получить информацию о предложении

        :param offer_id: ID предложения
        """
        return await GetOffers(offer_id=offer_id).emit(self._api)

    async def get_offers_author(
        self,
        *,
        category: int | None = None,
        search: str | None = None,
        skip: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        status: int | None = None,
        take: int | None = None,
        auto_paginate: bool = False,
    ) -> OfferResponseList | list[Any]:
        """Получить список своих предложений

        :param category: Фильтрация по категории контента: - `1` — Видеоконтент - `2` — Аудиоконтент - `4` —
            Документ
        :param search: Поиск по названию предложения
        :param skip: Смещение. Количество предложений, которые нужно пропустить в результирующем наборе
        :param sort: Сортировка предложений по дате создания или обновления
        :param sort_dir: Направление сортировки: - `asc` — по возрастанию - `desc` — по убыванию
        :param status: Фильтрация по статусу: - `0` — Черновик - `1` — Опубликован - `2` — Приостановлен
        :param take: Количество предложений для получения
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = GetOffersAuthor(
            category=category,
            search=search,
            skip=skip,
            sort=sort,
            sort_dir=sort_dir,
            status=status,
            take=take,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_get_offers_author(
        self,
        *,
        category: int | None = None,
        search: str | None = None,
        skip: int | None = None,
        sort: str | None = None,
        sort_dir: str | None = None,
        status: int | None = None,
        take: int | None = None,
    ) -> AsyncIterator[Any]:
        """Получить список своих предложений — постранично, по одной записи.

        :param category: Фильтрация по категории контента: - `1` — Видеоконтент - `2` — Аудиоконтент - `4` —
            Документ
        :param search: Поиск по названию предложения
        :param skip: Смещение. Количество предложений, которые нужно пропустить в результирующем наборе
        :param sort: Сортировка предложений по дате создания или обновления
        :param sort_dir: Направление сортировки: - `asc` — по возрастанию - `desc` — по убыванию
        :param status: Фильтрация по статусу: - `0` — Черновик - `1` — Опубликован - `2` — Приостановлен
        :param take: Количество предложений для получения
        """
        async for item in GetOffersAuthor(
            category=category,
            search=search,
            skip=skip,
            sort=sort,
            sort_dir=sort_dir,
            status=status,
            take=take,
        ).stream(self._api):
            yield item

    async def update_author(
        self, *, content_id: str | int, description: str | None = None, title: str | None = None
    ) -> Content:
        """Редактировать контент

        :param content_id: ID контента
        :param description: Описание контента.Максимальная длина — **1000 символов.**
        :param title: Название контента.Максимальная длина — **500 символов.**
        """
        return await UpdateAuthor(content_id=content_id, description=description, title=title).emit(self._api)

    async def update_offer(
        self,
        *,
        offer_id: str | int,
        age_rating: str | None = None,
        catalog_path: list[int] | None = None,
        description: str | None = None,
        discount_price: int | None = None,
        gallery: list[str] | None = None,
        meta: OfferMetaRequest | None = None,
        price: int | None = None,
        status: int | None = None,
        tags: list[str] | None = None,
        title: str | None = None,
    ) -> None:
        """Редактировать предложение

        :param offer_id: ID предложения
        :param age_rating: Возрастное ограничение. Это система, которая используется для определения,
            подходит ли ваше предложение для определенной возрастной группы.
        :param catalog_path: Массив ID подкатегорий, в котором находится предложение. …
        :param description: Описание предложения. Это текст, который описывает ваше предложение и помогает
            людям понять, что именно представляет из себя продаваемый вами товар и чем он
            мож …
        :param discount_price: Цена с учетом скидки, ₽
        :param gallery: Список URL-адресов дополнительных изображений, а так же видео превью. **Можно
            передать до 8 медиафайлов.** …
        :param price: Цена предложения, ₽
        :param status: Статус вашего предложения: - `0` — Добавить в черновик - `1` — Опубликовать - `2` —
            Приостановить продажу - `3` — Удалить
        :param tags: Массив тегов. Теги нужны для группирования, ранжирования и облегчения поиска вашего
            товара.  **Ограничения**: - Максимальное количество тегов — **5** …
        :param title: Название предложения.Максимальная длина — **500 символов.**
        """
        await UpdateOffer(
            offer_id=offer_id,
            age_rating=age_rating,
            catalog_path=catalog_path,
            description=description,
            discount_price=discount_price,
            gallery=gallery,
            meta=meta,
            price=price,
            status=status,
            tags=tags,
            title=title,
        ).emit(self._api)

    async def update_offer_price(
        self, *, offer_id: str | int, discount_price: int | None = None, regular_price: int | None = None
    ) -> None:
        """Обновить цену

        :param offer_id: ID предложения
        :param discount_price: Цена с учетом скидки, ₽
        :param regular_price: Цена, ₽
        """
        await UpdateOfferPrice(
            offer_id=offer_id, discount_price=discount_price, regular_price=regular_price
        ).emit(self._api)

    async def update_offer_status(self, *, offer_id: str | int, status: int) -> None:
        """Обновить статус

        :param offer_id: ID предложения
        """
        await UpdateOfferStatus(offer_id=offer_id, status=status).emit(self._api)

    async def upload_chunk(self) -> UploadChunkResponse:
        """Загрузить контент (файл)"""
        return await UploadChunk().emit(self._api)

    async def upload_gallery(self) -> UploadGalleryResponse:
        """Загрузить медиафайлы для предложения"""
        return await UploadGallery().emit(self._api)

    async def upload_illustration(self) -> IllustrationResponse:
        """Загрузить обложку контента"""
        return await UploadIllustration().emit(self._api)
