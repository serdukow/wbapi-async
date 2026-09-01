# @generated
# This file was auto-generated. Do not edit by hand.

from __future__ import annotations

from msgspec import field as _field

from ..client.model import WBModel


class Fee(WBModel):
    report: list[FeeReportItem] | None = _field(default=None)
    """Список комиссий"""


class FeeReportItem(WBModel):
    kgvp_booking: float | None = _field(default=None, name="kgvpBooking")
    """Комиссия по модели **Бронирование**, %"""
    kgvp_marketplace: float | None = _field(default=None, name="kgvpMarketplace")
    """Комиссия по модели **Маркетплейс** (`FBS`), %"""
    kgvp_pickup: float | None = _field(default=None, name="kgvpPickup")
    """Комиссия по модели **Самовывоз из магазина продавца** (`C&C`), %"""
    kgvp_supplier: float | None = _field(default=None, name="kgvpSupplier")
    """Комиссия по моделям **Витрина** (`DBS`) и **Курьер WB** (`DBW`), %"""
    kgvp_supplier_express: float | None = _field(default=None, name="kgvpSupplierExpress")
    """Комиссия по модели **Витрина экспресс** (`EDBS`), %"""
    paid_storage_kgvp: float | None = _field(default=None, name="paidStorageKgvp")
    """Комиссия по модели **Склад WB** (`FBW`), %"""
    parent_id: int | None = _field(default=None, name="parentID")
    """ID родительской категории"""
    parent_name: str | None = _field(default=None, name="parentName")
    """Название родительской категории"""
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""


class ModelsAcceptanceCoefficient(WBModel):
    allow_unload: bool | None = _field(default=None, name="allowUnload")
    """Доступность приёмки для поставок данного типа, смотри значение поля `boxTypeID`:   - `true`
    — приёмка доступна  - `false` — приёмка не доступна
    """
    box_type_id: int | None = _field(default=None, name="boxTypeID")
    """ID типа поставки:   - `2` — Короба   - `5` — Монопаллеты   - `6` — Суперсейф Для типа
    поставки **QR-поставка с коробами** поле не возвращается
    """
    coefficient: float | None = _field(default=None)
    """Коэффициент приёмки:   - `-1` — приёмка недоступна, вне зависимости от значения поля
    `allowUnload`   - `0` — бесплатная приёмка …
    """
    date: str | None = _field(default=None)
    """Дата начала действия коэффициента"""
    delivery_additional_liter: str | None = _field(default=None, name="deliveryAdditionalLiter")
    """Стоимость логистики каждого следующего литра"""
    delivery_base_liter: str | None = _field(default=None, name="deliveryBaseLiter")
    """Стоимость логистики первого литра"""
    delivery_coef: str | None = _field(default=None, name="deliveryCoef")
    """Коэффициент логистики"""
    is_sorting_center: bool | None = _field(default=None, name="isSortingCenter")
    """Тип склада:   - `true` — сортировочный центр (СЦ)  - `false` — обычный"""
    storage_additional_liter: str | None = _field(default=None, name="storageAdditionalLiter")
    """Стоимость хранения каждого последующего литра: …"""
    storage_base_liter: str | None = _field(default=None, name="storageBaseLiter")
    """Стоимость хранения:   - для паллет — стоимость за одну паллету   - для коробов — стоимость
    хранения за первый литр
    """
    storage_coef: str | None = _field(default=None, name="storageCoef")
    """Коэффициент хранения"""
    warehouse_id: int | None = _field(default=None, name="warehouseID")
    """ID склада. По нему можно получить информацию о складе"""
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Название склада"""


class ModelsRatesBoxResponse(WBModel):
    data: ModelsWarehousesBoxRates | None = _field(default=None)


class ModelsRatesPalletResponse(WBModel):
    data: ModelsWarehousesPalletRates | None = _field(default=None)


class ModelsReturnRatesResponse(WBModel):
    data: ModelsWarehousesReturnRates | None = _field(default=None)


class ModelsWarehouseBoxRates(WBModel):
    box_delivery_base: str | None = _field(default=None, name="boxDeliveryBase")
    """Логистика, первый литр, ₽"""
    box_delivery_coef_expr: str | None = _field(default=None, name="boxDeliveryCoefExpr")
    """Коэффициент **Логистика**, %. На него умножается стоимость логистики. Уже учтён в тарифах
    """
    box_delivery_liter: str | None = _field(default=None, name="boxDeliveryLiter")
    """Логистика, дополнительный литр, ₽"""
    box_delivery_marketplace_base: str | None = _field(default=None, name="boxDeliveryMarketplaceBase")
    """Логистика FBS, первый литр, ₽"""
    box_delivery_marketplace_coef_expr: str | None = _field(
        default=None, name="boxDeliveryMarketplaceCoefExpr"
    )
    """Коэффициент **FBS**, %. На него умножается стоимость логистики FBS. Уже учтён в тарифах
    """
    box_delivery_marketplace_liter: str | None = _field(default=None, name="boxDeliveryMarketplaceLiter")
    """Логистика FBS, дополнительный литр, ₽"""
    box_storage_base: str | None = _field(default=None, name="boxStorageBase")
    """Хранение в день, первый литр, ₽"""
    box_storage_coef_expr: str | None = _field(default=None, name="boxStorageCoefExpr")
    """Коэффициент **Хранение**, %. На него умножается стоимость хранения в день. Уже учтён
    в тарифах
    """
    box_storage_liter: str | None = _field(default=None, name="boxStorageLiter")
    """Хранение в день, дополнительный литр, ₽"""
    geo_name: str | None = _field(default=None, name="geoName")
    """Местонахождение склада"""
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Название склада"""


