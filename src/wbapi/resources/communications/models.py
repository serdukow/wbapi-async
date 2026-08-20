from __future__ import annotations

from typing import Any

from msgspec import field as _field

from ...client.model import WBModel


class Chat(WBModel):
    chat_id: str | None = _field(default=None, name="chatID")
    """ID чата"""
    client_name: str | None = _field(default=None, name="clientName")
    """Имя покупателя"""
    good_card: Listing | None = _field(default=None, name="goodCard")
    last_message: LastMessage | None = _field(default=None, name="lastMessage")
    """Последнее сообщение в чате"""
    reply_sign: str | None = _field(default=None, name="replySign")
    """Подпись чата. Требуется при отправке сообщения"""


class ChatsResponse(WBModel):
    errors: list[str] | None = _field(default=None)
    """Ошибки, если есть"""
    result: list[Chat] | None = _field(default=None)


class Event(WBModel):
    add_time: Any | None = _field(default=None, name="addTime")
    """Время появления события на сервере в UTC"""
    add_timestamp: Any | None = _field(default=None, name="addTimestamp")
    """Время появления события на сервере. Формат Unix timestamp"""
    chat_id: Any | None = _field(default=None, name="chatID")
    """ID чата"""
    client_name: Any | None = _field(default=None, name="clientName")
    """Имя покупателя"""
    event_id: Any | None = _field(default=None, name="eventID")
    """ID события"""
    event_type: Any | None = _field(default=None, name="eventType")
    is_new_chat: Any | None = _field(default=None, name="isNewChat")
    """Признак нового чата: - `false` — чат не новый - `true` — чат новый"""
    message: Any | None = _field(default=None)
    """Данные сообщения"""
    reply_sign: Any | None = _field(default=None, name="replySign")
    """Подпись чата. Доступна только при `"isNewChat": true`. Требуется при отправке сообщения
    """
    sender: Any | None = _field(default=None)
    source: Any | None = _field(default=None)
    """Источник отправки сообщения: - `seller-portal` — портал продавцов - `seller-public-api` —
    API Чата с покупателями - `rusite` — портал покупателей …
    """


class EventsResponse(WBModel):
    errors: list[str] | None = _field(default=None)
    """Ошибки, если есть"""
    result: EventsResult | None = _field(default=None)


class EventsResult(WBModel):
    events: list[Event] | None = _field(default=None)
    newest_event_time: str | None = _field(default=None, name="newestEventTime")
    """Время новейшего события в ответе"""
    next: int | None = _field(default=None)
    """Пагинатор. Значение поля необходимо указать в запросе для получения следующего пакета данных
    """
    oldest_event_time: str | None = _field(default=None, name="oldestEventTime")
    """Время старейшего события в ответе"""
    total_events: int | None = _field(default=None, name="totalEvents")
    """Количество событий"""


class FeedbackResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: FeedbackResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class FeedbackResponseData(WBModel):
    answer: FeedbackResponseDataAnswer | None = _field(default=None)
    """Структура ответа"""
    bables: list[str] | None = _field(default=None)
    """Список тегов покупателя"""
    child_feedback_id: str | None = _field(default=None, name="childFeedbackId")
    """ID дополненного отзыва (`null`, если этот отзыв дополненный)"""
    color: str | None = _field(default=None)
    """Цвет товара"""
    cons: str | None = _field(default=None)
    """Недостатки товара"""
    created_date: str | None = _field(default=None, name="createdDate")
    """Дата и время создания отзыва"""
    id: str | None = _field(default=None)
    """ID отзыва"""
    is_able_return_product_orders: bool | None = _field(default=None, name="isAbleReturnProductOrders")
    """Опция возврата товара:   - `true` — доступна   - `false` — недоступна"""
    is_able_supplier_feedback_valuation: bool | None = _field(
        default=None, name="isAbleSupplierFeedbackValuation"
    )
    """Доступна ли продавцу возможность оставить жалобу на отзыв:   - `true`— да   - `false` — нет
    """
    is_able_supplier_product_valuation: bool | None = _field(
        default=None, name="isAbleSupplierProductValuation"
    )
    """Доступна ли продавцу возможность сообщить о проблеме с товаром  (`true` - доступна, `false`
    - не доступна)
    """
    last_order_created_at: str | None = _field(default=None, name="lastOrderCreatedAt")
    """Дата покупки"""
    last_order_shk_id: int | None = _field(default=None, name="lastOrderShkId")
    """Штрихкод единицы товара"""
    matching_size: str | None = _field(default=None, name="matchingSize")
    """Соответствие заявленного размера реальному. Возможные значения: - ` ` - для безразмерных
    товаров - `ок` - соответствует размеру - `smaller` - маломерит …
    """
    order_status: str | None = _field(default=None, name="orderStatus")
    """Статус заказа. Возможные значения: - `buyout` — выкуплен - `rejected` — отказались -
    `returned` — возврат - `notSpecified` — статус не присвоен
    """
    parent_feedback_id: str | None = _field(default=None, name="parentFeedbackId")
    """ID начального отзыва (`null`, если этот отзыв начальный)"""
    photo_links: list[FeedbackResponseDataPhotoLinksItem] | None = _field(default=None, name="photoLinks")
    """Массив структур фотографий"""
    product_details: FeedbackResponseDataProductDetails | None = _field(default=None, name="productDetails")
    """Item information"""
    product_valuation: int | None = _field(default=None, name="productValuation")
    """Оценка товара"""
    pros: str | None = _field(default=None)
    """Достоинства товара"""
    return_product_orders_date: str | None = _field(default=None, name="returnProductOrdersDate")
    """Дата и время, когда на запрос возврата был получен ответ со статус-кодом 200."""
    state: str | None = _field(default=None)
    """Статус отзыва:   - `none` - не обработан (новый)   - `wbRu` - обработан"""
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    supplier_feedback_valuation: int | None = _field(default=None, name="supplierFeedbackValuation")
    """Ключ причины жалобы на отзыв"""
    supplier_product_valuation: int | None = _field(default=None, name="supplierProductValuation")
    """Ключ проблемы с товаром"""
    text: str | None = _field(default=None)
    """Текст отзыва"""
    user_name: str | None = _field(default=None, name="userName")
    """Имя автора отзыва"""
    video: FeedbackResponseDataVideo | None = _field(default=None)
    """Структура видео"""
    was_viewed: bool | None = _field(default=None, name="wasViewed")
    """Просмотрен ли отзыв"""


class FeedbackResponseDataAnswer(WBModel):
    """Структура ответа"""

    editable: bool | None = _field(default=None)
    """Можно ли отредактировать ответ:   - `false` — нет   - `true` — да"""
    state: str | None = _field(default=None)
    """Статус:   - `none` — новый   - `wbRu`— отображается на сайте   - `reviewRequired` — ответ
    проходит проверку   - `rejected` — ответ отклонён
    """
    text: str | None = _field(default=None)
    """Текст ответа"""


class FeedbackResponseDataPhotoLinksItem(WBModel):
    full_size: Any | None = _field(default=None, name="fullSize")
    """Адрес фотографии полного размера"""
    mini_size: Any | None = _field(default=None, name="miniSize")
    """Адрес фотографии маленького размера"""


class FeedbackResponseDataProductDetails(WBModel):
    """Item information"""

    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд товара"""
    imt_id: int | None = _field(default=None, name="imtId")
    """ID для объединённых карточек товаров"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    product_name: str | None = _field(default=None, name="productName")
    """Название товара"""
    size: str | None = _field(default=None)
    """Размер товара (`techSize` в КТ)"""
    supplier_article: str | None = _field(default=None, name="supplierArticle")
    """Артикул продавца"""
    supplier_name: str | None = _field(default=None, name="supplierName")
    """Имя продавца"""


class FeedbackResponseDataVideo(WBModel):
    """Структура видео"""

    duration_sec: int | None = _field(default=None, name="durationSec")
    """Общая продолжительность видео"""
    link: str | None = _field(default=None)
    """Ссылка на файл плейлиста видео (доступно по протоколу hls)"""
    preview_image: str | None = _field(default=None, name="previewImage")
    """Ссылка на обложку видео"""


