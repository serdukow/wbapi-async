# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from msgspec import field as _field

from ..client.model import WBModel


class CreateTaskResponse(WBModel):
    data: CreateTaskResponseData | None = _field(default=None)


class CreateTaskResponseData(WBModel):
    task_id: str | None = _field(default=None, name="taskId")
    """ID задания на генерацию"""


class ExciseReportRequest(WBModel):
    countries: list[str] | None = _field(default=None)
    """Код стран по стандарту ISO 3166-2. Чтобы получить данные по всем странам, оставьте параметр
    пустым
    """


class ExciseReportResponse(WBModel):
    response: ModelsExciseReportResponse | None = _field(default=None)


class GetAcceptanceReportTasksDownloadResponseItem(WBModel):
    count: int | None = _field(default=None)
    """Количество товаров, шт."""
    gi_create_date: str | None = _field(default=None, name="giCreateDate")
    """Дата создания поставки"""
    income_id: int | None = _field(default=None, name="incomeId")
    """Номер поставки"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    shk_create_date: str | None = _field(default=None, name="shkCreateDate")
    """Дата приёмки"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Предмет"""
    total: float | None = _field(default=None)
    """Суммарная стоимость приёмки, ₽ с копейками"""


class GetAnalyticsAntifraudDetailsResponse(WBModel):
    details: list[GetAnalyticsAntifraudDetailsResponseDetailsItem] | None = _field(default=None)


class GetAnalyticsAntifraudDetailsResponseDetailsItem(WBModel):
    currency: str | None = _field(default=None)
    """Валюта заказа"""
    date_from: str | None = _field(default=None, name="dateFrom")
    """Начало отчётного периода"""
    date_to: str | None = _field(default=None, name="dateTo")
    """Конец отчётного периода"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    sum: int | None = _field(default=None)
    """Сумма заказа"""


class GetAnalyticsBannedProductsBlockedResponse(WBModel):
    report: list[GetAnalyticsBannedProductsBlockedResponseReportItem] | None = _field(default=None)
    """Отчёт"""


class GetAnalyticsBannedProductsBlockedResponseReportItem(WBModel):
    brand: str | None = _field(default=None)
    """Бренд"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    reason: str | None = _field(default=None)
    """Причина блокировки"""
    title: str | None = _field(default=None)
    """Наименование товара"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class GetAnalyticsBrandShareBrandsResponse(WBModel):
    data: list[str] | None = _field(default=None)
    """Список брендов"""


class GetAnalyticsBrandShareParentSubjectsResponse(WBModel):
    data: list[GetAnalyticsBrandShareParentSubjectsResponseDataItem] | None = _field(default=None)
    """Категории бренда"""


class GetAnalyticsBrandShareParentSubjectsResponseDataItem(WBModel):
    parent_id: int | None = _field(default=None, name="parentId")
    """ID родительской категории"""
    parent_name: str | None = _field(default=None, name="parentName")
    """Название родительской категории"""


class GetAnalyticsBrandShareResponse(WBModel):
    report: list[GetAnalyticsBrandShareResponseReportItem] | None = _field(default=None)
    """Отчёт"""


class GetAnalyticsBrandShareResponseReportItem(WBModel):
    apply_date: str | None = _field(default=None, name="applyDate")
    """Дата"""
    brand_rating: int | None = _field(default=None, name="brandRating")
    """Рейтинг бренда в родительской категории"""
    price_percent: float | None = _field(default=None, name="pricePercent")
    """Доля от продаж в родительской категории — цена, %"""
    qty_percent: float | None = _field(default=None, name="qtyPercent")
    """Доля от продаж в родительской категории — количество, %"""


class GetAnalyticsDeductionsResponse(WBModel):
    data: GetAnalyticsDeductionsResponseData | None = _field(default=None)
    """Данные ответа"""


class GetAnalyticsDeductionsResponseData(WBModel):
    """Данные ответа"""

    reports: list[GetAnalyticsDeductionsResponseDataReportsItem] | None = _field(default=None)
    """Удержания"""
    total: int | None = _field(default=None)
    """Количество удержаний в отчёте. Без учёта `limit` и `offset`"""


class GetAnalyticsDeductionsResponseDataReportsItem(WBModel):
    bonus_summ: float | None = _field(default=None, name="bonusSumm")
    """Сумма удержания"""
    bonus_type: str | None = _field(default=None, name="bonusType")
    """Причина удержания"""
    dt_bonus: str | None = _field(default=None, name="dtBonus")
    """Дата и время удержания"""
    new_color: str | None = _field(default=None, name="newColor")
    """Новый цвет"""
    new_shk_id: int | None = _field(default=None, name="newShkId")
    """Новый штрихкод"""
    new_size: str | None = _field(default=None, name="newSize")
    """Новый размер"""
    new_sku: str | None = _field(default=None, name="newSku")
    """Новый баркод"""
    new_vendor_code: str | None = _field(default=None, name="newVendorCode")
    """Новый артикул продавца"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    old_color: str | None = _field(default=None, name="oldColor")
    """Старый цвет"""
    old_shk_id: int | None = _field(default=None, name="oldShkId")
    """Старый штрихкод"""
    old_size: str | None = _field(default=None, name="oldSize")
    """Старый размер"""
    old_sku: str | None = _field(default=None, name="oldSku")
    """Старый баркод"""
    old_vendor_code: str | None = _field(default=None, name="oldVendorCode")
    """Старый артикул продавца"""
    photo_urls: list[str] | None = _field(default=None, name="photoUrls")
    """Фото замеров"""


