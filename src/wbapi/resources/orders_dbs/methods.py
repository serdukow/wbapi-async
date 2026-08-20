from __future__ import annotations

from ...client.method import WBMethod
from ...utils.token import Scope
from .models import (
    ApiB2bClientInfoResponses,
    ApiGTIN,
    ApiIMEI,
    ApiOrderCodeRequest,
    ApiOrdersFinalPriceResponse,
    ApiOrdersMetaDetailsResponse,
    ApiOrderStatusesV2,
    ApiSGTINs,
    ApiStatusSetDeliverResponses,
    ApiStatusSetResponses,
    ApiUIN,
    DbsOnlyClientInfoResp,
    DeliveryDatesInfoResp,
    GroupsInfoResponseItem,
    OrdersMetaCustomsDeclarationUpdateOrdersItem,
    OrdersNewResponse,
    OrdersResponse,
    OrdersStatusReceiveCreateResponse,
    OrdersStickersResponse,
)


class GroupsInfo(WBMethod[list[GroupsInfoResponseItem]]):
    """Получить информацию о платной доставке

    POST /api/v3/dbs/groups/info
    """

    __path__ = "/api/v3/dbs/groups/info"
    __http_method__ = "POST"
    __returns__ = list[GroupsInfoResponseItem]
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"groups": "groups"}

    groups: list[str] | None = None
    """Список значений `groupId`. Можно получить из новых и завершенных сборочных заданий"""


class Orders(WBMethod[OrdersResponse]):
    """Получить информацию о завершенных сборочных заданиях

    GET /api/v3/dbs/orders
    """

    __path__ = "/api/v3/dbs/orders"
    __http_method__ = "GET"
    __returns__ = OrdersResponse
    __query_params__ = {"limit": "limit", "next_": "next", "date_from": "dateFrom", "date_to": "dateTo"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __paginate__ = "next"
    __items__ = "orders"

    date_from: int
    """Дата начала периода в формате Unix timestamp"""
    date_to: int
    """Дата конца периода в формате Unix timestamp"""
    limit: int
    """Параметр пагинации. Устанавливает предельное количество возвращаемых данных."""
    next_: int
    """Параметр пагинации. Устанавливает значение, с которого надо получить следующий пакет данных.
    Для получения полного списка данных должен быть равен `0` в первом …
    """


class OrdersB2bInfo(WBMethod[ApiB2bClientInfoResponses]):
    """Информация о покупателе B2B

    POST /api/marketplace/v3/dbs/orders/b2b/info
    """

    __path__ = "/api/marketplace/v3/dbs/orders/b2b/info"
    __http_method__ = "POST"
    __returns__ = ApiB2bClientInfoResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersClient(WBMethod[DbsOnlyClientInfoResp]):
    """Информация о покупателе

    POST /api/v3/dbs/orders/client
    """

    __path__ = "/api/v3/dbs/orders/client"
    __http_method__ = "POST"
    __returns__ = DbsOnlyClientInfoResp
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class OrdersDeliveryDate(WBMethod[DeliveryDatesInfoResp]):
    """Получить дату и время доставки

    POST /api/v3/dbs/orders/delivery-date
    """

    __path__ = "/api/v3/dbs/orders/delivery-date"
    __http_method__ = "POST"
    __returns__ = DeliveryDatesInfoResp
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class OrdersFinalPrice(WBMethod[ApiOrdersFinalPriceResponse]):
    """Получить цены продавца и суммы к оплате

    POST /api/marketplace/v3/dbs/orders/final-price
    """

    __path__ = "/api/marketplace/v3/dbs/orders/final-price"
    __http_method__ = "POST"
    __returns__ = ApiOrdersFinalPriceResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (400, 20)}
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class OrdersMetaCustomsDeclarationUpdate(WBMethod[ApiStatusSetResponses]):
    """Закрепить номера ДТ за сборочными заданиями

    POST /api/marketplace/v3/dbs/orders/meta/customs-declaration
    """

    __path__ = "/api/marketplace/v3/dbs/orders/meta/customs-declaration"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (120, 20)}
    __body_fields__ = {"orders": "orders"}

    orders: list[OrdersMetaCustomsDeclarationUpdateOrdersItem]


