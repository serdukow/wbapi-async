# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from typing import Any

from msgspec import field as _field

from ..client.model import WBModel


class CreatePassesBody(WBModel):
    car_model: str | None = _field(default=None, name="carModel")
    """Марка машины"""
    car_number: str | None = _field(default=None, name="carNumber")
    """Номер машины"""
    first_name: str | None = _field(default=None, name="firstName")
    """Имя водителя"""
    last_name: str | None = _field(default=None, name="lastName")
    """Фамилия водителя"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада"""


class CreatePassesResponse(WBModel):
    id: int | None = _field(default=None)
    """ID пропуска продавца"""


class CreateSuppliesTrbxBody(WBModel):
    amount: int | None = _field(default=None)
    """Количество грузомест, которые необходимо добавить к поставке"""


class CreateSuppliesTrbxResponse(WBModel):
    trbx_ids: list[str] | None = _field(default=None, name="trbxIds")
    """Список ID грузомест, которые были созданы"""


class CreateSupplyBody(WBModel):
    name: str | None = _field(default=None)
    """Наименование поставки"""


class CreateSupplyResponse(WBModel):
    id: str | None = _field(default=None)
    """ID поставки"""


class CrossborderTurkeyClientInfo(WBModel):
    first_name: str | None = _field(default=None, name="firstName")
    """Имя клиента"""
    full_name: str | None = _field(default=None, name="fullName")
    """Фамилия, Имя, Отчество"""
    last_name: str | None = _field(default=None, name="lastName")
    """Фамилия клиента"""
    middle_name: str | None = _field(default=None, name="middleName")
    """Отчество клиента"""
    order_id: int | None = _field(default=None, name="orderID")
    """Номер заказа"""
    phone: str | None = _field(default=None)
    """Телефон для связи с клиентом"""
    phone_code: str | None = _field(default=None, name="phoneCode")
    """Не используется"""


class CrossborderTurkeyClientInfoResp(WBModel):
    orders: list[CrossborderTurkeyClientInfo] | None = _field(default=None)
    """Информация по клиенту для трансграничных поставок из Турции"""


class DeleteSuppliesTrbxBody(WBModel):
    trbx_ids: list[str] | None = _field(default=None, name="trbxIds")
    """Список ID грузомест, которые необходимо удалить"""


class GetOrdersNewResponse(WBModel):
    orders: list[OrderNew] | None = _field(default=None)
    """Список новых сборочных заданий"""


class GetOrdersResponse(WBModel):
    next: int | None = _field(default=None)
    """Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения
    следующего пакета данных
    """
    orders: list[Order] | None = _field(default=None)


class GetOrdersStatusBody(WBModel):
    orders: list[int] | None = _field(default=None)
    """Список ID сборочных заданий"""


class GetOrdersStatusResponse(WBModel):
    orders: list[GetOrdersStatusResponseOrdersItem] | None = _field(default=None)


class GetOrdersStatusResponseOrdersItem(WBModel):
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    is_cancellable: bool | None = _field(default=None, name="isCancellable")
    """Доступна ли отмена сборочного задания: - `false` — недоступна - `true` — доступна"""
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
    """Полное представление стикера в заданном формате"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    part_a: str | None = _field(default=None, name="partA")
    """Первая часть ID стикера для печати подписи"""
    part_b: str | None = _field(default=None, name="partB")
    """Вторая часть ID стикера для печати подписи"""


class GetSettingsAutoreturnsItemsBody(WBModel):
    chrt_ids: list[int] | None = _field(default=None, name="chrtIds")
    """Список ID размеров товаров в системе WB"""


class GetSettingsAutoreturnsItemsResponse(WBModel):
    results: list[GetSettingsAutoreturnsItemsResponseResultsItem] | None = _field(default=None)


class GetSettingsAutoreturnsItemsResponseResultsItem(WBModel):
    changeable: bool | None = _field(default=None)
    """- `true` — настройки автовозврата товара можно изменить"""
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара в системе WB"""
    error: list[GetSettingsAutoreturnsItemsResponseResultsItemErrorItem] | None = _field(default=None)
    """Детали ошибки"""
    success: bool | None = _field(default=None)
    """- `true` — настройки автовозврата товара успешно получены"""
    type: str | None = _field(default=None)
    """Куда будет возвращён товар:   - `auto` — место возврата определяется автоматически   -
    `byWarehouse` — на склад WB …
    """