class FeedbacksAnswerCreateBody(WBModel):
    id: str | None = _field(default=None)
    """ID отзыва"""
    text: str | None = _field(default=None)
    """Текст ответа"""


class FeedbacksAnswerUpdateBody(WBModel):
    id: str | None = _field(default=None)
    """ID отзыва"""
    text: str | None = _field(default=None)
    """Текст ответа"""


class FeedbacksArchiveResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: FeedbacksArchiveResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class FeedbacksArchiveResponseData(WBModel):
    feedbacks: list[FeedbacksArchiveResponseDataFeedbacksItem] | None = _field(default=None)


class FeedbacksArchiveResponseDataFeedbacksItem(WBModel):
    answer: Any | None = _field(default=None)
    """Структура ответа"""
    bables: Any | None = _field(default=None)
    """Список тегов покупателя"""
    child_feedback_id: Any | None = _field(default=None, name="childFeedbackId")
    """ID дополненного отзыва (`null`, если этот отзыв дополненный)"""
    color: Any | None = _field(default=None)
    """Цвет товара"""
    cons: Any | None = _field(default=None)
    """Недостатки товара"""
    created_date: Any | None = _field(default=None, name="createdDate")
    """Дата и время создания отзыва"""
    id: Any | None = _field(default=None)
    """ID отзыва"""
    is_able_return_product_orders: Any | None = _field(default=None, name="isAbleReturnProductOrders")
    """Опция возврата товара:  - `true` — доступна  - `false` — недоступна"""
    is_able_supplier_feedback_valuation: Any | None = _field(
        default=None, name="isAbleSupplierFeedbackValuation"
    )
    """Доступна ли продавцу возможность оставить жалобу на отзыв (`true` — доступна, `false` — не
    доступна)
    """
    is_able_supplier_product_valuation: Any | None = _field(
        default=None, name="isAbleSupplierProductValuation"
    )
    """Доступна ли продавцу возможность сообщить о проблеме с товаром:   - `true` — да   - `false`
    — нет
    """
    last_order_created_at: Any | None = _field(default=None, name="lastOrderCreatedAt")
    """Дата покупки"""
    last_order_shk_id: Any | None = _field(default=None, name="lastOrderShkId")
    """Штрихкод единицы товара"""
    matching_size: Any | None = _field(default=None, name="matchingSize")
    """Соответствие заявленного размера реальному. Возможные значения: - ` ` — для безразмерных
    товаров - `ок` — соответствует размеру - `smaller` — маломерит …
    """
    order_status: Any | None = _field(default=None, name="orderStatus")
    """Статус заказа. Возможные значения: - `buyout` — выкуплен - `rejected` — отказались -
    `returned` — возврат - `notSpecified` — статус не присвоен
    """
    parent_feedback_id: Any | None = _field(default=None, name="parentFeedbackId")
    """ID начального отзыва (`null`, если этот отзыв начальный)"""
    photo_links: Any | None = _field(default=None, name="photoLinks")
    """Массив структур фотографий"""
    product_details: Any | None = _field(default=None, name="productDetails")
    """Информация о товаре"""
    product_valuation: Any | None = _field(default=None, name="productValuation")
    """Оценка товара"""
    pros: Any | None = _field(default=None)
    """Достоинства товара"""
    return_product_orders_date: Any | None = _field(default=None, name="returnProductOrdersDate")
    """Дата и время, когда на запрос возврата был получен ответ со статус-кодом 200."""
    state: Any | None = _field(default=None)
    """Статус отзыва:   - `none` - не обработан (новый)   - `wbRu` - обработан"""
    subject_id: Any | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: Any | None = _field(default=None, name="subjectName")
    """Название предмета"""
    supplier_feedback_valuation: Any | None = _field(default=None, name="supplierFeedbackValuation")
    """Ключ причины жалобы на отзыв"""
    supplier_product_valuation: Any | None = _field(default=None, name="supplierProductValuation")
    """Ключ проблемы с товаром"""
    text: Any | None = _field(default=None)
    """Текст отзыва"""
    user_name: Any | None = _field(default=None, name="userName")
    """Имя автора отзыва"""
    video: Any | None = _field(default=None)
    """Структура видео"""
    was_viewed: Any | None = _field(default=None, name="wasViewed")
    """Просмотрен ли отзыв"""


class FeedbacksCountResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: int | None = _field(default=None)
    """Количество отзывов"""
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class FeedbacksCountUnansweredResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: FeedbacksCountUnansweredResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class FeedbacksCountUnansweredResponseData(WBModel):
    count_unanswered: int | None = _field(default=None, name="countUnanswered")
    """Количество необработанных отзывов"""
    count_unanswered_today: int | None = _field(default=None, name="countUnansweredToday")
    """Количество необработанных отзывов за сегодня"""


class FeedbacksOrderReturnCreateBody(WBModel):
    feedback_id: str | None = _field(default=None, name="feedbackId")
    """ID отзыва"""


class FeedbacksOrderReturnCreateResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: dict[str, Any] | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class FeedbacksResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: FeedbacksResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class FeedbacksResponseData(WBModel):
    count_archive: int | None = _field(default=None, name="countArchive")
    """Количество обработанных отзывов"""
    count_unanswered: int | None = _field(default=None, name="countUnanswered")
    """Количество необработанных отзывов"""
    feedbacks: list[FeedbacksResponseDataFeedbacksItem] | None = _field(default=None)


class FeedbacksResponseDataFeedbacksItem(WBModel):
    answer: Any | None = _field(default=None)
    """Структура ответа"""
    bables: Any | None = _field(default=None)
    """Список тегов покупателя"""
    child_feedback_id: Any | None = _field(default=None, name="childFeedbackId")
    """ID дополненного отзыва (`null`, если этот отзыв дополненный)"""
    color: Any | None = _field(default=None)
    """Цвет товара"""
    cons: Any | None = _field(default=None)
    """Недостатки товара"""
    created_date: Any | None = _field(default=None, name="createdDate")
    """Дата и время создания отзыва"""
    id: Any | None = _field(default=None)
    """ID отзыва"""
    is_able_return_product_orders: Any | None = _field(default=None, name="isAbleReturnProductOrders")
    """Опция возврата товара:  - `true` — доступна  - `false` — недоступна"""
    is_able_supplier_feedback_valuation: Any | None = _field(
        default=None, name="isAbleSupplierFeedbackValuation"
    )
    """Доступна ли продавцу возможность оставить жалобу на отзыв (`true` — доступна, `false` — не
    доступна)
    """
    is_able_supplier_product_valuation: Any | None = _field(
        default=None, name="isAbleSupplierProductValuation"
    )
    """Доступна ли продавцу возможность сообщить о проблеме с товаром:   - `true` — да   - `false`
    — нет
    """
    last_order_created_at: Any | None = _field(default=None, name="lastOrderCreatedAt")
    """Дата покупки"""
    last_order_shk_id: Any | None = _field(default=None, name="lastOrderShkId")
    """Штрихкод единицы товара"""
    matching_size: Any | None = _field(default=None, name="matchingSize")
    """Соответствие заявленного размера реальному. Возможные значения: - ` ` — для безразмерных
    товаров - `ок` — соответствует размеру - `smaller` — маломерит …
    """
    order_status: Any | None = _field(default=None, name="orderStatus")
    """Статус заказа. Возможные значения: - `buyout` — выкуплен - `rejected` — отказались -
    `returned` — возврат - `notSpecified` — статус не присвоен
    """
    parent_feedback_id: Any | None = _field(default=None, name="parentFeedbackId")
    """ID начального отзыва (`null`, если этот отзыв начальный)"""
    photo_links: Any | None = _field(default=None, name="photoLinks")
    """Массив структур фотографий"""
    product_details: Any | None = _field(default=None, name="productDetails")
    """Информация о товаре"""
    product_valuation: Any | None = _field(default=None, name="productValuation")
    """Оценка товара"""
    pros: Any | None = _field(default=None)
    """Достоинства товара"""
    return_product_orders_date: Any | None = _field(default=None, name="returnProductOrdersDate")
    """Дата и время, когда на запрос возврата был получен ответ со статус-кодом 200."""
    state: Any | None = _field(default=None)
    """Статус отзыва:   - `none` - не обработан (новый)   - `wbRu` - обработан"""
    subject_id: Any | None = _field(default=None, name="subjectId")
    """ID предмета"""
    subject_name: Any | None = _field(default=None, name="subjectName")
    """Название предмета"""
    supplier_feedback_valuation: Any | None = _field(default=None, name="supplierFeedbackValuation")
    """Ключ причины жалобы на отзыв"""
    supplier_product_valuation: Any | None = _field(default=None, name="supplierProductValuation")
    """Ключ проблемы с товаром"""
    text: Any | None = _field(default=None)
    """Текст отзыва"""
    user_name: Any | None = _field(default=None, name="userName")
    """Имя автора отзыва"""
    video: Any | None = _field(default=None)
    """Структура видео"""
    was_viewed: Any | None = _field(default=None, name="wasViewed")
    """Просмотрен ли отзыв"""


