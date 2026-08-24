from __future__ import annotations

from typing import Any

from ..client.method import WBMethod
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
    OfferCreateRequest,
    OfferMetaRequest,
    OfferResponse,
    OfferResponseList,
    UploadChunkResponse,
    UploadGalleryResponse,
    UploadInitResponse,
)


class CreateKeysApiKey(WBMethod[None]):
    """Добавить ключи активации

    POST /api/v1/keys-api/keys
    """

    __path__ = "/api/v1/keys-api/keys"
    __http_method__ = "POST"
    __returns__ = None
    __host__ = "https://devapi-digital.wildberries.ru"
    __body_fields__ = {"keys": "keys", "offer_id": "offer_id"}

    keys: list[str]
    """Список ключей.  **Ограничения:** - Максимальное количество ключей — **1000** - Максимальная
    длина ключа — **200 символов**
    """
    offer_id: int
    """ID предложения"""


class CreateOffer(WBMethod[OfferResponse]):
    """Создать новое предложение

    POST /api/v1/offers
    """

    __path__ = "/api/v1/offers"
    __http_method__ = "POST"
    __returns__ = OfferResponse
    __host__ = "https://devapi-digital.wildberries.ru"

    body: OfferCreateRequest | list[Any] | dict[str, Any]


class CreateOffersThumb(WBMethod[None]):
    """Добавить или обновить обложку предложения

    POST /api/v1/offers/thumb
    """

    __path__ = "/api/v1/offers/thumb"
    __http_method__ = "POST"
    __returns__ = None
    __host__ = "https://devapi-digital.wildberries.ru"


class CreateUploadInit(WBMethod[UploadInitResponse]):
    """Инициализировать новый контент

    POST /api/v1/content/upload/init
    """

    __path__ = "/api/v1/content/upload/init"
    __http_method__ = "POST"
    __returns__ = UploadInitResponse
    __host__ = "https://devapi-digital.wildberries.ru"
    __body_fields__ = {
        "title": "title",
        "description": "description",
        "catalog_id": "catalog_id",
        "content_type": "content_type",
        "parts": "parts",
        "meta": "meta",
    }

    catalog_id: int
    """ID категории контента: - `1` — Видеоконтент - `2` — Аудиоконтент - `4` — Документ"""
    content_type: str
    """Тип файла: - Видеоконтент:     - `video/mp4` - Аудиоконтент:     - `audio/mpeg` - Документ:
    - `application/pdf`     - `application/epub+zip` …
    """
    description: str
    """Описание контента.Максимальная длина — **1000 символов.**"""
    meta: ContentMeta
    parts: list[ChunkPart]
    """Для оптимальной скорости загрузки контента следует разбить файл на фреймы по 2 Мб. В массиве
    указываются индекс каждого фрейма и его размер
    """
    title: str
    """Название контента.Максимальная длина — **500 символов.**"""


class DeleteContent(WBMethod[None]):
    """Удалить контент

    POST /api/v1/content/delete
    """

    __path__ = "/api/v1/content/delete"
    __http_method__ = "POST"
    __returns__ = None
    __host__ = "https://devapi-digital.wildberries.ru"
    __body_fields__ = {"content_id": "content_id"}

    content_id: int | None = None
    """ID контента"""


class DeleteKeysApiKey(WBMethod[KeysDeleteResponse]):
    """Удалить ключи активации

    DELETE /api/v1/keys-api/keys
    """

    __path__ = "/api/v1/keys-api/keys"
    __http_method__ = "DELETE"
    __returns__ = KeysDeleteResponse
    __query_params__ = {"ids": "ids"}
    __host__ = "https://devapi-digital.wildberries.ru"

    ids: list[int]
    """Список ID ключей"""