class GetSettingsAutoreturnsItemsResponseResultsItemErrorItem(WBModel):
    code: int | None = _field(default=None)
    """Код ошибки"""
    detail: str | None = _field(default=None)
    """Дополнительная информация об ошибке"""


class GetSettingsAutoreturnsResponse(WBModel):
    type: str | None = _field(default=None)
    """Тип автовозврата:   - `allToWarehouse` — все товары отправляются на склад WB, кроме товаров
    тех предметов, которые автоматически возвращаются в ПВЗ …
    """


class GetSettingsAutoreturnsSubcategoriesRestrictedResponse(WBModel):
    data: list[GetSettingsAutoreturnsSubcategoriesRestrictedResponseDataItem] | None = _field(default=None)
    """Список ID предметов, товары которых не хранятся на складах WB"""
    next: int | None = _field(default=None)
    """Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения
    следующего пакета данных
    """


class GetSettingsAutoreturnsSubcategoriesRestrictedResponseDataItem(WBModel):
    subject_id: int | None = _field(default=None, name="subjectId")
    """ID предмета"""


class GetStatusHistoryBody(WBModel):
    orders: list[int] | None = _field(default=None)
    """ID сборочных заданий"""


class GetStatusHistoryResponse(WBModel):
    orders: list[GetStatusHistoryResponseOrdersItem] | None = _field(default=None)
    """Список сборочных заданий"""


class GetStatusHistoryResponseOrdersItem(WBModel):
    delivery_date: str | None = _field(default=None, name="deliveryDate")
    """Планируемая дата доставки, RFC3339"""
    order_id: int | None = _field(default=None, name="orderID")
    """ID сборочного задания"""
    statuses: list[GetStatusHistoryResponseOrdersItemStatusesItem] | None = _field(default=None)
    """Статусы"""


class GetStatusHistoryResponseOrdersItemStatusesItem(WBModel):
    code: str | None = _field(default=None)
    """Статус-код сборочного задания/заказа:   - `dispatched_to_delivery_service` — Продавец
    передал заказ в службу доставки в своей стране …
    """
    date: str | None = _field(default=None)
    """Дата присвоения статуса"""


class GetStickersCrossBorderBody(WBModel):
    orders: list[int] | None = _field(default=None)
    """Список ID сборочных заданий"""


class GetStickersCrossBorderResponse(WBModel):
    stickers: list[GetStickersCrossBorderResponseStickersItem] | None = _field(default=None)


