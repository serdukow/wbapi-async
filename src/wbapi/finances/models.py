# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from msgspec import field as _field

from ..client.model import WBModel


class AcquiringReportListReq(WBModel):
    """Параметры запроса"""

    date_from: str | None = _field(default=None, name="dateFrom")
    """Начальная дата отчёта.Можно передать дату или дату со временем. Время можно указывать с
    точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339, в …
    """
    date_to: str | None = _field(default=None, name="dateTo")
    """Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со временем. Время
    можно указывать с точностью до секунд или миллисекунд.Время передаё …
    """
    limit: int | None = _field(default=None)
    """Количество отчётов в ответе"""
    offset: int | None = _field(default=None)
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""


class AcquiringReportListRes(WBModel):
    """Список отчётов об издержках на приём платежей"""

    acquiring_fee_sum: str | None = _field(default=None, name="acquiringFeeSum")
    """Сумма издержек по эквайрингу"""
    acquiring_fee_vat_sum: str | None = _field(default=None, name="acquiringFeeVatSum")
    """В том числе НДС"""
    create_date: str | None = _field(default=None, name="createDate")
    """Дата формирования отчёта"""
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    date_from: str | None = _field(default=None, name="dateFrom")
    """Дата начала отчётного периода"""
    date_to: str | None = _field(default=None, name="dateTo")
    """Дата конца отчётного периода"""
    report_id: int | None = _field(default=None, name="reportId")
    """ID отчёта"""
    seller_finance_name: str | None = _field(default=None, name="sellerFinanceName")
    """Наименование продавца"""


class AcquiringReportsDetailedReq(WBModel):
    """Параметры запроса"""

    date_from: str | None = _field(default=None, name="dateFrom")
    """Начальная дата отчёта.Можно передать дату или дату со временем. Время можно указывать с
    точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339, в …
    """
    date_to: str | None = _field(default=None, name="dateTo")
    """Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со временем. Время
    можно указывать с точностью до секунд или миллисекунд.Время передаё …
    """
    fields: list[str] | None = _field(default=None)
    """Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все поля
    """
    limit: int | None = _field(default=None)
    """Количество строк в ответе"""
    rrd_id: int | None = _field(default=None, name="rrdId")
    """ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
    `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
    """