class GetAnalyticsGoodsLabelingResponse(WBModel):
    report: list[GetAnalyticsGoodsLabelingResponseReportItem] | None = _field(default=None)


class GetAnalyticsGoodsLabelingResponseReportItem(WBModel):
    amount: float | None = _field(default=None)
    """Сумма штрафа, руб"""
    date: str | None = _field(default=None)
    """Дата"""
    income_id: int | None = _field(default=None, name="incomeId")
    """Номер поставки"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    photo_urls: list[str] | None = _field(default=None, name="photoUrls")
    """URL фото товара"""
    shk_id: int | None = _field(default=None, name="shkID")
    """Штрихкод товара в WB"""
    sku: str | None = _field(default=None)
    """Баркод из карточки товара"""


class GetAnalyticsGoodsReturnsResponse(WBModel):
    report: list[GetAnalyticsGoodsReturnsResponseReportItem] | None = _field(default=None)
    """Отчёт"""


class GetAnalyticsGoodsReturnsResponseReportItem(WBModel):
    barcode: str | None = _field(default=None)
    """Баркод"""
    brand: str | None = _field(default=None)
    """Бренд"""
    completed_dt: str | None = _field(default=None, name="completedDt")
    """Дата и время выдачи возврата продавцу"""
    dst_office_address: str | None = _field(default=None, name="dstOfficeAddress")
    """Адрес ПВЗ выдачи возврата"""
    dst_office_id: int | None = _field(default=None, name="dstOfficeId")
    """ID ПВЗ выдачи возврата"""
    expired_dt: str | None = _field(default=None, name="expiredDt")
    """Дата и время истечения срока хранения возврата"""
    is_status_active: int | None = _field(default=None, name="isStatusActive")
    """Тип статуса возврата:    * `0` — архивный   * `1` — активный"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    order_dt: str | None = _field(default=None, name="orderDt")
    """Дата заказа на возврат"""
    order_id: int | None = _field(default=None, name="orderId")
    """Номер сборочного задания"""
    ready_to_return_dt: str | None = _field(default=None, name="readyToReturnDt")
    """Дата и время готовности возврата к выдаче"""
    reason: str | None = _field(default=None)
    """Причина возврата"""
    return_type: str | None = _field(default=None, name="returnType")
    """Тип возврата"""
    shk_id: int | None = _field(default=None, name="shkId")
    """Штрихкод"""
    srid: str | None = _field(default=None)
    """Уникальный ID заказа на возврат"""
    status: str | None = _field(default=None)
    """Статус возврата"""
    sticker_id: str | None = _field(default=None, name="stickerId")
    """Стикер заказа на возврат"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Предмет"""
    tech_size: str | None = _field(default=None, name="techSize")
    """Размер"""