class GetStickersCrossBorderResponseStickersItem(WBModel):
    barcode: str | None = _field(default=None)
    """Закодированное значение стикера"""
    file: str | None = _field(default=None)
    """Стикер в формате PDF, кодировка base64"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    parcel_id: str | None = _field(default=None, name="parcelId")
    """Трек-номер в стикере для отслеживания сборочного задания"""
    part_a: str | None = _field(default=None, name="partA")
    """Первая часть ID стикера для печати подписи"""
    part_b: str | None = _field(default=None, name="partB")
    """Вторая часть ID стикера для печати подписи"""
    status: str | None = _field(default=None)
    """Статус генерации стикера:   - `awaitingTrackNumber` — стикер не готов. Ожидается трек-номер
    от перевозчика.   - `ready` — стикер готов
    """


class GetSuppliesBarcodeResponse(WBModel):
    barcode: str | None = _field(default=None)
    """Закодированное значение стикера (ID поставки)"""
    file: str | None = _field(default=None)
    """Полное представление стикера в заданном формате (кодировка base64)"""


class GetSuppliesOrdersReshipmentResponse(WBModel):
    orders: list[GetSuppliesOrdersReshipmentResponseOrdersItem] | None = _field(default=None)
    """Список сборочных заданий"""


class GetSuppliesOrdersReshipmentResponseOrdersItem(WBModel):
    order_id: Any | None = _field(default=None, name="orderID")
    """ID сборочного задания"""
    supply_id: Any | None = _field(default=None, name="supplyID")
    """ID поставки"""


class GetSuppliesResponse(WBModel):
    next: int | None = _field(default=None)
    """Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения
    следующего пакета данных
    """
    supplies: list[Supply] | None = _field(default=None)
    """Список поставок"""


class GetSuppliesTrbxResponse(WBModel):
    trbxes: list[SupplyTrbx] | None = _field(default=None)


class GetSuppliesTrbxStickersBody(WBModel):
    trbx_ids: list[str] | None = _field(default=None, name="trbxIds")
    """Список ID грузомест, по которым необходимо вернуть стикеры"""


class GetSuppliesTrbxStickersResponse(WBModel):
    stickers: list[TrbxStickers] | None = _field(default=None)
    """Не менее 1 элемент"""


class Order(WBModel):
    address: OrderAddress | None = _field(default=None)
    """Точный адрес покупателя для доставки, если применимо. Из-за особенностей адреса некоторые
    поля могут быть пустыми
    """
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
    """Дата создания сборочного задания (RFC3339). Часовой пояс — UTC"""
    cross_border_type: int | None = _field(default=None, name="crossBorderType")
    """Тип сборочного задания:   - `0` — внутренняя поставка   - `1` — трансграничная поставка
    """
    currency_code: int | None = _field(default=None, name="currencyCode")
    """Код валюты продажи"""
    delivery_type: str | None = _field(default=None, name="deliveryType")
    """Тип доставки: - `fbs` — доставка на склад Wildberries (FBS)"""
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    is_zero_order: bool | None = _field(default=None, name="isZeroOrder")
    """Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым
    остатком …
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада WB, к которому привязан склад продавца"""
    offices: list[str] | None = _field(default=None)
    """Список офисов, куда следует привезти товар"""
    options: OrderOptions | None = _field(default=None)
    """Опции заказа"""
    order_uid: str | None = _field(default=None, name="orderUid")
    """ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине
    покупателя будут иметь одинаковый `orderUid`
    """
    price: int | None = _field(default=None)
    """Цена в валюте продажи с учётом всех скидок, кроме скидки по WB Кошельку, умноженная на 100.
    Код валюты продажи — в поле `currencyCode`. Предоставляется в информ …
    """
    rid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание: `rid` — это `srid` в ответах методов:   - Заявки
    покупателей на возврат   - Лента заказов   - Заказы   - Продажи …
    """
    scan_price: float | None = _field(default=None, name="scanPrice")
    """Цена приёмки в копейках. Отображается после фактической приёмки заказа"""
    skus: list[str] | None = _field(default=None)
    """Список баркодов"""
    supply_id: str | None = _field(default=None, name="supplyId")
    """ID поставки. Возвращается, если заказ закреплён за поставкой"""
    warehouse_id: int | None = _field(default=None, name="warehouseId")
    """ID склада продавца, на который поступило сборочное задание"""


class OrderAddress(WBModel):
    """Точный адрес покупателя для доставки, если применимо. Из-за особенностей адреса некоторы"""

    full_address: str | None = _field(default=None, name="fullAddress")
    """Адрес доставки"""
    latitude: float | None = _field(default=None)
    """Широта"""
    longitude: float | None = _field(default=None)
    """Долгота"""