class GetAuthor(WBMethod[ContentList]):
    """Получить список своего контента

    GET /api/v1/content/author
    """

    __path__ = "/api/v1/content/author"
    __http_method__ = "GET"
    __returns__ = ContentList
    __query_params__ = {
        "search": "search",
        "category": "category",
        "status": "status",
        "sort": "sort",
        "sort_dir": "sort_dir",
        "skip": "skip",
        "take": "take",
    }
    __host__ = "https://devapi-digital.wildberries.ru"
    __paginate__ = "skip_take"
    __items__ = "items"

    category: int | None = None
    """Фильтрация по категории: - `1` — Видеоконтент - `2` — Аудиоконтент - `4` — Документ"""
    search: str | None = None
    """Поиск по названию контента"""
    skip: int | None = 0
    """Смещение. Количество контента, которые нужно пропустить в результирующем наборе."""
    sort: str | None = None
    """Сортировка контента по дате создания или обновления"""
    sort_dir: str | None = None
    """Направление сортировки: - `asc` — по возрастанию - `desc` — по убыванию"""
    status: int | None = None
    """Фильтрация по статусу: - `0` — Создан - `1` — Загружено на сервер - `2` — Опубликован - `3`
    — Ошибка в обработке или публикации - `4` — Обрабатывается …
    """
    take: int | None = 50
    """Количество контента для получения"""


class GetAuthorById(WBMethod[Content]):
    """Получить информацию о контенте

    GET /api/v1/content/author/{content_id}
    """

    __path__ = "/api/v1/content/author/{content_id}"
    __http_method__ = "GET"
    __returns__ = Content
    __path_params__ = ("content_id",)
    __host__ = "https://devapi-digital.wildberries.ru"

    content_id: str | int
    """ID контента"""


class GetCatalog(WBMethod[GetFullCatalogResponse]):
    """Получить категории и их подкатегории

    GET /api/v1/catalog
    """

    __path__ = "/api/v1/catalog"
    __http_method__ = "GET"
    __returns__ = GetFullCatalogResponse
    __host__ = "https://devapi-digital.wildberries.ru"
    __items__ = "items"


class GetDownload(WBMethod[None]):
    """Скачать контент

    GET /api/v1/content/download/{uri}
    """

    __path__ = "/api/v1/content/download/{uri}"
    __http_method__ = "GET"
    __returns__ = None
    __path_params__ = ("uri",)
    __host__ = "https://devapi-digital.wildberries.ru"

    uri: str | int
    """URI-адрес контента"""


class GetKeysApiKeysRedeemed(WBMethod[KeysRedeemedResponseList]):
    """Получить купленные ключи

    GET /api/v1/keys-api/keys/redeemed
    """

    __path__ = "/api/v1/keys-api/keys/redeemed"
    __http_method__ = "GET"
    __returns__ = KeysRedeemedResponseList
    __query_params__ = {
        "offer_id": "offer_id",
        "skip": "skip",
        "take": "take",
        "date_from": "date_from",
        "date_to": "date_to",
    }
    __host__ = "https://devapi-digital.wildberries.ru"
    __paginate__ = "skip_take"
    __items__ = "items"

    date_from: str | None = None
    """Фильтрация по дате покупки начиная с указанной даты (включительно).  Формат даты:
    **RFC3339** (`2023-06-17T19:20:30Z`)
    """
    date_to: str | None = None
    """Фильтрация по дате покупки до указанной даты (не включительно).  Формат даты: **RFC3339**
    (`2024-10-18T19:20:30Z`)
    """
    offer_id: int | None = None
    """Фильтрация по ID предложения. Позволяет выбрать ключи, связанные с определенным предложением
    """
    skip: int | None = 0
    """Смещение. Указывает, сколько записей нужно пропустить в результирующем наборе. Используется
    для пагинации
    """
    take: int | None = 50
    """Количество записей для получения. Указывает, сколько ключей должно быть возвращено в ответе
    """


class GetOfferKeys(WBMethod[KeysCountResponse]):
    """Получить количество ключей для предложения

    GET /api/v1/offer/keys/{offer_id}
    """

    __path__ = "/api/v1/offer/keys/{offer_id}"
    __http_method__ = "GET"
    __returns__ = KeysCountResponse
    __path_params__ = ("offer_id",)
    __host__ = "https://devapi-digital.wildberries.ru"

    offer_id: str | int
    """ID предложения"""