class GetAnalyticsRegionSaleResponse(WBModel):
    report: list[GetAnalyticsRegionSaleResponseReportItem] | None = _field(default=None)


class GetAnalyticsRegionSaleResponseReportItem(WBModel):
    city_name: str | None = _field(default=None, name="cityName")
    """Населённый пункт"""
    country_name: str | None = _field(default=None, name="countryName")
    """Страна"""
    fo_name: str | None = _field(default=None, name="foName")
    """Федеральный округ"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    region_name: str | None = _field(default=None, name="regionName")
    """Регион"""
    sa: str | None = _field(default=None)
    """Артикул продавца"""
    sale_invoice_cost_price: float | None = _field(default=None, name="saleInvoiceCostPrice")
    """К перечислению за товар, ₽"""
    sale_invoice_cost_price_perc: float | None = _field(default=None, name="saleInvoiceCostPricePerc")
    """Доля, %"""
    sale_item_invoice_qty: int | None = _field(default=None, name="saleItemInvoiceQty")
    """Выкупили, шт."""


class GetPaidStorageTasksDownloadResponseItem(WBModel):
    barcode: str | None = _field(default=None)
    """Баркод"""
    barcodes_count: int | None = _field(default=None, name="barcodesCount")
    """Количество единиц товара (штук), подлежащих тарифицированию за расчётные сутки"""
    brand: str | None = _field(default=None)
    """Бренд"""
    calc_type: str | None = _field(default=None, name="calcType")
    """Способ расчёта"""
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера для этого артикула WB"""
    date: str | None = _field(default=None)
    """Дата, за которую был расчёт или перерасчёт"""
    gi_id: int | None = _field(default=None, name="giId")
    """ID поставки"""
    log_warehouse_coef: float | None = _field(default=None, name="logWarehouseCoef")
    """Коэффициент логистики и хранения. На данный момент может быть только `0`"""
    loyalty_discount: float | None = _field(default=None, name="loyaltyDiscount")
    """Скидка программы лояльности, ₽"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада. На данный момент может быть только `0`"""
    original_date: str | None = _field(default=None, name="originalDate")
    """Если был перерасчёт, это дата первоначального расчёта. Если перерасчёта не было, совпадает с
    `date`
    """
    pallet_count: float | None = _field(default=None, name="palletCount")
    """Количество паллет"""
    pallet_place_code: int | None = _field(default=None, name="palletPlaceCode")
    """Код паллетоместа. На данный момент может быть только `0`"""
    size: str | None = _field(default=None)
    """Размер (`techSize` в карточке товара)"""
    subject: str | None = _field(default=None)
    """Предмет"""
    tariff_fix_date: str | None = _field(default=None, name="tariffFixDate")
    """Дата фиксации тарифа"""
    tariff_lower_date: str | None = _field(default=None, name="tariffLowerDate")
    """Дата понижения тарифа"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""
    volume: float | None = _field(default=None)
    """Объём товара"""
    warehouse: str | None = _field(default=None)
    """Название склада. На данный момент может быть только `Склад WB РФ`"""
    warehouse_coef: float | None = _field(default=None, name="warehouseCoef")
    """Коэффициент хранения"""
    warehouse_price: float | None = _field(default=None, name="warehousePrice")
    """Сумма хранения"""


class GetTasksResponse(WBModel):
    data: GetTasksResponseData | None = _field(default=None)


class GetTasksResponseData(WBModel):
    id: str | None = _field(default=None)
    """ID задания"""
    status: str | None = _field(default=None)
    """Статус задания:   * `new` — новое   * `processing` —  обрабатывается   * `done` — отчёт
    готов   * `purged` — отчёт удалён   * `canceled` — отклонено
    """


class GetWarehouseRemainsTasksDownloadResponseItem(WBModel):
    barcode: str | None = _field(default=None)
    """Баркод"""
    brand: str | None = _field(default=None)
    """Бренд"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    tech_size: str | None = _field(default=None, name="techSize")
    """Размер"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""
    volume: float | None = _field(default=None)
    """Объём, л"""
    warehouses: list[GetWarehouseRemainsTasksDownloadResponseItemWarehousesItem] | None = _field(default=None)
    """Остатки на складах и товары в пути. Будут в ответе только при ненулевом `quantity`"""


class GetWarehouseRemainsTasksDownloadResponseItemWarehousesItem(WBModel):
    quantity: int | None = _field(default=None)
    """Количество, шт."""
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Название склада"""