class OrderNew(WBModel):
    address: OrderNewAddress | None = _field(default=None)
    """Точный адрес покупателя для доставки, если применимо. Из-за особенностей адреса некоторые
    поля могут быть пустыми
    """
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
    converted_final_price: int | None = _field(default=None, name="convertedFinalPrice")
    """Сумма к оплате покупателем в валюте страны продавца с учетом всех скидок, умноженная на 100.
    Предоставляется в информационных целях
    """
    converted_price: int | None = _field(default=None, name="convertedPrice")
    """Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная
    на 100. Предоставляется в информационных целях
    """
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата создания сборочного задания (RFC3339)"""
    cross_border_type: int | None = _field(default=None, name="crossBorderType")
    """Тип сборочного задания:   - `0` — внутренняя поставка   - `1` — трансграничная поставка
    """
    currency_code: int | None = _field(default=None, name="currencyCode")
    """Код валюты продажи"""
    ddate: str | None = _field(default=None)
    """Планируемая дата доставки заказа покупателю. Поле отображается для сборочных заданий со
    сверхгабаритными товарами `СГТ`, `cargoType: 2`
    """
    delivery_type: str | None = _field(default=None, name="deliveryType")
    """Тип доставки: - `fbs` — доставка на склад Wildberries (FBS)"""
    final_price: int | None = _field(default=None, name="finalPrice")
    """Сумма к оплате покупателем в валюте продажи с учетом всех скидок, умноженная на 100. Код
    валюты продажи указан в поле `currencyCode`. Предоставляется в информац …
    """
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    is_pickup_point_shipment_allowed: bool | None = _field(default=None, name="isPickupPointShipmentAllowed")
    """Можно ли отгрузить заказ на ПВЗ:   - `false` — нет   - `true` — да"""
    is_zero_order: bool | None = _field(default=None, name="isZeroOrder")
    """Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым
    остатком …
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада WB, к которому привязан склад продавца"""
    offices: list[str] | None = _field(default=None)
    """Список офисов, куда следует привезти товар"""
    optional_meta: list[str] | None = _field(default=None, name="optionalMeta")
    """Список идентификаторов маркировки, которые можно добавить в сборочное задание. …"""
    options: OrderNewOptions | None = _field(default=None)
    """Опции заказа"""
    order_uid: str | None = _field(default=None, name="orderUid")
    """ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине
    покупателя будут иметь одинаковый `orderUid`
    """
    price: int | None = _field(default=None)
    """Цена в валюте продажи с учётом всех скидок, кроме скидки по WB Кошельку, умноженная на 100.
    Код валюты продажи — в поле `currencyCode`. Предоставляется в информ …
    """
    required_meta: list[str] | None = _field(default=None, name="requiredMeta")
    """Список идентификаторов маркировки, которые необходимо добавить в сборочное задание, чтобы
    поставку с этим сборочным заданием можно было перевести в доставку
    """
    rid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание: `rid` — это `srid` в ответах методов:   - Заявки
    покупателей на возврат   - Лента заказов   - Заказы   - Продажи …
    """
    sale_price: int | None = _field(default=None, name="salePrice")
    """Цена продавца в валюте продажи с учётом скидки продавца, без учёта скидки WB Клуба,
    умноженная на 100. Предоставляется в информационных целях
    """
    scan_price: float | None = _field(default=None, name="scanPrice")
    """Цена приёмки в копейках. Отображается после фактической приёмки заказа. Для данного метода
    всегда будет возвращаться `null`. Предоставляется в информационных це …
    """
    seller_date: str | None = _field(default=None, name="sellerDate")
    """Рекомендуемая дата доставки СГТ в сортировочный центр или на склад. Поле отображается для
    сборочных заданий со сверхгабаритными товарами `СГТ`, `cargoType: 2`
    """
    skus: list[str] | None = _field(default=None)
    """Список баркодов"""
    warehouse_id: int | None = _field(default=None, name="warehouseId")
    """ID склада продавца, на который поступило сборочное задание"""


class OrderNewAddress(WBModel):
    """Точный адрес покупателя для доставки, если применимо. Из-за особенностей адреса некоторы"""

    full_address: str | None = _field(default=None, name="fullAddress")
    """Адрес доставки"""
    latitude: float | None = _field(default=None)
    """Широта"""
    longitude: float | None = _field(default=None)
    """Долгота"""


class OrderNewOptions(WBModel):
    """Опции заказа"""

    is_b2_b: bool | None = _field(default=None, name="isB2B")
    """Признак B2B-продажи:   - `false` — не B2B-продажа   - `true` — B2B-продажа"""


