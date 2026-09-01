# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from typing import Any

from ..client.method import WBMethod
from ..utils.token import Scope
from .models import (
    BrandsResponse,
    CreateBarcodeResponse,
    CreateCardsUploadAddCardsToAddItem,
    CreateCardsUploadBodyItem,
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
    RequestMoveNmsImtConn,
    ResponseContentError,
    ResponseItemList,
    ResponsePublicViewerPublicErrorsTableListV2,
    SetDiscountsPricesUploadTaskB2bWholesaleResponse,
    SetRecommendationRecListItem,
    SetRecomRes,
    SwaggerPublicErrorsCursorInput,
    SwaggerPublicErrorsOrderV2,
    TaskCreated,
    UpdateCardBodyItem,
    UpdateCardsDeleteTrashResponse,
    UpdateCardsRecoverResponse,
    UpdateDbwWarehousesContactContactsItem,
    UpdateStockStocksItem,
    UploadMediaFileResponse,
    UploadMediaSaveResponse,
    Warehouse,
)


class CreateBarcode(WBMethod[CreateBarcodeResponse]):
    """Генерация баркодов

    POST /content/v2/barcodes
    """

    __path__ = "/content/v2/barcodes"
    __http_method__ = "POST"
    __returns__ = CreateBarcodeResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __items__ = "data"
    __body_fields__ = {"count": "count"}
    __body_required__ = True

    count: int | None = None
    """Кол-во баркодов которые надо сгенерировать, максимальное доступное количество баркодов для
    генерации - `5 000`
    """


class CreateCardsUpload(WBMethod[ResponseItemList]):
    """Создание карточек товаров

    POST /content/v2/cards/upload
    """

    __path__ = "/content/v2/cards/upload"
    __http_method__ = "POST"
    __returns__ = ResponseItemList
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (30000, 5)}
    __items__ = "data"

    body: list[CreateCardsUploadBodyItem] | list[Any] | dict[str, Any]


class CreateCardsUploadAdd(WBMethod[ResponseItemList]):
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
        "personal": (30000, 5),
        "service": (30000, 5),
        "basic_secret": (30000, 5),
        "basic": (7200000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"imt_id": "imtID", "cards_to_add": "cardsToAdd"}

    cards_to_add: list[CreateCardsUploadAddCardsToAddItem] | None = None
    """Добавляемые карточки товаров"""
    imt_id: int | None = None
    """`imtID` отдельной карточки товара или группы объединённых карточек товаров, к которой
    присоединяются создаваемые карточки
    """


class CreateTag(WBMethod[ResponseContentError]):
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
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"color": "color", "name": "name"}
    __body_required__ = True

    color: str | None = None
    """Цвет ярлыка.  Доступные цвета:   - `D1CFD7` — серый   - `FEE0E0` — красный   - `ECDAFF` —
    фиолетовый   - `E4EAFF` — синий   - `DEF1DD` — зеленый …
    """
    name: str | None = None
    """Имя ярлыка"""


class CreateTagNomenclatureLink(WBMethod[ResponseContentError]):
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
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"nm_id": "nmID", "tags_ids": "tagsIDs"}
    __body_required__ = True

    nm_id: int | None = None
    """Артикул WB"""
    tags_ids: list[int] | None = None
    """Массив числовых ID ярлыков. Что бы снять ярлыки с карточки товара, необходимо передать
    пустой массив. …
    """


class CreateWarehouse(WBMethod[CreateWarehouseResponse]):
    """Создать склад продавца

    POST /api/v3/warehouses
    """

    __path__ = "/api/v3/warehouses"
    __http_method__ = "POST"
    __returns__ = CreateWarehouseResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (4000, 20)}
    __body_fields__ = {"name": "name", "office_id": "officeId"}
    __body_required__ = True

    name: str
    """Имя склада продавца"""
    office_id: int
    """ID склада WB.Нельзя привязывать склад WB, который уже используется"""