class MeasurementPenalties(WBModel):
    data: MeasurementPenaltiesData | None = _field(default=None)
    """Данные ответа"""


class MeasurementPenaltiesData(WBModel):
    """Данные ответа"""

    reports: list[MeasurementPenaltiesDataReportsItem] | None = _field(default=None)
    """Удержания"""
    total: int | None = _field(default=None)
    """Количество удержаний в отчёте. Без учёта `limit` и `offset`"""


class MeasurementPenaltiesDataReportsItem(WBModel):
    dim_id: int | None = _field(default=None, name="dimId")
    """ID замера"""
    dt_bonus: str | None = _field(default=None, name="dtBonus")
    """Дата штрафа"""
    height: int | None = _field(default=None)
    """Высота, см (фактические габариты по замеру на складе)"""
    height_sup: int | None = _field(default=None, name="heightSup")
    """Высота, см (габариты карточки товара)"""
    is_valid: bool | None = _field(default=None, name="isValid")
    """Статус обмера:   - `false` — отменён   - `true` — подтверждён"""
    is_valid_dt: str | None = _field(default=None, name="isValidDt")
    """Дата и время подтверждения или отмены обмера"""
    length: int | None = _field(default=None)
    """Длина, см (фактические габариты по замеру на складе)"""
    length_sup: int | None = _field(default=None, name="lengthSup")
    """Длина, см (габариты карточки товара)"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    penalty_amount: float | None = _field(default=None, name="penaltyAmount")
    """Сумма штрафа"""
    photo_urls: list[str] | None = _field(default=None, name="photoUrls")
    """Фото замеров"""
    prc_over: float | None = _field(default=None, name="prcOver")
    """Разница в габаритах, %"""
    reversal_amount: float | None = _field(default=None, name="reversalAmount")
    """Сумма сторно"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Предмет"""
    volume: float | None = _field(default=None)
    """Объём, л (фактические габариты по замеру на складе)"""
    volume_sup: float | None = _field(default=None, name="volumeSup")
    """Объём, л (габариты карточки товара)"""
    width: int | None = _field(default=None)
    """Ширина, см (фактические габариты по замеру на складе)"""
    width_sup: int | None = _field(default=None, name="widthSup")
    """Ширина, см (габариты карточки товара)"""


class ModelsExciseReportResponse(WBModel):
    data: list[ModelsExciseReportResponseDataItem] | None = _field(default=None)