class OrderOptions(WBModel):
    """Опции заказа"""

    is_b2_b: bool | None = _field(default=None, name="isB2B")
    """Признак B2B-продажи:   - `false` — не B2B-продажа   - `true` — B2B-продажа"""


class OrdersRequestAPI(WBModel):
    orders: list[int] | None = _field(default=None)
    """Список заказов"""


class Pass(WBModel):
    """Данные о пропуске продавца"""

    car_model: str | None = _field(default=None, name="carModel")
    """Марка машины"""
    car_number: str | None = _field(default=None, name="carNumber")
    """Номер машины"""
    date_end: str | None = _field(default=None, name="dateEnd")
    """Дата окончания действия пропуска"""
    first_name: str | None = _field(default=None, name="firstName")
    """Имя водителя"""
    id: int | None = _field(default=None)
    """ID пропуска"""
    last_name: str | None = _field(default=None, name="lastName")
    """Фамилия водителя"""
    office_address: str | None = _field(default=None, name="officeAddress")
    """Адрес склада"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада"""
    office_name: str | None = _field(default=None, name="officeName")
    """Название склада"""


class PassOffice(WBModel):
    """Данные о складе, для которого требуется пропуск"""

    address: str | None = _field(default=None)
    """Адрес"""
    id: int | None = _field(default=None)
    """ID"""
    name: str | None = _field(default=None)
    """Название"""


class SetMetaCustomsDeclarationBody(WBModel):
    customs_declaration: str | None = _field(default=None, name="customsDeclaration")
    """Номер ДТ"""


class SetMetaExpirationBody(WBModel):
    expiration: str | None = _field(default=None)
    """Дата, до которой годен товар. Не менее 30 дней с текущей даты"""


class SetMetaGtinBody(WBModel):
    gtin: str | None = _field(default=None)
    """GTIN"""


class SetMetaImeiBody(WBModel):
    imei: str | None = _field(default=None)
    """IMEI"""


class SetMetaSgtinBody(WBModel):
    sgtins: list[str] | None = _field(default=None)
    """Массив кодов маркировки Честного знака. Вы можете передать коды маркировки:   - полностью —
    с GS-разделителями и кодом проверки подлинности (криптохвостом) …
    """


class SetMetaUinBody(WBModel):
    uin: str | None = _field(default=None)
    """УИН"""


class Supply(WBModel):
    cargo_type: int | None = _field(default=None, name="cargoType")
    """Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   -
    `3` — крупногабаритный товар (КГТ+)
    """
    closed_at: str | None = _field(default=None, name="closedAt")
    """Дата закрытия поставки (RFC3339)"""
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата создания поставки (RFC3339)"""
    cross_border_type: int | None = _field(default=None, name="crossBorderType")
    """Тип поставки:   - `0` — внутренняя поставка   - `1` — трансграничная поставка   - `null` —
    значение отсутствует
    """
    destination_office_id: int | None = _field(default=None, name="destinationOfficeId")
    """ID склада назначения поставки. Если `null`, склад назначения не указан"""
    done: bool | None = _field(default=None)
    """Флаг закрытия поставки:   - `true` — закрыта   - `false` — открыта"""
    id: str | None = _field(default=None)
    """ID поставки"""
    is_b2b: bool | None = _field(default=None, name="isB2b")
    """Признак B2B-продажи:   - `true` — B2B-продажа   - `false` — не B2B-продажа   - `null` —
    признак отсутствует, сборочные задания не добавлены к поставке
    """
    is_pickup_point_shipment_allowed: bool | None = _field(default=None, name="isPickupPointShipmentAllowed")
    """Можно ли отгрузить заказ на ПВЗ:   - `false` — нет   - `true` — да"""
    name: str | None = _field(default=None)
    """Наименование поставки"""
    recommended_wh_id: int | None = _field(default=None, name="recommendedWhId")
    """ID рекомендуемого склада для приёмки поставки для Москвы и МО. …"""
    scan_dt: str | None = _field(default=None, name="scanDt")
    """Дата сканирования поставки или первого заказа (RFC3339)"""


class SupplyTrbx(WBModel):
    id: str | None = _field(default=None)
    """ID грузоместа"""


class TrbxStickers(WBModel):
    barcode: str | None = _field(default=None)
    """Закодированное значение стикера"""
    file: str | None = _field(default=None)
    """Полное представление стикера в заданном формате (кодировка base64)"""


class UpdatePassesBody(WBModel):
    car_model: str | None = _field(default=None, name="carModel")
    """Марка машины"""
    car_number: str | None = _field(default=None, name="carNumber")
    """Номер машины"""
    first_name: str | None = _field(default=None, name="firstName")
    """Имя водителя"""
    last_name: str | None = _field(default=None, name="lastName")
    """Фамилия водителя"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада"""


