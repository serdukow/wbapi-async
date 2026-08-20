from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    AdvertV0BidsRecommendations,
    AdvertV1BidsMinCreate,
    AdvertV1BidsUpdate,
    AdvertV1Config,
    AdvertV1NormqueryBidsUpdate,
    AdvertV2Adverts,
    AdvV0AuctionNmsUpdate,
    AdvV0AuctionPlacementsUpdate,
    AdvV0Delete,
    AdvV0NormqueryBidsDelete,
    AdvV0NormqueryBidsUpdate,
    AdvV0NormqueryGetBids,
    AdvV0NormqueryGetMinus,
    AdvV0NormqueryListCreate,
    AdvV0NormquerySetMinusCreate,
    AdvV0NormqueryStatsCreate,
    AdvV0Pause,
    AdvV0RenameCreate,
    AdvV0Start,
    AdvV0Stop,
    AdvV1Advert,
    AdvV1Adverts,
    AdvV1Balance,
    AdvV1Budget,
    AdvV1BudgetDepositCreate,
    AdvV1Count,
    AdvV1NormqueryStatsCreate,
    AdvV1Payments,
    AdvV1PromotionCount,
    AdvV1StatsCreate,
    AdvV1SupplierSubjects,
    AdvV1Upd,
    AdvV2SeacatSaveAdCreate,
    AdvV2SupplierNmsCreate,
    AdvV3Fullstats,
    CalendarPromotions,
    CalendarPromotionsDetails,
    CalendarPromotionsNomenclatures,
    CalendarPromotionsUploadCreate,
)
from .models import (
    AdvertV1BidsMinCreateResponse,
    AdvertV1BidsUpdateBidsItem,
    AdvertV1BidsUpdateResponse,
    AdvV0AuctionNmsUpdateNmsItem,
    AdvV0AuctionNmsUpdateResponse,
    AdvV0AuctionPlacementsUpdatePlacementsItem,
    AdvV0NormqueryStatsCreateItemsItem,
    AdvV1AdvertResponse,
    AdvV1AdvertsResponseItem,
    AdvV1BalanceResponse,
    AdvV1BudgetResponse,
    AdvV1CountResponse,
    AdvV1NormqueryStatsCreateItemsItem,
    AdvV1PaymentsResponseItem,
    AdvV1PromotionCountResponse,
    AdvV1SupplierSubjectsResponseItem,
    AdvV1UpdResponseItem,
    AdvV2SupplierNmsCreateResponseItem,
    FullStatsItem,
    GetAdverts,
    ResponseWithReturn,
    StatInterval,
    V0BidsRecommendationsCpmResponse,
    V0DeleteNormQueryBidsRequestItem,
    V0GetNormQueryBidsRequestItem,
    V0GetNormQueryBidsResponse,
    V0GetNormQueryListRequestItem,
    V0GetNormQueryListResponse,
    V0GetNormQueryMinusRequestItem,
    V0GetNormQueryMinusResponse,
    V0GetNormQueryStatsResponse,
    V0SetNormQueryBidsRequestItem,
    V1GetNormQueryStatsResponse,
    V1SetNormQueryBidsRequestItem,
    V1SetNormQueryBidsResponse,
    V2GetConfigResponse,
)


if TYPE_CHECKING:
    from ...client import WBApi