class ModelsWarehousePalletRates(WBModel):
    pallet_delivery_expr: str | None = _field(default=None, name="palletDeliveryExpr")
    """Коэффициент доставки, %. На него умножается стоимость доставки. Во всех тарифах этот
    коэффициент уже учтён
    """
    pallet_delivery_value_base: str | None = _field(default=None, name="palletDeliveryValueBase")
    """Доставка 1 литра, ₽"""
    pallet_delivery_value_liter: str | None = _field(default=None, name="palletDeliveryValueLiter")
    """Доставка каждого дополнительного литра, ₽"""
    pallet_storage_expr: str | None = _field(default=None, name="palletStorageExpr")
    """Коэффициент хранения, %. На него умножается стоимость хранения. Во всех тарифах этот
    коэффициент уже учтён
    """
    pallet_storage_value_expr: str | None = _field(default=None, name="palletStorageValueExpr")
    """Хранение 1 монопаллеты, ₽"""
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Название склада"""


class ModelsWarehouseReturnRates(WBModel):
    delivery_dump_kgt_office_base: str | None = _field(default=None, name="deliveryDumpKgtOfficeBase")
    """**Стоимость возврата при грузовой доставке, доставка на ПВЗ (базовая цена за 1 л), ₽**
    Применяется для крупногабаритных товаров, когда: …
    """
    delivery_dump_kgt_office_liter: str | None = _field(default=None, name="deliveryDumpKgtOfficeLiter")
    """**Стоимость возврата при грузовой доставке, доставка на ПВЗ (доп. литр), ₽** Стоимость
    за каждый дополнительный литр.
    """
    delivery_dump_kgt_return_expr: str | None = _field(default=None, name="deliveryDumpKgtReturnExpr")
    """**Стоимость возврата при грузовой доставке, обратная логистика невостребованного
    возврата, ₽** …
    """
    delivery_dump_srg_office_expr: str | None = _field(default=None, name="deliveryDumpSrgOfficeExpr")
    """**Стоимость возврата неопознанного складом товара за каждую единицу, доставка на ПВЗ, ₽**
    Применяется для товаров, которые не смогли принять на складе.
    """
    delivery_dump_srg_return_expr: str | None = _field(default=None, name="deliveryDumpSrgReturnExpr")
    """**Стоимость возврата неопознанного складом товара за каждую единицу, обратная логистика
    невостребованного возврата, ₽** Доставка невостребованного возврата обра …
    """
    delivery_dump_sup_courier_base: str | None = _field(default=None, name="deliveryDumpSupCourierBase")
    """**Стоимость возврата, доставка курьером (базовая цена за 1 л), ₽**  Применяется, когда:   -
    продавец хочет вывезти товары со склада Wildberries …
    """
    delivery_dump_sup_courier_liter: str | None = _field(default=None, name="deliveryDumpSupCourierLiter")
    """**Стоимость возврата, доставка курьером (доп. л), ₽** Стоимость за каждый дополнительный
    литр.
    """
    delivery_dump_sup_office_base: str | None = _field(default=None, name="deliveryDumpSupOfficeBase")
    """**Стоимость возврата, доставка на ПВЗ (базовая цена за 1 л), ₽**  Применяется, когда:   -
    продавец хочет вывезти товары со склада Wildberries …
    """
    delivery_dump_sup_office_liter: str | None = _field(default=None, name="deliveryDumpSupOfficeLiter")
    """**Стоимость возврата, доставка на ПВЗ (доп. литр), ₽** Стоимость за каждый дополнительный
    литр
    """
    delivery_dump_sup_return_expr: str | None = _field(default=None, name="deliveryDumpSupReturnExpr")
    """**Стоимость возврата, обратная логистика невостребованного возврата, за единицу товара, ₽**
    Доставка невостребованного возврата обратно на склад Wildberries. …
    """
    warehouse_name: str | None = _field(default=None, name="warehouseName")
    """Название склада"""


class ModelsWarehousesBoxRates(WBModel):
    currency: str | None = _field(default=None)
    """Валюта тарифов"""
    dt_next_box: str | None = _field(default=None, name="dtNextBox")
    """Дата начала следующего тарифа"""
    dt_till_max: str | None = _field(default=None, name="dtTillMax")
    """Дата окончания последнего установленного тарифа"""
    warehouse_list: list[ModelsWarehouseBoxRates] | None = _field(default=None, name="warehouseList")
    """Тарифы для коробов, сгруппированные по складам"""


class ModelsWarehousesPalletRates(WBModel):
    currency: str | None = _field(default=None)
    """Валюта тарифов"""
    dt_next_pallet: str | None = _field(default=None, name="dtNextPallet")
    """Дата начала следующего тарифа"""
    dt_till_max: str | None = _field(default=None, name="dtTillMax")
    """Дата окончания последнего установленного тарифа"""
    warehouse_list: list[ModelsWarehousePalletRates] | None = _field(default=None, name="warehouseList")
    """Тарифы для монопаллет, сгруппированные по складам"""


class ModelsWarehousesReturnRates(WBModel):
    currency: str | None = _field(default=None)
    """Валюта тарифов"""
    dt_next_delivery_dump_kgt: str | None = _field(default=None, name="dtNextDeliveryDumpKgt")
    """Дата начала следующего тарифа при грузовой доставке"""
    dt_next_delivery_dump_srg: str | None = _field(default=None, name="dtNextDeliveryDumpSrg")
    """Дата начала следующего тарифа для неопознанных товаров"""
    dt_next_delivery_dump_sup: str | None = _field(default=None, name="dtNextDeliveryDumpSup")
    """Дата начала следующего тарифа при обычной доставке"""
    warehouse_list: list[ModelsWarehouseReturnRates] | None = _field(default=None, name="warehouseList")
    """Тарифы на возврат, сгруппированные по складам:   - стоимость возврата брака и возврата по
    инициативе продавца при грузовой доставке. …
    """


class RatesBoxResponse(WBModel):
    response: ModelsRatesBoxResponse | None = _field(default=None)


class RatesPalletResponse(WBModel):
    response: ModelsRatesPalletResponse | None = _field(default=None)


class ReturnRatesResponse(WBModel):
    response: ModelsReturnRatesResponse | None = _field(default=None)
