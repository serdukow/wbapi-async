# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from msgspec import field as _field

from ..client.model import WBModel


class ApiBatchErrorResponse(WBModel):
    code: int | None = _field(default=None)
    """Код ошибки:   - `404`   - `409`"""
    detail: str | None = _field(default=None)
    """- `NotFound` — сборочное задание не найдено - `StatusMismatch` — операция невозможна для
    этого статуса сборочного задания …
    """
    meta_details: list[ApiBatchErrorResponseMetaDetailsItem] | None = _field(default=None, name="metaDetails")
    """Детали ошибки валидации идентификаторов маркировки"""


class ApiBatchErrorResponseMetaDetailsItem(WBModel):
    decision: str | None = _field(default=None)
    """Статус проверки: - `sgtin`   - `sgtinInvalidFormat` — Неверный формат маркировки   -
    `sgtinNotFound` — Маркировка не найдена в Честном знаке …
    """
    key: str | None = _field(default=None)
    """Идентификатор маркировки"""
    value: str | None = _field(default=None)
    """Значение идентификатора маркировки"""


class ApiOrdersMetaDetailsResponse(WBModel):
    orders: list[ApiOrdersMetaDetailsResponseOrdersItem] | None = _field(default=None)
    """Идентификаторы маркировки сборочных заданий и статусы их валидации"""
    request_id: str | None = _field(default=None, name="requestId")
    """Уникальный ID запроса"""


class ApiOrdersMetaDetailsResponseOrdersItem(WBModel):
    errors: list[ApiOrdersMetaDetailsResponseOrdersItemErrorsItem] | None = _field(default=None)
    """Информация об ошибке"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки"""
    meta_details: list[ApiOrdersMetaDetailsResponseOrdersItemMetaDetailsItem] | None = _field(
        default=None, name="metaDetails"
    )
    """Идентификаторы маркировки и статусы их валидации"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""


class ApiOrdersMetaDetailsResponseOrdersItemErrorsItem(WBModel):
    code: int | None = _field(default=None)
    """Код ошибки"""
    detail: str | None = _field(default=None)
    """Дополнительная информация об ошибке"""


class ApiOrdersMetaDetailsResponseOrdersItemMetaDetailsItem(WBModel):
    decision: str | None = _field(default=None)
    """Статус проверки: - `imei`   - `pending` — Маркировка на проверке   - `optional` — Маркировка
    не обязательна   - `filled` — Валидация пройдена …
    """
    key: str | None = _field(default=None)
    """Идентификатор маркировки"""
    value: str | None = _field(default=None)
    """Значение идентификатора маркировки"""


class ApiOrdersMetaDleteRequestV2(WBModel):
    key: str | None = _field(default=None)
    """Название идентификатора маркировки для удаления. Передаётся только одно значение"""
    orders_ids: list[int] | None = _field(default=None, name="ordersIds")
    """Список ID сборочных заданий"""


class ApiOrdersRequestV2(WBModel):
    orders_ids: list[int] | None = _field(default=None, name="ordersIds")
    """Список ID сборочных заданий"""


class ApiOrdersSGTINsSetRequest(WBModel):
    orders: list[ApiSGTINs] | None = _field(default=None)
    """Не более 1000 элементов"""


class ApiSGTINs(WBModel):
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    sgtins: list[str] | None = _field(default=None)
    """Массив кодов маркировки. Допускается от 16 до 135 символов для кода одной маркировки"""


class ApiStatusSetResponse(WBModel):
    errors: list[ApiBatchErrorResponse] | None = _field(default=None)
    """Детали ошибки"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания с успешно обновлёнными данными"""


class ApiStatusSetResponses(WBModel):
    request_id: str | None = _field(default=None, name="requestId")
    """Уникальный ID запроса, содержащего ошибки."""
    results: list[ApiStatusSetResponse] | None = _field(default=None)


