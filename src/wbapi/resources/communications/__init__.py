from __future__ import annotations

from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any

from .methods import (
    Claims,
    ClaimUpdate,
    Feedback,
    Feedbacks,
    FeedbacksAnswerCreate,
    FeedbacksAnswerUpdate,
    FeedbacksArchive,
    FeedbacksCount,
    FeedbacksCountUnanswered,
    FeedbacksOrderReturnCreate,
    FeedbacksV1Pins,
    FeedbacksV1PinsCount,
    FeedbacksV1PinsDelete,
    FeedbacksV1PinsLimits,
    FeedbacksV1PinsUpdate,
    NewFeedbacksQuestions,
    Question,
    Questions,
    QuestionsCount,
    QuestionsCountUnanswered,
    QuestionsUpdate,
    SellerChats,
    SellerDownloadId,
    SellerEvents,
    SellerMessageCreate,
)
from .models import (
    ChatsResponse,
    EventsResponse,
    FeedbackResponse,
    FeedbacksArchiveResponse,
    FeedbacksCountResponse,
    FeedbacksCountUnansweredResponse,
    FeedbacksOrderReturnCreateResponse,
    FeedbacksResponse,
    MessageResponse,
    NewFeedbacksQuestionsResponse,
    QuestionResponse,
    QuestionsCountResponse,
    QuestionsCountUnansweredResponse,
    QuestionsResponse,
    QuestionsUpdateResponse,
    RespondSuccessResponse,
)


if TYPE_CHECKING:
    from ...client import WBApi