class ModelsExciseReportResponseDataItem(WBModel):
    barcode: str | None = _field(default=None)
    """Баркод"""
    currency_name_short: str | None = _field(default=None)
    """Валюта"""
    excise_short: str | None = _field(default=None)
    """Код маркировки"""
    fiscal_doc_number: int | None = _field(default=None)
    """Номер фискального документа (чека полного расчёта), если есть"""
    fiscal_drive_number: str | None = _field(default=None)
    """Номер фискального накопителя, если есть"""
    fiscal_dt: str | None = _field(default=None)
    """Дата фискализации (дата в чеке), если есть, `ГГГГ-ММ-ДД`"""
    name: str | None = _field(default=None)
    """Страна покупателя"""
    nm_id: int | None = _field(default=None)
    """Артикул WB"""
    operation_type_id: int | None = _field(default=None)
    """Тип операции, если есть:    * `1` — вывод из оборота   * `2` — возврат в оборот"""
    price: float | None = _field(default=None)
    """Цена товара, с НДС"""
    rid: int | None = _field(default=None)
    """`Rid`"""
    srid: str | None = _field(default=None)
    """`Srid`"""


class OrdersItem(WBModel):
    barcode: str | None = _field(default=None)
    """Баркод"""
    brand: str | None = _field(default=None)
    """Бренд"""
    cancel_date: str | None = _field(default=None, name="cancelDate")
    """Дата и время отмены заказа. Если заказ не был отменен, то "0001-01-01T00:00:00".Если часовой
    пояс не указан, то берётся Московское время UTC+3.
    """
    category: str | None = _field(default=None)
    """Категория"""
    country_name: str | None = _field(default=None, name="countryName")
    """Страна"""
    date: str | None = _field(default=None)
    """Дата и время заказа. Это поле соответствует параметру `dateFrom` в запросе, если параметр
    `flag`=1. Если часовой пояс не указан, то берётся Московское время (UT …
    """
    discount_percent: int | None = _field(default=None, name="discountPercent")
    """Скидка продавца, %"""
    finished_price: float | None = _field(default=None, name="finishedPrice")
    """Цена с учетом всех скидок, кроме суммы по WB Кошельку"""
    g_number: str | None = _field(default=None, name="gNumber")
    """ID корзины покупателя. Заказы одной транзакции будут иметь одинаковый `gNumber`"""
    income_id: int | None = _field(default=None, name="incomeID")
    """Номер поставки"""
    is_cancel: bool | None = _field(default=None, name="isCancel")
    """Отмена заказа:   - `true` — заказ отменен"""
    is_realization: bool | None = _field(default=None, name="isRealization")
    """Договор реализации"""
    is_supply: bool | None = _field(default=None, name="isSupply")
    """Договор поставки"""
    last_change_date: str | None = _field(default=None, name="lastChangeDate")
    """Дата и время обновления информации в сервисе. Это поле соответствует параметру `dateFrom` в
    запросе, если параметр `flag`=0 или не указан. Если часовой пояс не …
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    oblast_okrug_name: str | None = _field(default=None, name="oblastOkrugName")
    """Округ"""
    price_with_disc: float | None = _field(default=None, name="priceWithDisc")
    """Цена со скидкой продавца, в том числе со скидкой WB Клуба"""
    region_name: str | None = _field(default=None, name="regionName")
    """Регион"""
    spp: float | None = _field(default=None)
    """Скидка WB, %"""
    srid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание для использующих API Маркетплейс: `srid` равен `rid` в
    ответах методов сборочных заданий.
    """
    sticker: str | None = _field(default=None)
    """ID стикера"""
    subject: str | None = _field(default=None)
    """Предмет"""
    supplier_article: str | None = _field(default=None, name="supplierArticle")
    """Артикул продавца"""
    tech_size: str | None = _field(default=None, name="techSize")
    """Размер товара"""
    total_price: float | None = _field(default=None, name="totalPrice")
    """Цена без скидок"""
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Склад отгрузки"""
    warehouse_type: str | None = _field(default=None, name="warehouseType")
    """Тип склада хранения товаров"""


class SalesItem(WBModel):
    barcode: str | None = _field(default=None)
    """Баркод"""
    brand: str | None = _field(default=None)
    """Бренд"""
    category: str | None = _field(default=None)
    """Категория"""
    country_name: str | None = _field(default=None, name="countryName")
    """Страна"""
    date: str | None = _field(default=None)
    """Дата и время продажи. Это поле соответствует параметру `dateFrom` в запросе, если параметр
    `flag`=1. Если часовой пояс не указан, то берётся Московское время (U …
    """
    discount_percent: int | None = _field(default=None, name="discountPercent")
    """Скидка продавца, %"""
    finished_price: float | None = _field(default=None, name="finishedPrice")
    """Фактическая цена с учётом всех скидок (к взиманию с покупателя).Синхронизация данных
    занимает до 24 часов, в течение этого времени в поле может отображаться зна …
    """
    for_pay: float | None = _field(default=None, name="forPay")
    """К перечислению продавцу.Синхронизация данных занимает до 24 часов, в течение этого времени в
    поле может отображаться значение `0`
    """
    g_number: str | None = _field(default=None, name="gNumber")
    """ID корзины покупателя. Заказы одной транзакции будут иметь одинаковый `gNumber`"""
    income_id: int | None = _field(default=None, name="incomeID")
    """Номер поставки"""
    is_realization: bool | None = _field(default=None, name="isRealization")
    """Договор реализации"""
    is_supply: bool | None = _field(default=None, name="isSupply")
    """Договор поставки"""
    last_change_date: str | None = _field(default=None, name="lastChangeDate")
    """Дата и время обновления информации в сервисе. Это поле соответствует параметру `dateFrom` в
    запросе, если параметр `flag`=0 или не указан. Если часовой пояс не …
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    oblast_okrug_name: str | None = _field(default=None, name="oblastOkrugName")
    """Округ"""
    payment_sale_amount: int | None = _field(default=None, name="paymentSaleAmount")
    """Скидка за оплату WB Кошельком, ₽"""
    price_with_disc: float | None = _field(default=None, name="priceWithDisc")
    """Цена со скидкой продавца, в том числе со скидкой WB Клуба, от которой рассчитывается сумма к
    перечислению продавцу `forPay`.Синхронизация данных занимает до 24 …
    """
    region_name: str | None = _field(default=None, name="regionName")
    """Регион"""
    sale_id: str | None = _field(default=None, name="saleID")
    """Уникальный ID продажи/возврата - `S**********` — продажа - `R**********` — возврат (на склад
    WB)
    """
    spp: float | None = _field(default=None)
    """Скидка WB, %"""
    srid: str | None = _field(default=None)
    """Уникальный ID заказа. Примечание для использующих API Маркетплейс: `srid` равен `rid` в
    ответах методов сборочных заданий.
    """
    sticker: str | None = _field(default=None)
    """ID стикера"""
    subject: str | None = _field(default=None)
    """Предмет"""
    supplier_article: str | None = _field(default=None, name="supplierArticle")
    """Артикул продавца"""
    tech_size: str | None = _field(default=None, name="techSize")
    """Размер товара"""
    total_price: float | None = _field(default=None, name="totalPrice")
    """Цена без скидок"""
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Склад отгрузки"""
    warehouse_type: str | None = _field(default=None, name="warehouseType")
    """Тип склада хранения товаров"""


class WHM(WBModel):
    data: WHMData | None = _field(default=None)
    """Данные ответа"""


class WHMData(WBModel):
    """Данные ответа"""

    reports: list[WHMDataReportsItem] | None = _field(default=None)
    """Замеры"""
    total: int | None = _field(default=None)
    """Количество замеров в отчёте. Без учёта `limit` и `offset`"""


class WHMDataReportsItem(WBModel):
    dim_id: int | None = _field(default=None, name="dimId")
    """ID замера"""
    dt: str | None = _field(default=None)
    """Дата и время"""
    height: int | None = _field(default=None)
    """Высота, см"""
    length: int | None = _field(default=None)
    """Длина, см"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    photo_urls: list[str] | None = _field(default=None, name="photoUrls")
    """Фото замеров"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Предмет"""
    volume: float | None = _field(default=None)
    """Объём, л"""
    width: int | None = _field(default=None)
    """Ширина, см"""