class ClientInfo(WBModel):
    additional_phone_codes: list[int] | None = _field(default=None, name="additionalPhoneCodes")
    """Дополнительные добавочные коды. Используйте, если не получилось дозвониться по добавочному
    коду из `phoneCode`. Пустое значение указывает, коды ещё не назначены
    """
    additional_phones: list[str] | None = _field(default=None, name="additionalPhones")
    """Дополнительные номера телефонов для связи с покупателем. Используйте, чтобы позвонить
    покупателю, если недоступен основной номер из `phone`. …
    """
    first_name: str | None = _field(default=None, name="firstName")
    """Имя покупателя"""
    full_name: str | None = _field(default=None, name="fullName")
    """Полное имя покупателя, используется для оформления документов"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    phone: str | None = _field(default=None)
    """Номер телефона для связи с покупателем: …"""
    phone_code: int | None = _field(default=None, name="phoneCode")
    """Добавочный код. Используйте, чтобы связаться с покупателем по номеру из `phone`. Если код не
    указан, вы можете связаться с покупателем без кода
    """
    replacement_phone: str | None = _field(default=None, name="replacementPhone")
    """Подменный номер для связи с покупателем. Пустое значение `""` указывает, что номер ещё не
    назначен
    """


class ClientInfoResp(WBModel):
    orders: list[ClientInfo] | None = _field(default=None)
    """Информация о покупателях"""


class DeleteOrdersMetaResponse(WBModel):
    request_id: str | None = _field(default=None, name="requestId")
    """Уникальный ID запроса. Отображается для ответов с ошибками"""
    results: list[DeleteOrdersMetaResponseResultsItem] | None = _field(default=None)


class DeleteOrdersMetaResponseResultsItem(WBModel):
    errors: list[DeleteOrdersMetaResponseResultsItemErrorsItem] | None = _field(default=None)
    """Детали ошибки"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания с успешно обновлёнными данными"""


class DeleteOrdersMetaResponseResultsItemErrorsItem(WBModel):
    code: int | None = _field(default=None)
    """Код ошибки:   - `404`   - `409`"""
    detail: str | None = _field(default=None)
    """- `NotFound` — сборочное задание не найдено - `StatusMismatch` — операция невозможна для
    этого статуса сборочного задания - `ImeiIsNotFilled` — не заполнен IMEI
    """


class DeliveryDatesInfoResp(WBModel):
    orders: list[DeliveryDatesInfoRespOrdersItem] | None = _field(default=None)


class DeliveryDatesInfoRespOrdersItem(WBModel):
    d_date: str | None = _field(default=None, name="dDate")
    """Актуальная дата доставки"""
    d_date_old: str | None = _field(default=None, name="dDateOld")
    """Прежняя дата доставки. Доступна первые сутки после изменения"""
    d_time_from: str | None = _field(default=None, name="dTimeFrom")
    """Актуальное время доставки "с"""
    d_time_from_old: str | None = _field(default=None, name="dTimeFromOld")
    """Прежнее время доставки "с". Доступно первые сутки после изменения"""
    d_time_to: str | None = _field(default=None, name="dTimeTo")
    """Актуальное время доставки "по"""
    d_time_to_old: str | None = _field(default=None, name="dTimeToOld")
    """Прежнее время доставки "по". Доступно первые сутки после изменения"""
    id: int | None = _field(default=None)
    """ID сборочного задания"""


class DeliveryDatesRequest(WBModel):
    orders: list[int] | None = _field(default=None)
    """Список ID сборочных заданий"""


class GetDbwOrdersResponse(WBModel):
    next: int | None = _field(default=None)
    """Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения
    следующего пакета данных
    """
    orders: list[Order] | None = _field(default=None)


class GetOrdersNewResponse(WBModel):
    orders: list[OrderNewDBW] | None = _field(default=None)
    """Список новых сборочных заданий"""


class GetOrdersStatusBody(WBModel):
    orders: list[int] | None = _field(default=None)
    """Список ID сборочных заданий"""


class GetOrdersStatusResponse(WBModel):
    orders: list[GetOrdersStatusResponseOrdersItem] | None = _field(default=None)


class GetOrdersStatusResponseOrdersItem(WBModel):
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    supplier_status: str | None = _field(default=None, name="supplierStatus")
    """Статус сборочного задания, установленный продавцом"""
    wb_status: str | None = _field(default=None, name="wbStatus")
    """Статус сборочного задания в системе Wildberries"""


