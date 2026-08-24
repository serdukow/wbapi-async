from __future__ import annotations

from ..client.method import WBMethod
from ..utils.token import Scope
from .models import (
    CreateInviteAccessItem,
    CreateInviteInvite,
    CreateInviteResponse,
    GetCommunicationsNewsResponse,
    GetPingResponse,
    GetSellerInfoResponse,
    GetUsersResponse,
    PlanBuilderOptionsInfo,
    SubscriptionsJamInfo,
    SupplierRatingModel,
    UserAccess,
)


class CreateInvite(WBMethod[CreateInviteResponse]):
    """Создать приглашение для нового пользователя

    POST /api/v1/invite
    """

    __path__ = "/api/v1/invite"
    __http_method__ = "POST"
    __returns__ = CreateInviteResponse
    __scope__ = Scope.USERS
    __host__ = "https://user-management-api.wildberries.ru"
    __rate_limits__ = {"all": (5000, 5)}
    __body_fields__ = {"access": "access", "invite": "invite"}

    invite: CreateInviteInvite
    access: list[CreateInviteAccessItem] | None = None


class DeleteUser(WBMethod[None]):
    """Удалить пользователя

    DELETE /api/v1/user
    """

    __path__ = "/api/v1/user"
    __http_method__ = "DELETE"
    __returns__ = None
    __query_params__ = {"deleted_user_id": "deletedUserID"}
    __scope__ = Scope.USERS
    __host__ = "https://user-management-api.wildberries.ru"
    __rate_limits__ = {"all": (10000, 10)}

    deleted_user_id: int
    """ID пользователя, которому будет закрыт доступ"""


class GetCommonRating(WBMethod[SupplierRatingModel]):
    """Получить рейтинг продавца

    GET /api/common/v1/rating
    """

    __path__ = "/api/common/v1/rating"
    __http_method__ = "GET"
    __returns__ = SupplierRatingModel
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __rate_limits__ = {"all": (60000, 1)}


class GetCommonSubscriptions(WBMethod[SubscriptionsJamInfo]):
    """Получить информацию о подписке Джем

    GET /api/common/v1/subscriptions
    """

    __path__ = "/api/common/v1/subscriptions"
    __http_method__ = "GET"
    __returns__ = SubscriptionsJamInfo
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {"all": (600000, 10)}


class GetCommonTariffConstructorOptions(WBMethod[PlanBuilderOptionsInfo]):
    """Получить информацию об опциях Конструктора тарифов

    GET /api/common/v1/tariff-constructor/options
    """

    __path__ = "/api/common/v1/tariff-constructor/options"
    __http_method__ = "GET"
    __returns__ = PlanBuilderOptionsInfo
    __query_params__ = {"locale": "locale"}
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {"all": (600000, 10)}

    locale: str | None = None
    """Язык полей ответа:   - `ru` — русский   - `en` — английский"""


class GetCommunicationsNews(WBMethod[GetCommunicationsNewsResponse]):
    """Получение новостей портала продавцов

    GET /api/communications/v2/news
    """

    __path__ = "/api/communications/v2/news"
    __http_method__ = "GET"
    __returns__ = GetCommunicationsNewsResponse
    __query_params__ = {"from_": "from", "from_id": "fromID"}
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (600000, 10),
        "service": (600000, 10),
        "basic_secret": (600000, 10),
        "basic": (3600000, 1),
    }
    __items__ = "data"

    from_: str | None = None
    """Дата, от которой необходимо выдать новости"""
    from_id: int | None = None
    """ID новости, начиная с которой — включая её — нужно получить список новостей"""


class GetPing(WBMethod[GetPingResponse]):
    """Проверка подключения

    GET /ping
    """

    __path__ = "/ping"
    __http_method__ = "GET"
    __returns__ = GetPingResponse
    __host__ = "https://common-api.wildberries.ru"


class GetSellerInfo(WBMethod[GetSellerInfoResponse]):
    """Получить информацию о продавце

    GET /api/v1/seller-info
    """

    __path__ = "/api/v1/seller-info"
    __http_method__ = "GET"
    __returns__ = GetSellerInfoResponse
    __host__ = "https://common-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (600000, 10),
        "service": (600000, 10),
        "basic_secret": (600000, 10),
        "basic": (86400000, 1),
    }


class GetUsers(WBMethod[GetUsersResponse]):
    """Получить список активных или приглашённых пользователей продавца

    GET /api/v1/users
    """

    __path__ = "/api/v1/users"
    __http_method__ = "GET"
    __returns__ = GetUsersResponse
    __query_params__ = {"limit": "limit", "offset": "offset", "is_invite_only": "isInviteOnly"}
    __scope__ = Scope.USERS
    __host__ = "https://user-management-api.wildberries.ru"
    __rate_limits__ = {"all": (5000, 5)}
    __paginate__ = "offset_query"

    is_invite_only: bool | None = None
    """- `true` — список приглашённых пользователей, которые ещё не активировали доступ - `false`
    или не указан — список активных пользователей профиля продавца
    """
    limit: int | None = None
    """Количество активных или приглашённых пользователей в ответе"""
    offset: int | None = None
    """Сколько элементов пропустить. Например, для значения 10 ответ начнется с 11 элемента"""


class UpdateUsersAccess(WBMethod[None]):
    """Изменить права доступа пользователей

    PUT /api/v1/users/access
    """

    __path__ = "/api/v1/users/access"
    __http_method__ = "PUT"
    __returns__ = None
    __scope__ = Scope.USERS
    __host__ = "https://user-management-api.wildberries.ru"
    __rate_limits__ = {"all": (5000, 5)}
    __body_fields__ = {"users_accesses": "usersAccesses"}

    users_accesses: list[UserAccess]
    """Настройки доступа для пользователя"""
