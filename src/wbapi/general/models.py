# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from msgspec import field as _field

from ..client.model import WBModel


class CreateInviteAccessItem(WBModel):
    code: str | None = _field(default=None)
    """Код раздела профиля продавца, к которому пользователь получит доступ: * `balance` — Просмотр
    баланса и вывод средств * `brands` — Управление брендами …
    """
    disabled: bool | None = _field(default=None)
    """* `true` — доступ к разделу запрещён * `false` — доступ к разделу разрешён"""


class CreateInviteInvite(WBModel):
    phone_number: str | None = _field(default=None, name="phoneNumber")
    """Номер телефона пользователя для приглашения. …"""
    position: str | None = _field(default=None)
    """Должность пользователя"""


class CreateInviteRequest(WBModel):
    access: list[CreateInviteRequestAccessItem] | None = _field(default=None)
    """Настройки доступа к разделам профиля продавца"""
    invite: CreateInviteRequestInvite | None = _field(default=None)


class CreateInviteRequestAccessItem(WBModel):
    code: str | None = _field(default=None)
    """Код раздела профиля продавца, к которому пользователь получит доступ: * `balance` — Просмотр
    баланса и вывод средств * `brands` — Управление брендами …
    """
    disabled: bool | None = _field(default=None)
    """* `true` — доступ к разделу запрещён * `false` — доступ к разделу разрешён"""


class CreateInviteRequestInvite(WBModel):
    phone_number: str | None = _field(default=None, name="phoneNumber")
    """Номер телефона пользователя для приглашения. …"""
    position: str | None = _field(default=None)
    """Должность пользователя"""


class CreateInviteResponse(WBModel):
    """Данные приглашения"""

    expired_at: str | None = _field(default=None, name="expiredAt")
    """Дата и время окончания срока действия приглашения"""
    invite_id: str | None = _field(default=None, name="inviteID")
    """ID приглашения"""
    invite_url: str | None = _field(default=None, name="inviteUrl")
    """URL приглашения, по которому должен перейти пользователь"""
    is_success: bool | None = _field(default=None, name="isSuccess")
    """- `true` — приглашение создано успешно - `false` — повторите запрос"""


class GetCommunicationsNewsResponse(WBModel):
    data: list[GetCommunicationsNewsResponseDataItem] | None = _field(default=None)
    """Новости"""


class GetCommunicationsNewsResponseDataItem(WBModel):
    content: str | None = _field(default=None)
    """Текст новости"""
    date: str | None = _field(default=None)
    """Дата и время публикации новости"""
    header: str | None = _field(default=None)
    """Заголовок новости"""
    id: int | None = _field(default=None)
    """ID новости"""
    types: list[GetCommunicationsNewsResponseDataItemTypesItem] | None = _field(default=None)
    """Теги новости"""


class GetCommunicationsNewsResponseDataItemTypesItem(WBModel):
    id: int | None = _field(default=None)
    """ID тега"""
    name: str | None = _field(default=None)
    """Название тега"""


class GetPingResponse(WBModel):
    status: str | None = _field(default=None, name="Status")
    """Статус"""
    ts: str | None = _field(default=None, name="TS")
    """Timestamp запроса"""


class GetSellerInfoResponse(WBModel):
    name: str | None = _field(default=None)
    """Наименование продавца"""
    sid: str | None = _field(default=None)
    """Уникальный ID продавца на Wildberries, находящийся в публичном поле токена"""
    tin: str | None = _field(default=None)
    """ИНН"""
    trade_mark: str | None = _field(default=None, name="tradeMark")
    """Торговое наименование продавца"""


class GetUsersResponse(WBModel):
    count_in_response: int | None = _field(default=None, name="countInResponse")
    """Количество активных или приглашённых пользователей на текущей странице"""
    total: int | None = _field(default=None)
    """Общее количество активных или приглашённых пользователей"""
    users: list[GetUsersResponseUsersItem] | None = _field(default=None)
    """Информация о пользователях"""