class AcquiringReportsDetailedRes(WBModel):
    """Детализации к отчётам об издержках на приём платежей"""

    acq_date: str | None = _field(default=None, name="acqDate")
    """Дата операции"""
    acquiring_bank: str | None = _field(default=None, name="acquiringBank")
    """Наименование банка-эквайера"""
    acquiring_fee: str | None = _field(default=None, name="acquiringFee")
    """Размер комиссии за эквайринг, в том числе НДС"""
    acquiring_fee_vat: str | None = _field(default=None, name="acquiringFeeVat")
    """Сумма НДС"""
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    doc_type_name: str | None = _field(default=None, name="docTypeName")
    """Тип документа"""
    invoice_date: str | None = _field(default=None, name="invoiceDate")
    """Дата счёта-фактуры"""
    invoice_number: str | None = _field(default=None, name="invoiceNumber")
    """Номер счёта-фактуры"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    report_id: int | None = _field(default=None, name="reportId")
    """ID отчёта"""
    retail_amount: str | None = _field(default=None, name="retailAmount")
    """Вайлдберриз реализовал Товар (Пр)"""
    rrd_id: int | None = _field(default=None, name="rrdId")
    """ID строки"""
    sale_date: str | None = _field(default=None, name="saleDate")
    """Дата продажи"""
    shk_id: int | None = _field(default=None, name="shkId")
    """Штрихкод"""
    srid: str | None = _field(default=None)
    """ID заказа.В ответах методов сборочных заданий FBS, DBW, DBS и Самовывоз `srid` равен `rid`
    """
    tax_registration_reason_code: str | None = _field(default=None, name="taxRegistrationReasonCode")
    """КПП"""
    tin: str | None = _field(default=None)
    """ИНН"""


class FinancialReportsDetailedReportIdReq(WBModel):
    """Параметры запроса"""

    fields: list[str] | None = _field(default=None)
    """Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все поля
    """
    limit: int | None = _field(default=None)
    """Количество строк в ответе"""
    rrd_id: int | None = _field(default=None, name="rrdId")
    """ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
    `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
    """


class GetAccountBalanceResponse(WBModel):
    currency: str | None = _field(default=None)
    """Валюта"""
    current: float | None = _field(default=None)
    """Текущий баланс продавца"""
    for_withdraw: float | None = _field(default=None)
    """Сумма, доступная к выводу"""


class GetCategories(WBModel):
    data: GetCategoriesData | None = _field(default=None)


class GetCategoriesData(WBModel):
    categories: list[GetCategoriesDataCategoriesItem] | None = _field(default=None)
    """Категории документов"""


class GetCategoriesDataCategoriesItem(WBModel):
    name: str | None = _field(default=None)
    """ID категории документа из параметра запроса `category`"""
    title: str | None = _field(default=None)
    """Название категории документа из поля ответа `category`"""


class GetDoc(WBModel):
    data: GetDocData | None = _field(default=None)


class GetDocData(WBModel):
    document: str | None = _field(default=None)
    """Документ в кодировке base64"""
    extension: str | None = _field(default=None)
    """Формат документа"""
    file_name: str | None = _field(default=None, name="fileName")
    """Название документа"""


class GetDocs(WBModel):
    data: GetDocsData | None = _field(default=None)


class GetDocsData(WBModel):
    document: str | None = _field(default=None)
    """Документ в кодировке base64"""
    extension: str | None = _field(default=None)
    """Формат документа"""
    file_name: str | None = _field(default=None, name="fileName")
    """Название документа"""


class GetDocumentsDownloadAllParamsItem(WBModel):
    extension: str | None = _field(default=None)
    """Формат документа"""
    service_name: str | None = _field(default=None, name="serviceName")
    """Уникальный ID документа"""


class GetList(WBModel):
    data: GetListData | None = _field(default=None)


class GetListData(WBModel):
    documents: list[GetListDataDocumentsItem] | None = _field(default=None)
    """Категории документов"""


class GetListDataDocumentsItem(WBModel):
    category: str | None = _field(default=None)
    """Название категории документов из поля ответа `title`"""
    creation_time: str | None = _field(default=None, name="creationTime")
    """Дата и время создания документа"""
    extensions: list[str] | None = _field(default=None)
    """Форматы документа"""
    name: str | None = _field(default=None)
    """Название документа"""
    service_name: str | None = _field(default=None, name="serviceName")
    """Уникальный ID документа"""
    viewed: bool | None = _field(default=None)
    """Выгружен ли документ в личном кабинете"""


class RequestDownload(WBModel):
    params: list[RequestDownloadParamsItem] | None = _field(default=None)
    """Не более 50 элементов, не менее 1 элемент"""


class RequestDownloadParamsItem(WBModel):
    extension: str | None = _field(default=None)
    """Формат документа"""
    service_name: str | None = _field(default=None, name="serviceName")
    """Уникальный ID документа"""


class SalesReportListReq(WBModel):
    """Параметры запроса"""

    date_from: str | None = _field(default=None, name="dateFrom")
    """Начальная дата отчёта.Можно передать дату или дату со временем. Время можно указывать с
    точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339, в …
    """
    date_to: str | None = _field(default=None, name="dateTo")
    """Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со временем. Время
    можно указывать с точностью до секунд или миллисекунд.Время передаё …
    """
    limit: int | None = _field(default=None)
    """Количество отчётов в ответе"""
    offset: int | None = _field(default=None)
    """Сколько элементов пропустить. Например, для значения `10` ответ начнётся с 11 элемента"""
    period: str | None = _field(default=None)
    """Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные"""


class SalesReportListRes(WBModel):
    """Список отчётов реализации"""

    additional_payment_sum: str | None = _field(default=None, name="additionalPaymentSum")
    """Корректировка Вознаграждения Вайлдберриз (ВВ)"""
    avg_sale_percent: float | None = _field(default=None, name="avgSalePercent")
    """Согласованная скидка, %"""
    bank_payment_sum: str | None = _field(default=None, name="bankPaymentSum")
    """Итого к оплате"""
    cashback_amount_sum: str | None = _field(default=None, name="cashbackAmountSum")
    """Сумма, удержанная за начисленные баллы программы лояльности"""
    cashback_commission_change_sum: str | None = _field(default=None, name="cashbackCommissionChangeSum")
    """Стоимость участия в программе лояльности"""
    cashback_discount_sum: str | None = _field(default=None, name="cashbackDiscountSum")
    """Компенсация скидки по программе лояльности"""
    create_date: str | None = _field(default=None, name="createDate")
    """Дата формирования отчёта"""
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    date_from: str | None = _field(default=None, name="dateFrom")
    """Дата начала отчётного периода"""
    date_to: str | None = _field(default=None, name="dateTo")
    """Дата конца отчётного периода"""
    deduction_sum: str | None = _field(default=None, name="deductionSum")
    """Прочие удержания и выплаты"""
    delivery_service_sum: str | None = _field(default=None, name="deliveryServiceSum")
    """Стоимость логистики"""
    for_pay_sum: str | None = _field(default=None, name="forPaySum")
    """К перечислению за товар"""
    paid_acceptance_sum: str | None = _field(default=None, name="paidAcceptanceSum")
    """Стоимость операций при приёмке"""
    paid_storage_sum: str | None = _field(default=None, name="paidStorageSum")
    """Стоимость хранения"""
    payment_schedule: str | None = _field(default=None, name="paymentSchedule")
    """Разовое изменение срока перечисления денежных средств"""
    penalty_sum: str | None = _field(default=None, name="penaltySum")
    """Общая сумма штрафов"""
    report_id: int | None = _field(default=None, name="reportId")
    """ID отчёта"""
    report_type: int | None = _field(default=None, name="reportType")
    """Тип отчёта:   - `1` — основной   - `2` — по выкупам   - `3` — по выкупам для Грузии"""
    retail_amount_sum: str | None = _field(default=None, name="retailAmountSum")
    """Продажа"""
    seller_finance_name: str | None = _field(default=None, name="sellerFinanceName")
    """Наименование продавца"""


class SalesReportsDetailedReq(WBModel):
    """Параметры запроса"""

    date_from: str | None = _field(default=None, name="dateFrom")
    """Начальная дата отчёта.Можно передать дату или дату со временем. Время можно указывать с
    точностью до секунд или миллисекунд.Дата передаётся в формате RFC3339, в …
    """
    date_to: str | None = _field(default=None, name="dateTo")
    """Конечная дата отчёта.Дата в формате RFC3339. Можно передать дату или дату со временем. Время
    можно указывать с точностью до секунд или миллисекунд.Время передаё …
    """
    fields: list[str] | None = _field(default=None)
    """Список полей, которые вернутся в ответе. Если параметр не указан, возвращаются все поля
    """
    limit: int | None = _field(default=None)
    """Количество строк в ответе"""
    period: str | None = _field(default=None)
    """Периодичность отчётов:   - `weekly` — еженедельные   - `daily` — ежедневные"""
    rrd_id: int | None = _field(default=None, name="rrdId")
    """ID строки ответа. Необходим для получения отчёта частями.Начинайте загрузку отчёта с
    `"rrdid":0`. В последующих запросах передавайте значение `rrdId` из последн …
    """


class SalesReportsDetailedRes(WBModel):
    """Детализации к отчётам реализации"""

    acquiring_bank: str | None = _field(default=None, name="acquiringBank")
    """Наименование банка-эквайера"""
    acquiring_fee: str | None = _field(default=None, name="acquiringFee")
    """Компенсация платёжных услуг/Комиссия за интеграцию платёжных сервисов"""
    acquiring_percent: float | None = _field(default=None, name="acquiringPercent")
    """Размер компенсации платёжных услуг/Комиссии за интеграцию платёжных сервисов, %"""
    additional_payment: str | None = _field(default=None, name="additionalPayment")
    """Корректировка Вознаграждения Вайлдберриз (ВВ)"""
    agency_vat: float | None = _field(default=None, name="agencyVat")
    """Удержание Агентского НДС, %.Только для продавцов из Кыргызстана"""
    article_substitution: str | None = _field(default=None, name="articleSubstitution")
    """ID подменного артикула"""
    b2b_customer_tin: str | None = _field(default=None, name="b2bCustomerTin")
    """ИНН B2B-покупателя"""
    bonus_type_name: str | None = _field(default=None, name="bonusTypeName")
    """Виды логистики, штрафов и корректировок ВВ"""
    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    cashback_amount: str | None = _field(default=None, name="cashbackAmount")
    """Сумма, удержанная за начисленные баллы программы лояльности"""
    cashback_commission_change: str | None = _field(default=None, name="cashbackCommissionChange")
    """Стоимость участия в программе лояльности"""
    cashback_discount: str | None = _field(default=None, name="cashbackDiscount")
    """Компенсация скидки по программе лояльности"""
    commission_percent: float | None = _field(default=None, name="commissionPercent")
    """Размер кВВ, %"""
    country: str | None = _field(default=None)
    """Страна продажи"""
    create_date: str | None = _field(default=None, name="createDate")
    """Дата формирования отчёта"""
    currency: str | None = _field(default=None)
    """Валюта отчёта"""
    date_from: str | None = _field(default=None, name="dateFrom")
    """Дата начала отчётного периода"""
    date_to: str | None = _field(default=None, name="dateTo")
    """Дата конца отчётного периода"""
    declaration_number: str | None = _field(default=None, name="declarationNumber")
    """Номер таможенной декларации"""
    deduction: str | None = _field(default=None)
    """Удержания"""
    delivery_amount: int | None = _field(default=None, name="deliveryAmount")
    """Количество доставок"""
    delivery_method: str | None = _field(default=None, name="deliveryMethod")
    """Способ продажи и тип товара"""
    delivery_service: str | None = _field(default=None, name="deliveryService")
    """Услуги по доставке товара покупателю"""
    dlv_prc: float | None = _field(default=None, name="dlvPrc")
    """Фиксированный коэффициент склада по поставке"""
    doc_type_name: str | None = _field(default=None, name="docTypeName")
    """Тип документа"""
    fix_tariff_date_from: str | None = _field(default=None, name="fixTariffDateFrom")
    """Дата начала действия фиксации"""
    fix_tariff_date_to: str | None = _field(default=None, name="fixTariffDateTo")
    """Дата конца действия фиксации"""
    for_pay: str | None = _field(default=None, name="forPay")
    """К перечислению продавцу за реализованный товар"""
    gi_box_type_name: str | None = _field(default=None, name="giBoxTypeName")
    """Тип коробов"""
    gi_id: int | None = _field(default=None, name="giId")
    """ID поставки"""
    installment_cofinancing_amount: str | None = _field(default=None, name="installmentCofinancingAmount")
    """Скидка по программе софинансирования"""
    is_b2b: bool | None = _field(default=None, name="isB2b")
    """Признак B2B-продажи"""
    is_kgvp_v2: float | None = _field(default=None, name="isKgvpV2")
    """Размер снижения кВВ из-за акции, %"""
    kiz: str | None = _field(default=None)
    """Код маркировки Честного знака"""
    kvw: float | None = _field(default=None)
    """Итоговый кВВ без НДС, %"""
    kvw_base: float | None = _field(default=None, name="kvwBase")
    """Размер кВВ без НДС, % базовый"""
    loyalty_discount: float | None = _field(default=None, name="loyaltyDiscount")
    """Размер скидки лояльности от продавца, %"""
    loyalty_id: int | None = _field(default=None, name="loyaltyId")
    """ID скидки лояльности от продавца"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    office_name: str | None = _field(default=None, name="officeName")
    """Склад"""
    order_dt: str | None = _field(default=None, name="orderDt")
    """Дата и время заказа"""
    order_id: int | None = _field(default=None, name="orderId")
    """ID сборочного задания"""
    order_uid: str | None = _field(default=None, name="orderUid")
    """ID корзины заказа — транзакции.Заказы в одной корзине покупателя будут иметь одинаковый
    `orderUid`
    """
    paid_acceptance: str | None = _field(default=None, name="paidAcceptance")
    """Операции на приёмке"""
    paid_storage: str | None = _field(default=None, name="paidStorage")
    """Хранение"""
    paid_with_social_certificate: bool | None = _field(default=None, name="paidWithSocialCertificate")
    """Оплата социальным сертификатом"""
    payment_processing: str | None = _field(default=None, name="paymentProcessing")
    """Тип платежа: компенсация платёжных услуг/Комиссия за интеграцию платёжных сервисов"""
    payment_schedule: str | None = _field(default=None, name="paymentSchedule")
    """Разовое изменение срока перечисления денежных средств"""
    penalty: str | None = _field(default=None)
    """Общая сумма штрафов"""
    ppvz_office_id: int | None = _field(default=None, name="ppvzOfficeId")
    """ID офиса доставки"""
    ppvz_office_name: str | None = _field(default=None, name="ppvzOfficeName")
    """Наименование офиса доставки"""
    ppvz_reward: str | None = _field(default=None, name="ppvzReward")
    """Возмещение за выдачу и возврат товаров на ПВЗ"""
    ppvz_sales_commission: str | None = _field(default=None, name="ppvzSalesCommission")
    """Вознаграждение с продаж до вычета услуг поверенного, без НДС"""
    ppvz_supplier_inn: str | None = _field(default=None, name="ppvzSupplierInn")
    """ИНН партнёра"""
    ppvz_supplier_name: str | None = _field(default=None, name="ppvzSupplierName")
    """Партнёр"""
    product_discount_for_report: float | None = _field(default=None, name="productDiscountForReport")
    """Итоговая согласованная скидка, %"""
    quantity: int | None = _field(default=None)
    """Количество"""
    rebill_logistic_cost: str | None = _field(default=None, name="rebillLogisticCost")
    """Возмещение издержек по перевозке/по складским операциям с товаром"""
    rebill_logistic_org: str | None = _field(default=None, name="rebillLogisticOrg")
    """Организатор перевозки"""
    report_id: int | None = _field(default=None, name="reportId")
    """ID отчёта"""
    report_type: int | None = _field(default=None, name="reportType")
    """Тип отчёта:   - `1` — основной   - `2` — по выкупам   - `3` — по выкупам для Грузии"""
    retail_amount: str | None = _field(default=None, name="retailAmount")
    """Вайлдберриз реализовал Товар (Пр)"""
    retail_price: str | None = _field(default=None, name="retailPrice")
    """Цена розничная"""
    retail_price_with_disc: str | None = _field(default=None, name="retailPriceWithDisc")
    """Цена розничная с учётом согласованной скидки"""
    return_amount: int | None = _field(default=None, name="returnAmount")
    """Количество возврата"""
    rr_date: str | None = _field(default=None, name="rrDate")
    """Дата операции"""
    rrd_id: int | None = _field(default=None, name="rrdId")
    """ID строки"""
    sale_dt: str | None = _field(default=None, name="saleDt")
    """Дата и время продажи"""
    sale_percent: int | None = _field(default=None, name="salePercent")
    """Согласованный продуктовый дисконт, %"""
    sale_price_affiliated_discount_prc: float | None = _field(
        default=None, name="salePriceAffiliatedDiscountPrc"
    )
    """Скидка по подменному артикулу, %"""
    sale_price_promocode_discount_prc: float | None = _field(
        default=None, name="salePricePromocodeDiscountPrc"
    )
    """Скидка за промокод, %"""
    sale_price_wholesale_discount_prc: float | None = _field(
        default=None, name="salePriceWholesaleDiscountPrc"
    )
    """Оптовая скидка для бизнеса, %"""
    seller_oper_name: str | None = _field(default=None, name="sellerOperName")
    """Обоснование для оплаты"""
    seller_promo: str | None = _field(default=None, name="sellerPromo")
    """Промокод, %"""
    seller_promo_discount: float | None = _field(default=None, name="sellerPromoDiscount")
    """Размер дополнительной скидки по собственной акции продавца, %"""
    seller_promo_id: int | None = _field(default=None, name="sellerPromoId")
    """ID собственной акции продавца с дополнительной скидкой"""
    shk_id: int | None = _field(default=None, name="shkId")
    """Штрихкод"""
    sku: str | None = _field(default=None)
    """Баркод"""
    spp: float | None = _field(default=None)
    """Платформенные скидки, %"""
    srid: str | None = _field(default=None)
    """ID заказа.В ответах методов сборочных заданий FBS, DBW, DBS и Самовывоз `srid` равен `rid`
    """
    srv_dbs: bool | None = _field(default=None, name="srvDbs")
    """Признак услуги платной доставки"""
    sticker_id: str | None = _field(default=None, name="stickerId")
    """Стикер МП"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Предмет"""
    sup_rating_up: float | None = _field(default=None, name="supRatingUp")
    """Размер снижения кВВ из-за рейтинга, %"""
    tech_size: str | None = _field(default=None, name="techSize")
    """Размер"""
    title: str | None = _field(default=None)
    """Название товара"""
    trbx_id: str | None = _field(default=None, name="trbxId")
    """ID короба для обработки товара"""
    uuid_promocode: str | None = _field(default=None, name="uuidPromocode")
    """ID промокода"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""
    vw: str | None = _field(default=None)
    """Вознаграждение Вайлдберриз (ВВ), без НДС"""
    vw_nds: str | None = _field(default=None, name="vwNds")
    """НДС с вознаграждения Вайлдберриз"""
    warehouse_logistics_coeff: float | None = _field(default=None, name="warehouseLogisticsCoeff")
    """Коэффициент логистики"""
    wibes_discount_percent: float | None = _field(default=None, name="wibesDiscountPercent")
    """Скидка Wibes, %"""
