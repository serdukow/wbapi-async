from __future__ import annotations

from typing import Any

from ...client.method import WBMethod
from ...utils.token import Scope
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
    OpenapiPinReviewItem,
    QuestionResponse,
    QuestionsCountResponse,
    QuestionsCountUnansweredResponse,
    QuestionsResponse,
    QuestionsUpdateBody,
    QuestionsUpdateResponse,
    RespondSuccessResponse,
)


class ClaimUpdate(WBMethod[None]):
    """Ответ на заявку покупателя

    PATCH /api/v1/claim
    """

    __path__ = "/api/v1/claim"
    __http_method__ = "PATCH"
    __returns__ = None
    __scope__ = Scope.RETURNS
    __host__ = "https://returns-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 10),
        "service": (3000, 10),
        "basic_secret": (3000, 10),
        "basic": (3600000, 1),
    }


class Claims(WBMethod[None]):
    """Заявки покупателей на возврат

    GET /api/v1/claims
    """

    __path__ = "/api/v1/claims"
    __http_method__ = "GET"
    __returns__ = None
    __query_params__ = {
        "is_archive": "is_archive",
        "id_": "id",
        "limit": "limit",
        "offset": "offset",
        "nm_id": "nm_id",
    }
    __scope__ = Scope.RETURNS
    __host__ = "https://returns-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (3000, 10),
        "service": (3000, 10),
        "basic_secret": (3000, 10),
        "basic": (3600000, 1),
    }
    __paginate__ = "offset_query"

    is_archive: bool
    """Состояние заявки:   * `false` — на рассмотрении   * `true` — в архиве"""
    id_: str | None = None
    """ID заявки"""
    limit: int | None = None
    """Количество заявок в ответе"""
    nm_id: int | None = None
    """Артикул WB"""
    offset: int | None = None
    """После какого элемента выдавать данные"""


class Feedback(WBMethod[FeedbackResponse]):
    """Получить отзыв по ID

    GET /api/v1/feedback
    """

    __path__ = "/api/v1/feedback"
    __http_method__ = "GET"
    __returns__ = FeedbackResponse
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"

    id_: str
    """ID отзыва"""


class Feedbacks(WBMethod[FeedbacksResponse]):
    """Список отзывов

    GET /api/v1/feedbacks
    """

    __path__ = "/api/v1/feedbacks"
    __http_method__ = "GET"
    __returns__ = FeedbacksResponse
    __query_params__ = {
        "is_answered": "isAnswered",
        "nm_id": "nmId",
        "take": "take",
        "skip": "skip",
        "order": "order",
        "date_from": "dateFrom",
        "date_to": "dateTo",
    }
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __paginate__ = "skip_take"
    __items__ = "data"

    is_answered: bool
    """Вернуть только обработанные отзывы:   - `true` — да   - `false` — нет"""
    skip: int
    """Количество отзывов для пропуска (max. 199990)"""
    take: int
    """Количество отзывов (max. 5 000)"""
    date_from: int | None = None
    """Дата начала периода в формате Unix timestamp"""
    date_to: int | None = None
    """Дата конца периода в формате Unix timestamp"""
    nm_id: int | None = None
    """Артикул WB"""
    order: str | None = None
    """Сортировка отзывов по дате (dateAsc/dateDesc)"""


class FeedbacksAnswerCreate(WBMethod[None]):
    """Ответить на отзыв

    POST /api/v1/feedbacks/answer
    """

    __path__ = "/api/v1/feedbacks/answer"
    __http_method__ = "POST"
    __returns__ = None
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __body_fields__ = {"id_": "id", "text": "text"}

    id_: str
    """ID отзыва"""
    text: str
    """Текст ответа"""


class FeedbacksAnswerUpdate(WBMethod[None]):
    """Отредактировать ответ на отзыв

    PATCH /api/v1/feedbacks/answer
    """

    __path__ = "/api/v1/feedbacks/answer"
    __http_method__ = "PATCH"
    __returns__ = None
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __body_fields__ = {"id_": "id", "text": "text"}

    id_: str
    """ID отзыва"""
    text: str
    """Текст ответа"""