class Promotion:
    """Маркетинг и продвижение.

    Узнать больше о маркетинге и продвижении можно в справочном центре

    Методы маркетинга и продвижения позволяют:
      1. Получать информацию о кампаниях продвижения и медиакампаниях
      2. Создавать и управлять кампаниями
      3. Управлять финансами кампаний
      4. Выгружать статистику кампаний продвижения и медиакампаний
      5. Работать с календарём акций

    Данные синхронизируются с базой раз в 3 минуты. Статусы кампаний меняются раз в минуту. Ставки
    кампаний меняются раз в 30 секунд.

    Вы можете протестировать методы продвижения в песочнице. Также в песочнице доступны специальные
    методы для управления тестовым балансом
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def adv_v0_auction_nms_update(
        self, *, nms: list[AdvV0AuctionNmsUpdateNmsItem]
    ) -> AdvV0AuctionNmsUpdateResponse:
        """Изменение списка карточек товаров в кампаниях

        :param nms: Карточки товаров в кампаниях
        """
        return await AdvV0AuctionNmsUpdate(nms=nms).emit(self._api)

    async def adv_v0_auction_placements_update(
        self, *, placements: list[AdvV0AuctionPlacementsUpdatePlacementsItem]
    ) -> None:
        """Изменение мест размещения в кампаниях с ручной ставкой

        :param placements: Места размещения в кампаниях
        """
        await AdvV0AuctionPlacementsUpdate(placements=placements).emit(self._api)

    async def adv_v0_delete(self, *, id_: int) -> None:
        """Удаление кампании

        :param id_: ID кампании
        """
        await AdvV0Delete(id_=id_).emit(self._api)

    async def adv_v0_normquery_bids_delete(self, *, bids: list[V0DeleteNormQueryBidsRequestItem]) -> None:
        """Удалить ставки поисковых кластеров"""
        await AdvV0NormqueryBidsDelete(bids=bids).emit(self._api)

    async def adv_v0_normquery_bids_update(self, *, bids: list[V0SetNormQueryBidsRequestItem]) -> None:
        """Установить ставки для поисковых кластеров"""
        await AdvV0NormqueryBidsUpdate(bids=bids).emit(self._api)

    async def adv_v0_normquery_get_bids(
        self, *, items: list[V0GetNormQueryBidsRequestItem]
    ) -> V0GetNormQueryBidsResponse:
        """Список ставок поисковых кластеров"""
        return await AdvV0NormqueryGetBids(items=items).emit(self._api)

    async def adv_v0_normquery_get_minus(
        self, *, items: list[V0GetNormQueryMinusRequestItem]
    ) -> V0GetNormQueryMinusResponse:
        """Список минус-фраз кампаний"""
        return await AdvV0NormqueryGetMinus(items=items).emit(self._api)

    async def adv_v0_normquery_list_create(
        self, *, items: list[V0GetNormQueryListRequestItem]
    ) -> V0GetNormQueryListResponse:
        """Списки активных и неактивных поисковых кластеров"""
        return await AdvV0NormqueryListCreate(items=items).emit(self._api)

    async def adv_v0_normquery_set_minus_create(
        self, *, advert_id: int, nm_id: int, norm_queries: list[str]
    ) -> None:
        """Установка и удаление минус-фраз

        :param advert_id: ID кампании
        :param nm_id: Артикул WB
        """
        await AdvV0NormquerySetMinusCreate(advert_id=advert_id, nm_id=nm_id, norm_queries=norm_queries).emit(
            self._api
        )

    async def adv_v0_normquery_stats_create(
        self, *, from_: str, items: list[AdvV0NormqueryStatsCreateItemsItem], to: str
    ) -> V0GetNormQueryStatsResponse:
        """Статистика поисковых кластеров

        :param from_: Дата начала периода
        :param to: Дата окончания периода
        """
        return await AdvV0NormqueryStatsCreate(from_=from_, items=items, to=to).emit(self._api)

    async def adv_v0_pause(self, *, id_: int) -> None:
        """Пауза кампании

        :param id_: ID кампании
        """
        await AdvV0Pause(id_=id_).emit(self._api)

    async def adv_v0_rename_create(self, *, advert_id: int, name: str) -> None:
        """Переименование кампании

        :param advert_id: ID кампании, в которой меняется название
        :param name: Новое название (максимум 100 символов)
        """
        await AdvV0RenameCreate(advert_id=advert_id, name=name).emit(self._api)

    async def adv_v0_start(self, *, id_: int) -> None:
        """Запуск кампании

        :param id_: ID кампании
        """
        await AdvV0Start(id_=id_).emit(self._api)

    async def adv_v0_stop(self, *, id_: int) -> None:
        """Завершение кампании

        :param id_: ID кампании
        """
        await AdvV0Stop(id_=id_).emit(self._api)

    async def adv_v1_advert(self, *, id_: int) -> AdvV1AdvertResponse:
        """Информация о медиакампании

        :param id_: ID медиакампании
        """
        return await AdvV1Advert(id_=id_).emit(self._api)

    async def adv_v1_adverts(
        self,
        *,
        direction: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        status: str | None = None,
        type_: int | None = None,
        auto_paginate: bool = False,
    ) -> list[AdvV1AdvertsResponseItem] | list[Any]:
        """Список медиакампаний

        :param direction: Порядок сортировки: - `desc` — от большего к меньшему - `asc` — от меньшего к
            большему
        :param limit: Количество кампаний в ответе
        :param offset: Смещение относительно первой медиакампании
        :param order: Порядок вывода ответа: - `create` — по времени создания медиакампании - `id` — по ID
            медиакампании
        :param status: Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с
            возможностью вернуть на модерацию)   - `4` — готова к запуску …
        :param type_: Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = AdvV1Adverts(
            direction=direction, limit=limit, offset=offset, order=order, status=status, type_=type_
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_adv_v1_adverts(
        self,
        *,
        direction: str | None = None,
        limit: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        status: str | None = None,
        type_: int | None = None,
    ) -> AsyncIterator[Any]:
        """Список медиакампаний — постранично, по одной записи.

        :param direction: Порядок сортировки: - `desc` — от большего к меньшему - `asc` — от меньшего к
            большему
        :param limit: Количество кампаний в ответе
        :param offset: Смещение относительно первой медиакампании
        :param order: Порядок вывода ответа: - `create` — по времени создания медиакампании - `id` — по ID
            медиакампании
        :param status: Статус медиакампании:   - `1` — черновик   - `2` — модерация   - `3` — отклонена (с
            возможностью вернуть на модерацию)   - `4` — готова к запуску …
        :param type_: Тип медиакампании: - `1` — размещение по дням - `2` — размещение по просмотрам
        """
        async for item in AdvV1Adverts(
            direction=direction, limit=limit, offset=offset, order=order, status=status, type_=type_
        ).stream(self._api):
            yield item

    async def adv_v1_balance(self) -> AdvV1BalanceResponse:
        """Баланс"""
        return await AdvV1Balance().emit(self._api)

    async def adv_v1_budget(self, *, id_: int) -> AdvV1BudgetResponse:
        """Бюджет кампании

        :param id_: ID кампании
        """
        return await AdvV1Budget(id_=id_).emit(self._api)

    async def adv_v1_budget_deposit_create(
        self,
        *,
        id_: int,
        cashback_percent: int | None = None,
        cashback_sum: int | None = None,
        return_: bool | None = None,
        sum: int | None = None,
        type_: int | None = None,
    ) -> ResponseWithReturn:
        """Пополнение бюджета кампании

        :param id_: ID кампании
        :param cashback_percent: Процент от суммы пополнения, который можно пополнить промо-бонусами. Нужно
            указать значение поля percent из ответа метода получения баланса …
        :param cashback_sum: Сумма пополнения бюджета промо-бонусами. …
        :param return_: Флаг возврата ответа (`true` — в ответе вернется обновлённый размер бюджета
            кампании, `false` или не указать параметр вообще — не вернётся.)
        :param sum: Общая сумма пополнения бюджета в базовых единицах валюты аккаунта продавца
        :param type_: Тип источника пополнения: - `0` — Счёт - `1` — Баланс - `3` — Бонусы
        """
        return await AdvV1BudgetDepositCreate(
            id_=id_,
            cashback_percent=cashback_percent,
            cashback_sum=cashback_sum,
            return_=return_,
            sum=sum,
            type_=type_,
        ).emit(self._api)

    async def adv_v1_count(self) -> AdvV1CountResponse:
        """Количество медиакампаний"""
        return await AdvV1Count().emit(self._api)

    async def adv_v1_normquery_stats_create(
        self, *, from_: str, items: list[AdvV1NormqueryStatsCreateItemsItem], to: str
    ) -> V1GetNormQueryStatsResponse:
        """Статистика по поисковым кластерам с детализацией по дням

        :param from_: Дата начала периода
        :param to: Дата окончания периода периода
        """
        return await AdvV1NormqueryStatsCreate(from_=from_, items=items, to=to).emit(self._api)

    async def adv_v1_payments(
        self, *, from_: str | None = None, to: str | None = None
    ) -> list[AdvV1PaymentsResponseItem]:
        """Получение истории пополнений счёта

        :param from_: Начало интервала
        :param to: Конец интервала. (Минимальный интервал 1 день, максимальный 31)
        """
        return await AdvV1Payments(from_=from_, to=to).emit(self._api)

    async def adv_v1_promotion_count(self) -> AdvV1PromotionCountResponse:
        """Списки кампаний"""
        return await AdvV1PromotionCount().emit(self._api)

    async def adv_v1_stats_create(self, *, body: Any) -> list[StatInterval]:
        """Статистика медиакампаний"""
        return await AdvV1StatsCreate(body=body).emit(self._api)

    async def adv_v1_supplier_subjects(
        self, *, payment_type: str | None = None
    ) -> list[AdvV1SupplierSubjectsResponseItem]:
        """Предметы для кампаний

        :param payment_type: Тип оплаты: - `cpm` — за показы - `cpc` — за клик
        """
        return await AdvV1SupplierSubjects(payment_type=payment_type).emit(self._api)

    async def adv_v1_upd(self, *, from_: str, to: str) -> list[AdvV1UpdResponseItem]:
        """Получение истории затрат

        :param from_: Начало интервала
        :param to: Конец интервала. (Минимальный интервал 1 день, максимальный 31)
        """
        return await AdvV1Upd(from_=from_, to=to).emit(self._api)

    async def adv_v2_seacat_save_ad_create(
        self,
        *,
        name: str,
        bid_type: str | None = None,
        nms: list[int] | None = None,
        payment_type: str | None = None,
        placement_types: list[str] | None = None,
    ) -> int:
        """Создать кампанию

        :param name: Название кампании
        :param bid_type: Тип ставки:   - `manual` — ручная   - `unified` — единая
        :param nms: Карточки товаров для кампании. Доступные карточки товаров можно получить с помощью
            метода Карточки товаров для кампаний. Максимум 50 товаров (`nm`)
        :param payment_type: Тип оплаты: - `cpm` — за показы - `cpc` — за клик. При создании с этим типом
            оплаты в кампании автоматически устанавливается минимальная ставка
        :param placement_types: Места размещения:   - `search` — в поиске   - `recommendations` — в
            рекомендациях  Укажите только для кампании с ручной ставкой
        """
        return await AdvV2SeacatSaveAdCreate(
            name=name, bid_type=bid_type, nms=nms, payment_type=payment_type, placement_types=placement_types
        ).emit(self._api)

    async def adv_v2_supplier_nms_create(self, *, body: Any) -> list[AdvV2SupplierNmsCreateResponseItem]:
        """Карточки товаров для кампаний"""
        return await AdvV2SupplierNmsCreate(body=body).emit(self._api)

    async def adv_v3_fullstats(self, *, begin_date: str, end_date: str, ids: str) -> list[FullStatsItem]:
        """Статистика кампаний

        :param begin_date: Дата начала интервала
        :param end_date: Дата окончания интервала
        :param ids: ID кампаний, максимум 50 значений
        """
        return await AdvV3Fullstats(begin_date=begin_date, end_date=end_date, ids=ids).emit(self._api)

    async def advert_v0_bids_recommendations(
        self, *, advert_id: int, nm_id: int
    ) -> V0BidsRecommendationsCpmResponse:
        """Рекомендуемые ставки для карточек товаров и поисковых кластеров

        :param advert_id: ID кампании
        :param nm_id: Артикул WB
        """
        return await AdvertV0BidsRecommendations(advert_id=advert_id, nm_id=nm_id).emit(self._api)

    async def advert_v1_bids_min_create(
        self, *, advert_id: int, nm_ids: list[int], payment_type: str, placement_types: list[str]
    ) -> AdvertV1BidsMinCreateResponse:
        """Минимальные ставки для карточек товаров

        :param advert_id: ID кампании
        :param nm_ids: Список артикулов WB
        :param payment_type: Тип оплаты:       - `cpm` — за показы       - `cpc` — за клик
        :param placement_types: Места размещения:   - `search` — поиск   - `recommendation` — рекомендации
            - `combined` — поиск и рекомендации
        """
        return await AdvertV1BidsMinCreate(
            advert_id=advert_id, nm_ids=nm_ids, payment_type=payment_type, placement_types=placement_types
        ).emit(self._api)

    async def advert_v1_bids_update(
        self, *, bids: list[AdvertV1BidsUpdateBidsItem]
    ) -> AdvertV1BidsUpdateResponse:
        """Изменение ставок в кампаниях

        :param bids: Ставки в кампаниях
        """
        return await AdvertV1BidsUpdate(bids=bids).emit(self._api)

    async def advert_v1_config(self) -> V2GetConfigResponse:
        """Конфигурационные значения продвижения"""
        return await AdvertV1Config().emit(self._api)

    async def advert_v1_normquery_bids_update(
        self, *, bids: list[V1SetNormQueryBidsRequestItem]
    ) -> V1SetNormQueryBidsResponse:
        """Установить ставки для поисковых кластеров в валюте аккаунта продавца"""
        return await AdvertV1NormqueryBidsUpdate(bids=bids).emit(self._api)

    async def advert_v2_adverts(
        self, *, ids: str | None = None, payment_type: str | None = None, statuses: str | None = None
    ) -> GetAdverts:
        """Информация о кампаниях

        :param ids: ID кампаний, максимум 50
        :param payment_type: Тип оплаты: - `cpm` — за показы - `cpc` — за клик
        :param statuses: Статусы кампаний: - `-1` — удалена, процесс удаления будет завершён в течение 10
            минут - `4` — готова к запуску - `7` — завершена - `8` — отменена …
        """
        return await AdvertV2Adverts(ids=ids, payment_type=payment_type, statuses=statuses).emit(self._api)

    async def calendar_promotions(
        self,
        *,
        all_promo: bool,
        end_date_time: str,
        start_date_time: str,
        limit: int | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> None | list[Any]:
        """Список акций

        :param all_promo: Показать акции:   - `false` — доступные для участия   - `true` — все акции
        :param end_date_time: Конец периода, формат `YYYY-MM-DDTHH:MM:SSZ`
        :param start_date_time: Начало периода, формат `YYYY-MM-DDTHH:MM:SSZ`
        :param limit: Количество запрашиваемых акций
        :param offset: После какого элемента выдавать данные
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = CalendarPromotions(
            all_promo=all_promo,
            end_date_time=end_date_time,
            start_date_time=start_date_time,
            limit=limit,
            offset=offset,
        )
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_calendar_promotions(
        self,
        *,
        all_promo: bool,
        end_date_time: str,
        start_date_time: str,
        limit: int | None = None,
        offset: int | None = None,
    ) -> AsyncIterator[Any]:
        """Список акций — постранично, по одной записи.

        :param all_promo: Показать акции:   - `false` — доступные для участия   - `true` — все акции
        :param end_date_time: Конец периода, формат `YYYY-MM-DDTHH:MM:SSZ`
        :param start_date_time: Начало периода, формат `YYYY-MM-DDTHH:MM:SSZ`
        :param limit: Количество запрашиваемых акций
        :param offset: После какого элемента выдавать данные
        """
        async for item in CalendarPromotions(
            all_promo=all_promo,
            end_date_time=end_date_time,
            start_date_time=start_date_time,
            limit=limit,
            offset=offset,
        ).stream(self._api):
            yield item

    async def calendar_promotions_details(self, *, promotion_ids: list[int]) -> None:
        """Детальная информация об акциях

        :param promotion_ids: ID акций, по которым нужно вернуть информацию
        """
        await CalendarPromotionsDetails(promotion_ids=promotion_ids).emit(self._api)

    async def calendar_promotions_nomenclatures(
        self,
        *,
        in_action: bool,
        promotion_id: int,
        limit: int | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> None | list[Any]:
        """Список товаров для участия в акции

        :param in_action: Участвует в акции:   - `true` — да   - `false` — нет
        :param promotion_id: ID акции
        :param limit: Количество запрашиваемых товаров
        :param offset: После какого элемента выдавать данные
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = CalendarPromotionsNomenclatures(
            in_action=in_action, promotion_id=promotion_id, limit=limit, offset=offset
        )
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_calendar_promotions_nomenclatures(
        self, *, in_action: bool, promotion_id: int, limit: int | None = None, offset: int | None = None
    ) -> AsyncIterator[Any]:
        """Список товаров для участия в акции — постранично, по одной записи.

        :param in_action: Участвует в акции:   - `true` — да   - `false` — нет
        :param promotion_id: ID акции
        :param limit: Количество запрашиваемых товаров
        :param offset: После какого элемента выдавать данные
        """
        async for item in CalendarPromotionsNomenclatures(
            in_action=in_action, promotion_id=promotion_id, limit=limit, offset=offset
        ).stream(self._api):
            yield item

    async def calendar_promotions_upload_create(self) -> None:
        """Добавить товар в акцию"""
        await CalendarPromotionsUploadCreate().emit(self._api)