class OrdersMetaDelete(WBMethod[ApiStatusSetResponses]):
    """Удалить идентификаторы маркировки сборочных заданий

    POST /api/marketplace/v3/dbs/orders/meta/delete
    """

    __path__ = "/api/marketplace/v3/dbs/orders/meta/delete"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (400, 20)}
    __body_fields__ = {"key": "key", "order_ids": "orderIds"}

    key: str
    """Название идентификатора маркировки для удаления. Передаётся только одно значение"""
    order_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersMetaDetails(WBMethod[ApiOrdersMetaDetailsResponse]):
    """Получить идентификаторы маркировки сборочных заданий

    POST /api/marketplace/v3/dbs/orders/meta/details
    """

    __path__ = "/api/marketplace/v3/dbs/orders/meta/details"
    __http_method__ = "POST"
    __returns__ = ApiOrdersMetaDetailsResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersMetaGtinUpdate(WBMethod[ApiStatusSetResponses]):
    """Закрепить GTIN за сборочными заданиями

    POST /api/marketplace/v3/dbs/orders/meta/gtin
    """

    __path__ = "/api/marketplace/v3/dbs/orders/meta/gtin"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (120, 20)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiGTIN]


class OrdersMetaImeiUpdate(WBMethod[ApiStatusSetResponses]):
    """Закрепить IMEI за сборочными заданиями

    POST /api/marketplace/v3/dbs/orders/meta/imei
    """

    __path__ = "/api/marketplace/v3/dbs/orders/meta/imei"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (120, 20)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiIMEI]


class OrdersMetaSgtinUpdate(WBMethod[ApiStatusSetResponses]):
    """Закрепить коды маркировки Честного знака за сборочными заданиями

    POST /api/marketplace/v3/dbs/orders/meta/sgtin
    """

    __path__ = "/api/marketplace/v3/dbs/orders/meta/sgtin"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (120, 20),
        "service": (120, 20),
        "basic_secret": (120, 20),
        "basic": (360000, 1),
    }
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiSGTINs]


class OrdersMetaUinUpdate(WBMethod[ApiStatusSetResponses]):
    """Закрепить УИН за сборочными заданиями

    POST /api/marketplace/v3/dbs/orders/meta/uin
    """

    __path__ = "/api/marketplace/v3/dbs/orders/meta/uin"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (120, 20)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiUIN]


class OrdersNew(WBMethod[OrdersNewResponse]):
    """Получить список новых сборочных заданий

    GET /api/v3/dbs/orders/new
    """

    __path__ = "/api/v3/dbs/orders/new"
    __http_method__ = "GET"
    __returns__ = OrdersNewResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"


class OrdersStatusCancel(WBMethod[ApiStatusSetResponses]):
    """Отменить сборочные задания

    POST /api/marketplace/v3/dbs/orders/status/cancel
    """

    __path__ = "/api/marketplace/v3/dbs/orders/status/cancel"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersStatusConfirmUpdate(WBMethod[ApiStatusSetResponses]):
    """Перевести сборочные задания на сборку

    POST /api/marketplace/v3/dbs/orders/status/confirm
    """

    __path__ = "/api/marketplace/v3/dbs/orders/status/confirm"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersStatusDeliverUpdate(WBMethod[ApiStatusSetDeliverResponses]):
    """Перевести сборочные задания в доставку

    POST /api/marketplace/v3/dbs/orders/status/deliver
    """

    __path__ = "/api/marketplace/v3/dbs/orders/status/deliver"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetDeliverResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersStatusInfo(WBMethod[ApiOrderStatusesV2]):
    """Получить статусы сборочных заданий

    POST /api/marketplace/v3/dbs/orders/status/info
    """

    __path__ = "/api/marketplace/v3/dbs/orders/status/info"
    __http_method__ = "POST"
    __returns__ = ApiOrderStatusesV2
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class OrdersStatusReceiveCreate(WBMethod[OrdersStatusReceiveCreateResponse]):
    """Сообщить о получении заказов

    POST /api/marketplace/v3/dbs/orders/status/receive
    """

    __path__ = "/api/marketplace/v3/dbs/orders/status/receive"
    __http_method__ = "POST"
    __returns__ = OrdersStatusReceiveCreateResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiOrderCodeRequest]


class OrdersStatusRejectCreate(WBMethod[ApiStatusSetResponses]):
    """Сообщить об отказе от заказов

    POST /api/marketplace/v3/dbs/orders/status/reject
    """

    __path__ = "/api/marketplace/v3/dbs/orders/status/reject"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiOrderCodeRequest]


class OrdersStickers(WBMethod[OrdersStickersResponse]):
    """Получить стикеры для сборочных заданий с доставкой в ПВЗ

    POST /api/marketplace/v3/dbs/orders/stickers
    """

    __path__ = "/api/marketplace/v3/dbs/orders/stickers"
    __http_method__ = "POST"
    __returns__ = OrdersStickersResponse
    __query_params__ = {"type_": "type", "width": "width", "height": "height"}
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __body_fields__ = {"orders": "orders"}

    height: int
    """Высота стикера"""
    orders: list[int]
    """Список ID сборочных заданий"""
    type_: str
    """Формат стикера"""
    width: int
    """Ширина стикера"""
