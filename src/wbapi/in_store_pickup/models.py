from __future__ import annotations

from typing import Any

from msgspec import field as _field

from ..client.model import WBModel


class ApiBatchCustomsDeclarationErrorResponse(WBModel):
    code: Any | None = _field(default=None)
    """Код ошибки:   - `404`   - `409`   - `400`"""
    detail: Any | None = _field(default=None)
    """- `NotFound` — сборочное задание не найдено - `StatusMismatch` — операция невозможна для
    этого статуса сборочного задания …
    """


class ApiBatchErrorFinalPriceResponse(WBModel):
    code: Any | None = _field(default=None)
    """Код ошибки:   - `404` — `NotFound`   - `400` — `StatusMismatch`   - `422` —
    `PriceNotCalculated`
    """
    detail: Any | None = _field(default=None)
    """- `NotFound` — сборочное задание не найдено (`404`) - `StatusMismatch` — операция невозможна
    для этого статуса сборочного задания (`400`) …
    """


class ApiBatchErrorResponse(WBModel):
    code: Any | None = _field(default=None)
    """Код ошибки:   - `404`   - `409`   - `400`"""
    detail: Any | None = _field(default=None)
    """- `NotFound` — сборочное задание не найдено - `StatusMismatch` — операция невозможна для
    этого статуса сборочного задания …
    """


class ApiCheckIdentityRequest(WBModel):
    order_code: str | None = _field(default=None, name="orderCode")
    """Уникальный ID заказа покупателя"""
    passcode: str | None = _field(default=None)
    """Код подтверждения"""


class ApiCheckedIdentity(WBModel):
    ok: bool | None = _field(default=None)
    """Принадлежит ли заказ покупателю:   - `true` — принадлежит …"""


class ApiCustomsDeclarationSetResponse(WBModel):
    request_id: Any | None = _field(default=None, name="requestId")
    """Уникальный ID запроса"""
    results: list[ApiStatusSetCustomsDeclarationResponse] | None = _field(default=None)


class ApiGTIN(WBModel):
    gtin: str | None = _field(default=None)
    """GTIN"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""


class ApiIMEI(WBModel):
    imei: str | None = _field(default=None)
    """IMEI"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""


class ApiMetaDetailsResponse(WBModel):
    request_id: Any | None = _field(default=None, name="requestId")
    """Уникальный ID запроса"""
    results: Any | None = _field(default=None)


class ApiMetaErrorResponse(WBModel):
    code: Any | None = _field(default=None)
    """Код ошибки"""
    detail: Any | None = _field(default=None)
    """- `NotFound` — сборочное задание не найдено - `IncorrectRequestBody` — неправильный запрос -
    `IncorrectRequest` — передан некорректный параметр
    """