class Communications:
    """Общение с покупателями.

    Узнать больше об общении с покупателями можно в справочном центре

    С помощью методов общения с покупателями вы можете работать с:
      1. Вопросами и отзывами покупателей
      2. Закреплёнными отзывами
      3. Чатами с покупателями
      4. Заявками покупателей на возврат

    Вы можете протестировать методы общения с покупателями в песочнице. Также в песочнице доступны
    специальные методы для управления тестовыми вопросами и отзывами

      Узнать, как использовать методы в бизнес-кейсах, можно в инструкции по работе с разделом Общение с
      покупателями
    """

    __slots__ = ("_api",)

    def __init__(self, api: WBApi) -> None:
        self._api = api

    async def claim_update(self) -> None:
        """Ответ на заявку покупателя"""
        await ClaimUpdate().emit(self._api)

    async def claims(
        self,
        *,
        is_archive: bool,
        id_: str | None = None,
        limit: int | None = None,
        nm_id: int | None = None,
        offset: int | None = None,
        auto_paginate: bool = False,
    ) -> None | list[Any]:
        """Заявки покупателей на возврат

        :param is_archive: Состояние заявки:   * `false` — на рассмотрении   * `true` — в архиве
        :param id_: ID заявки
        :param limit: Количество заявок в ответе
        :param nm_id: Артикул WB
        :param offset: После какого элемента выдавать данные
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = Claims(is_archive=is_archive, id_=id_, limit=limit, nm_id=nm_id, offset=offset)
        if auto_paginate:
            return await call.paginate(self._api)
        await call.emit(self._api)
        return None

    async def iter_claims(
        self,
        *,
        is_archive: bool,
        id_: str | None = None,
        limit: int | None = None,
        nm_id: int | None = None,
        offset: int | None = None,
    ) -> AsyncIterator[Any]:
        """Заявки покупателей на возврат — постранично, по одной записи.

        :param is_archive: Состояние заявки:   * `false` — на рассмотрении   * `true` — в архиве
        :param id_: ID заявки
        :param limit: Количество заявок в ответе
        :param nm_id: Артикул WB
        :param offset: После какого элемента выдавать данные
        """
        async for item in Claims(
            is_archive=is_archive, id_=id_, limit=limit, nm_id=nm_id, offset=offset
        ).stream(self._api):
            yield item

    async def feedback(self, *, id_: str) -> FeedbackResponse:
        """Получить отзыв по ID

        :param id_: ID отзыва
        """
        return await Feedback(id_=id_).emit(self._api)

    async def feedbacks(
        self,
        *,
        is_answered: bool,
        skip: int,
        take: int,
        date_from: int | None = None,
        date_to: int | None = None,
        nm_id: int | None = None,
        order: str | None = None,
        auto_paginate: bool = False,
    ) -> FeedbacksResponse | list[Any]:
        """Список отзывов

        :param is_answered: Вернуть только обработанные отзывы:   - `true` — да   - `false` — нет
        :param skip: Количество отзывов для пропуска (max. 199990)
        :param take: Количество отзывов (max. 5 000)
        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param nm_id: Артикул WB
        :param order: Сортировка отзывов по дате (dateAsc/dateDesc)
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = Feedbacks(
            is_answered=is_answered,
            skip=skip,
            take=take,
            date_from=date_from,
            date_to=date_to,
            nm_id=nm_id,
            order=order,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_feedbacks(
        self,
        *,
        is_answered: bool,
        skip: int,
        take: int,
        date_from: int | None = None,
        date_to: int | None = None,
        nm_id: int | None = None,
        order: str | None = None,
    ) -> AsyncIterator[Any]:
        """Список отзывов — постранично, по одной записи.

        :param is_answered: Вернуть только обработанные отзывы:   - `true` — да   - `false` — нет
        :param skip: Количество отзывов для пропуска (max. 199990)
        :param take: Количество отзывов (max. 5 000)
        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param nm_id: Артикул WB
        :param order: Сортировка отзывов по дате (dateAsc/dateDesc)
        """
        async for item in Feedbacks(
            is_answered=is_answered,
            skip=skip,
            take=take,
            date_from=date_from,
            date_to=date_to,
            nm_id=nm_id,
            order=order,
        ).stream(self._api):
            yield item

    async def feedbacks_answer_create(self, *, id_: str, text: str) -> None:
        """Ответить на отзыв

        :param id_: ID отзыва
        :param text: Текст ответа
        """
        await FeedbacksAnswerCreate(id_=id_, text=text).emit(self._api)

    async def feedbacks_answer_update(self, *, id_: str, text: str) -> None:
        """Отредактировать ответ на отзыв

        :param id_: ID отзыва
        :param text: Текст ответа
        """
        await FeedbacksAnswerUpdate(id_=id_, text=text).emit(self._api)

    async def feedbacks_archive(
        self,
        *,
        skip: int,
        take: int,
        nm_id: int | None = None,
        order: str | None = None,
        auto_paginate: bool = False,
    ) -> FeedbacksArchiveResponse | list[Any]:
        """Список архивных отзывов

        :param skip: Количество отзывов для пропуска
        :param take: Количество отзывов (max. 5 000)
        :param nm_id: Артикул WB
        :param order: Сортировка отзывов по дате (dateAsc/dateDesc)
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = FeedbacksArchive(skip=skip, take=take, nm_id=nm_id, order=order)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_feedbacks_archive(
        self, *, skip: int, take: int, nm_id: int | None = None, order: str | None = None
    ) -> AsyncIterator[Any]:
        """Список архивных отзывов — постранично, по одной записи.

        :param skip: Количество отзывов для пропуска
        :param take: Количество отзывов (max. 5 000)
        :param nm_id: Артикул WB
        :param order: Сортировка отзывов по дате (dateAsc/dateDesc)
        """
        async for item in FeedbacksArchive(skip=skip, take=take, nm_id=nm_id, order=order).stream(self._api):
            yield item

    async def feedbacks_count(
        self, *, is_answered: bool, date_from: int | None = None, date_to: int | None = None
    ) -> FeedbacksCountResponse:
        """Количество отзывов

        :param is_answered: Вернуть только обработанные отзывы:   - `true` — да   - `false` — нет
        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        """
        return await FeedbacksCount(is_answered=is_answered, date_from=date_from, date_to=date_to).emit(
            self._api
        )

    async def feedbacks_count_unanswered(self) -> FeedbacksCountUnansweredResponse:
        """Необработанные отзывы"""
        return await FeedbacksCountUnanswered().emit(self._api)

    async def feedbacks_order_return_create(
        self, *, feedback_id: str | None = None
    ) -> FeedbacksOrderReturnCreateResponse:
        """Возврат товара по ID отзыва

        :param feedback_id: ID отзыва
        """
        return await FeedbacksOrderReturnCreate(feedback_id=feedback_id).emit(self._api)

    async def feedbacks_v1_pins(
        self,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        feedback_id: int | None = None,
        imt_id: int | None = None,
        limit: int | None = None,
        next_: int | None = None,
        nm_id: int | None = None,
        pin_on: str | None = None,
        state: str | None = None,
        auto_paginate: bool = False,
    ) -> RespondSuccessResponse | list[Any]:
        """Список закреплённых и откреплённых отзывов

        :param date_from: Дата закрепления первого отзыва в списке
        :param date_to: Дата закрепления последнего отзыва в списке
        :param feedback_id: ID отзыва
        :param imt_id: ID для объединённых карточек товаров.Един для всех артикулов WB группы объединённых
            карточек.У каждой карточки товара есть `imtId`, даже если она не объединена …
        :param limit: Количество отзывов на одной странице (пагинация)
        :param next_: ID последней операции закрепления (пагинатор)
        :param nm_id: Артикул WB
        :param pin_on: Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа объединённых
            карточек товаров
        :param state: Закреплён ли отзыв:   - `pinned` — да   - `unpinned` — нет
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = FeedbacksV1Pins(
            date_from=date_from,
            date_to=date_to,
            feedback_id=feedback_id,
            imt_id=imt_id,
            limit=limit,
            next_=next_,
            nm_id=nm_id,
            pin_on=pin_on,
            state=state,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_feedbacks_v1_pins(
        self,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        feedback_id: int | None = None,
        imt_id: int | None = None,
        limit: int | None = None,
        next_: int | None = None,
        nm_id: int | None = None,
        pin_on: str | None = None,
        state: str | None = None,
    ) -> AsyncIterator[Any]:
        """Список закреплённых и откреплённых отзывов — постранично, по одной записи.

        :param date_from: Дата закрепления первого отзыва в списке
        :param date_to: Дата закрепления последнего отзыва в списке
        :param feedback_id: ID отзыва
        :param imt_id: ID для объединённых карточек товаров.Един для всех артикулов WB группы объединённых
            карточек.У каждой карточки товара есть `imtId`, даже если она не объединена …
        :param limit: Количество отзывов на одной странице (пагинация)
        :param next_: ID последней операции закрепления (пагинатор)
        :param nm_id: Артикул WB
        :param pin_on: Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа объединённых
            карточек товаров
        :param state: Закреплён ли отзыв:   - `pinned` — да   - `unpinned` — нет
        """
        async for item in FeedbacksV1Pins(
            date_from=date_from,
            date_to=date_to,
            feedback_id=feedback_id,
            imt_id=imt_id,
            limit=limit,
            next_=next_,
            nm_id=nm_id,
            pin_on=pin_on,
            state=state,
        ).stream(self._api):
            yield item

    async def feedbacks_v1_pins_count(
        self,
        *,
        date_from: str | None = None,
        date_to: str | None = None,
        feedback_id: int | None = None,
        imt_id: int | None = None,
        nm_id: int | None = None,
        pin_on: str | None = None,
        state: str | None = None,
    ) -> RespondSuccessResponse:
        """Количество закреплённых и откреплённых отзывов

        :param date_from: Дата закрепления первого отзыва в списке
        :param date_to: Дата закрепления последнего отзыва в списке
        :param feedback_id: ID отзыва
        :param imt_id: ID для объединённых карточек товаров.Един для всех артикулов WB группы объединённых
            карточек.У каждой карточки товара есть `imtId`, даже если она не объединена …
        :param nm_id: Артикул WB
        :param pin_on: Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа объединённых
            карточек товаров
        :param state: Закреплён ли отзыв:   - `pinned` — да   - `unpinned` — нет
        """
        return await FeedbacksV1PinsCount(
            date_from=date_from,
            date_to=date_to,
            feedback_id=feedback_id,
            imt_id=imt_id,
            nm_id=nm_id,
            pin_on=pin_on,
            state=state,
        ).emit(self._api)

    async def feedbacks_v1_pins_delete(self, *, body: Any) -> RespondSuccessResponse:
        """Открепить отзывы"""
        return await FeedbacksV1PinsDelete(body=body).emit(self._api)

    async def feedbacks_v1_pins_limits(self) -> RespondSuccessResponse:
        """Лимиты закреплённых отзывов"""
        return await FeedbacksV1PinsLimits().emit(self._api)

    async def feedbacks_v1_pins_update(self, *, body: Any) -> RespondSuccessResponse:
        """Закрепить отзывы"""
        return await FeedbacksV1PinsUpdate(body=body).emit(self._api)

    async def new_feedbacks_questions(self) -> NewFeedbacksQuestionsResponse:
        """Непросмотренные отзывы и вопросы"""
        return await NewFeedbacksQuestions().emit(self._api)

    async def question(self, *, id_: str) -> QuestionResponse:
        """Получить вопрос по ID

        :param id_: ID вопроса
        """
        return await Question(id_=id_).emit(self._api)

    async def questions(
        self,
        *,
        is_answered: bool,
        skip: int,
        take: int,
        date_from: int | None = None,
        date_to: int | None = None,
        nm_id: int | None = None,
        order: str | None = None,
        auto_paginate: bool = False,
    ) -> QuestionsResponse | list[Any]:
        """Список вопросов

        :param is_answered: Есть ли ответ на вопрос:   - `true` — да   - `false` — нет
        :param skip: Количество вопросов для пропуска (максимально допустимое значение для параметра - 10
            000, …
        :param take: Количество запрашиваемых вопросов (максимально допустимое значение для параметра - 10
            000, …
        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param nm_id: Артикул WB
        :param order: Сортировка вопросов по дате (`dateAsc`/`dateDesc`)
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = Questions(
            is_answered=is_answered,
            skip=skip,
            take=take,
            date_from=date_from,
            date_to=date_to,
            nm_id=nm_id,
            order=order,
        )
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_questions(
        self,
        *,
        is_answered: bool,
        skip: int,
        take: int,
        date_from: int | None = None,
        date_to: int | None = None,
        nm_id: int | None = None,
        order: str | None = None,
    ) -> AsyncIterator[Any]:
        """Список вопросов — постранично, по одной записи.

        :param is_answered: Есть ли ответ на вопрос:   - `true` — да   - `false` — нет
        :param skip: Количество вопросов для пропуска (максимально допустимое значение для параметра - 10
            000, …
        :param take: Количество запрашиваемых вопросов (максимально допустимое значение для параметра - 10
            000, …
        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param nm_id: Артикул WB
        :param order: Сортировка вопросов по дате (`dateAsc`/`dateDesc`)
        """
        async for item in Questions(
            is_answered=is_answered,
            skip=skip,
            take=take,
            date_from=date_from,
            date_to=date_to,
            nm_id=nm_id,
            order=order,
        ).stream(self._api):
            yield item

    async def questions_count(
        self, *, date_from: int | None = None, date_to: int | None = None, is_answered: bool | None = None
    ) -> QuestionsCountResponse:
        """Количество вопросов

        :param date_from: Дата начала периода в формате Unix timestamp
        :param date_to: Дата конца периода в формате Unix timestamp
        :param is_answered: Есть ли ответ на вопрос:   - `true` — да   - `false` — нет
        """
        return await QuestionsCount(date_from=date_from, date_to=date_to, is_answered=is_answered).emit(
            self._api
        )

    async def questions_count_unanswered(self) -> QuestionsCountUnansweredResponse:
        """Неотвеченные вопросы"""
        return await QuestionsCountUnanswered().emit(self._api)

    async def questions_update(self, *, body: Any) -> QuestionsUpdateResponse:
        """Работа с вопросами"""
        return await QuestionsUpdate(body=body).emit(self._api)

    async def seller_chats(self) -> ChatsResponse:
        """Список чатов"""
        return await SellerChats().emit(self._api)

    async def seller_download_id(self, *, id_: str | int) -> None:
        """Получить файл из сообщения

        :param id_: ID файла, см. значение поля `downloadID` в методе События чатов
        """
        await SellerDownloadId(id_=id_).emit(self._api)

    async def seller_events(
        self, *, next_: int | None = None, auto_paginate: bool = False
    ) -> EventsResponse | list[Any]:
        """События чатов

        :param next_: Пагинатор. С какого момента получить следующий пакет данных.Формат Unix timestamp **с
            миллисекундами**
        :param auto_paginate: автоматически собрать все страницы выборки
        """
        call = SellerEvents(next_=next_)
        return await call.paginate(self._api) if auto_paginate else await call.emit(self._api)

    async def iter_seller_events(self, *, next_: int | None = None) -> AsyncIterator[Any]:
        """События чатов — постранично, по одной записи.

        :param next_: Пагинатор. С какого момента получить следующий пакет данных.Формат Unix timestamp **с
            миллисекундами**
        """
        async for item in SellerEvents(next_=next_).stream(self._api):
            yield item

    async def seller_message_create(self) -> MessageResponse:
        """Отправить сообщение"""
        return await SellerMessageCreate().emit(self._api)