class LastMessage(WBModel):
    add_timestamp: Any | None = _field(default=None, name="addTimestamp")
    """Время сообщения"""
    text: Any | None = _field(default=None)
    """Текст сообщения"""


class Listing(WBModel):
    """Информация о заказе"""

    nm_id: Any | None = _field(default=None, name="nmID")
    """Артикул WB"""
    price: Any | None = _field(default=None)
    """Фактическая цена с учетом всех скидок. Взимается с покупателя"""
    price_currency: Any | None = _field(default=None, name="priceCurrency")
    """Валюта"""
    rid: Any | None = _field(default=None)
    """Уникальный ID заказа. Примечание: `rid` — это `srid` в ответах методов:   - Заявки
    покупателей на возврат   - Лента заказов   - Заказы   - Продажи …
    """
    size: Any | None = _field(default=None)
    """Размер товара, соответствует `wbSize` в карточке товара"""


class MessageResponse(WBModel):
    errors: list[str] | None = _field(default=None)
    """Ошибки загрузки файлов, если есть"""
    result: MessageResponseResult | None = _field(default=None)


class MessageResponseResult(WBModel):
    add_time: int | None = _field(default=None, name="addTime")
    """Дата и время создания чата"""
    chat_id: str | None = _field(default=None, name="chatID")
    """ID чата"""
    sign: str | None = _field(default=None)
    """Подпись чата"""


class NewFeedbacksQuestionsResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: NewFeedbacksQuestionsResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class NewFeedbacksQuestionsResponseData(WBModel):
    has_new_feedbacks: bool | None = _field(default=None, name="hasNewFeedbacks")
    """Есть ли непросмотренные отзывы:  - `true` — да  - `false` — нет"""
    has_new_questions: bool | None = _field(default=None, name="hasNewQuestions")
    """Есть ли непросмотренные вопросы:    - `true` — да    - `false` — нет"""


class OpenapiPinReviewItem(WBModel):
    feedback_id: str | None = _field(default=None, name="feedbackId")
    """ID отзыва"""
    pin_method: str | None = _field(default=None, name="pinMethod")
    """Метод закрепления:   - `subscription` — подписка Джем   - `tariff` — тарифная опция"""
    pin_on: str | None = _field(default=None, name="pinOn")
    """Место закрепления отзыва:   - `nm` — карточка товара   - `imt` — группа объединённых
    карточек товаров
    """


class QuestionResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: QuestionResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class QuestionResponseData(WBModel):
    answer: QuestionResponseDataAnswer | None = _field(default=None)
    """Ответ"""
    created_date: str | None = _field(default=None, name="createdDate")
    """Дата и время создания вопроса"""
    id: str | None = _field(default=None)
    """ID вопроса"""
    is_warned: bool | None = _field(default=None, name="isWarned")
    """Признак подозрительного вопроса. Если `true`, то вопрос опубликован, но на портале продавцов
    вы увидите баннер **Сообщение подозрительное**
    """
    product_details: QuestionResponseDataProductDetails | None = _field(default=None, name="productDetails")
    """Item information"""
    state: str | None = _field(default=None)
    """Статус вопроса:   - `none` - вопрос отклонён продавцом (такой вопрос не отображается на
    портале покупателей) …
    """
    text: str | None = _field(default=None)
    """Текст вопроса"""
    was_viewed: bool | None = _field(default=None, name="wasViewed")
    """Просмотрен ли вопрос"""


class QuestionResponseDataAnswer(WBModel):
    """Ответ"""

    create_date: str | None = _field(default=None, name="createDate")
    """Дата и время создания ответа"""
    editable: bool | None = _field(default=None)
    """Можно ли отредактировать ответ (`false` - нельзя, `true` - можно)"""
    text: str | None = _field(default=None)
    """Текст ответа"""


class QuestionResponseDataProductDetails(WBModel):
    """Item information"""

    brand_name: str | None = _field(default=None, name="brandName")
    """Название бренда"""
    imt_id: int | None = _field(default=None, name="imtId")
    """ID для объединённых карточек товаров"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    product_name: str | None = _field(default=None, name="productName")
    """Название товара"""
    supplier_article: str | None = _field(default=None, name="supplierArticle")
    """Артикул продавца"""
    supplier_name: str | None = _field(default=None, name="supplierName")
    """Имя продавца"""


class QuestionsCountResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: int | None = _field(default=None)
    """Количество вопросов"""
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class QuestionsCountUnansweredResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: QuestionsCountUnansweredResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class QuestionsCountUnansweredResponseData(WBModel):
    count_unanswered: int | None = _field(default=None, name="countUnanswered")
    """Количество неотвеченных вопросов"""
    count_unanswered_today: int | None = _field(default=None, name="countUnansweredToday")
    """Количество неотвеченных вопросов за сегодня"""


class QuestionsResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: QuestionsResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class QuestionsResponseData(WBModel):
    count_archive: int | None = _field(default=None, name="countArchive")
    """Количество отвеченных вопросов"""
    count_unanswered: int | None = _field(default=None, name="countUnanswered")
    """Количество неотвеченных вопросов"""
    questions: list[QuestionsResponseDataQuestionsItem] | None = _field(default=None)
    """Вопросы"""


class QuestionsResponseDataQuestionsItem(WBModel):
    answer: Any | None = _field(default=None)
    """Структура ответа"""
    created_date: Any | None = _field(default=None, name="createdDate")
    """Дата и время создания вопроса"""
    id: Any | None = _field(default=None)
    """id вопроса"""
    is_warned: Any | None = _field(default=None, name="isWarned")
    """Признак подозрительного вопроса. Если `true`, то вопрос опубликован, но на портале продавцов
    вы увидите баннер **Сообщение подозрительное**
    """
    product_details: Any | None = _field(default=None, name="productDetails")
    """Информация о товаре"""
    state: Any | None = _field(default=None)
    """Статус вопроса:   - `none` — вопрос отклонён продавцом (такой вопрос не отображается на
    портале покупателей) …
    """
    text: Any | None = _field(default=None)
    """Текст вопроса"""
    was_viewed: Any | None = _field(default=None, name="wasViewed")
    """Просмотрен ли вопрос"""


class QuestionsUpdateBody(WBModel):
    id: str | None = _field(default=None)
    """Id вопроса"""
    was_viewed: bool | None = _field(default=None, name="wasViewed")
    """Просмотрен ли вопрос"""


class QuestionsUpdateResponse(WBModel):
    additional_errors: list[str] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: dict[str, Any] | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Есть ли ошибка"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class RespondSuccessResponse(WBModel):
    data: dict[str, Any] | None = _field(default=None)
