from __future__ import annotations

from typing import Any

from ...client.method import WBMethod
from ...utils.token import Scope
from .models import (
    BrandsResponse,
    ContentV1RecommendationsSetUpdateRecListItem,
    ContentV2BarcodesCreateResponse,
    ContentV2CardsDeleteTrashCreateResponse,
    ContentV2CardsLimitsResponse,
    ContentV2CardsRecoverCreateResponse,
    ContentV2CardsUpdateCreateBodyItem,
    ContentV2CardsUploadAddCreateCardsToAddItem,
    ContentV2CardsUploadCreateBodyItem,
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
    RequestMoveNmsImtConn,
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


class BufferGoodsTask(WBMethod[None]):
    """Детализация необработанной загрузки

    GET /api/v2/buffer/goods/task
    """

    __path__ = "/api/v2/buffer/goods/task"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"limit": "limit", "offset": "offset", "upload_id": "uploadID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    upload_id: int
    """ID загрузки"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class BufferTasks(WBMethod[None]):
    """Состояние необработанной загрузки

    GET /api/v2/buffer/tasks
    """

    __path__ = "/api/v2/buffer/tasks"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"upload_id": "uploadID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }

    upload_id: int
    """ID загрузки"""


class ContentV1Brands(WBMethod[BrandsResponse]):
    """Бренды

    GET /api/content/v1/brands
    """

    __path__ = "/api/content/v1/brands"
    __http_method__ = "GET"
    __returns__ = BrandsResponse
    __query_params__ = {"subject_id": "subjectId", "next_": "next"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 5),
        "service": (1000, 5),
        "basic_secret": (1000, 5),
        "basic": (3600000, 1),
    }
    __paginate__ = "next"

    subject_id: int
    """ID предмета"""
    next_: int | None = None
    """Параметр пагинации. Используйте значение `next` из ответа, чтобы получить следующий пакет
    данных
    """


class ContentV1RecommendationsList(WBMethod[GetRecomRes]):
    """Список рекомендаций в карточках товаров

    POST /api/content/v1/recommendations/list
    """

    __path__ = "/api/content/v1/recommendations/list"
    __http_method__ = "POST"
    __returns__ = GetRecomRes
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __paginate__ = "next"
    __items__ = "data"
    __body_fields__ = {
        "brand_names": "brandNames",
        "limit": "limit",
        "next_": "next",
        "search": "search",
        "subject_ids": "subjectIds",
    }

    brand_names: list[str] | None = None
    """Бренды"""
    limit: int | None = None
    """Количество товаров в ответе"""
    next_: int | None = None
    """Курсор. Последний `nmId` в ответе"""
    search: str | None = None
    """Поиск:   - по артикулу WB `nmId` — полное совпадение   - по артикулу продавца `vendorCode` —
    частичное совпадение
    """
    subject_ids: list[int] | None = None
    """ID предметов"""


class ContentV1RecommendationsSetUpdate(WBMethod[SetRecomRes]):
    """Установить рекомендации для товаров

    POST /api/content/v1/recommendations/set
    """

    __path__ = "/api/content/v1/recommendations/set"
    __http_method__ = "POST"
    __returns__ = SetRecomRes
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __body_fields__ = {"rec_list": "recList", "replace": "replace"}

    rec_list: list[ContentV1RecommendationsSetUpdateRecListItem]
    """Список рекомендаций для товаров"""
    replace: bool | None = None
    """Действие в запросе:   - `false` — добавить новые рекомендации к существующим   - `true` —
    заменить существующие рекомендации новыми
    """


class ContentV2BarcodesCreate(WBMethod[ContentV2BarcodesCreateResponse]):
    """Генерация баркодов

    POST /content/v2/barcodes
    """

    __path__ = "/content/v2/barcodes"
    __http_method__ = "POST"
    __returns__ = ContentV2BarcodesCreateResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __items__ = "data"
    __body_fields__ = {"count": "count"}

    count: int | None = None
    """Кол-во баркодов которые надо сгенерировать, максимальное доступное количество баркодов для
    генерации - `5 000`
    """


class ContentV2CardsDeleteTrashCreate(WBMethod[ContentV2CardsDeleteTrashCreateResponse]):
    """Перенос карточек товаров в корзину

    POST /content/v2/cards/delete/trash
    """

    __path__ = "/content/v2/cards/delete/trash"
    __http_method__ = "POST"
    __returns__ = ContentV2CardsDeleteTrashCreateResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"nm_ids": "nmIDs"}

    nm_ids: list[int] | None = None
    """Артикулы WB"""


class ContentV2CardsErrorList(WBMethod[ResponsePublicViewerPublicErrorsTableListV2]):
    """Список несозданных карточек товаров с ошибками

    POST /content/v2/cards/error/list
    """

    __path__ = "/content/v2/cards/error/list"
    __http_method__ = "POST"
    __returns__ = ResponsePublicViewerPublicErrorsTableListV2
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (6000, 5)}
    __paginate__ = "cursor"
    __items__ = "data"
    __body_fields__ = {"cursor": "cursor", "order": "order"}

    cursor: SwaggerPublicErrorsCursorInput | None = None
    locale: str | None = None
    """Язык названий предметов:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не
    используется в песочнице
    """
    order: SwaggerPublicErrorsOrderV2 | None = None


class ContentV2CardsLimits(WBMethod[ContentV2CardsLimitsResponse]):
    """Лимиты карточек товаров

    GET /content/v2/cards/limits
    """

    __path__ = "/content/v2/cards/limits"
    __http_method__ = "GET"
    __returns__ = ContentV2CardsLimitsResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"


class ContentV2CardsMoveNmCreate(WBMethod[ResponseItemList]):
    """Объединение и разъединение карточек товаров

    POST /content/v2/cards/moveNm
    """

    __path__ = "/content/v2/cards/moveNm"
    __http_method__ = "POST"
    __returns__ = ResponseItemList
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __items__ = "data"

    body: RequestMoveNmsImtConn | list[Any] | dict[str, Any]


class ContentV2CardsRecoverCreate(WBMethod[ContentV2CardsRecoverCreateResponse]):
    """Восстановление карточек товаров из корзины

    POST /content/v2/cards/recover
    """

    __path__ = "/content/v2/cards/recover"
    __http_method__ = "POST"
    __returns__ = ContentV2CardsRecoverCreateResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (20000, 5),
        "service": (20000, 5),
        "basic_secret": (20000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"nm_ids": "nmIDs"}

    nm_ids: list[int] | None = None
    """Артикулы WB"""


class ContentV2CardsUpdateCreate(WBMethod[ResponseItemList]):
    """Редактирование карточек товаров

    POST /content/v2/cards/update
    """

    __path__ = "/content/v2/cards/update"
    __http_method__ = "POST"
    __returns__ = ResponseItemList
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (6000, 5)}
    __items__ = "data"

    body: list[ContentV2CardsUpdateCreateBodyItem] | list[Any] | dict[str, Any]


class ContentV2CardsUploadAddCreate(WBMethod[ResponseItemList]):
    """Создание карточек товаров с присоединением

    POST /content/v2/cards/upload/add
    """

    __path__ = "/content/v2/cards/upload/add"
    __http_method__ = "POST"
    __returns__ = ResponseItemList
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (6000, 5),
        "service": (6000, 5),
        "basic_secret": (6000, 5),
        "basic": (7200000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"imt_id": "imtID", "cards_to_add": "cardsToAdd"}

    cards_to_add: list[ContentV2CardsUploadAddCreateCardsToAddItem] | None = None
    """Добавляемые карточки товаров"""
    imt_id: int | None = None
    """`imtID` отдельной карточки товара или группы объединённых карточек товаров, к которой
    присоединяются создаваемые карточки
    """


class ContentV2CardsUploadCreate(WBMethod[ResponseItemList]):
    """Создание карточек товаров

    POST /content/v2/cards/upload
    """

    __path__ = "/content/v2/cards/upload"
    __http_method__ = "POST"
    __returns__ = ResponseItemList
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (6000, 5)}
    __items__ = "data"

    body: list[ContentV2CardsUploadCreateBodyItem] | list[Any] | dict[str, Any]


class ContentV2DirectoryColors(WBMethod[ContentV2DirectoryColorsResponse]):
    """Цвет

    GET /content/v2/directory/colors
    """

    __path__ = "/content/v2/directory/colors"
    __http_method__ = "GET"
    __returns__ = ContentV2DirectoryColorsResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class ContentV2DirectoryCountries(WBMethod[ContentV2DirectoryCountriesResponse]):
    """Страна производства

    GET /content/v2/directory/countries
    """

    __path__ = "/content/v2/directory/countries"
    __http_method__ = "GET"
    __returns__ = ContentV2DirectoryCountriesResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class ContentV2DirectoryKinds(WBMethod[ContentV2DirectoryKindsResponse]):
    """Пол

    GET /content/v2/directory/kinds
    """

    __path__ = "/content/v2/directory/kinds"
    __http_method__ = "GET"
    __returns__ = ContentV2DirectoryKindsResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class ContentV2DirectorySeasons(WBMethod[ContentV2DirectorySeasonsResponse]):
    """Сезон

    GET /content/v2/directory/seasons
    """

    __path__ = "/content/v2/directory/seasons"
    __http_method__ = "GET"
    __returns__ = ContentV2DirectorySeasonsResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class ContentV2DirectoryTnved(WBMethod[ContentV2DirectoryTnvedResponse]):
    """ТНВЭД-код

    GET /content/v2/directory/tnved
    """

    __path__ = "/content/v2/directory/tnved"
    __http_method__ = "GET"
    __returns__ = ContentV2DirectoryTnvedResponse
    __query_params__ = {"subject_id": "subjectID", "search": "search", "locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __items__ = "data"

    subject_id: int
    """ID предмета"""
    locale: str | None = None
    """Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский …"""
    search: int | None = None
    """Поиск по ТНВЭД-коду. Работает только в паре с `subjectID`"""


class ContentV2DirectoryVat(WBMethod[ContentV2DirectoryVatResponse]):
    """Ставка НДС

    GET /content/v2/directory/vat
    """

    __path__ = "/content/v2/directory/vat"
    __http_method__ = "GET"
    __returns__ = ContentV2DirectoryVatResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class ContentV2GetCardsList(WBMethod[ContentV2GetCardsListResponse]):
    """Список карточек товаров

    POST /content/v2/get/cards/list
    """

    __path__ = "/content/v2/get/cards/list"
    __http_method__ = "POST"
    __returns__ = ContentV2GetCardsListResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __paginate__ = "cursor"
    __items__ = "cards"
    __body_fields__ = {"settings": "settings"}

    locale: str | None = None
    """Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` — английский   -
    `zh` — китайский …
    """
    settings: ContentV2GetCardsListSettings | None = None
    """Настройки"""


class ContentV2GetCardsTrash(WBMethod[ContentV2GetCardsTrashResponse]):
    """Список карточек товаров в корзине

    POST /content/v2/get/cards/trash
    """

    __path__ = "/content/v2/get/cards/trash"
    __http_method__ = "POST"
    __returns__ = ContentV2GetCardsTrashResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __paginate__ = "cursor"
    __items__ = "cards"
    __body_fields__ = {"settings": "settings"}

    locale: str | None = None
    """Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` — английский   -
    `zh` — китайский …
    """
    settings: ContentV2GetCardsTrashSettings | None = None
    """Настройки"""


class ContentV2ObjectAll(WBMethod[ContentV2ObjectAllResponse]):
    """Список предметов

    GET /content/v2/object/all
    """

    __path__ = "/content/v2/object/all"
    __http_method__ = "GET"
    __returns__ = ContentV2ObjectAllResponse
    __query_params__ = {
        "locale": "locale",
        "name": "name",
        "limit": "limit",
        "offset": "offset",
        "parent_id": "parentID",
    }
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __paginate__ = "offset_query"
    __items__ = "data"

    limit: int | None = None
    """Количество предметов, максимум 1000"""
    locale: str | None = None
    """Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский …"""
    name: str | None = None
    """Поиск по названию предмета (Носки), поиск работает по подстроке, искать можно на любом из
    поддерживаемых языков
    """
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""
    parent_id: int | None = None
    """ID родительской категории предмета"""


class ContentV2ObjectCharcsSubjectId(WBMethod[ContentV2ObjectCharcsSubjectIdResponse]):
    """Характеристики предмета

    GET /content/v2/object/charcs/{subjectId}
    """

    __path__ = "/content/v2/object/charcs/{subjectId}"
    __http_method__ = "GET"
    __returns__ = ContentV2ObjectCharcsSubjectIdResponse
    __path_params__ = ("subjectId",)
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __items__ = "data"

    subject_id: str | int
    """ID предмета"""
    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class ContentV2ObjectParentAll(WBMethod[ContentV2ObjectParentAllResponse]):
    """Родительские категории товаров

    GET /content/v2/object/parent/all
    """

    __path__ = "/content/v2/object/parent/all"
    __http_method__ = "GET"
    __returns__ = ContentV2ObjectParentAllResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 5)}
    __items__ = "data"

    locale: str | None = None
    """Язык поля ответа `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский …
    """


class ContentV2TagCreate(WBMethod[ResponseContentError]):
    """Создание ярлыка

    POST /content/v2/tag
    """

    __path__ = "/content/v2/tag"
    __http_method__ = "POST"
    __returns__ = ResponseContentError
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"color": "color", "name": "name"}

    color: str | None = None
    """Цвет ярлыка.  Доступные цвета:   - `D1CFD7` — серый   - `FEE0E0` — красный   - `ECDAFF` —
    фиолетовый   - `E4EAFF` — синий   - `DEF1DD` — зеленый …
    """
    name: str | None = None
    """Имя ярлыка"""


class ContentV2TagIdDelete(WBMethod[ResponseContentError]):
    """Удаление ярлыка

    DELETE /content/v2/tag/{id}
    """

    __path__ = "/content/v2/tag/{id}"
    __http_method__ = "DELETE"
    __returns__ = ResponseContentError
    __path_params__ = ("id",)
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    id_: str | int
    """Числовой ID ярлыка"""


class ContentV2TagIdUpdate(WBMethod[ResponseContentError]):
    """Изменение ярлыка

    PATCH /content/v2/tag/{id}
    """

    __path__ = "/content/v2/tag/{id}"
    __http_method__ = "PATCH"
    __returns__ = ResponseContentError
    __path_params__ = ("id",)
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"color": "color", "name": "name"}

    id_: str | int
    """Числовой ID ярлыка"""
    color: str | None = None
    """Цвет ярлыка"""
    name: str | None = None
    """Имя ярлыка"""


class ContentV2TagNomenclatureLinkCreate(WBMethod[ResponseContentError]):
    """Управление ярлыками в карточке товара

    POST /content/v2/tag/nomenclature/link
    """

    __path__ = "/content/v2/tag/nomenclature/link"
    __http_method__ = "POST"
    __returns__ = ResponseContentError
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"nm_id": "nmID", "tags_ids": "tagsIDs"}

    nm_id: int | None = None
    """Артикул WB"""
    tags_ids: list[int] | None = None
    """Массив числовых ID ярлыков. Что бы снять ярлыки с карточки товара, необходимо передать
    пустой массив. …
    """


class ContentV2Tags(WBMethod[ContentV2TagsResponse]):
    """Список ярлыков

    GET /content/v2/tags
    """

    __path__ = "/content/v2/tags"
    __http_method__ = "GET"
    __returns__ = ContentV2TagsResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"


class ContentV3MediaFileCreate(WBMethod[ContentV3MediaFileCreateResponse]):
    """Загрузить медиафайл

    POST /content/v3/media/file
    """

    __path__ = "/content/v3/media/file"
    __http_method__ = "POST"
    __returns__ = ContentV3MediaFileCreateResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"


class ContentV3MediaSaveCreate(WBMethod[ContentV3MediaSaveCreateResponse]):
    """Загрузить медиафайлы по ссылкам

    POST /content/v3/media/save
    """

    __path__ = "/content/v3/media/save"
    __http_method__ = "POST"
    __returns__ = ContentV3MediaSaveCreateResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"nm_id": "nmId", "data": "data"}

    data: list[str] | None = None
    """Ссылки на изображения в том порядке, в котором они будут в карточке товара, и на видео, на
    любой позиции массива
    """
    nm_id: int | None = None
    """Артикул WB"""


class DbwWarehousesWarehouseIdContacts(WBMethod[DbwWarehousesWarehouseIdContactsResponse]):
    """Список контактов

    GET /api/v3/dbw/warehouses/{warehouseId}/contacts
    """

    __path__ = "/api/v3/dbw/warehouses/{warehouseId}/contacts"
    __http_method__ = "GET"
    __returns__ = DbwWarehousesWarehouseIdContactsResponse
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    warehouse_id: str | int
    """ID склада продавца"""


class DbwWarehousesWarehouseIdContactsUpdate(WBMethod[None]):
    """Обновить список контактов

    PUT /api/v3/dbw/warehouses/{warehouseId}/contacts
    """

    __path__ = "/api/v3/dbw/warehouses/{warehouseId}/contacts"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"contacts": "contacts"}

    warehouse_id: str | int
    """ID склада продавца"""
    contacts: list[DbwWarehousesWarehouseIdContactsUpdateContactsItem] | None = None


class DiscountsPricesV1UploadTaskB2bWholesaleUpdate(WBMethod[None]):
    """Установить оптовые скидки для B2B-продаж

    POST /api/discounts-prices/v1/upload/task/b2b/wholesale
    """

    __path__ = "/api/discounts-prices/v1/upload/task/b2b/wholesale"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __rate_limits__ = {"personal": (600, 5), "service": (600, 5)}


class HistoryGoodsTask(WBMethod[None]):
    """Детализация обработанной загрузки

    GET /api/v2/history/goods/task
    """

    __path__ = "/api/v2/history/goods/task"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"limit": "limit", "offset": "offset", "upload_id": "uploadID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    upload_id: int
    """ID загрузки"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class HistoryTasks(WBMethod[None]):
    """Состояние обработанной загрузки

    GET /api/v2/history/tasks
    """

    __path__ = "/api/v2/history/tasks"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"upload_id": "uploadID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }

    upload_id: int
    """ID загрузки"""


class ListGoodsFilterGet(WBMethod[None]):
    """Получить товары с ценами

    GET /api/v2/list/goods/filter
    """

    __path__ = "/api/v2/list/goods/filter"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"limit": "limit", "offset": "offset", "filter_nm_id": "filterNmID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    filter_nm_id: int | None = None
    """Артикул WB для поиска товара"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class ListGoodsFilterPost(WBMethod[None]):
    """Получить товары с ценами по артикулам

    POST /api/v2/list/goods/filter
    """

    __path__ = "/api/v2/list/goods/filter"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }


class ListGoodsSizeNm(WBMethod[None]):
    """Получить размеры товара с ценами

    GET /api/v2/list/goods/size/nm
    """

    __path__ = "/api/v2/list/goods/size/nm"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"limit": "limit", "offset": "offset", "nm_id": "nmID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    nm_id: int
    """Артикул WB"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class Offices(WBMethod[list[Office]]):
    """Получить список складов WB

    GET /api/v3/offices
    """

    __path__ = "/api/v3/offices"
    __http_method__ = "GET"
    __returns__ = list[Office]
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}


class QuarantineGoods(WBMethod[None]):
    """Получить товары в карантине

    GET /api/v2/quarantine/goods
    """

    __path__ = "/api/v2/quarantine/goods"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {"limit": "limit", "offset": "offset"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class StocksWarehouseId(WBMethod[StocksWarehouseIdResponse]):
    """Получить остатки товаров

    POST /api/v3/stocks/{warehouseId}
    """

    __path__ = "/api/v3/stocks/{warehouseId}"
    __http_method__ = "POST"
    __returns__ = StocksWarehouseIdResponse
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"chrt_ids": "chrtIds"}

    chrt_ids: list[int]
    """Массив ID размеров товаров"""
    warehouse_id: str | int
    """ID склада продавца"""


class StocksWarehouseIdDelete(WBMethod[None]):
    """Удалить остатки товаров

    DELETE /api/v3/stocks/{warehouseId}
    """

    __path__ = "/api/v3/stocks/{warehouseId}"
    __http_method__ = "DELETE"
    __returns__ = None
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (6000, 2)}
    __body_fields__ = {"chrt_ids": "chrtIds"}

    chrt_ids: list[int]
    """Массив ID размеров товаров"""
    warehouse_id: str | int
    """ID склада продавца"""


class StocksWarehouseIdUpdate(WBMethod[None]):
    """Обновить остатки товаров

    PUT /api/v3/stocks/{warehouseId}
    """

    __path__ = "/api/v3/stocks/{warehouseId}"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"stocks": "stocks"}

    stocks: list[StocksWarehouseIdUpdateStocksItem]
    """Массив ID размеров товаров и их остатков"""
    warehouse_id: str | int
    """ID склада продавца"""


class UploadTaskClubDiscountUpdate(WBMethod[None]):
    """Установить скидки WB Клуба

    POST /api/v2/upload/task/club-discount
    """

    __path__ = "/api/v2/upload/task/club-discount"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }


class UploadTaskSizeUpdate(WBMethod[None]):
    """Установить цены для размеров

    POST /api/v2/upload/task/size
    """

    __path__ = "/api/v2/upload/task/size"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }


class UploadTaskUpdate(WBMethod[None]):
    """Установить цены и скидки

    POST /api/v2/upload/task
    """

    __path__ = "/api/v2/upload/task"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (600, 5),
        "service": (600, 5),
        "basic_secret": (600, 5),
        "basic": (900000, 1),
    }


class Warehouses(WBMethod[list[Warehouse]]):
    """Получить список складов продавца

    GET /api/v3/warehouses
    """

    __path__ = "/api/v3/warehouses"
    __http_method__ = "GET"
    __returns__ = list[Warehouse]
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}


class WarehousesCreate(WBMethod[WarehousesCreateResponse]):
    """Создать склад продавца

    POST /api/v3/warehouses
    """

    __path__ = "/api/v3/warehouses"
    __http_method__ = "POST"
    __returns__ = WarehousesCreateResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"name": "name", "office_id": "officeId"}

    name: str
    """Имя склада продавца"""
    office_id: int
    """ID склада WB.Нельзя привязывать склад WB, который уже используется"""


class WarehousesWarehouseIdDelete(WBMethod[None]):
    """Удалить склад продавца

    DELETE /api/v3/warehouses/{warehouseId}
    """

    __path__ = "/api/v3/warehouses/{warehouseId}"
    __http_method__ = "DELETE"
    __returns__ = None
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    warehouse_id: str | int
    """ID склада продавца"""


class WarehousesWarehouseIdUpdate(WBMethod[None]):
    """Обновить склад продавца

    PUT /api/v3/warehouses/{warehouseId}
    """

    __path__ = "/api/v3/warehouses/{warehouseId}"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"name": "name", "office_id": "officeId"}

    name: str
    """Имя склада продавца"""
    office_id: int
    """ID склада WB.Нельзя привязывать склад WB, который уже используется.Можно менять не чаще
    одного раза в сутки
    """
    warehouse_id: str | int
    """ID склада продавца"""