class ApiMetaSetResponse(WBModel):
    errors: list[ApiMetaErrorResponse] | None = _field(default=None)
    """Детали ошибки"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""


class ApiMetaSetResponses(WBModel):
    request_id: Any | None = _field(default=None, name="requestId")
    """Уникальный ID запроса"""
    results: list[ApiMetaSetResponse] | None = _field(default=None)


class ApiNewOrder(WBModel):
    article: str | None = _field(default=None)
    """Артикул продавца"""
    cargo_type: int | None = _field(default=None, name="cargoType")
    """Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   -
    `3` — крупногабаритный товар (КГТ+)
    """
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара в системе WB"""
    converted_currency_code: int | None = _field(default=None, name="convertedCurrencyCode")
    """Код валюты страны продавца"""
    converted_final_price: int | None = _field(default=None, name="convertedFinalPrice")
    """Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок, умноженная на 100.
    Предоставляется в информационных целях. …
    """
    converted_price: int | None = _field(default=None, name="convertedPrice")
    """Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная
    на 100. Код валюты продажи указан в поле `currencyCode`. Предоставля …
    """
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата и время создания сборочного задания"""
    currency_code: int | None = _field(default=None, name="currencyCode")
    """Код валюты продажи"""
    ddate: str | None = _field(default=None)
    """Планируемая дата доставки"""
    final_price: int | None = _field(default=None, name="finalPrice")
    """Сумма к оплате покупателем в валюте продажи с учётом всех скидок, умноженная на 100.  Код
    валюты продажи указан в поле `currencyCode`. …
    """
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    is_zero_order: bool | None = _field(default=None, name="isZeroOrder")
    """Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым
    остатком …
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    options: ApiNewOrderOptions | None = _field(default=None)
    """Опции заказа"""
    order_code: str | None = _field(default=None, name="orderCode")
    """Уникальный ID заказа покупателя"""
    pay_mode: str | None = _field(default=None, name="payMode")
    """Режим оплаты:   - `prepaid` — предоплатный   - `postpaid` — постоплатный   - `unknown` —
    неизвестный
    """
    price: int | None = _field(default=None)
    """Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100.
    …
    """
    required_meta: list[str] | None = _field(default=None, name="requiredMeta")
    """Список идентификаторов маркировки, доступных для сборочного задания"""
    rid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание: `rid` — это `srid` в ответах методов:   - Заявки
    покупателей на возврат   - Лента заказов   - Заказы   - Продажи …
    """
    sale_price: int | None = _field(default=None, name="salePrice")
    """Цена продавца в валюте продажи с учётом скидки продавца, без учёта скидки WB Клуба,
    умноженная на 100. Предоставляется в информационных целях
    """
    skus: list[str] | None = _field(default=None)
    """Массив баркодов товара"""
    warehouse_address: str | None = _field(default=None, name="warehouseAddress")
    """Адрес магазина (склада продавца), на который поступило сборочное задание"""
    warehouse_id: int | None = _field(default=None, name="warehouseId")
    """ID склада продавца, на который поступило сборочное задание"""


class ApiNewOrderOptions(WBModel):
    """Опции заказа"""

    is_b2b: Any | None = _field(default=None, name="isB2b")
    """Признак B2B-продажи:   - `false` — не B2B-продажа   - `true` — B2B-продажа"""


class ApiNewOrders(WBModel):
    orders: list[ApiNewOrder] | None = _field(default=None)
    """Список сборочных заданий"""


class ApiOrder(WBModel):
    article: str | None = _field(default=None)
    """Артикул продавца"""
    cargo_type: int | None = _field(default=None, name="cargoType")
    """Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   -
    `3` — крупногабаритный товар (КГТ+)
    """
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара в системе WB"""
    converted_currency_code: int | None = _field(default=None, name="convertedCurrencyCode")
    """Код валюты страны продавца"""
    converted_final_price: int | None = _field(default=None, name="convertedFinalPrice")
    """Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок, умноженная на 100.
    Предоставляется в информационных целях. …
    """
    converted_price: int | None = _field(default=None, name="convertedPrice")
    """Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная
    на 100. Код валюты продажи указан в поле `currencyCode`. Предоставля …
    """
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата и время создания сборочного задания"""
    currency_code: int | None = _field(default=None, name="currencyCode")
    """Код валюты продажи"""
    final_price: int | None = _field(default=None, name="finalPrice")
    """Сумма к оплате покупателем в валюте продажи с учётом всех скидок, умноженная на 100.  Код
    валюты продажи указан в поле `currencyCode`. …
    """
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    is_zero_order: bool | None = _field(default=None, name="isZeroOrder")
    """Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым
    остатком …
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    options: ApiOrderOptions | None = _field(default=None)
    """Опции заказа"""
    order_code: str | None = _field(default=None, name="orderCode")
    """Уникальный ID заказа покупателя"""
    pay_mode: str | None = _field(default=None, name="payMode")
    """Режим оплаты:   - `prepaid` — предоплатный   - `postpaid` — постоплатный   - `unknown` —
    неизвестный
    """
    price: int | None = _field(default=None)
    """Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100.
    …
    """
    rid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание: `rid` — это `srid` в ответах методов:   - Заявки
    покупателей на возврат   - Лента заказов   - Заказы   - Продажи …
    """
    skus: list[str] | None = _field(default=None)
    """Массив баркодов товара"""
    warehouse_address: str | None = _field(default=None, name="warehouseAddress")
    """Адрес магазина (склада продавца), на который поступило сборочное задание"""
    warehouse_id: int | None = _field(default=None, name="warehouseId")
    """ID склада продавца, на который поступило сборочное задание"""


class ApiOrderClientInfo(WBModel):
    first_name: str | None = _field(default=None, name="firstName")
    """Имя покупателя"""
    order_id: int | None = _field(default=None, name="orderID")
    """ID сборочного задания"""
    phone: str | None = _field(default=None)
    """Телефон для связи с покупателем. Чтобы связаться с покупателем наберите этот номер и введите
    добавочный код. Данный номер не является прямым номером покупателя
    """
    phone_code: int | None = _field(default=None, name="phoneCode")
    """Добавочный код"""


class ApiOrderClientInfoResp(WBModel):
    orders: list[ApiOrderClientInfo] | None = _field(default=None)


class ApiOrderFinalPriceResult(WBModel):
    data: ApiOrderFinalPriceResultData | None = _field(default=None)
    """Данные сборочного задания.  Если `"data":{}`, данные формируются. Повторите запрос позднее.
    Максимальное время формирования данных около 3 минут. …
    """
    errors: list[ApiBatchErrorFinalPriceResponse] | None = _field(default=None)
    """Детали ошибки"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""