class FeedbacksArchive(WBMethod[FeedbacksArchiveResponse]):
    """Список архивных отзывов

    GET /api/v1/feedbacks/archive
    """

    __path__ = "/api/v1/feedbacks/archive"
    __http_method__ = "GET"
    __returns__ = FeedbacksArchiveResponse
    __query_params__ = {"nm_id": "nmId", "take": "take", "skip": "skip", "order": "order"}
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __paginate__ = "skip_take"
    __items__ = "data"

    skip: int
    """Количество отзывов для пропуска"""
    take: int
    """Количество отзывов (max. 5 000)"""
    nm_id: int | None = None
    """Артикул WB"""
    order: str | None = None
    """Сортировка отзывов по дате (dateAsc/dateDesc)"""


class FeedbacksCount(WBMethod[FeedbacksCountResponse]):
    """Количество отзывов

    GET /api/v1/feedbacks/count
    """

    __path__ = "/api/v1/feedbacks/count"
    __http_method__ = "GET"
    __returns__ = FeedbacksCountResponse
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo", "is_answered": "isAnswered"}
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"

    is_answered: bool
    """Вернуть только обработанные отзывы:   - `true` — да   - `false` — нет"""
    date_from: int | None = None
    """Дата начала периода в формате Unix timestamp"""
    date_to: int | None = None
    """Дата конца периода в формате Unix timestamp"""


class FeedbacksCountUnanswered(WBMethod[FeedbacksCountUnansweredResponse]):
    """Необработанные отзывы

    GET /api/v1/feedbacks/count-unanswered
    """

    __path__ = "/api/v1/feedbacks/count-unanswered"
    __http_method__ = "GET"
    __returns__ = FeedbacksCountUnansweredResponse
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"


class FeedbacksOrderReturnCreate(WBMethod[FeedbacksOrderReturnCreateResponse]):
    """Возврат товара по ID отзыва

    POST /api/v1/feedbacks/order/return
    """

    __path__ = "/api/v1/feedbacks/order/return"
    __http_method__ = "POST"
    __returns__ = FeedbacksOrderReturnCreateResponse
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"
    __body_fields__ = {"feedback_id": "feedbackId"}

    feedback_id: str | None = None
    """ID отзыва"""


class FeedbacksV1Pins(WBMethod[RespondSuccessResponse]):
    """Список закреплённых и откреплённых отзывов

    GET /api/feedbacks/v1/pins
    """

    __path__ = "/api/feedbacks/v1/pins"
    __http_method__ = "GET"
    __returns__ = RespondSuccessResponse
    __query_params__ = {
        "state": "state",
        "pin_on": "pinOn",
        "imt_id": "imtId",
        "nm_id": "nmId",
        "feedback_id": "feedbackId",
        "date_from": "dateFrom",
        "date_to": "dateTo",
        "next_": "next",
        "limit": "limit",
    }
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __paginate__ = "next"

    date_from: str | None = None
    """Дата закрепления первого отзыва в списке"""
    date_to: str | None = None
    """Дата закрепления последнего отзыва в списке"""
    feedback_id: int | None = None
    """ID отзыва"""
    imt_id: int | None = None
    """ID для объединённых карточек товаров.Един для всех артикулов WB группы объединённых
    карточек.У каждой карточки товара есть `imtId`, даже если она не объединена …
    """
    limit: int | None = None
    """Количество отзывов на одной странице (пагинация)"""
    next_: int | None = None
    """ID последней операции закрепления (пагинатор)"""
    nm_id: int | None = None
    """Артикул WB"""
    pin_on: str | None = None
    """Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа объединённых
    карточек товаров
    """
    state: str | None = None
    """Закреплён ли отзыв:   - `pinned` — да   - `unpinned` — нет"""