class GetUsersResponseUsersItem(WBModel):
    access: list[GetUsersResponseUsersItemAccessItem] | None = _field(default=None)
    """Настройки доступа к разделам профиля продавца"""
    email: str | None = _field(default=None)
    """Email пользователя"""
    first_name: str | None = _field(default=None, name="firstName")
    """Имя пользователя"""
    goods_return: bool | None = _field(default=None, name="goodsReturn")
    """Может ли пользователь одобрять возвраты товаров"""
    id: int | None = _field(default=None)
    """ID пользователя"""
    invitee_info: GetUsersResponseUsersItemInviteeInfo | None = _field(default=None, name="inviteeInfo")
    """Информация о приглашении, если пользователь приглашён"""
    is_invitee: bool | None = _field(default=None, name="isInvitee")
    """Приглашён ли пользователь"""
    is_owner: bool | None = _field(default=None, name="isOwner")
    """Является ли пользователь владельцем профиля продавца"""
    patronymic: str | None = _field(default=None)
    """Отчество пользователя"""
    phone: str | None = _field(default=None)
    """Номер телефона пользователя"""
    position: str | None = _field(default=None)
    """Должность пользователя"""
    role: str | None = _field(default=None)
    """Роль пользователя:   * `user` — пользователь, который активировал доступ   * ` ` (пустая
    строка) — пользователь, который не активировал доступ
    """
    second_name: str | None = _field(default=None, name="secondName")
    """Фамилия пользователя"""


class GetUsersResponseUsersItemAccessItem(WBModel):
    code: str | None = _field(default=None)
    """Код раздела профиля продавца, к которому пользователь получит доступ: * `balance` — Просмотр
    баланса и вывод средств * `brands` — Управление брендами …
    """
    disabled: bool | None = _field(default=None)
    """* `true` — доступ к разделу запрещён * `false` — доступ к разделу разрешён"""


class GetUsersResponseUsersItemInviteeInfo(WBModel):
    """Информация о приглашении, если пользователь приглашён"""

    expired_at: str | None = _field(default=None, name="expiredAt")
    """Дата и время окончания срока действия приглашения"""
    invite_uuid: str | None = _field(default=None, name="inviteUuid")
    """ID приглашения"""
    is_active: bool | None = _field(default=None, name="isActive")
    """- `true` — приглашение активно - `false` — приглашение неактивно"""
    phone_number: str | None = _field(default=None, name="phoneNumber")
    """Номер телефона приглашённого пользователя"""
    position: str | None = _field(default=None)
    """Должность приглашённого пользователя"""


class PlanBuilderOption(WBModel):
    activated_at: str | None = _field(default=None, name="activatedAt")
    """Дата активации опции"""
    commission_rate: float | None = _field(default=None, name="commissionRate")
    """Стоимость подключения опции, % от оборота. Возвращается, если в ответе нет объекта
    `promotion`
    """
    expires_at: str | None = _field(default=None, name="expiresAt")
    """Дата окончания минимального срока действия опции. До этого дня опцию нельзя отключить"""
    id: str | None = _field(default=None)
    """ID опции"""
    name: str | None = _field(default=None)
    """Название опции на языке из параметра `locale`"""
    period_duration: float | None = _field(default=None, name="periodDuration")
    """Минимальный срок действия опции в днях"""
    promotion: PlanBuilderOptionPromotion | None = _field(default=None)
    """Акция, по которой подключена опция. Не возвращается, если опция подключена без акции или
    срок действия акции истёк
    """
    slug: str | None = _field(default=None)
    """Код опции"""
    status: str | None = _field(default=None)
    """Статус опции:   - `active` — активна   - `pendingActivation` — подключена, начнёт работать с
    00:00 следующего дня …
    """


class PlanBuilderOptionPromotion(WBModel):
    commission_rate: float | None = _field(default=None, name="commissionRate")
    """Стоимость подключения опции по акции, % от оборота"""
    expires_at: str | None = _field(default=None, name="expiresAt")
    """Дата окончания действия цены по акции"""