class ApiOrderFinalPriceResultData(WBModel):
    """Данные сборочного задания."""

    converted_currency_code: Any | None = _field(default=None, name="convertedCurrencyCode")
    """Код валюты страны продавца"""
    converted_original_final_price: Any | None = _field(default=None, name="convertedOriginalFinalPrice")
    """Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок и кэшбека,
    умноженная на 100. Предоставляется в информационных целях
    """
    converted_original_price: Any | None = _field(default=None, name="convertedOriginalPrice")
    """Цена продавца в валюте страны продавца без учёта скидок, умноженная на 100. Предоставляется
    в информационных целях
    """
    currency_code: Any | None = _field(default=None, name="currencyCode")
    """Код валюты продажи"""
    original_final_price: Any | None = _field(default=None, name="originalFinalPrice")
    """Сумма к оплате покупателем в валюте продажи с учетом всех скидок и кэшбека, умноженная на
    100. Код валюты продажи указан в поле `currencyCode`. Предоставляется …
    """
    original_price: Any | None = _field(default=None, name="originalPrice")
    """Цена продавца в валюте продажи без учёта скидок, умноженная на 100. Предоставляется в
    информационных целях
    """


class ApiOrderOptions(WBModel):
    """Опции заказа"""

    is_b2b: Any | None = _field(default=None, name="isB2b")
    """Признак B2B-продажи:   - `false` — не B2B-продажа   - `true` — B2B-продажа"""