class FeedbacksV1PinsCount(WBMethod[RespondSuccessResponse]):
    """Количество закреплённых и откреплённых отзывов

    GET /api/feedbacks/v1/pins/count
    """

    __path__ = "/api/feedbacks/v1/pins/count"
    __http_method__ = "GET"
    __returns__ = RespondSuccessResponse
    __query_params__ = {
        "state": "state",
        "pin_on": "pinOn",
        "imt_id": "imtId",
        "nm_id": "nmId",
        "feedback_id": "feedbackId",
        "date_from": "dateFrom",
        "date_to": "dateTo",
    }
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }

    date_from: str | None = None
    """Дата закрепления первого отзыва в списке"""
    date_to: str | None = None
    """Дата закрепления последнего отзыва в списке"""
    feedback_id: int | None = None
    """ID отзыва"""
    imt_id: int | None = None
    """ID для объединённых карточек товаров.Един для всех артикулов WB группы объединённых
    карточек.У каждой карточки товара есть `imtId`, даже если она не объединена …
    """
    nm_id: int | None = None
    """Артикул WB"""
    pin_on: str | None = None
    """Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа объединённых
    карточек товаров
    """
    state: str | None = None
    """Закреплён ли отзыв:   - `pinned` — да   - `unpinned` — нет"""


class FeedbacksV1PinsDelete(WBMethod[RespondSuccessResponse]):
    """Открепить отзывы

    DELETE /api/feedbacks/v1/pins
    """

    __path__ = "/api/feedbacks/v1/pins"
    __http_method__ = "DELETE"
    __returns__ = RespondSuccessResponse
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }

    body: list[int] | list[Any] | dict[str, Any]


class FeedbacksV1PinsLimits(WBMethod[RespondSuccessResponse]):
    """Лимиты закреплённых отзывов

    GET /api/feedbacks/v1/pins/limits
    """

    __path__ = "/api/feedbacks/v1/pins/limits"
    __http_method__ = "GET"
    __returns__ = RespondSuccessResponse
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }


class FeedbacksV1PinsUpdate(WBMethod[RespondSuccessResponse]):
    """Закрепить отзывы

    POST /api/feedbacks/v1/pins
    """

    __path__ = "/api/feedbacks/v1/pins"
    __http_method__ = "POST"
    __returns__ = RespondSuccessResponse
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }

    body: list[OpenapiPinReviewItem] | list[Any] | dict[str, Any]


class NewFeedbacksQuestions(WBMethod[NewFeedbacksQuestionsResponse]):
    """Непросмотренные отзывы и вопросы

    GET /api/v1/new-feedbacks-questions
    """

    __path__ = "/api/v1/new-feedbacks-questions"
    __http_method__ = "GET"
    __returns__ = NewFeedbacksQuestionsResponse
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"


class Question(WBMethod[QuestionResponse]):
    """Получить вопрос по ID

    GET /api/v1/question
    """

    __path__ = "/api/v1/question"
    __http_method__ = "GET"
    __returns__ = QuestionResponse
    __query_params__ = {"id_": "id"}
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"

    id_: str
    """ID вопроса"""


class Questions(WBMethod[QuestionsResponse]):
    """Список вопросов

    GET /api/v1/questions
    """

    __path__ = "/api/v1/questions"
    __http_method__ = "GET"
    __returns__ = QuestionsResponse
    __query_params__ = {
        "is_answered": "isAnswered",
        "nm_id": "nmId",
        "take": "take",
        "skip": "skip",
        "order": "order",
        "date_from": "dateFrom",
        "date_to": "dateTo",
    }
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __paginate__ = "skip_take"
    __items__ = "data"

    is_answered: bool
    """Есть ли ответ на вопрос:   - `true` — да   - `false` — нет"""
    skip: int
    """Количество вопросов для пропуска (максимально допустимое значение для параметра - 10 000, …
    """
    take: int
    """Количество запрашиваемых вопросов (максимально допустимое значение для параметра - 10 000, …
    """
    date_from: int | None = None
    """Дата начала периода в формате Unix timestamp"""
    date_to: int | None = None
    """Дата конца периода в формате Unix timestamp"""
    nm_id: int | None = None
    """Артикул WB"""
    order: str | None = None
    """Сортировка вопросов по дате (`dateAsc`/`dateDesc`)"""