class GetOrdersStickersBody(WBModel):
    orders: list[int] | None = _field(default=None)
    """Список ID сборочных заданий"""


class GetOrdersStickersResponse(WBModel):
    stickers: list[GetOrdersStickersResponseStickersItem] | None = _field(default=None)


class GetOrdersStickersResponseStickersItem(WBModel):
    barcode: str | None = _field(default=None)
    """Закодированное значение стикера"""
    file: str | None = _field(default=None)
    """Полное представление стикера в заданном формате (кодировка base64)"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    part_a: str | None = _field(default=None, name="partA")
    """Первая часть ID стикера для печати подписи"""
    part_b: str | None = _field(default=None, name="partB")
    """Вторая часть ID стикера для печати подписи"""


class Order(WBModel):
    address: OrderAddress | None = _field(default=None)
    """Адрес покупателя для доставки"""
    article: str | None = _field(default=None)
    """Артикул продавца"""
    cargo_type: int | None = _field(default=None, name="cargoType")
    """Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   -
    `3` — крупногабаритный товар (КГТ+)
    """
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара в системе WB"""
    color_code: str | None = _field(default=None, name="colorCode")
    """Код цвета (только для колеруемых товаров)"""
    comment: str | None = _field(default=None)
    """Комментарий покупателя"""
    converted_currency_code: int | None = _field(default=None, name="convertedCurrencyCode")
    """Код валюты страны продавца"""
    converted_price: int | None = _field(default=None, name="convertedPrice")
    """Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная
    на 100. Предоставляется в информационных целях
    """
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата создания сборочного задания"""
    currency_code: int | None = _field(default=None, name="currencyCode")
    """Код валюты продажи"""
    group_id: str | None = _field(default=None, name="groupId")
    """ID группы сборочных заданий.  Объединяет сборочные задания, поступившие на один склад
    (`warehouseId`) в рамках одной транзакции покупателя (`orderUid`)
    """
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    is_zero_order: bool | None = _field(default=None, name="isZeroOrder")
    """Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым
    остатком …
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    options: OrderOptions | None = _field(default=None)
    """Опции заказа"""
    order_uid: str | None = _field(default=None, name="orderUid")
    """ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине
    покупателя будут иметь одинаковый `orderUid`
    """
    price: int | None = _field(default=None)
    """Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100.
    Код валюты продажи указан в поле `currencyCode`. Предоставляется в и …
    """
    rid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание: `rid` — это `srid` в ответах методов:   - Заявки
    покупателей на возврат   - Лента заказов   - Заказы   - Продажи …
    """
    skus: list[str] | None = _field(default=None)
    """Массив баркодов товара"""
    warehouse_id: int | None = _field(default=None, name="warehouseId")
    """ID склада продавца, на который поступило сборочное задание"""


class OrderAddress(WBModel):
    """Адрес покупателя для доставки"""

    full_address: str | None = _field(default=None, name="fullAddress")
    """Адрес доставки"""
    latitude: float | None = _field(default=None)
    """Широта"""
    longitude: float | None = _field(default=None)
    """Долгота"""


class OrderCourierInfo(WBModel):
    courier_info: OrderCourierInfoCourierInfo | None = _field(default=None, name="courierInfo")
    """Информация о курьере"""
    order_id: int | None = _field(default=None, name="orderID")
    """ID сборочного задания"""


class OrderCourierInfoCourierInfo(WBModel):
    contacts: OrderCourierInfoCourierInfoContacts | None = _field(default=None)
    """Контактные данные курьера"""
    must_be_assigned: bool | None = _field(default=None, name="mustBeAssigned")
    """Должен ли быть назначен курьер к текущему моменту:   - `false` — нет   - `true` — да …"""
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время обновления информации о курьере.  Если `null`, информация не обновлялась"""


class OrderCourierInfoCourierInfoContacts(WBModel):
    car_number: str | None = _field(default=None, name="carNumber")
    """Номер автомобиля"""
    full_name: str | None = _field(default=None, name="fullName")
    """ФИО курьера"""
    p_time_from: str | None = _field(default=None, name="pTimeFrom")
    """Дата и время, с которого прибудет курьер"""
    p_time_to: str | None = _field(default=None, name="pTimeTo")
    """Дата и время, до которого прибудет курьер"""
    phone: str | None = _field(default=None)
    """Номер телефона"""