class ApiOrderStatusV2(WBModel):
    errors: list[ApiOrdersErrorResponse] | None = _field(default=None)
    """Информация об ошибке"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    supplier_status: str | None = _field(default=None, name="supplierStatus")
    """Статус сборочного задания, установленный продавцом"""
    wb_status: str | None = _field(default=None, name="wbStatus")
    """Статус сборочного задания в системе Wildberries"""


class ApiOrderStatusesV2(WBModel):
    orders: list[ApiOrderStatusV2] | None = _field(default=None)
    """Информация о статусах"""


class ApiOrders(WBModel):
    next: int | None = _field(default=None)
    """Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения
    следующего пакета данных
    """
    orders: list[ApiOrder] | None = _field(default=None)
    """Список сборочных заданий"""


class ApiOrdersErrorResponse(WBModel):
    code: Any | None = _field(default=None)
    """Код ошибки"""
    detail: Any | None = _field(default=None)
    """- `NotFound` — сборочное задание не найдено"""


class ApiOrdersFinalPriceResponse(WBModel):
    request_id: str | None = _field(default=None, name="requestId")
    """Уникальный ID запроса"""
    results: list[ApiOrderFinalPriceResult] | None = _field(default=None)
    """Данные ответа"""


class ApiOrdersGTINSetRequest(WBModel):
    orders: list[ApiGTIN] | None = _field(default=None)


class ApiOrdersIMEISetRequest(WBModel):
    orders: list[ApiIMEI] | None = _field(default=None)


class ApiOrdersMetaDeleteRequest(WBModel):
    key: str | None = _field(default=None)
    """Тип идентификаторов маркировки для удаления. Передаётся только одно значение"""
    orders_ids: list[int] | None = _field(default=None, name="ordersIds")
    """Список ID сборочных заданий"""


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
    code: Any | None = _field(default=None)
    """Код ошибки"""
    detail: Any | None = _field(default=None)
    """Дополнительная информация об ошибке"""


class ApiOrdersMetaDetailsResponseOrdersItemMetaDetailsItem(WBModel):
    decision: Any | None = _field(default=None)
    """Статусы проверки идентификатора маркировки. - `imei`   - `filled` — Маркировка закреплена за
    сборочным заданием, проверка не требуется …
    """
    key: Any | None = _field(default=None)
    """Идентификатор маркировки:   - `imei` — IMEI   - `uin` — УИН   - `gtin` — GTIN   - `sgtin` —
    код маркировки   - `customsDeclaration` — номер ДТ …
    """
    value: Any | None = _field(default=None)
    """Значение идентификатора маркировки"""


class ApiOrdersRequest(WBModel):
    orders: list[int] | None = _field(default=None)
    """Список ID сборочных заданий"""


class ApiOrdersRequestV2(WBModel):
    orders_ids: list[int] | None = _field(default=None, name="ordersIds")
    """Список ID сборочных заданий"""


class ApiOrdersResponse(WBModel):
    errors: list[ApiOrdersErrorResponse] | None = _field(default=None)
    """Детали ошибки"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""


class ApiOrdersResponses(WBModel):
    request_id: Any | None = _field(default=None, name="requestId")
    """Уникальный ID запроса"""
    results: list[ApiOrdersResponse] | None = _field(default=None)


class ApiOrdersSGTINsSetRequest(WBModel):
    orders: list[ApiSGTINs] | None = _field(default=None)


class ApiOrdersUINSetRequest(WBModel):
    orders: list[ApiUIN] | None = _field(default=None)


class ApiSGTINs(WBModel):
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    sgtins: list[str] | None = _field(default=None)
    """Массив кодов маркировки. Допускается от 16 до 135 символов для кода одной маркировки"""


class ApiStatusSetCustomsDeclarationResponse(WBModel):
    errors: list[ApiBatchCustomsDeclarationErrorResponse] | None = _field(default=None)
    """Детали ошибки"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""


class ApiStatusSetResponse(WBModel):
    errors: list[ApiBatchErrorResponse] | None = _field(default=None)
    """Детали ошибки"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""


class ApiStatusSetResponses(WBModel):
    request_id: Any | None = _field(default=None, name="requestId")
    """Уникальный ID запроса"""
    results: list[ApiStatusSetResponse] | None = _field(default=None)


class ApiUIN(WBModel):
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    uin: str | None = _field(default=None)
    """УИН"""


class SetClickCollectOrdersMetaCustomsDeclarationBody(WBModel):
    orders: list[SetClickCollectOrdersMetaCustomsDeclarationBodyOrdersItem] | None = _field(default=None)


class SetClickCollectOrdersMetaCustomsDeclarationBodyOrdersItem(WBModel):
    customs_declaration: str | None = _field(default=None, name="customsDeclaration")
    """Номер ДТ"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    origin_country_code: str | None = _field(default=None, name="originCountryCode")
    """Числовой код страны происхождения товара из Общероссийского классификатора стран мира.
    Необходимо указывать только для сборочных заданий с признаком B2B-продажи …
    """


class SetClickCollectOrdersMetaCustomsDeclarationOrdersItem(WBModel):
    customs_declaration: str | None = _field(default=None, name="customsDeclaration")
    """Номер ДТ"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    origin_country_code: str | None = _field(default=None, name="originCountryCode")
    """Числовой код страны происхождения товара из Общероссийского классификатора стран мира.
    Необходимо указывать только для сборочных заданий с признаком B2B-продажи …
    """