class GetOfferKeysList(WBMethod[KeysResponseList]):
    """Получить список ключей

    GET /api/v1/offer/keys/{offer_id}/list
    """

    __path__ = "/api/v1/offer/keys/{offer_id}/list"
    __http_method__ = "GET"
    __returns__ = KeysResponseList
    __path_params__ = ("offer_id",)
    __query_params__ = {
        "take": "take",
        "skip": "skip",
        "deleted": "deleted",
        "sold": "sold",
        "reserved": "reserved",
        "expired": "expired",
    }
    __host__ = "https://devapi-digital.wildberries.ru"
    __paginate__ = "skip_take"
    __items__ = "items"

    offer_id: str | int
    """ID предложения"""
    deleted: bool | None = True
    """Указывает, будут ли в ответе присутствовать удалённые ключи"""
    expired: bool | None = True
    """Указывает, будут ли в ответе присутствовать ключи с истекшим сроком действия"""
    reserved: bool | None = True
    """Указывает, будут ли в ответе присутствовать зарезервированные ключи"""
    skip: int | None = 0
    """Смещение. Указывает, сколько записей нужно пропустить в результирующем наборе. Используется
    для пагинации
    """
    sold: bool | None = True
    """Указывает, будут ли в ответе присутствовать проданные ключи"""
    take: int | None = 50
    """Количество записей для получения. Указывает, сколько ключей должно быть возвращено в ответе
    """


class GetOffers(WBMethod[OfferResponse]):
    """Получить информацию о предложении

    GET /api/v1/offers/{offer_id}
    """

    __path__ = "/api/v1/offers/{offer_id}"
    __http_method__ = "GET"
    __returns__ = OfferResponse
    __path_params__ = ("offer_id",)
    __host__ = "https://devapi-digital.wildberries.ru"

    offer_id: str | int
    """ID предложения"""


class GetOffersAuthor(WBMethod[OfferResponseList]):
    """Получить список своих предложений

    GET /api/v1/offers/author
    """

    __path__ = "/api/v1/offers/author"
    __http_method__ = "GET"
    __returns__ = OfferResponseList
    __query_params__ = {
        "search": "search",
        "category": "category",
        "status": "status",
        "sort": "sort",
        "sort_dir": "sort_dir",
        "skip": "skip",
        "take": "take",
    }
    __host__ = "https://devapi-digital.wildberries.ru"
    __paginate__ = "skip_take"
    __items__ = "items"

    category: int | None = None
    """Фильтрация по категории контента: - `1` — Видеоконтент - `2` — Аудиоконтент - `4` — Документ
    """
    search: str | None = None
    """Поиск по названию предложения"""
    skip: int | None = 0
    """Смещение. Количество предложений, которые нужно пропустить в результирующем наборе"""
    sort: str | None = None
    """Сортировка предложений по дате создания или обновления"""
    sort_dir: str | None = None
    """Направление сортировки: - `asc` — по возрастанию - `desc` — по убыванию"""
    status: int | None = None
    """Фильтрация по статусу: - `0` — Черновик - `1` — Опубликован - `2` — Приостановлен"""
    take: int | None = 50
    """Количество предложений для получения"""


class UpdateAuthor(WBMethod[Content]):
    """Редактировать контент

    POST /api/v1/content/author/{content_id}
    """

    __path__ = "/api/v1/content/author/{content_id}"
    __http_method__ = "POST"
    __returns__ = Content
    __path_params__ = ("content_id",)
    __host__ = "https://devapi-digital.wildberries.ru"
    __body_fields__ = {"title": "title", "description": "description"}

    content_id: str | int
    """ID контента"""
    description: str | None = None
    """Описание контента.Максимальная длина — **1000 символов.**"""
    title: str | None = None
    """Название контента.Максимальная длина — **500 символов.**"""


