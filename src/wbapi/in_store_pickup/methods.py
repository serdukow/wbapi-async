from __future__ import annotations

from ..client.method import WBMethod
from ..utils.token import Scope
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
    SetClickCollectOrdersMetaCustomsDeclarationOrdersItem,
)


class CancelClickCollectOrdersStatus(WBMethod[ApiStatusSetResponses]):
    """Отменить сборочные задания

    POST /api/marketplace/v3/click-collect/orders/status/cancel
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/status/cancel"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class CreateClickCollectOrdersStatusPrepare(WBMethod[ApiMetaDetailsResponse]):
    """Сообщить, что сборочные задания готовы к выдаче

    POST /api/marketplace/v3/click-collect/orders/status/prepare
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/status/prepare"
    __http_method__ = "POST"
    __returns__ = ApiMetaDetailsResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class CreateClickCollectOrdersStatusReceive(WBMethod[ApiStatusSetResponses]):
    """Сообщить, что заказы приняты покупателями

    POST /api/marketplace/v3/click-collect/orders/status/receive
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/status/receive"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class CreateClickCollectOrdersStatusReject(WBMethod[ApiStatusSetResponses]):
    """Сообщить об отказе от заказов

    POST /api/marketplace/v3/click-collect/orders/status/reject
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/status/reject"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class DeleteClickCollectOrdersMeta(WBMethod[ApiOrdersResponses]):
    """Удалить идентификаторы маркировки сборочных заданий

    POST /api/marketplace/v3/click-collect/orders/meta/delete
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/meta/delete"
    __http_method__ = "POST"
    __returns__ = ApiOrdersResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (400, 20)}
    __body_fields__ = {"key": "key", "orders_ids": "ordersIds"}

    key: str
    """Тип идентификаторов маркировки для удаления. Передаётся только одно значение"""
    orders_ids: list[int]
    """Список ID сборочных заданий"""


class GetClickCollectOrders(WBMethod[ApiOrders]):
    """Получить информацию о завершённых сборочных заданиях

    GET /api/v3/click-collect/orders
    """

    __path__ = "/api/v3/click-collect/orders"
    __http_method__ = "GET"
    __returns__ = ApiOrders
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
    """Количество элементов в ответе"""
    next_: int
    """Параметр пагинации. Чтобы получить полный список данных, укажите `0` в первом запросе. Чтобы
    получить следующий пакет данных, используйте значение `next` из отв …
    """


class GetClickCollectOrdersClient(WBMethod[ApiOrderClientInfoResp]):
    """Информация о покупателе

    POST /api/v3/click-collect/orders/client
    """

    __path__ = "/api/v3/click-collect/orders/client"
    __http_method__ = "POST"
    __returns__ = ApiOrderClientInfoResp
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class GetClickCollectOrdersClientIdentity(WBMethod[ApiCheckedIdentity]):
    """Проверить, что заказ принадлежит покупателю

    POST /api/v3/click-collect/orders/client/identity
    """

    __path__ = "/api/v3/click-collect/orders/client/identity"
    __http_method__ = "POST"
    __returns__ = ApiCheckedIdentity
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (2000, 20)}
    __body_fields__ = {"order_code": "orderCode", "passcode": "passcode"}

    order_code: str | None = None
    """Уникальный ID заказа покупателя"""
    passcode: str | None = None
    """Код подтверждения"""


class GetClickCollectOrdersFinalPrice(WBMethod[ApiOrdersFinalPriceResponse]):
    """Получить цены продавца и суммы к оплате

    POST /api/marketplace/v3/click-collect/orders/final-price
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/final-price"
    __http_method__ = "POST"
    __returns__ = ApiOrdersFinalPriceResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (400, 20)}
    __body_fields__ = {"orders": "orders"}

    orders: list[int] | None = None
    """Список ID сборочных заданий"""