class DeleteStock(WBMethod[None]):
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
    __rate_limits__ = {"all": (12000, 2)}
    __body_fields__ = {"chrt_ids": "chrtIds"}
    __body_required__ = True

    chrt_ids: list[int]
    """Массив ID размеров товаров"""
    warehouse_id: str | int
    """ID склада продавца"""


class DeleteTag(WBMethod[ResponseContentError]):
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
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    id_: str | int
    """Числовой ID ярлыка"""


class DeleteWarehouse(WBMethod[None]):
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
    __rate_limits__ = {"all": (4000, 20)}

    warehouse_id: str | int
    """ID склада продавца"""


class GetBrands(WBMethod[BrandsResponse]):
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
        "personal": (5000, 5),
        "service": (5000, 5),
        "basic_secret": (5000, 5),
        "basic": (3600000, 1),
    }
    __paginate__ = "next"

    subject_id: int
    """ID предмета"""
    next_: int | None = None
    """Параметр пагинации. Используйте значение `next` из ответа, чтобы получить следующий пакет
    данных
    """


class GetBufferGoodsTask(WBMethod[GetBufferGoodsTaskResponse]):
    """Детализация необработанной загрузки

    GET /api/v2/buffer/goods/task
    """

    __path__ = "/api/v2/buffer/goods/task"
    __http_method__ = "GET"
    __returns__ = GetBufferGoodsTaskResponse
    __query_params__ = {"limit": "limit", "offset": "offset", "upload_id": "uploadID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"
    __items__ = "data"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    upload_id: int
    """ID загрузки"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class GetBufferTasks(WBMethod[GetBufferTasksResponse]):
    """Состояние необработанной загрузки

    GET /api/v2/buffer/tasks
    """

    __path__ = "/api/v2/buffer/tasks"
    __http_method__ = "GET"
    __returns__ = GetBufferTasksResponse
    __query_params__ = {"upload_id": "uploadID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __items__ = "data"

    upload_id: int
    """ID загрузки"""


class GetCardsErrorList(WBMethod[ResponsePublicViewerPublicErrorsTableListV2]):
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
    __rate_limits__ = {"all": (30000, 5)}
    __paginate__ = "cursor"
    __items__ = "data"
    __body_fields__ = {"cursor": "cursor", "order": "order"}
    __body_required__ = True

    cursor: SwaggerPublicErrorsCursorInput | None = None
    """Пагинатор"""
    locale: str | None = None
    """Язык названий предметов:   - `ru` — русский   - `en` — английский   - `zh` — китайский  Не
    используется в песочнице
    """
    order: SwaggerPublicErrorsOrderV2 | None = None
    """Порядок выдачи пакетов"""


class GetCardsLimits(WBMethod[GetCardsLimitsResponse]):
    """Лимиты карточек товаров

    GET /content/v2/cards/limits
    """

    __path__ = "/content/v2/cards/limits"
    __http_method__ = "GET"
    __returns__ = GetCardsLimitsResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"


class GetCardsList(WBMethod[GetCardsListResponse]):
    """Список карточек товаров

    POST /content/v2/get/cards/list
    """

    __path__ = "/content/v2/get/cards/list"
    __http_method__ = "POST"
    __returns__ = GetCardsListResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __paginate__ = "cursor"
    __items__ = "cards"
    __body_fields__ = {"settings": "settings"}
    __body_required__ = True

    locale: str | None = None
    """Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` — английский   -
    `zh` — китайский …
    """
    settings: GetCardsListSettings | None = None
    """Настройки"""


class GetCardsTrash(WBMethod[GetCardsTrashResponse]):
    """Список карточек товаров в корзине

    POST /content/v2/get/cards/trash
    """

    __path__ = "/content/v2/get/cards/trash"
    __http_method__ = "POST"
    __returns__ = GetCardsTrashResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __paginate__ = "cursor"
    __items__ = "cards"
    __body_fields__ = {"settings": "settings"}
    __body_required__ = True

    locale: str | None = None
    """Язык полей ответа `name`, `value` и `object`:   - `ru` — русский   - `en` — английский   -
    `zh` — китайский …
    """
    settings: GetCardsTrashSettings | None = None
    """Настройки"""


class GetDbwWarehousesContacts(WBMethod[GetDbwWarehousesContactsResponse]):
    """Список контактов

    GET /api/v3/dbw/warehouses/{warehouseId}/contacts
    """

    __path__ = "/api/v3/dbw/warehouses/{warehouseId}/contacts"
    __http_method__ = "GET"
    __returns__ = GetDbwWarehousesContactsResponse
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (4000, 20)}

    warehouse_id: str | int
    """ID склада продавца"""


class GetDirectoryColors(WBMethod[GetDirectoryColorsResponse]):
    """Цвет

    GET /content/v2/directory/colors
    """

    __path__ = "/content/v2/directory/colors"
    __http_method__ = "GET"
    __returns__ = GetDirectoryColorsResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class GetDirectoryCountries(WBMethod[GetDirectoryCountriesResponse]):
    """Страна производства

    GET /content/v2/directory/countries
    """

    __path__ = "/content/v2/directory/countries"
    __http_method__ = "GET"
    __returns__ = GetDirectoryCountriesResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class GetDirectoryKinds(WBMethod[GetDirectoryKindsResponse]):
    """Пол

    GET /content/v2/directory/kinds
    """

    __path__ = "/content/v2/directory/kinds"
    __http_method__ = "GET"
    __returns__ = GetDirectoryKindsResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class GetDirectorySeasons(WBMethod[GetDirectorySeasonsResponse]):
    """Сезон

    GET /content/v2/directory/seasons
    """

    __path__ = "/content/v2/directory/seasons"
    __http_method__ = "GET"
    __returns__ = GetDirectorySeasonsResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class GetDirectoryTnved(WBMethod[GetDirectoryTnvedResponse]):
    """ТНВЭД-код

    GET /content/v2/directory/tnved
    """

    __path__ = "/content/v2/directory/tnved"
    __http_method__ = "GET"
    __returns__ = GetDirectoryTnvedResponse
    __query_params__ = {"subject_id": "subjectID", "search": "search", "locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __items__ = "data"

    subject_id: int
    """ID предмета"""
    locale: str | None = None
    """Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский …"""
    search: int | None = None
    """Поиск по ТНВЭД-коду. Работает только в паре с `subjectID`"""


class GetDirectoryVat(WBMethod[GetDirectoryVatResponse]):
    """Ставка НДС

    GET /content/v2/directory/vat
    """

    __path__ = "/content/v2/directory/vat"
    __http_method__ = "GET"
    __returns__ = GetDirectoryVatResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"

    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class GetGoodsFilterGet(WBMethod[GetGoodsFilterResponse]):
    """Получить товары с ценами

    GET /api/v2/list/goods/filter
    """

    __path__ = "/api/v2/list/goods/filter"
    __http_method__ = "GET"
    __returns__ = GetGoodsFilterResponse
    __query_params__ = {"limit": "limit", "offset": "offset", "filter_nm_id": "filterNmID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"
    __items__ = "data"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    filter_nm_id: int | None = None
    """Артикул WB для поиска товара"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class GetGoodsFilterPost(WBMethod[GetGoodsFilterResponse]):
    """Получить товары с ценами по артикулам

    POST /api/v2/list/goods/filter
    """

    __path__ = "/api/v2/list/goods/filter"
    __http_method__ = "POST"
    __returns__ = GetGoodsFilterResponse
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __items__ = "data"


class GetGoodsSizeNm(WBMethod[GetGoodsSizeNmResponse]):
    """Получить размеры товара с ценами

    GET /api/v2/list/goods/size/nm
    """

    __path__ = "/api/v2/list/goods/size/nm"
    __http_method__ = "GET"
    __returns__ = GetGoodsSizeNmResponse
    __query_params__ = {"limit": "limit", "offset": "offset", "nm_id": "nmID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"
    __items__ = "data"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    nm_id: int
    """Артикул WB"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class GetHistoryGoodsTask(WBMethod[GetHistoryGoodsTaskResponse]):
    """Детализация обработанной загрузки

    GET /api/v2/history/goods/task
    """

    __path__ = "/api/v2/history/goods/task"
    __http_method__ = "GET"
    __returns__ = GetHistoryGoodsTaskResponse
    __query_params__ = {"limit": "limit", "offset": "offset", "upload_id": "uploadID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"
    __items__ = "data"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    upload_id: int
    """ID загрузки"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class GetHistoryTasks(WBMethod[GetHistoryTasksResponse]):
    """Состояние обработанной загрузки

    GET /api/v2/history/tasks
    """

    __path__ = "/api/v2/history/tasks"
    __http_method__ = "GET"
    __returns__ = GetHistoryTasksResponse
    __query_params__ = {"upload_id": "uploadID"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __items__ = "data"

    upload_id: int
    """ID загрузки"""


class GetObjectAll(WBMethod[GetObjectAllResponse]):
    """Список предметов

    GET /content/v2/object/all
    """

    __path__ = "/content/v2/object/all"
    __http_method__ = "GET"
    __returns__ = GetObjectAllResponse
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
    __rate_limits__ = {"all": (3000, 5)}
    __paginate__ = "offset_query"
    __items__ = "data"

    limit: int | None = 30
    """Количество предметов, максимум 1000"""
    locale: str | None = None
    """Язык полей ответа:   - `ru` — русский   - `en` — английский   - `zh` — китайский …"""
    name: str | None = None
    """Поиск по названию предмета (Носки), поиск работает по подстроке, искать можно на любом из
    поддерживаемых языков
    """
    offset: int | None = 0
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""
    parent_id: int | None = None
    """ID родительской категории предмета"""


class GetObjectCharcs(WBMethod[GetObjectCharcsResponse]):
    """Характеристики предмета

    GET /content/v2/object/charcs/{subjectId}
    """

    __path__ = "/content/v2/object/charcs/{subjectId}"
    __http_method__ = "GET"
    __returns__ = GetObjectCharcsResponse
    __path_params__ = ("subjectId",)
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __items__ = "data"

    subject_id: str | int
    """ID предмета"""
    locale: str | None = None
    """Язык полей ответа `subjectName` и `name`:   - `ru` — русский   - `en` — английский   - `zh`
    — китайский …
    """


class GetObjectParentAll(WBMethod[GetObjectParentAllResponse]):
    """Родительские категории товаров

    GET /content/v2/object/parent/all
    """

    __path__ = "/content/v2/object/parent/all"
    __http_method__ = "GET"
    __returns__ = GetObjectParentAllResponse
    __query_params__ = {"locale": "locale"}
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __items__ = "data"

    locale: str | None = None
    """Язык поля ответа `name`:   - `ru` — русский   - `en` — английский   - `zh` — китайский …
    """


class GetOffices(WBMethod[list[Office]]):
    """Получить список складов WB

    GET /api/v3/offices
    """

    __path__ = "/api/v3/offices"
    __http_method__ = "GET"
    __returns__ = list[Office]
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (4000, 20)}


class GetQuarantineGoods(WBMethod[GetQuarantineGoodsResponse]):
    """Получить товары в карантине

    GET /api/v2/quarantine/goods
    """

    __path__ = "/api/v2/quarantine/goods"
    __http_method__ = "GET"
    __returns__ = GetQuarantineGoodsResponse
    __query_params__ = {"limit": "limit", "offset": "offset"}
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __paginate__ = "offset_query"
    __items__ = "data"

    limit: int
    """Сколько элементов вывести на одной странице (пагинация)"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения `10` ответ начнется с 11 элемента"""


class GetRecommendationsList(WBMethod[GetRecomRes]):
    """Список рекомендаций в карточках товаров

    POST /api/content/v1/recommendations/list
    """

    __path__ = "/api/content/v1/recommendations/list"
    __http_method__ = "POST"
    __returns__ = GetRecomRes
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
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
    limit: int | None = 20
    """Количество товаров в ответе"""
    next_: int | None = 0
    """Курсор. Последний `nmId` в ответе"""
    search: str | None = None
    """Поиск:   - по артикулу WB `nmId` — полное совпадение   - по артикулу продавца `vendorCode` —
    частичное совпадение
    """
    subject_ids: list[int] | None = None
    """ID предметов"""


class GetStocks(WBMethod[GetStocksResponse]):
    """Получить остатки товаров

    POST /api/v3/stocks/{warehouseId}
    """

    __path__ = "/api/v3/stocks/{warehouseId}"
    __http_method__ = "POST"
    __returns__ = GetStocksResponse
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (4000, 20)}
    __body_fields__ = {"chrt_ids": "chrtIds"}
    __body_required__ = True

    chrt_ids: list[int]
    """Массив ID размеров товаров"""
    warehouse_id: str | int
    """ID склада продавца"""


class GetTags(WBMethod[GetTagsResponse]):
    """Список ярлыков

    GET /content/v2/tags
    """

    __path__ = "/content/v2/tags"
    __http_method__ = "GET"
    __returns__ = GetTagsResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"


class GetWarehouses(WBMethod[list[Warehouse]]):
    """Получить список складов продавца

    GET /api/v3/warehouses
    """

    __path__ = "/api/v3/warehouses"
    __http_method__ = "GET"
    __returns__ = list[Warehouse]
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (4000, 20)}


class SetDiscountsPricesUploadTaskB2bWholesale(WBMethod[SetDiscountsPricesUploadTaskB2bWholesaleResponse]):
    """Установить оптовые скидки для B2B-продаж

    POST /api/discounts-prices/v1/upload/task/b2b/wholesale
    """

    __path__ = "/api/discounts-prices/v1/upload/task/b2b/wholesale"
    __http_method__ = "POST"
    __returns__ = SetDiscountsPricesUploadTaskB2bWholesaleResponse
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __rate_limits__ = {"personal": (3000, 5), "service": (3000, 5)}


class SetRecommendation(WBMethod[SetRecomRes]):
    """Установить рекомендации для товаров

    POST /api/content/v1/recommendations/set
    """

    __path__ = "/api/content/v1/recommendations/set"
    __http_method__ = "POST"
    __returns__ = SetRecomRes
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __body_fields__ = {"rec_list": "recList", "replace": "replace"}
    __body_required__ = True

    rec_list: list[SetRecommendationRecListItem]
    """Список рекомендаций для товаров"""
    replace: bool | None = False
    """Действие в запросе:   - `false` — добавить новые рекомендации к существующим   - `true` —
    заменить существующие рекомендации новыми
    """


class SetUploadTask(WBMethod[TaskCreated]):
    """Установить цены и скидки

    POST /api/v2/upload/task
    """

    __path__ = "/api/v2/upload/task"
    __http_method__ = "POST"
    __returns__ = TaskCreated
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __items__ = "data"


class SetUploadTaskClubDiscount(WBMethod[TaskCreated]):
    """Установить скидки WB Клуба

    POST /api/v2/upload/task/club-discount
    """

    __path__ = "/api/v2/upload/task/club-discount"
    __http_method__ = "POST"
    __returns__ = TaskCreated
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __items__ = "data"


class SetUploadTaskSize(WBMethod[TaskCreated]):
    """Установить цены для размеров

    POST /api/v2/upload/task/size
    """

    __path__ = "/api/v2/upload/task/size"
    __http_method__ = "POST"
    __returns__ = TaskCreated
    __scope__ = Scope.PRICES
    __host__ = "https://discounts-prices-api.wildberries.ru"
    __sandbox_host__ = "https://discounts-prices-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (900000, 1),
    }
    __items__ = "data"


class UpdateCard(WBMethod[ResponseItemList]):
    """Редактирование карточек товаров

    POST /content/v2/cards/update
    """

    __path__ = "/content/v2/cards/update"
    __http_method__ = "POST"
    __returns__ = ResponseItemList
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (30000, 5)}
    __items__ = "data"

    body: list[UpdateCardBodyItem] | list[Any] | dict[str, Any]


class UpdateCardsDeleteTrash(WBMethod[UpdateCardsDeleteTrashResponse]):
    """Перенос карточек товаров в корзину

    POST /content/v2/cards/delete/trash
    """

    __path__ = "/content/v2/cards/delete/trash"
    __http_method__ = "POST"
    __returns__ = UpdateCardsDeleteTrashResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"nm_ids": "nmIDs"}
    __body_required__ = True

    nm_ids: list[int] | None = None
    """Артикулы WB"""


class UpdateCardsMoveNm(WBMethod[ResponseItemList]):
    """Объединение и разъединение карточек товаров

    POST /content/v2/cards/moveNm
    """

    __path__ = "/content/v2/cards/moveNm"
    __http_method__ = "POST"
    __returns__ = ResponseItemList
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 5)}
    __items__ = "data"

    body: RequestMoveNmsImtConn | list[Any] | dict[str, Any]


class UpdateCardsRecover(WBMethod[UpdateCardsRecoverResponse]):
    """Восстановление карточек товаров из корзины

    POST /content/v2/cards/recover
    """

    __path__ = "/content/v2/cards/recover"
    __http_method__ = "POST"
    __returns__ = UpdateCardsRecoverResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (100000, 5),
        "service": (100000, 5),
        "basic_secret": (100000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"nm_ids": "nmIDs"}
    __body_required__ = True

    nm_ids: list[int] | None = None
    """Артикулы WB"""


class UpdateDbwWarehousesContact(WBMethod[None]):
    """Обновить список контактов

    PUT /api/v3/dbw/warehouses/{warehouseId}/contacts
    """

    __path__ = "/api/v3/dbw/warehouses/{warehouseId}/contacts"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("warehouseId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (4000, 20)}
    __body_fields__ = {"contacts": "contacts"}
    __body_required__ = True

    warehouse_id: str | int
    """ID склада продавца"""
    contacts: list[UpdateDbwWarehousesContactContactsItem] | None = None
    """Не более 5 элементов"""


class UpdateStock(WBMethod[None]):
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
    __rate_limits__ = {"all": (4000, 20)}
    __body_fields__ = {"stocks": "stocks"}

    stocks: list[UpdateStockStocksItem]
    """Массив ID размеров товаров и их остатков"""
    warehouse_id: str | int
    """ID склада продавца"""


class UpdateTag(WBMethod[ResponseContentError]):
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
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"color": "color", "name": "name"}
    __body_required__ = True

    id_: str | int
    """Числовой ID ярлыка"""
    color: str | None = None
    """Цвет ярлыка"""
    name: str | None = None
    """Имя ярлыка"""


class UpdateWarehouse(WBMethod[None]):
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
    __rate_limits__ = {"all": (4000, 20)}
    __body_fields__ = {"name": "name", "office_id": "officeId"}
    __body_required__ = True

    name: str
    """Имя склада продавца"""
    office_id: int
    """ID склада WB.Нельзя привязывать склад WB, который уже используется.Можно менять не чаще
    одного раза в сутки
    """
    warehouse_id: str | int
    """ID склада продавца"""


class UploadMediaFile(WBMethod[UploadMediaFileResponse]):
    """Загрузить медиафайл

    POST /content/v3/media/file
    """

    __path__ = "/content/v3/media/file"
    __http_method__ = "POST"
    __returns__ = UploadMediaFileResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_required__ = True


class UploadMediaSave(WBMethod[UploadMediaSaveResponse]):
    """Загрузить медиафайлы по ссылкам

    POST /content/v3/media/save
    """

    __path__ = "/content/v3/media/save"
    __http_method__ = "POST"
    __returns__ = UploadMediaSaveResponse
    __scope__ = Scope.CONTENT
    __host__ = "https://content-api.wildberries.ru"
    __sandbox_host__ = "https://content-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 5),
        "service": (3000, 5),
        "basic_secret": (3000, 5),
        "basic": (1800000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"nm_id": "nmId", "data": "data"}
    __body_required__ = True

    data: list[str] | None = None
    """Ссылки на изображения в том порядке, в котором они будут в карточке товара, и на видео, на
    любой позиции массива
    """
    nm_id: int | None = None
    """Артикул WB"""