class UpdateSettingsAutoreturnBody(WBModel):
    type: str | None = _field(default=None)
    """Тип автовозврата малогабаритных товаров: …"""


class UpdateSettingsAutoreturnsItemBody(WBModel):
    chrt_ids: list[int] | None = _field(default=None, name="chrtIds")
    """Список ID размеров товаров в системе WB"""
    type: str | None = _field(default=None)
    """Тип автовозврата малогабаритных товаров:   - `byWarehouse` — все товары отправляются на
    склад WB …
    """


class UpdateSettingsAutoreturnsItemResponse(WBModel):
    results: list[UpdateSettingsAutoreturnsItemResponseResultsItem] | None = _field(default=None)


class UpdateSettingsAutoreturnsItemResponseResultsItem(WBModel):
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара в системе WB"""
    error: Any | None = _field(default=None)
    """Детали ошибки"""
    success: bool | None = _field(default=None)
    """- `true` — настройки автовозврата товара обновлены"""


class UpdateSuppliesOrderBody(WBModel):
    orders: list[int] | None = _field(default=None)
    """ID сборочных заданий"""


class V3ArchiveOrder(WBModel):
    """Архивное сборочное задание"""

    cargo_type: str | None = _field(default=None, name="cargoType")
    """Тип товара:   - `mgt` — малогабаритный товар (МГТ)   - `sgt` — сверхгабаритный товар (СГТ)
    - `kgtPlus` — крупногабаритный товар (КГТ+)
    """
    color_code: str | None = _field(default=None, name="colorCode")
    """Код цвета для колеруемых товаров"""
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата создания заказа"""
    cross_border: V3ArchiveOrderCrossBorder | None = _field(default=None, name="crossBorder")
    """Информация о заказе по модели кроссбордер"""
    cross_border_type: str | None = _field(default=None, name="crossBorderType")
    """Тип сборочного задания:   - `local` — внутренняя поставка   - `crossBorder` — трансграничная
    поставка
    """
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    is_zero_order: bool | None = _field(default=None, name="isZeroOrder")
    """Признак заказа товара с нулевым остатком:   - `false` — заказ сделан на товар с ненулевым
    остатком   - `true` — заказ сделан на товар с нулевым остатком
    """
    meta_details: list[V3ArchiveOrderMetaDetailsItem] | None = _field(default=None, name="metaDetails")
    """Детали маркировки"""
    options: V3ArchiveOrderOptions | None = _field(default=None)
    """Опции заказа"""
    order_uid: str | None = _field(default=None, name="orderUid")
    """ID транзакции для группировки сборочных заданий. Сборочные задания в одной корзине
    покупателя будут иметь одинаковый `orderUid`
    """
    price_info: V3ArchiveOrderPriceInfo | None = _field(default=None, name="priceInfo")
    """Информация о цене заказа"""
    product: V3ArchiveOrderProduct | None = _field(default=None)
    """Информация о товаре"""
    rid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание: `rid` — это `srid` в ответах методов:   - Заявки
    покупателей на возврат   - Лента заказов   - Заказы   - Продажи …
    """
    scan_price: int | None = _field(default=None, name="scanPrice")
    """Цена приёмки заказа в копейках"""
    status: V3ArchiveOrderStatus | None = _field(default=None)
    """Последние статусы сборочного задания"""
    sticker_id: int | None = _field(default=None, name="stickerId")
    """ID стикера"""
    supply_id: str | None = _field(default=None, name="supplyId")
    """ID поставки"""
    warehouse_id: int | None = _field(default=None, name="warehouseId")
    """ID склада продавца, с которого был отгружен товар"""


class V3ArchiveOrderCrossBorder(WBModel):
    """Информация о заказе по модели кроссбордер"""

    parcel: str | None = _field(default=None)
    """ID посылки"""


class V3ArchiveOrderMetaDetailsItem(WBModel):
    decision: str | None = _field(default=None)
    """Статусы проверки идентификаторов маркировки. Статусы проверки `imei`, с которыми поставку
    можно перевести в доставку: …
    """
    key: str | None = _field(default=None)
    """Идентификатор маркировки"""
    value: str | None = _field(default=None)
    """Значение идентификатора маркировки"""


class V3ArchiveOrderOptions(WBModel):
    """Опции заказа"""

    is_b2_b: bool | None = _field(default=None, name="isB2B")
    """Признак B2B-продажи:   - `false` — не B2B-продажа   - `true` — B2B-продажа"""


class V3ArchiveOrderPriceInfo(WBModel):
    """Информация о цене заказа"""

    converted_currency_code: int | None = _field(default=None, name="convertedCurrencyCode")
    """Код валюты страны продавца"""
    converted_price: int | None = _field(default=None, name="convertedPrice")
    """Цена в валюте страны продавца с учетом всех скидок, кроме скидки по WB Кошельку, умноженная
    на 100
    """
    currency_code: int | None = _field(default=None, name="currencyCode")
    """Код валюты продажи"""
    price: int | None = _field(default=None)
    """Цена в валюте продажи с учетом всех скидок, кроме скидки по WB Кошельку, умноженная на 100
    """


class V3ArchiveOrderProduct(WBModel):
    """Информация о товаре"""

    article: str | None = _field(default=None)
    """Артикул продавца"""
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара в системе WB"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    skus: list[str] | None = _field(default=None)
    """Список баркодов"""


class V3ArchiveOrderStatus(WBModel):
    """Последние статусы сборочного задания"""

    supplier_status: str | None = _field(default=None, name="supplierStatus")
    """Статус сборочного задания, установленный продавцом"""
    wb_status: str | None = _field(default=None, name="wbStatus")
    """Статус сборочного задания в системе Wildberries"""


class V3ArchiveOrders(WBModel):
    """Список архивных сборочных заданий"""

    next: int | None = _field(default=None)
    """Параметр пагинации. Содержит значение, которое необходимо указать в запросе для получения
    следующего пакета данных
    """
    orders: list[V3ArchiveOrder] | None = _field(default=None)
    """Архивные сборочные задания"""


class V3GetMetaMultiRequest(WBModel):
    """ID сборочных заданий"""

    orders: list[int] | None = _field(default=None)
    """Не более 100 элементов"""


class V3OrderMetaAPI(WBModel):
    id: int | None = _field(default=None)
    """ID сборочного задания"""
    meta_details: list[V3OrderMetaAPIMetaDetailsItem] | None = _field(default=None, name="metaDetails")
    """Детали маркировки"""


class V3OrderMetaAPIMetaDetailsItem(WBModel):
    decision: str | None = _field(default=None)
    """Статусы проверки идентификаторов маркировки. Статусы проверки `imei`, с которыми поставку
    можно перевести в доставку: …
    """
    key: str | None = _field(default=None)
    """Идентификатор маркировки"""
    value: str | None = _field(default=None)
    """Значение идентификатора маркировки"""


class V3OrdersMetaAPI(WBModel):
    orders: list[V3OrderMetaAPI] | None = _field(default=None)


class V3SupplyOrderIDsAPI(WBModel):
    order_ids: list[int] | None = _field(default=None, name="orderIds")
    """ID сборочных заданий"""