class GetClickCollectOrdersMetaDetails(WBMethod[ApiOrdersMetaDetailsResponse]):
    """Получить идентификаторы маркировки сборочных заданий

    POST /api/marketplace/v3/click-collect/orders/meta/details
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/meta/details"
    __http_method__ = "POST"
    __returns__ = ApiOrdersMetaDetailsResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (400, 20)}
    __items__ = "orders"
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class GetClickCollectOrdersNew(WBMethod[ApiNewOrders]):
    """Получить список новых сборочных заданий

    GET /api/v3/click-collect/orders/new
    """

    __path__ = "/api/v3/click-collect/orders/new"
    __http_method__ = "GET"
    __returns__ = ApiNewOrders
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (200, 20)}
    __items__ = "orders"


class GetClickCollectOrdersStatus(WBMethod[ApiOrderStatusesV2]):
    """Получить статусы сборочных заданий

    POST /api/marketplace/v3/click-collect/orders/status/info
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/status/info"
    __http_method__ = "POST"
    __returns__ = ApiOrderStatusesV2
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __items__ = "orders"
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""


class SetClickCollectOrdersMetaCustomsDeclaration(WBMethod[ApiCustomsDeclarationSetResponse]):
    """Закрепить номера ДТ за сборочными заданиями

    POST /api/marketplace/v3/click-collect/orders/meta/customs-declaration
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/meta/customs-declaration"
    __http_method__ = "POST"
    __returns__ = ApiCustomsDeclarationSetResponse
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __rate_limits__ = {"all": (3000, 500)}
    __body_fields__ = {"orders": "orders"}

    orders: list[SetClickCollectOrdersMetaCustomsDeclarationOrdersItem]


class SetClickCollectOrdersMetaGtin(WBMethod[ApiMetaSetResponses]):
    """Закрепить GTIN за сборочными заданиями

    POST /api/marketplace/v3/click-collect/orders/meta/gtin
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/meta/gtin"
    __http_method__ = "POST"
    __returns__ = ApiMetaSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 500)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiGTIN]


class SetClickCollectOrdersMetaImei(WBMethod[ApiMetaSetResponses]):
    """Закрепить IMEI за сборочными заданиями

    POST /api/marketplace/v3/click-collect/orders/meta/imei
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/meta/imei"
    __http_method__ = "POST"
    __returns__ = ApiMetaSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 500)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiIMEI]


class SetClickCollectOrdersMetaSgtin(WBMethod[ApiMetaSetResponses]):
    """Закрепить коды маркировки Честного знака за сборочными заданиями

    POST /api/marketplace/v3/click-collect/orders/meta/sgtin
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/meta/sgtin"
    __http_method__ = "POST"
    __returns__ = ApiMetaSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 500)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiSGTINs]


class SetClickCollectOrdersMetaUin(WBMethod[ApiMetaSetResponses]):
    """Закрепить УИН за сборочными заданиями

    POST /api/marketplace/v3/click-collect/orders/meta/uin
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/meta/uin"
    __http_method__ = "POST"
    __returns__ = ApiMetaSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (3000, 500)}
    __body_fields__ = {"orders": "orders"}

    orders: list[ApiUIN]


class UpdateClickCollectOrdersStatusConfirm(WBMethod[ApiStatusSetResponses]):
    """Перевести сборочные задания на сборку

    POST /api/marketplace/v3/click-collect/orders/status/confirm
    """

    __path__ = "/api/marketplace/v3/click-collect/orders/status/confirm"
    __http_method__ = "POST"
    __returns__ = ApiStatusSetResponses
    __scope__ = Scope.MARKETPLACE
    __host__ = "https://marketplace-api.wildberries.ru"
    __sandbox_host__ = "https://marketplace-api-sandbox.wildberries.ru"
    __rate_limits__ = {"all": (1000, 10)}
    __body_fields__ = {"orders_ids": "ordersIds"}

    orders_ids: list[int]
    """Список ID сборочных заданий"""