class UpdateOffer(WBMethod[None]):
    """Редактировать предложение

    POST /api/v1/offers/{offer_id}
    """

    __path__ = "/api/v1/offers/{offer_id}"
    __http_method__ = "POST"
    __returns__ = None
    __path_params__ = ("offer_id",)
    __host__ = "https://devapi-digital.wildberries.ru"
    __body_fields__ = {
        "title": "title",
        "description": "description",
        "price": "price",
        "discount_price": "discount_price",
        "gallery": "gallery",
        "age_rating": "age_rating",
        "tags": "tags",
        "status": "status",
        "catalog_path": "catalog_path",
        "meta": "meta",
    }

    offer_id: str | int
    """ID предложения"""
    age_rating: str | None = None
    """Возрастное ограничение. Это система, которая используется для определения, подходит ли ваше
    предложение для определенной возрастной группы.
    """
    catalog_path: list[int] | None = None
    """Массив ID подкатегорий, в котором находится предложение. …"""
    description: str | None = None
    """Описание предложения. Это текст, который описывает ваше предложение и помогает людям понять,
    что именно представляет из себя продаваемый вами товар и чем он мож …
    """
    discount_price: int | None = None
    """Цена с учетом скидки, ₽"""
    gallery: list[str] | None = None
    """Список URL-адресов дополнительных изображений, а так же видео превью. **Можно передать до 8
    медиафайлов.** …
    """
    meta: OfferMetaRequest | None = None
    price: int | None = None
    """Цена предложения, ₽"""
    status: int | None = None
    """Статус вашего предложения: - `0` — Добавить в черновик - `1` — Опубликовать - `2` —
    Приостановить продажу - `3` — Удалить
    """
    tags: list[str] | None = None
    """Массив тегов. Теги нужны для группирования, ранжирования и облегчения поиска вашего товара.
    **Ограничения**: - Максимальное количество тегов — **5** …
    """
    title: str | None = None
    """Название предложения.Максимальная длина — **500 символов.**"""


class UpdateOfferPrice(WBMethod[None]):
    """Обновить цену

    POST /api/v1/offer/price/{offer_id}
    """

    __path__ = "/api/v1/offer/price/{offer_id}"
    __http_method__ = "POST"
    __returns__ = None
    __path_params__ = ("offer_id",)
    __host__ = "https://devapi-digital.wildberries.ru"
    __body_fields__ = {"regular_price": "regular_price", "discount_price": "discount_price"}

    offer_id: str | int
    """ID предложения"""
    discount_price: int | None = None
    """Цена с учетом скидки, ₽"""
    regular_price: int | None = None
    """Цена, ₽"""


class UpdateOfferStatus(WBMethod[None]):
    """Обновить статус

    POST /api/v1/offer/{offer_id}
    """

    __path__ = "/api/v1/offer/{offer_id}"
    __http_method__ = "POST"
    __returns__ = None
    __path_params__ = ("offer_id",)
    __host__ = "https://devapi-digital.wildberries.ru"
    __body_fields__ = {"status": "status"}

    offer_id: str | int
    """ID предложения"""
    status: int


class UploadChunk(WBMethod[UploadChunkResponse]):
    """Загрузить контент (файл)

    POST /api/v1/content/upload/chunk
    """

    __path__ = "/api/v1/content/upload/chunk"
    __http_method__ = "POST"
    __returns__ = UploadChunkResponse
    __host__ = "https://devapi-digital.wildberries.ru"


class UploadGallery(WBMethod[UploadGalleryResponse]):
    """Загрузить медиафайлы для предложения

    POST /api/v1/content/gallery
    """

    __path__ = "/api/v1/content/gallery"
    __http_method__ = "POST"
    __returns__ = UploadGalleryResponse
    __host__ = "https://devapi-digital.wildberries.ru"


class UploadIllustration(WBMethod[IllustrationResponse]):
    """Загрузить обложку контента

    POST /api/v1/content/illustration
    """

    __path__ = "/api/v1/content/illustration"
    __http_method__ = "POST"
    __returns__ = IllustrationResponse
    __host__ = "https://devapi-digital.wildberries.ru"
