from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    CommonV1Rating,
    CommonV1Subscriptions,
    CommonV1TariffConstructorOptions,
    CommunicationsV2News,
    InviteCreate,
    Ping,
    SellerInfo,
    UserDelete,
    Users,
    UsersAccessUpdate,
)
from .models import (
    CommunicationsV2NewsResponse,
    CreateInviteResponse,
    GetUsersResponse,
    InviteCreateAccessItem,
    InviteCreateInvite,
    PingResponse,
    PlanBuilderOptionsInfo,
    SellerInfoResponse,
    SubscriptionsJamInfo,
    SupplierRatingModel,
    UserAccess,
)


if TYPE_CHECKING:
    from ...client import WBApi


class General:
    """Общее.

    В этом разделе:
    - общая информация о WB API
    - как начать работу с WB API
    - как авторизоваться и создавать токены
    - основные статус-коды ответов
    - лимиты запросов
    - как обратиться в поддержку

    С помощью методов этого раздела вы можете:
    - проверить подключение к WB API
    - получить новости портала продавцов
    - получить информацию о продавце
    - управлять пользователями продавца
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def common_v1_rating(self) -> SupplierRatingModel:
        """Получить рейтинг продавца"""
        return await CommonV1Rating().emit(self._api)

    async def common_v1_subscriptions(self) -> SubscriptionsJamInfo:
        """Получить информацию о подписке Джем"""
        return await CommonV1Subscriptions().emit(self._api)

    async def common_v1_tariff_constructor_options(
        self, *, locale: str | None = None
    ) -> PlanBuilderOptionsInfo:
        """Получить информацию об опциях Конструктора тарифов

        :param locale: Язык полей ответа:   - `ru` — русский   - `en` — английский
        """
        return await CommonV1TariffConstructorOptions(locale=locale).emit(self._api)

    async def communications_v2_news(
        self, *, from_: str | None = None, from_id: int | None = None
    ) -> CommunicationsV2NewsResponse:
        """Получение новостей портала продавцов

        :param from_: Дата, от которой необходимо выдать новости
        :param from_id: ID новости, начиная с которой — включая её — нужно получить список новостей
        """
        return await CommunicationsV2News(from_=from_, from_id=from_id).emit(self._api)

    async def invite_create(
        self, *, invite: InviteCreateInvite, access: list[InviteCreateAccessItem] | None = None
    ) -> CreateInviteResponse:
        """Создать приглашение для нового пользователя"""
        return await InviteCreate(invite=invite, access=access).emit(self._api)

    async def ping(self) -> PingResponse:
        """Проверка подключения"""
        return await Ping().emit(self._api)

    async def seller_info(self) -> SellerInfoResponse:
        """Получить информацию о продавце"""
        return await SellerInfo().emit(self._api)

    async def user_delete(self, *, deleted_user_id: int) -> None:
        """Удалить пользователя

        :param deleted_user_id: ID пользователя, которому будет закрыт доступ
        """
        await UserDelete(deleted_user_id=deleted_user_id).emit(self._api)

    async def users(
        self,
        *,
        is_invite_only: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> GetUsersResponse | list[Any]:
        """Получить список активных или приглашённых пользователей продавца

        :param is_invite_only: - `true` — список приглашённых пользователей, которые ещё не активировали
            доступ - `false` или не указан — список активных пользователей профиля
            продавца
        :param limit: Количество активных или приглашённых пользователей в ответе
        :param offset: Сколько элементов пропустить. Например, для значения 10 ответ начнется с 11 элемента
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = Users(is_invite_only=is_invite_only, limit=limit, offset=offset)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_users(
        self, *, is_invite_only: bool | None = None, limit: int | None = None, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Получить список активных или приглашённых пользователей продавца — постранично, по одной записи.

        :param is_invite_only: - `true` — список приглашённых пользователей, которые ещё не активировали
            доступ - `false` или не указан — список активных пользователей профиля
            продавца
        :param limit: Количество активных или приглашённых пользователей в ответе
        :param offset: Сколько элементов пропустить. Например, для значения 10 ответ начнется с 11 элемента
        """
        async for item in Users(is_invite_only=is_invite_only, limit=limit, offset=offset).stream(self._api):
            yield item

    async def users_access_update(self, *, users_accesses: list[UserAccess]) -> None:
        """Изменить права доступа пользователей

        :param users_accesses: Настройки доступа для пользователя
        """
        await UsersAccessUpdate(users_accesses=users_accesses).emit(self._api)