class QuestionsCount(WBMethod[QuestionsCountResponse]):
    """Количество вопросов

    GET /api/v1/questions/count
    """

    __path__ = "/api/v1/questions/count"
    __http_method__ = "GET"
    __returns__ = QuestionsCountResponse
    __query_params__ = {"date_from": "dateFrom", "date_to": "dateTo", "is_answered": "isAnswered"}
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"

    date_from: int | None = None
    """Дата начала периода в формате Unix timestamp"""
    date_to: int | None = None
    """Дата конца периода в формате Unix timestamp"""
    is_answered: bool | None = None
    """Есть ли ответ на вопрос:   - `true` — да   - `false` — нет"""


class QuestionsCountUnanswered(WBMethod[QuestionsCountUnansweredResponse]):
    """Неотвеченные вопросы

    GET /api/v1/questions/count-unanswered
    """

    __path__ = "/api/v1/questions/count-unanswered"
    __http_method__ = "GET"
    __returns__ = QuestionsCountUnansweredResponse
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"


class QuestionsUpdate(WBMethod[QuestionsUpdateResponse]):
    """Работа с вопросами

    PATCH /api/v1/questions
    """

    __path__ = "/api/v1/questions"
    __http_method__ = "PATCH"
    __returns__ = QuestionsUpdateResponse
    __scope__ = Scope.FEEDBACKS
    __host__ = "https://feedbacks-api.wildberries.ru"
    __sandbox_host__ = "https://feedbacks-api-sandbox.wildberries.ru"
    __rate_limits__ = {
        "personal": (333, 6),
        "service": (333, 6),
        "basic_secret": (333, 6),
        "basic": (720000, 1),
    }
    __items__ = "data"

    body: QuestionsUpdateBody | list[Any] | dict[str, Any]


class SellerChats(WBMethod[ChatsResponse]):
    """Список чатов

    GET /api/v1/seller/chats
    """

    __path__ = "/api/v1/seller/chats"
    __http_method__ = "GET"
    __returns__ = ChatsResponse
    __scope__ = Scope.BUYER_CHAT
    __host__ = "https://buyer-chat-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 10),
        "service": (1000, 10),
        "basic_secret": (1000, 10),
        "basic": (3600000, 1),
    }
    __items__ = "result"


class SellerDownloadId(WBMethod[None]):
    """Получить файл из сообщения

    GET /api/v1/seller/download/{id}
    """

    __path__ = "/api/v1/seller/download/{id}"
    __http_method__ = "GET"
    __returns__ = None
    __path_params__ = ("id",)
    __scope__ = Scope.BUYER_CHAT
    __host__ = "https://buyer-chat-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 10),
        "service": (1000, 10),
        "basic_secret": (1000, 10),
        "basic": (360000, 1),
    }

    id_: str | int
    """ID файла, см. значение поля `downloadID` в методе События чатов"""


class SellerEvents(WBMethod[EventsResponse]):
    """События чатов

    GET /api/v1/seller/events
    """

    __path__ = "/api/v1/seller/events"
    __http_method__ = "GET"
    __returns__ = EventsResponse
    __query_params__ = {"next_": "next"}
    __scope__ = Scope.BUYER_CHAT
    __host__ = "https://buyer-chat-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 10),
        "service": (1000, 10),
        "basic_secret": (1000, 10),
        "basic": (3600000, 1),
    }
    __paginate__ = "next"
    __items__ = "result"

    next_: int | None = None
    """Пагинатор. С какого момента получить следующий пакет данных.Формат Unix timestamp **с
    миллисекундами**
    """


class SellerMessageCreate(WBMethod[MessageResponse]):
    """Отправить сообщение

    POST /api/v1/seller/message
    """

    __path__ = "/api/v1/seller/message"
    __http_method__ = "POST"
    __returns__ = MessageResponse
    __scope__ = Scope.BUYER_CHAT
    __host__ = "https://buyer-chat-api.wildberries.ru"
    __rate_limits__ = {
        "personal": (1000, 10),
        "service": (1000, 10),
        "basic_secret": (1000, 10),
        "basic": (3600000, 1),
    }
    __items__ = "result"