class OrderCourierInfoResp(WBModel):
    orders: list[OrderCourierInfo] | None = _field(default=None)


class OrderNewDBW(WBModel):
    address: OrderNewDBWAddress | None = _field(default=None)
    """Адрес покупателя для доставки"""
    article: str | None = _field(default=None)
    """Артикул продавца"""
    cargo_type: int | None = _field(default=None, name="cargoType")
    """Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   -
    `3` — крупногабаритный товар (КГТ+)
    """
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара в системе WB"""
    color_code: str | None = _field(default=None, name="colorCode")
    """Код цвета (только для колеруемых товаров)"""
    comment: str | None = _field(default=None)
    """Комментарий покупателя"""
    converted_currency_code: int | None = _field(default=None, name="convertedCurrencyCode")
    """Код валюты страны продавца"""
    converted_price: int | None = _field(default=None, name="convertedPrice")
    """Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная
    на 100. Предоставляется в информационных целях
    """
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата создания сборочного задания"""
    currency_code: int | None = _field(default=None, name="currencyCode")
    """Код валюты продажи"""
    group_id: str | None = _field(default=None, name="groupId")
    """ID группы сборочных заданий.  Объединяет сборочные задания, поступившие на один склад
    (`warehouseId`) в рамках одной транзакции покупателя (`orderUid`)
    """
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    is_zero_order: bool | None = _field(default=None, name="isZeroOrder")
    """Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым
    остатком …
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    options: OrderNewDBWOptions | None = _field(default=None)
    """Опции заказа"""
    order_uid: str | None = _field(default=None, name="orderUid")
    """ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине
    покупателя будут иметь одинаковый `orderUid`
    """
    price: int | None = _field(default=None)
    """Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100.
    Код валюты продажи указан в поле `currencyCode`. Предоставляется в и …
    """
    required_meta: list[str] | None = _field(default=None, name="requiredMeta")
    """Список идентификаторов маркировки, доступных для сборочного задания. Указывать IMEI
    обязательно для предмета `Смартфоны`, `"subjectId":515`
    """
    rid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание: `rid` — это `srid` в ответах методов:   - Заявки
    покупателей на возврат   - Лента заказов   - Заказы   - Продажи …
    """
    sale_price: int | None = _field(default=None, name="salePrice")
    """Цена в валюте продажи с учетом скидки продавца, без учета скидки WB Клуба, умноженная на
    100. Предоставляется в информационных целях
    """
    skus: list[str] | None = _field(default=None)
    """Массив баркодов товара"""
    warehouse_id: int | None = _field(default=None, name="warehouseId")
    """ID склада продавца, на который поступило сборочное задание"""


class OrderNewDBWAddress(WBModel):
    """Адрес покупателя для доставки"""

    full_address: str | None = _field(default=None, name="fullAddress")
    """Адрес доставки"""
    latitude: float | None = _field(default=None)
    """Широта"""
    longitude: float | None = _field(default=None)
    """Долгота"""


class OrderNewDBWOptions(WBModel):
    """Опции заказа"""

    is_b2b: bool | None = _field(default=None, name="isB2b")
    """Признак B2B-продажи:   - `false` — не B2B-продажа   - `true` — B2B-продажа"""


class OrderOptions(WBModel):
    """Опции заказа"""

    is_b2b: bool | None = _field(default=None, name="isB2b")
    """Признак B2B-продажи:   - `false` — не B2B-продажа   - `true` — B2B-продажа"""


class OrdersRequestAPI(WBModel):
    orders: list[int] | None = _field(default=None)
    """Список ID сборочных заданий"""


class SetOrdersMetaGtinBody(WBModel):
    gtin: str | None = _field(default=None)
    """GTIN"""


class SetOrdersMetaImeiBody(WBModel):
    imei: str | None = _field(default=None)
    """IMEI"""


class SetOrdersMetaUinBody(WBModel):
    uin: str | None = _field(default=None)
    """УИН"""
