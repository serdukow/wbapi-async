from __future__ import annotations

from ...client.method import WBMethod
from ...utils.token import Scope
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


class Orders(WBMethod[OrdersResponse]):
    """Получить информацию о завершенных сборочных заданиях

    GET /api/v3/dbw/orders
    """

    __path__ = "/api/v3/dbw/orders"
    __http_method__ = "GET"
    __returns__ = OrdersResponse
    __query_params__ = {"limit": "limit", "next_": "next", "date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __paginate__ = "next"
    __items__ = "orders"

    date_from: int
    """Дата начала периода в формате Unix timestamp"""
    date_to: int
    """Дата конца периода в формате Unix timestamp"""
    limit: int
    """Параметр пагинации. Устанавливает предельное количество возвращаемых данных"""
    next_: int
    """Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных.
    Для получения полного списка данных должен быть равен `0` в первом …
    """


class OrdersClient(WBMethod[ClientInfoResp]):
    """Информация о покупателе

    POST /api/marketplace/v3/dbw/orders/client
    """

    __path__ = "/api/marketplace/v3/dbw/orders/client"
    __http_method__ = "POST"
    __returns__ = ClientInfoResp
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class OrdersCourier(WBMethod[OrderCourierInfoResp]):
    """Информация о курьере

    POST /api/v3/dbw/orders/courier
    """

    __path__ = "/api/v3/dbw/orders/courier"
    __http_method__ = "POST"
    __returns__ = OrderCourierInfoResp
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class OrdersDeliveryDate(WBMethod[DeliveryDatesInfoResp]):
    """Получить дату и время доставки

    POST /api/v3/dbw/orders/delivery-date
    """

    __path__ = "/api/v3/dbw/orders/delivery-date"
    __http_method__ = "POST"
    __returns__ = DeliveryDatesInfoResp
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class OrdersMetaDelete(WBMethod[ApiMetaDeleteResponses]):
    """Удалить идентификаторы маркировки сборочных заданий

    POST /api/marketplace/v3/dbw/orders/meta/delete
    """

    __path__ = "/api/marketplace/v3/dbw/orders/meta/delete"
    __http_method__ = "POST"
    __returns__ = ApiMetaDeleteResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"key": "key", "orders_ids": "ordersIds"}

    key: str
    """Название идентификатора маркировки для удаления. Передаётся только одно значение"""
    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersMetaDetails(WBMethod[ApiOrdersMetaDetailsResponse]):
    """Получить идентификаторы маркировки сборочных заданий

    POST /api/marketplace/v3/dbw/orders/meta/details
    """

    __path__ = "/api/marketplace/v3/dbw/orders/meta/details"
    __http_method__ = "POST"
    __returns__ = ApiOrdersMetaDetailsResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersMetaSgtinUpdate(WBMethod[ApiStatusSetResponses]):
    """Закрепить коды маркировки Честного знака за сборочными заданиями

    POST /api/marketplace/v3/dbw/orders/meta/sgtin
    """

    __path__ = "/api/marketplace/v3/dbw/orders/meta/sgtin"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiSGTINs]


class OrdersNew(WBMethod[OrdersNewResponse]):
    """Получить список новых сборочных заданий

    GET /api/v3/dbw/orders/new
    """

    __path__ = "/api/v3/dbw/orders/new"
    __http_method__ = "GET"
    __returns__ = OrdersNewResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"


class OrdersOrderIdCancel(WBMethod[None]):
    """Отменить сборочное задание

    PATCH /api/v3/dbw/orders/{orderId}/cancel
    """

    __path__ = "/api/v3/dbw/orders/{orderId}/cancel"
    __http_method__ = "PATCH"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (200, 20),
        "service": (200, 20),
        "basic_secret": (200, 20),
        "basic": (360000, 1),
    }

    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdConfirmUpdate(WBMethod[None]):
    """Перевести на сборку

    PATCH /api/v3/dbw/orders/{orderId}/confirm
    """

    __path__ = "/api/v3/dbw/orders/{orderId}/confirm"
    __http_method__ = "PATCH"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}

    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaGtinUpdate(WBMethod[None]):
    """Закрепить GTIN за сборочным заданием

    PUT /api/v3/dbw/orders/{orderId}/meta/gtin
    """

    __path__ = "/api/v3/dbw/orders/{orderId}/meta/gtin"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"gtin": "gtin"}

    gtin: str
    """GTIN"""
    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaImeiUpdate(WBMethod[None]):
    """Закрепить IMEI за сборочным заданием

    PUT /api/v3/dbw/orders/{orderId}/meta/imei
    """

    __path__ = "/api/v3/dbw/orders/{orderId}/meta/imei"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"imei": "imei"}

    imei: str
    """IMEI"""
    order_id: str | int
    """ID сборочного задания"""


class OrdersOrderIdMetaUinUpdate(WBMethod[None]):
    """Закрепить УИН за сборочным заданием

    PUT /api/v3/dbw/orders/{orderId}/meta/uin
    """

    __path__ = "/api/v3/dbw/orders/{orderId}/meta/uin"
    __http_method__ = "PUT"
    __returns__ = None
    __path_params__ = ("orderId",)
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (60, 20)}
    __body_fields__ = {"uin": "uin"}

    order_id: str | int
    """ID сборочного задания"""
    uin: str
    """УИН"""


class OrdersStatus(WBMethod[OrdersStatusResponse]):
    """Получить статусы сборочных заданий

    POST /api/v3/dbw/orders/status
    """

    __path__ = "/api/v3/dbw/orders/status"
    __http_method__ = "POST"
    __returns__ = OrdersStatusResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int]
    """Список ID сборочных заданий"""


class OrdersStatusDeliverUpdate(WBMethod[ApiStatusSetResponses]):
    """Перевести сборочные задания в доставку

    POST /api/marketplace/v3/dbw/orders/status/deliver
    """

    __path__ = "/api/marketplace/v3/dbw/orders/status/deliver"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersStickers(WBMethod[OrdersStickersResponse]):
    """Получить стикеры сборочных заданий

    POST /api/v3/dbw/orders/stickers
    """

    __path__ = "/api/v3/dbw/orders/stickers"
    __http_method__ = "POST"
    __returns__ = OrdersStickersResponse
    __query_params__ = {"type_": "type", "width": "width", "height": "height"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
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