class PlanBuilderOptionShort(WBModel):
    id: str | None = _field(default=None)
    """ID опции"""
    name: str | None = _field(default=None)
    """Название опции на языке из параметра `locale`"""
    slug: str | None = _field(default=None)
    """Код опции"""


class PlanBuilderOptionsInfo(WBModel):
    active_option_count: float | None = _field(default=None, name="activeOptionCount")
    """Количество активных опций, не включённых в пакеты"""
    active_package_count: float | None = _field(default=None, name="activePackageCount")
    """Количество активных пакетов опций"""
    options: list[PlanBuilderOption] | None = _field(default=None)
    """Подключённые опции"""
    packages: list[PlanBuilderPackage] | None = _field(default=None)
    """Подключённые пакеты опций"""
    total_commission_rate: float | None = _field(default=None, name="totalCommissionRate")
    """Итоговая комиссия за подключённые опции и пакеты, % от оборота"""


class PlanBuilderPackage(WBModel):
    activated_at: str | None = _field(default=None, name="activatedAt")
    """Дата активации пакета"""
    commission_rate: float | None = _field(default=None, name="commissionRate")
    """Комиссия за пакет, % от оборота"""
    expires_at: str | None = _field(default=None, name="expiresAt")
    """Дата окончания минимального срока действия пакета. До этого дня пакет опций нельзя отключить
    """
    id: str | None = _field(default=None)
    """ID пакета"""
    name: str | None = _field(default=None)
    """Название пакета на языке из параметра `locale`"""
    options: list[PlanBuilderOptionShort] | None = _field(default=None)
    """Опции, которые входят в пакет"""
    period_duration: float | None = _field(default=None, name="periodDuration")
    """Минимальный срок действия пакета в днях"""
    slug: str | None = _field(default=None)
    """Код пакета"""
    status: str | None = _field(default=None)
    """Статус пакета:   - `active` — активен   - `pendingActivation` — подключён, начнёт работать с
    00:00 следующего дня …
    """


class SubscriptionsJamInfo(WBModel):
    """Информация о подписке Джем"""

    activation_source: str | None = _field(default=None, name="activationSource")
    """Источник подключения подписки:   - `constructor` — покупка через раздел **Конструктор
    тарифов**   - `jam` — покупка через раздел **Подписка «Джем»**
    """
    level: str | None = _field(default=None)
    """Уровень подписки:   - `standard`   - `advanced`   - `premium`"""
    since: str | None = _field(default=None)
    """Дата и время первой активации подписки. Не меняется при продлении или повторной активации
    """
    state: str | None = _field(default=None)
    """Статус подписки:   - `active` — активна   - `inactive` — истекла или отменена"""
    till: str | None = _field(default=None)
    """Дата и время окончания подписки"""


class SupplierRatingModel(WBModel):
    feedback_count: int | None = _field(default=None, name="feedbackCount")
    """Количество отзывов"""
    valuation: float | None = _field(default=None)
    """Рейтинг продавца"""


class UpdateUserAccessRequest(WBModel):
    users_accesses: list[UserAccess] | None = _field(default=None, name="usersAccesses")
    """Настройки доступа для пользователя"""


class UserAccess(WBModel):
    access: list[UserAccessAccessItem] | None = _field(default=None)
    """Настройки доступа к разделам профиля продавца"""
    user_id: int | None = _field(default=None, name="userId")
    """ID пользователя"""


class UserAccessAccessItem(WBModel):
    code: str | None = _field(default=None)
    """Код раздела профиля продавца, к которому пользователь получит доступ: * `balance` — Просмотр
    баланса и вывод средств * `brands` — Управление брендами …
    """
    disabled: bool | None = _field(default=None)
    """* `true` — доступ к разделу запрещён * `false` — доступ к разделу разрешён"""
