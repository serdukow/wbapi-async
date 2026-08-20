from __future__ import annotations

from ...client.method import WBMethod
from ...utils.token import Scope
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


class Orders(WBMethod[OrdersResponse]):
    """Получить информацию о сборочных заданиях

    GET /api/v3/orders
    """

    __path__ = "/api/v3/orders"
    __http_method__ = "GET"
    __returns__ = OrdersResponse
    __query_params__ = {"limit": "limit", "next_": "next", "date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __paginate__ = "next"
    __items__ = "orders"

    limit: int
    """Параметр пагинации. Устанавливает предельное количество возвращаемых данных."""
    next_: int
    """Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных.
    Для получения полного списка данных должен быть равен `0` в первом …
    """
    date_from: int | None = None
    """Дата начала периода в формате Unix timestamp. По умолчанию — дата за 30 дней до запроса.
    Часовой пояс — UTC
    """
    date_to: int | None = None
    """Дата конца периода в формате Unix timestamp. Часовой пояс — UTC"""


class OrdersArchive(WBMethod[V3ArchiveOrders]):
    """Получить список архивных сборочных заданий

    GET /api/marketplace/v3/fbs/orders/archive
    """

    __path__ = "/api/marketplace/v3/fbs/orders/archive"
    __http_method__ = "GET"
    __returns__ = V3ArchiveOrders
    __query_params__ = {"year": "year", "month": "month", "next_": "next", "limit": "limit"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __paginate__ = "next"
    __items__ = "orders"

    limit: int
    """Количество сборочных заданий в ответе"""
    month: int
    """Месяц создания заказа"""
    next_: int
    """Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных.
    Для получения полного списка данных должен быть равен `0` в первом …
    """
    year: int
    """Год создания заказа"""


class OrdersClientCreate(WBMethod[CrossborderTurkeyClientInfoResp]):
    """Заказы с информацией по клиенту

    POST /api/v3/orders/client
    """

    __path__ = "/api/v3/orders/client"
    __http_method__ = "POST"
    __returns__ = CrossborderTurkeyClientInfoResp
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список заказов"""


class OrdersMeta(WBMethod[V3OrdersMetaAPI]):
    """Получить идентификаторы маркировки сборочных заданий

    POST /api/marketplace/v3/orders/meta
    """

    __path__ = "/api/marketplace/v3/orders/meta"
    __http_method__ = "POST"
    __returns__ = V3OrdersMetaAPI
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int]


class OrdersNew(WBMethod[OrdersNewResponse]):
    """Получить список новых сборочных заданий

    GET /api/v3/orders/new
    """

    __path__ = "/api/v3/orders/new"
    __http_method__ = "GET"
    __returns__ = OrdersNewResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"


class OrdersOrderIdCancel(WBMethod[None]):
    """Отменить сборочное задание

    PATCH /api/v3/orders/{orderId}/cancel
    """

    __path__ = "/api/v3/orders/{orderId}/cancel"
    __http_method__ = "PATCH"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (600, 20)}

    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaCustomsDeclarationUpdate(WBMethod[None]):
    """Закрепить номер ДТ за сборочным заданием

    PUT /api/marketplace/v3/orders/{orderId}/meta/customs-declaration
    """

    __path__ = "/api/marketplace/v3/orders/{orderId}/meta/customs-declaration"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"customs_declaration": "customsDeclaration"}

    customs_declaration: str
    """Номер ДТ"""
    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaDelete(WBMethod[None]):
    """Удалить идентификаторы маркировки сборочного задания

    DELETE /api/v3/orders/{orderId}/meta
    """

    __path__ = "/api/v3/orders/{orderId}/meta"
    __http_method__ = "DELETE"
    __returns__ = None
    __path_params__ = ("orderId",)
    __query_params__ = {"key": "key"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    key: str
    """Название идентификаторов маркировки для удаления. Передаётся только одно значение."""
    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaExpirationUpdate(WBMethod[None]):
    """Закрепить за сборочным заданием срок годности товара

    PUT /api/v3/orders/{orderId}/meta/expiration
    """

    __path__ = "/api/v3/orders/{orderId}/meta/expiration"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"expiration": "expiration"}

    expiration: str
    """Дата, до которой годен товар. Не менее 30 дней с текущей даты"""
    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaGtinUpdate(WBMethod[None]):
    """Закрепить GTIN за сборочным заданием

    PUT /api/v3/orders/{orderId}/meta/gtin
    """

    __path__ = "/api/v3/orders/{orderId}/meta/gtin"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"gtin": "gtin"}

    gtin: str
    """GTIN"""
    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaImeiUpdate(WBMethod[None]):
    """Закрепить IMEI за сборочным заданием

    PUT /api/v3/orders/{orderId}/meta/imei
    """

    __path__ = "/api/v3/orders/{orderId}/meta/imei"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"imei": "imei"}

    imei: str
    """IMEI"""
    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaSgtinUpdate(WBMethod[None]):
    """Закрепить код маркировки Честного знака за сборочным заданием

    PUT /api/v3/orders/{orderId}/meta/sgtin
    """

    __path__ = "/api/v3/orders/{orderId}/meta/sgtin"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"sgtins": "sgtins"}

    order_id: str | int
    """ID сборочного задания"""
    sgtins: list[str]
    """Массив кодов маркировки Честного знака. Вы можете передать коды маркировки:   - полностью —
    с GS-разделителями и кодом проверки подлинности (криптохвостом) …
    """


class OrdersOrderIdMetaUinUpdate(WBMethod[None]):
    """Закрепить УИН за сборочным заданием

    PUT /api/v3/orders/{orderId}/meta/uin
    """

    __path__ = "/api/v3/orders/{orderId}/meta/uin"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"uin": "uin"}

    order_id: str | int
    """ID сборочного задания"""
    uin: str
    """УИН"""


class OrdersStatus(WBMethod[OrdersStatusResponse]):
    """Получить статусы сборочных заданий

    POST /api/v3/orders/status
    """

    __path__ = "/api/v3/orders/status"
    __http_method__ = "POST"
    __returns__ = OrdersStatusResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int]
    """Список ID сборочных заданий"""


class OrdersStatusHistory(WBMethod[OrdersStatusHistoryResponse]):
    """История статусов для сборочных заданий трансграничных поставок

    POST /api/v3/orders/status/history
    """

    __path__ = "/api/v3/orders/status/history"
    __http_method__ = "POST"
    __returns__ = OrdersStatusHistoryResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """ID сборочных заданий"""


class OrdersStickers(WBMethod[OrdersStickersResponse]):
    """Получить стикеры сборочных заданий

    POST /api/v3/orders/stickers
    """

    __path__ = "/api/v3/orders/stickers"
    __http_method__ = "POST"
    __returns__ = OrdersStickersResponse
    __query_params__ = {"type_": "type", "width": "width", "height": "height"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"orders": "orders"}

    height: int
    """Высота стикера"""
    type_: str
    """Тип стикера"""
    width: int
    """Ширина стикера"""
    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class OrdersStickersCrossBorder(WBMethod[OrdersStickersCrossBorderResponse]):
    """Получить стикеры сборочных заданий трансграничных поставок

    POST /api/v3/orders/stickers/cross-border
    """

    __path__ = "/api/v3/orders/stickers/cross-border"
    __http_method__ = "POST"
    __returns__ = OrdersStickersCrossBorderResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class Passes(WBMethod[list[Pass]]):
    """Получить список пропусков

    GET /api/v3/passes
    """

    __path__ = "/api/v3/passes"
    __http_method__ = "GET"
    __returns__ = list[Pass]
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}


class PassesCreate(WBMethod[PassesCreateResponse]):
    """Создать пропуск

    POST /api/v3/passes
    """

    __path__ = "/api/v3/passes"
    __http_method__ = "POST"
    __returns__ = PassesCreateResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __body_fields__ = {
        "first_name": "firstName",
        "last_name": "lastName",
        "car_model": "carModel",
        "car_number": "carNumber",
        "office_id": "officeId",
    }

    car_model: str
    """Марка машины"""
    car_number: str
    """Номер машины"""
    first_name: str
    """Имя водителя"""
    last_name: str
    """Фамилия водителя"""
    office_id: int
    """ID склада"""


class PassesOffices(WBMethod[list[PassOffice]]):
    """Получить список складов, для которых требуется пропуск

    GET /api/v3/passes/offices
    """

    __path__ = "/api/v3/passes/offices"
    __http_method__ = "GET"
    __returns__ = list[PassOffice]
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}


class PassesPassIdDelete(WBMethod[None]):
    """Удалить пропуск

    DELETE /api/v3/passes/{passId}
    """

    __path__ = "/api/v3/passes/{passId}"
    __http_method__ = "DELETE"
    __returns__ = None
    __path_params__ = ("passId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    pass_id: str | int
    """ID пропуска"""


class PassesPassIdUpdate(WBMethod[None]):
    """Обновить пропуск

    PUT /api/v3/passes/{passId}
    """

    __path__ = "/api/v3/passes/{passId}"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("passId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {
        "first_name": "firstName",
        "last_name": "lastName",
        "car_model": "carModel",
        "car_number": "carNumber",
        "office_id": "officeId",
    }

    car_model: str
    """Марка машины"""
    car_number: str
    """Номер машины"""
    first_name: str
    """Имя водителя"""
    last_name: str
    """Фамилия водителя"""
    office_id: int
    """ID склада"""
    pass_id: str | int
    """ID пропуска"""


class SettingsAutoreturns(WBMethod[SettingsAutoreturnsResponse]):
    """Получить настройки автовозврата продавца

    GET /api/marketplace/v3/fbs/settings/autoreturns
    """

    __path__ = "/api/marketplace/v3/fbs/settings/autoreturns"
    __http_method__ = "GET"
    __returns__ = SettingsAutoreturnsResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}


class SettingsAutoreturnsItems(WBMethod[SettingsAutoreturnsItemsResponse]):
    """Получить настройки автовозврата товаров

    POST /api/marketplace/v3/fbs/settings/autoreturns/items
    """

    __path__ = "/api/marketplace/v3/fbs/settings/autoreturns/items"
    __http_method__ = "POST"
    __returns__ = SettingsAutoreturnsItemsResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"chrt_ids": "chrtIds"}

    chrt_ids: list[int]
    """Список ID размеров товаров в системе WB"""


class SettingsAutoreturnsItemsUpdate(WBMethod[SettingsAutoreturnsItemsUpdateResponse]):
    """Обновить настройки автовозврата товаров

    PATCH /api/marketplace/v3/fbs/settings/autoreturns/items
    """

    __path__ = "/api/marketplace/v3/fbs/settings/autoreturns/items"
    __http_method__ = "PATCH"
    __returns__ = SettingsAutoreturnsItemsUpdateResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"chrt_ids": "chrtIds", "type_": "type"}

    chrt_ids: list[int]
    """Список ID размеров товаров в системе WB"""
    type_: str
    """Тип автовозврата малогабаритных товаров:   - `byWarehouse` — все товары отправляются на
    склад WB …
    """


class SettingsAutoreturnsSubcategoriesRestricted(
    WBMethod[SettingsAutoreturnsSubcategoriesRestrictedResponse]
):
    """Получить предметы, которые не хранятся на складах WB

    GET /api/marketplace/v3/fbs/settings/autoreturns/subcategories/restricted
    """

    __path__ = "/api/marketplace/v3/fbs/settings/autoreturns/subcategories/restricted"
    __http_method__ = "GET"
    __returns__ = SettingsAutoreturnsSubcategoriesRestrictedResponse
    __query_params__ = {"next_": "next", "limit": "limit"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __paginate__ = "next"
    __items__ = "data"

    limit: int
    """Количество предметов в ответе"""
    next_: int
    """Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных.
    Для получения полного списка данных должен быть равен `0` в первом …
    """


class SettingsAutoreturnsUpdate(WBMethod[None]):
    """Обновить настройки автовозврата продавца

    PATCH /api/marketplace/v3/fbs/settings/autoreturns
    """

    __path__ = "/api/marketplace/v3/fbs/settings/autoreturns"
    __http_method__ = "PATCH"
    __returns__ = None
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"type_": "type"}

    type_: str
    """Тип автовозврата малогабаритных товаров: …"""


class Supplies(WBMethod[SuppliesResponse]):
    """Получить список поставок

    GET /api/v3/supplies
    """

    __path__ = "/api/v3/supplies"
    __http_method__ = "GET"
    __returns__ = SuppliesResponse
    __query_params__ = {"limit": "limit", "next_": "next"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __paginate__ = "next"
    __items__ = "supplies"

    limit: int
    """Параметр пагинации. Устанавливает предельное количество возвращаемых данных."""
    next_: int
    """Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных.
    Для получения полного списка данных должен быть равен `0` в первом …
    """


class SuppliesCreate(WBMethod[SuppliesCreateResponse]):
    """Создать новую поставку

    POST /api/v3/supplies
    """

    __path__ = "/api/v3/supplies"
    __http_method__ = "POST"
    __returns__ = SuppliesCreateResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"name": "name"}

    name: str | None = None
    """Наименование поставки"""


class SuppliesOrdersReshipment(WBMethod[SuppliesOrdersReshipmentResponse]):
    """Получить все сборочные задания для повторной отгрузки

    GET /api/v3/supplies/orders/reshipment
    """

    __path__ = "/api/v3/supplies/orders/reshipment"
    __http_method__ = "GET"
    __returns__ = SuppliesOrdersReshipmentResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"


class SuppliesSupplyId(WBMethod[Supply]):
    """Получить информацию о поставке

    GET /api/v3/supplies/{supplyId}
    """

    __path__ = "/api/v3/supplies/{supplyId}"
    __http_method__ = "GET"
    __returns__ = Supply
    __path_params__ = ("supplyId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    supply_id: str | int
    """ID поставки"""


class SuppliesSupplyIdBarcode(WBMethod[SuppliesSupplyIdBarcodeResponse]):
    """Получить QR-код поставки

    GET /api/v3/supplies/{supplyId}/barcode
    """

    __path__ = "/api/v3/supplies/{supplyId}/barcode"
    __http_method__ = "GET"
    __returns__ = SuppliesSupplyIdBarcodeResponse
    __path_params__ = ("supplyId",)
    __query_params__ = {"type_": "type"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    supply_id: str | int
    """ID поставки"""
    type_: str
    """Тип стикера"""


class SuppliesSupplyIdDelete(WBMethod[None]):
    """Удалить поставку

    DELETE /api/v3/supplies/{supplyId}
    """

    __path__ = "/api/v3/supplies/{supplyId}"
    __http_method__ = "DELETE"
    __returns__ = None
    __path_params__ = ("supplyId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    supply_id: str | int
    """ID поставки"""


class SuppliesSupplyIdDeliverUpdate(WBMethod[None]):
    """Передать поставку в доставку

    PATCH /api/v3/supplies/{supplyId}/deliver
    """

    __path__ = "/api/v3/supplies/{supplyId}/deliver"
    __http_method__ = "PATCH"
    __returns__ = None
    __path_params__ = ("supplyId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    supply_id: str | int
    """ID поставки"""


class SuppliesSupplyIdOrderIds(WBMethod[V3SupplyOrderIDsAPI]):
    """Получить ID сборочных заданий поставки

    GET /api/marketplace/v3/supplies/{supplyId}/order-ids
    """

    __path__ = "/api/marketplace/v3/supplies/{supplyId}/order-ids"
    __http_method__ = "GET"
    __returns__ = V3SupplyOrderIDsAPI
    __path_params__ = ("supplyId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    supply_id: str | int
    """ID поставки"""


class SuppliesSupplyIdOrdersCreate(WBMethod[None]):
    """Добавить сборочные задания к поставке

    PATCH /api/marketplace/v3/supplies/{supplyId}/orders
    """

    __path__ = "/api/marketplace/v3/supplies/{supplyId}/orders"
    __http_method__ = "PATCH"
    __returns__ = None
    __path_params__ = ("supplyId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"orders": "orders"}

    supply_id: str | int
    """ID поставки"""
    orders: list[int] | None = None
    """ID сборочных заданий"""


class SuppliesSupplyIdTrbx(WBMethod[SuppliesSupplyIdTrbxResponse]):
    """Получить список грузомест поставки

    GET /api/v3/supplies/{supplyId}/trbx
    """

    __path__ = "/api/v3/supplies/{supplyId}/trbx"
    __http_method__ = "GET"
    __returns__ = SuppliesSupplyIdTrbxResponse
    __path_params__ = ("supplyId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    supply_id: str | int
    """ID поставки"""


class SuppliesSupplyIdTrbxCreate(WBMethod[SuppliesSupplyIdTrbxCreateResponse]):
    """Добавить грузоместа к поставке

    POST /api/v3/supplies/{supplyId}/trbx
    """

    __path__ = "/api/v3/supplies/{supplyId}/trbx"
    __http_method__ = "POST"
    __returns__ = SuppliesSupplyIdTrbxCreateResponse
    __path_params__ = ("supplyId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"amount": "amount"}

    amount: int
    """Количество грузомест, которые необходимо добавить к поставке"""
    supply_id: str | int
    """ID поставки"""


class SuppliesSupplyIdTrbxDelete(WBMethod[None]):
    """Удалить грузоместа из поставки

    DELETE /api/v3/supplies/{supplyId}/trbx
    """

    __path__ = "/api/v3/supplies/{supplyId}/trbx"
    __http_method__ = "DELETE"
    __returns__ = None
    __path_params__ = ("supplyId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"trbx_ids": "trbxIds"}

    supply_id: str | int
    """ID поставки"""
    trbx_ids: list[str]
    """Список ID грузомест, которые необходимо удалить"""


class SuppliesSupplyIdTrbxStickers(WBMethod[SuppliesSupplyIdTrbxStickersResponse]):
    """Получить стикеры грузомест поставки

    POST /api/v3/supplies/{supplyId}/trbx/stickers
    """

    __path__ = "/api/v3/supplies/{supplyId}/trbx/stickers"
    __http_method__ = "POST"
    __returns__ = SuppliesSupplyIdTrbxStickersResponse
    __path_params__ = ("supplyId",)
    __query_params__ = {"type_": "type"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"trbx_ids": "trbxIds"}

    supply_id: str | int
    """ID поставки"""
    trbx_ids: list[str]
    """Список ID грузомест, по которым необходимо вернуть стикеры"""
    type_: str
    """Тип стикера"""
