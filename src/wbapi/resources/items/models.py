from __future__ import annotations

from typing import Any

from msgspec import field as _field

from ...client.model import WBModel


class BrandsResponse(WBModel):
    brands: list[BrandsResponseBrandsItem] | None = _field(default=None)
    next: int | None = _field(default=None)
    """Параметр пагинации. Укажите это значение в запросе, чтобы получить следующий пакет данных.
    Если поле отсутствует, вы получили все данные
    """
    total: int | None = _field(default=None)
    """Общее количество брендов предмета"""


class BrandsResponseBrandsItem(WBModel):
    id: int | None = _field(default=None)
    """ID бренда"""
    logo_url: str | None = _field(default=None, name="logoUrl")
    """URL логотипа бренда"""
    name: str | None = _field(default=None)
    """Название бренда"""


class ContentV1RecommendationsSetUpdateRecListItem(WBModel):
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    recommendations: list[ContentV1RecommendationsSetUpdateRecListItemRecommendationsItem] | None = _field(
        default=None
    )
    """Рекомендуемые товары.  Укажите `recomNm` товаров, чтобы добавить их в рекомендации к
    указанному `nmId`. …
    """


class ContentV1RecommendationsSetUpdateRecListItemRecommendationsItem(WBModel):
    recom_nm: int | None = _field(default=None, name="recomNm")
    """Артикул WB рекомендуемого товара"""
    sort: int | None = _field(default=None)
    """Позиция товара в списке рекомендаций.   Допустимые значения:  - `1`–`20` — фиксированная
    позиция: …
    """


class ContentV2BarcodesCreateBody(WBModel):
    count: int | None = _field(default=None)
    """Кол-во баркодов которые надо сгенерировать, максимальное доступное количество баркодов для
    генерации - `5 000`
    """


class ContentV2BarcodesCreateResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: list[str] | None = _field(default=None)
    """Массив сгенерированных баркодов"""
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2CardsDeleteTrashCreateBody(WBModel):
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Артикулы WB"""


class ContentV2CardsDeleteTrashCreateResponse(WBModel):
    additional_errors: dict[str, Any] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: dict[str, Any] | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2CardsLimitsResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: ContentV2CardsLimitsResponseData | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2CardsLimitsResponseData(WBModel):
    free_limits: int | None = _field(default=None, name="freeLimits")
    """Количество бесплатных лимитов"""
    paid_limits: int | None = _field(default=None, name="paidLimits")
    """Количество оплаченных лимитов"""


class ContentV2CardsRecoverCreateBody(WBModel):
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """Артикулы WB"""


class ContentV2CardsRecoverCreateResponse(WBModel):
    additional_errors: dict[str, Any] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: dict[str, Any] | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2CardsUpdateCreateBodyItem(WBModel):
    brand: str | None = _field(default=None)
    """Бренд"""
    characteristics: list[ContentV2CardsUpdateCreateBodyItemCharacteristicsItem] | None = _field(default=None)
    """Характеристики товара.  Можно получить методом Характеристики предмета"""
    description: str | None = _field(default=None)
    """Описание товара. Максимальное количество символов зависит от категории товара Стандарт —
    2000, минимум — 1000, максимум — 5000 …
    """
    dimensions: ContentV2CardsUpdateCreateBodyItemDimensions | None = _field(default=None)
    """Габариты и вес товара **c упаковкой**. Укажите в `сантиметрах` и `килограммах` для любого
    товара. …
    """
    kiz_marked: bool | None = _field(default=None, name="kizMarked")
    """Подтверждение, что на товар нанесён обязательный код маркировки Честного знака: …"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    sizes: list[ContentV2CardsUpdateCreateBodyItemSizesItem] | None = _field(default=None)
    """Массив размеров Для безразмерного товара всё равно нужно передавать данный массив без
    параметров (wbSize и techSize), но с баркодом
    """
    title: str | None = _field(default=None)
    """Наименование товара"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class ContentV2CardsUpdateCreateBodyItemCharacteristicsItem(WBModel):
    id: int | None = _field(default=None)
    """ID характеристики"""
    value: Any | None = _field(default=None)
    """Значения характеристики.  Тип данных — массив строк или число — зависит от типа
    характеристики, см. описание поля `charcType` в методе Характеристики предмета. …
    """


class ContentV2CardsUpdateCreateBodyItemDimensions(WBModel):
    """Габариты и вес товара **c упаковкой**.<br>"""

    height: int | None = _field(default=None)
    """Высота, см"""
    length: int | None = _field(default=None)
    """Длина, см"""
    weight_brutto: float | None = _field(default=None, name="weightBrutto")
    """Вес, кгКоличество знаков после запятой <=3"""
    width: int | None = _field(default=None)
    """Ширина, см"""


class ContentV2CardsUpdateCreateBodyItemSizesItem(WBModel):
    chrt_id: int | None = _field(default=None, name="chrtID")
    """ID размера для данного артикула WB Обязателен к заполнению для существующих размеров Для
    добавляемых размеров не указывается
    """
    price: int | None = _field(default=None)
    """Цена товара, ₽ Указывается при добавлении размера"""
    skus: list[Any] | None = _field(default=None)
    """Баркоды"""
    tech_size: str | None = _field(default=None, name="techSize")
    """Размер товара (например, XL, S, 45)"""
    wb_size: str | None = _field(default=None, name="wbSize")
    """Российский размер товара"""


class ContentV2CardsUploadAddCreateBody(WBModel):
    cards_to_add: list[ContentV2CardsUploadAddCreateBodyCardsToAddItem] | None = _field(
        default=None, name="cardsToAdd"
    )
    """Добавляемые карточки товаров"""
    imt_id: int | None = _field(default=None, name="imtID")
    """`imtID` отдельной карточки товара или группы объединённых карточек товаров, к которой
    присоединяются создаваемые карточки
    """


class ContentV2CardsUploadAddCreateBodyCardsToAddItem(WBModel):
    brand: str | None = _field(default=None)
    """Бренд"""
    characteristics: list[ContentV2CardsUploadAddCreateBodyCardsToAddItemCharacteristicsItem] | None = _field(
        default=None
    )
    """Характеристики товара.  Можно получить методом Характеристики предмета"""
    description: str | None = _field(default=None)
    """Описание товара. Максимальное количество символов зависит от категории товара Стандарт —
    2000, минимум — 1000, максимум — 5000 …
    """
    dimensions: ContentV2CardsUploadAddCreateBodyCardsToAddItemDimensions | None = _field(default=None)
    """Габариты и вес товара **c упаковкой**. Укажите в `сантиметрах` и `килограммах` для любого
    товара. …
    """
    kiz_marked: bool | None = _field(default=None, name="kizMarked")
    """Подтверждение, что на товар нанесён обязательный код маркировки Честного знака: …"""
    sizes: list[ContentV2CardsUploadAddCreateBodyCardsToAddItemSizesItem] | None = _field(default=None)
    """Массив размеров. Если не указать для размерного товара (обувь, одежда и др.), сгенерируется
    автоматически с `techSize` = "A", `wbSize` = "1" и баркодом
    """
    title: str | None = _field(default=None)
    """Наименование товара"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""
    wholesale: ContentV2CardsUploadAddCreateBodyCardsToAddItemWholesale | None = _field(default=None)
    """Оптовая продажа"""


class ContentV2CardsUploadAddCreateBodyCardsToAddItemCharacteristicsItem(WBModel):
    id: Any | None = _field(default=None)
    """ID характеристики"""
    value: Any | None = _field(default=None)
    """Значения характеристики.  Тип данных — массив строк или число — зависит от типа
    характеристики, см. описание поля `charcType` в методе Характеристики предмета. …
    """


class ContentV2CardsUploadAddCreateBodyCardsToAddItemDimensions(WBModel):
    """Габариты и вес товара **c упаковкой**.<br>"""

    height: Any | None = _field(default=None)
    """Высота, см"""
    length: Any | None = _field(default=None)
    """Длина, см"""
    weight_brutto: Any | None = _field(default=None, name="weightBrutto")
    """Вес, кгКоличество знаков после запятой <=3"""
    width: Any | None = _field(default=None)
    """Ширина, см"""


class ContentV2CardsUploadAddCreateBodyCardsToAddItemSizesItem(WBModel):
    price: Any | None = _field(default=None)
    """Цена товара"""
    skus: Any | None = _field(default=None)
    """Баркод. Если не указать, сгенерируется автоматически"""
    tech_size: Any | None = _field(default=None, name="techSize")
    """Размер товара (например, XL, 45)"""
    wb_size: Any | None = _field(default=None, name="wbSize")
    """Российский размер товара"""


class ContentV2CardsUploadAddCreateBodyCardsToAddItemWholesale(WBModel):
    """Оптовая продажа"""

    enabled: Any | None = _field(default=None)
    """Предназначена ли карточка товара для оптовой продажи"""
    quantum: Any | None = _field(default=None)
    """Количество единиц товара в упаковке"""


class ContentV2CardsUploadAddCreateCardsToAddItem(WBModel):
    brand: str | None = _field(default=None)
    """Бренд"""
    characteristics: list[ContentV2CardsUploadAddCreateCardsToAddItemCharacteristicsItem] | None = _field(
        default=None
    )
    """Характеристики товара.  Можно получить методом Характеристики предмета"""
    description: str | None = _field(default=None)
    """Описание товара. Максимальное количество символов зависит от категории товара Стандарт —
    2000, минимум — 1000, максимум — 5000 …
    """
    dimensions: ContentV2CardsUploadAddCreateCardsToAddItemDimensions | None = _field(default=None)
    """Габариты и вес товара **c упаковкой**. Укажите в `сантиметрах` и `килограммах` для любого
    товара. …
    """
    kiz_marked: bool | None = _field(default=None, name="kizMarked")
    """Подтверждение, что на товар нанесён обязательный код маркировки Честного знака: …"""
    sizes: list[ContentV2CardsUploadAddCreateCardsToAddItemSizesItem] | None = _field(default=None)
    """Массив размеров. Если не указать для размерного товара (обувь, одежда и др.), сгенерируется
    автоматически с `techSize` = "A", `wbSize` = "1" и баркодом
    """
    title: str | None = _field(default=None)
    """Наименование товара"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""
    wholesale: ContentV2CardsUploadAddCreateCardsToAddItemWholesale | None = _field(default=None)
    """Оптовая продажа"""


class ContentV2CardsUploadAddCreateCardsToAddItemCharacteristicsItem(WBModel):
    id: int | None = _field(default=None)
    """ID характеристики"""
    value: Any | None = _field(default=None)
    """Значения характеристики.  Тип данных — массив строк или число — зависит от типа
    характеристики, см. описание поля `charcType` в методе Характеристики предмета. …
    """


class ContentV2CardsUploadAddCreateCardsToAddItemDimensions(WBModel):
    """Габариты и вес товара **c упаковкой**.<br>"""

    height: int | None = _field(default=None)
    """Высота, см"""
    length: int | None = _field(default=None)
    """Длина, см"""
    weight_brutto: float | None = _field(default=None, name="weightBrutto")
    """Вес, кгКоличество знаков после запятой <=3"""
    width: int | None = _field(default=None)
    """Ширина, см"""


class ContentV2CardsUploadAddCreateCardsToAddItemSizesItem(WBModel):
    price: int | None = _field(default=None)
    """Цена товара"""
    skus: list[Any] | None = _field(default=None)
    """Баркод. Если не указать, сгенерируется автоматически"""
    tech_size: str | None = _field(default=None, name="techSize")
    """Размер товара (например, XL, 45)"""
    wb_size: str | None = _field(default=None, name="wbSize")
    """Российский размер товара"""


class ContentV2CardsUploadAddCreateCardsToAddItemWholesale(WBModel):
    """Оптовая продажа"""

    enabled: bool | None = _field(default=None)
    """Предназначена ли карточка товара для оптовой продажи"""
    quantum: float | None = _field(default=None)
    """Количество единиц товара в упаковке"""


class ContentV2CardsUploadCreateBodyItem(WBModel):
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    variants: list[ContentV2CardsUploadCreateBodyItemVariantsItem] | None = _field(default=None)
    """Объединённые карточки товаров.Чтобы создать отдельную карточку, передайте только один объект
    """


class ContentV2CardsUploadCreateBodyItemVariantsItem(WBModel):
    brand: str | None = _field(default=None)
    """Бренд"""
    characteristics: list[Any] | None = _field(default=None)
    """Характеристики товара.  Можно получить методом Характеристики предмета"""
    description: str | None = _field(default=None)
    """Описание товара. Максимальное количество символов зависит от категории товара Стандарт —
    2000, минимум — 1000, максимум — 5000 …
    """
    dimensions: ContentV2CardsUploadCreateBodyItemVariantsItemDimensions | None = _field(default=None)
    """Габариты и вес товара **c упаковкой**. Укажите в `сантиметрах` и `килограммах` для любого
    товара. …
    """
    kiz_marked: bool | None = _field(default=None, name="kizMarked")
    """Подтверждение, что на товар нанесён обязательный код маркировки Честного знака: …"""
    sizes: list[Any] | None = _field(default=None)
    """Массив размеров. Если не указать для размерного товара (обувь, одежда и др.), сгенерируется
    автоматически с `techSize` = "A", `wbSize` = "1" и баркодом
    """
    title: str | None = _field(default=None)
    """Наименование товара"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""
    wholesale: ContentV2CardsUploadCreateBodyItemVariantsItemWholesale | None = _field(default=None)
    """Оптовая продажа"""


class ContentV2CardsUploadCreateBodyItemVariantsItemDimensions(WBModel):
    """Габариты и вес товара **c упаковкой**.<br>"""

    height: Any | None = _field(default=None)
    """Высота, см"""
    length: Any | None = _field(default=None)
    """Длина, см"""
    weight_brutto: Any | None = _field(default=None, name="weightBrutto")
    """Вес, кгКоличество знаков после запятой <=3"""
    width: Any | None = _field(default=None)
    """Ширина, см"""


class ContentV2CardsUploadCreateBodyItemVariantsItemWholesale(WBModel):
    """Оптовая продажа"""

    enabled: Any | None = _field(default=None)
    """Предназначена ли карточка товара для оптовой продажи"""
    quantum: Any | None = _field(default=None)
    """Количество единиц товара в упаковке"""


class ContentV2DirectoryColorsResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: Any | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2DirectoryCountriesResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: Any | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2DirectoryKindsResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: list[str] | None = _field(default=None)
    """Массив значений для хар-ки Пол"""
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2DirectorySeasonsResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: list[str] | None = _field(default=None)
    """Массив значений для хар-ки Сезон"""
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2DirectoryTnvedResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: list[ContentV2DirectoryTnvedResponseDataItem] | None = _field(default=None)
    """Данные"""
    error: bool | None = _field(default=None)
    """Флаг наличия ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Текст ошибки"""


class ContentV2DirectoryTnvedResponseDataItem(WBModel):
    is_kiz: bool | None = _field(default=None, name="isKiz")
    """- `true` — код маркировки Честного знака требуется - `false` — код маркировки Честного знака
    не требуется
    """
    tnved: str | None = _field(default=None)
    """ТНВЭД-код"""


class ContentV2DirectoryVatResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: list[str] | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг наличия ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Текст ошибки"""


class ContentV2GetCardsListBody(WBModel):
    settings: ContentV2GetCardsListBodySettings | None = _field(default=None)
    """Настройки"""


class ContentV2GetCardsListBodySettings(WBModel):
    """Настройки"""

    cursor: ContentV2GetCardsListBodySettingsCursor | None = _field(default=None)
    """Курсор"""
    filter: ContentV2GetCardsListBodySettingsFilter | None = _field(default=None)
    """Параметры фильтрации"""
    sort: ContentV2GetCardsListBodySettingsSort | None = _field(default=None)
    """Параметр сортировки"""


class ContentV2GetCardsListBodySettingsCursor(WBModel):
    """Курсор"""

    limit: int | None = _field(default=None)
    """Сколько карточек товаров выдать в ответе"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB, с которого надо запрашивать следующий список карточек товаров"""
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время изменения"""


class ContentV2GetCardsListBodySettingsFilter(WBModel):
    """Параметры фильтрации"""

    allowed_categories_only: bool | None = _field(default=None, name="allowedCategoriesOnly")
    """Фильтр по категории:   - `true` — только разрешённые   - `false` — все    Не используется
    в песочнице
    """
    brands: list[Any] | None = _field(default=None)
    """Поиск по брендам"""
    imt_id: int | None = _field(default=None, name="imtID")
    """Поиск по ID для объединённых карточек товаров"""
    object_ids: list[Any] | None = _field(default=None, name="objectIDs")
    """Поиск по ID предметов"""
    tag_ids: list[Any] | None = _field(default=None, name="tagIDs")
    """Поиск по ID ярлыков"""
    text_search: str | None = _field(default=None, name="textSearch")
    """Поиск по артикулу продавца, артикулу WB, баркоду"""
    with_photo: int | None = _field(default=None, name="withPhoto")
    """Фильтр по фото:   * `-1` — любые карточки товаров   * `0` — только карточки без фото. С 16
    июня — любые карточки товаров   * `1` — только карточки с фото …
    """


class ContentV2GetCardsListBodySettingsSort(WBModel):
    """Параметр сортировки"""

    ascending: bool | None = _field(default=None)
    """Сортировать по полю `updatedAt`:   - `false` — по убыванию   -  `true` — по возрастанию
    """


class ContentV2GetCardsListResponse(WBModel):
    cards: list[ContentV2GetCardsListResponseCardsItem] | None = _field(default=None)
    """Список карточек товаров"""
    cursor: ContentV2GetCardsListResponseCursor | None = _field(default=None)
    """Пагинатор"""


class ContentV2GetCardsListResponseCardsItem(WBModel):
    brand: str | None = _field(default=None)
    """Бренд"""
    characteristics: list[ContentV2GetCardsListResponseCardsItemCharacteristicsItem] | None = _field(
        default=None
    )
    """Характеристики"""
    created_at: str | None = _field(default=None, name="createdAt")
    """Дата и время создания"""
    description: str | None = _field(default=None)
    """Описание товара"""
    dimensions: ContentV2GetCardsListResponseCardsItemDimensions | None = _field(default=None)
    """Габариты и вес товара c упаковкой, см и кг"""
    imt_id: int | None = _field(default=None, name="imtID")
    """ID для объединённых карточек товаров.Един для всех артикулов WB группы объединённых
    карточек.У каждой карточки товара есть `imtID`, даже если она не объединена …
    """
    kiz_marked: bool | None = _field(default=None, name="kizMarked")
    """Есть ли подтверждение от продавца, что обязательный код маркировки Честного знака нанесён на
    товар:   - `true` — да   - `false` — нет …
    """
    need_kiz: bool | None = _field(default=None, name="needKiz")
    """Требуется ли код маркировки Честного знака для этого товара:   - `false` — не требуется   -
    `true` — требуется
    """
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    nm_uuid: str | None = _field(default=None, name="nmUUID")
    """Внутренний технический ID карточки товара"""
    photos: list[ContentV2GetCardsListResponseCardsItemPhotosItem] | None = _field(default=None)
    """Массив фото"""
    sizes: list[ContentV2GetCardsListResponseCardsItemSizesItem] | None = _field(default=None)
    """Размеры товара"""
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    tags: list[ContentV2GetCardsListResponseCardsItemTagsItem] | None = _field(default=None)
    """Ярлыки"""
    title: str | None = _field(default=None)
    """Наименование товара"""
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время изменения"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""
    video: str | None = _field(default=None)
    """URL видео"""
    wholesale: ContentV2GetCardsListResponseCardsItemWholesale | None = _field(default=None)
    """Оптовая продажа"""


class ContentV2GetCardsListResponseCardsItemCharacteristicsItem(WBModel):
    id: Any | None = _field(default=None)
    """ID характеристики"""
    name: Any | None = _field(default=None)
    """Название характеристики"""
    value: Any | None = _field(default=None)
    """Значение характеристики. Тип значения зависит от типа характеристики"""


class ContentV2GetCardsListResponseCardsItemDimensions(WBModel):
    """Габариты и вес товара c упаковкой, см и кг"""

    height: Any | None = _field(default=None)
    """Высота, см"""
    is_valid: Any | None = _field(default=None, name="isValid")
    """Потенциальная некорректность габаритов товара: …"""
    length: Any | None = _field(default=None)
    """Длина, см"""
    weight_brutto: Any | None = _field(default=None, name="weightBrutto")
    """Вес, кгКоличество знаков после запятой <=3"""
    width: Any | None = _field(default=None)
    """Ширина, см"""


class ContentV2GetCardsListResponseCardsItemPhotosItem(WBModel):
    big: Any | None = _field(default=None)
    """URL фото `900x1200`"""
    c246x328: Any | None = _field(default=None)
    """URL фото `248x328`"""
    c516x688: Any | None = _field(default=None)
    """URL фото `516x688`"""
    square: Any | None = _field(default=None)
    """URL фото `600x600`"""
    tm: Any | None = _field(default=None)
    """URL фото `75x100`"""


class ContentV2GetCardsListResponseCardsItemSizesItem(WBModel):
    chrt_id: Any | None = _field(default=None, name="chrtID")
    """Числовой ID размера для данного артикула WB"""
    skus: Any | None = _field(default=None)
    """Баркод товара"""
    tech_size: Any | None = _field(default=None, name="techSize")
    """Размер товара (А, XXL, 57 и др.)"""
    wb_size: Any | None = _field(default=None, name="wbSize")
    """Российский размер товара"""


class ContentV2GetCardsListResponseCardsItemTagsItem(WBModel):
    color: Any | None = _field(default=None)
    """Цвет ярлыка. Доступные цвета: - `D1CFD7` — серый - `FEE0E0` — красный - `ECDAFF` —
    фиолетовый - `E4EAFF` — синий - `DEF1DD` — зеленый - `FFECC7` — желтый
    """
    id: Any | None = _field(default=None)
    """ID ярлыка"""
    name: Any | None = _field(default=None)
    """Название ярлыка"""


class ContentV2GetCardsListResponseCardsItemWholesale(WBModel):
    """Оптовая продажа"""

    enabled: Any | None = _field(default=None)
    """Предназначена ли карточка товара для оптовой продажи"""
    quantum: Any | None = _field(default=None)
    """Количество единиц товара в упаковке"""


class ContentV2GetCardsListResponseCursor(WBModel):
    """Пагинатор"""

    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB, с которого надо запрашивать следующий список карточек товаров"""
    total: int | None = _field(default=None)
    """Количество возвращённых карточек товаров"""
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время, с которых надо запрашивать следующий список карточек товаров"""


class ContentV2GetCardsListSettings(WBModel):
    """Настройки"""

    cursor: ContentV2GetCardsListSettingsCursor | None = _field(default=None)
    """Курсор"""
    filter: ContentV2GetCardsListSettingsFilter | None = _field(default=None)
    """Параметры фильтрации"""
    sort: ContentV2GetCardsListSettingsSort | None = _field(default=None)
    """Параметр сортировки"""


class ContentV2GetCardsListSettingsCursor(WBModel):
    """Курсор"""

    limit: int | None = _field(default=None)
    """Сколько карточек товаров выдать в ответе"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB, с которого надо запрашивать следующий список карточек товаров"""
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время изменения"""


class ContentV2GetCardsListSettingsFilter(WBModel):
    """Параметры фильтрации"""

    allowed_categories_only: bool | None = _field(default=None, name="allowedCategoriesOnly")
    """Фильтр по категории:   - `true` — только разрешённые   - `false` — все    Не используется
    в песочнице
    """
    brands: list[str] | None = _field(default=None)
    """Поиск по брендам"""
    imt_id: int | None = _field(default=None, name="imtID")
    """Поиск по ID для объединённых карточек товаров"""
    object_ids: list[int] | None = _field(default=None, name="objectIDs")
    """Поиск по ID предметов"""
    tag_ids: list[int] | None = _field(default=None, name="tagIDs")
    """Поиск по ID ярлыков"""
    text_search: str | None = _field(default=None, name="textSearch")
    """Поиск по артикулу продавца, артикулу WB, баркоду"""
    with_photo: int | None = _field(default=None, name="withPhoto")
    """Фильтр по фото:   * `-1` — любые карточки товаров   * `0` — только карточки без фото. С 16
    июня — любые карточки товаров   * `1` — только карточки с фото …
    """


class ContentV2GetCardsListSettingsSort(WBModel):
    """Параметр сортировки"""

    ascending: bool | None = _field(default=None)
    """Сортировать по полю `updatedAt`:   - `false` — по убыванию   -  `true` — по возрастанию
    """


class ContentV2GetCardsTrashBody(WBModel):
    settings: ContentV2GetCardsTrashBodySettings | None = _field(default=None)
    """Настройки"""


class ContentV2GetCardsTrashBodySettings(WBModel):
    """Настройки"""

    cursor: ContentV2GetCardsTrashBodySettingsCursor | None = _field(default=None)
    """Пагинатор"""
    filter: ContentV2GetCardsTrashBodySettingsFilter | None = _field(default=None)
    """Параметры фильтрации"""
    sort: ContentV2GetCardsTrashBodySettingsSort | None = _field(default=None)
    """Параметр сортировки"""


class ContentV2GetCardsTrashBodySettingsCursor(WBModel):
    """Пагинатор"""

    limit: int | None = _field(default=None)
    """Сколько карточек товаров выдать в ответе"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB, с которого надо запрашивать следующий список карточек товаров"""
    trashed_at: str | None = _field(default=None, name="trashedAt")
    """Дата и время помещения в корзину"""


class ContentV2GetCardsTrashBodySettingsFilter(WBModel):
    """Параметры фильтрации"""

    text_search: str | None = _field(default=None, name="textSearch")
    """Поиск по артикулу продавца, артикулу WB, баркоду"""


class ContentV2GetCardsTrashBodySettingsSort(WBModel):
    """Параметр сортировки"""

    ascending: bool | None = _field(default=None)
    """Сортировать по `trashedAt`:   - `false` — по убыванию   - `true` — по возрастанию"""


class ContentV2GetCardsTrashResponse(WBModel):
    cards: list[ContentV2GetCardsTrashResponseCardsItem] | None = _field(default=None)
    """Массив карточек товаров"""
    cursor: ContentV2GetCardsTrashResponseCursor | None = _field(default=None)
    """Пагинатор"""


class ContentV2GetCardsTrashResponseCardsItem(WBModel):
    characteristics: list[ContentV2GetCardsTrashResponseCardsItemCharacteristicsItem] | None = _field(
        default=None
    )
    """Характеристики"""
    created_at: str | None = _field(default=None, name="createdAt")
    """Date and time the item was listed"""
    dimensions: ContentV2GetCardsTrashResponseCardsItemDimensions | None = _field(default=None)
    """Габариты и вес товара c упаковкой, см и кг"""
    kiz_marked: bool | None = _field(default=None, name="kizMarked")
    """Есть ли подтверждение от продавца, что обязательный код маркировки Честного знака нанесён на
    товар:   - `true` — да   - `false` — нет …
    """
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    photos: list[ContentV2GetCardsTrashResponseCardsItemPhotosItem] | None = _field(default=None)
    """Массив фото"""
    sizes: list[ContentV2GetCardsTrashResponseCardsItemSizesItem] | None = _field(default=None)
    """Массив размеров"""
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    trashed_at: str | None = _field(default=None, name="trashedAt")
    """Дата и время помещения в корзину"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""
    video: str | None = _field(default=None)
    """URL видео"""
    wholesale: ContentV2GetCardsTrashResponseCardsItemWholesale | None = _field(default=None)
    """Оптовая продажа"""


class ContentV2GetCardsTrashResponseCardsItemCharacteristicsItem(WBModel):
    id: Any | None = _field(default=None)
    """ID характеристики"""
    name: Any | None = _field(default=None)
    """Название характеристики"""
    value: Any | None = _field(default=None)
    """Значение характеристики. Тип значения зависит от типа характеристики"""


class ContentV2GetCardsTrashResponseCardsItemDimensions(WBModel):
    """Габариты и вес товара c упаковкой, см и кг"""

    height: Any | None = _field(default=None)
    """Высота, см"""
    is_valid: Any | None = _field(default=None, name="isValid")
    """Потенциальная некорректность габаритов товара: …"""
    length: Any | None = _field(default=None)
    """Длина, см"""
    weight_brutto: Any | None = _field(default=None, name="weightBrutto")
    """Вес, кгКоличество знаков после запятой <=3"""
    width: Any | None = _field(default=None)
    """Ширина, см"""


class ContentV2GetCardsTrashResponseCardsItemPhotosItem(WBModel):
    big: Any | None = _field(default=None)
    """URL фото `900x1200`"""
    c246x328: Any | None = _field(default=None)
    """URL фото `248x328`"""
    c516x688: Any | None = _field(default=None)
    """URL фото `516x688`"""
    square: Any | None = _field(default=None)
    """URL фото `600x600`"""
    tm: Any | None = _field(default=None)
    """URL фото `75x100`"""


class ContentV2GetCardsTrashResponseCardsItemSizesItem(WBModel):
    chrt_id: Any | None = _field(default=None, name="chrtID")
    """ID размера"""
    skus: Any | None = _field(default=None)
    """Массив баркодов"""
    tech_size: Any | None = _field(default=None, name="techSize")
    """Размер товара"""
    wb_size: Any | None = _field(default=None, name="wbSize")
    """Российский размер товара"""


class ContentV2GetCardsTrashResponseCardsItemWholesale(WBModel):
    """Оптовая продажа"""

    enabled: Any | None = _field(default=None)
    """Предназначена ли карточка товара для оптовой продажи"""
    quantum: Any | None = _field(default=None)
    """Количество единиц товара в упаковке"""


class ContentV2GetCardsTrashResponseCursor(WBModel):
    """Пагинатор"""

    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB, с которого надо запрашивать следующий список карточек товаров"""
    total: int | None = _field(default=None)
    """Количество возвращённых карточек товаров"""
    trashed_at: str | None = _field(default=None, name="trashedAt")
    """Дата и время, с которых надо запрашивать следующий список карточек товаров"""


class ContentV2GetCardsTrashSettings(WBModel):
    """Настройки"""

    cursor: ContentV2GetCardsTrashSettingsCursor | None = _field(default=None)
    """Пагинатор"""
    filter: ContentV2GetCardsTrashSettingsFilter | None = _field(default=None)
    """Параметры фильтрации"""
    sort: ContentV2GetCardsTrashSettingsSort | None = _field(default=None)
    """Параметр сортировки"""


class ContentV2GetCardsTrashSettingsCursor(WBModel):
    """Пагинатор"""

    limit: int | None = _field(default=None)
    """Сколько карточек товаров выдать в ответе"""
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB, с которого надо запрашивать следующий список карточек товаров"""
    trashed_at: str | None = _field(default=None, name="trashedAt")
    """Дата и время помещения в корзину"""


class ContentV2GetCardsTrashSettingsFilter(WBModel):
    """Параметры фильтрации"""

    text_search: str | None = _field(default=None, name="textSearch")
    """Поиск по артикулу продавца, артикулу WB, баркоду"""


class ContentV2GetCardsTrashSettingsSort(WBModel):
    """Параметр сортировки"""

    ascending: bool | None = _field(default=None)
    """Сортировать по `trashedAt`:   - `false` — по убыванию   - `true` — по возрастанию"""


class ContentV2ObjectAllResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: list[ContentV2ObjectAllResponseDataItem] | None = _field(default=None)
    """Предметы"""
    error: bool | None = _field(default=None)
    """Флаг наличия ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Текст ошибки"""


class ContentV2ObjectAllResponseDataItem(WBModel):
    parent_id: int | None = _field(default=None, name="parentID")
    """ID родительской категории"""
    parent_name: str | None = _field(default=None, name="parentName")
    """Название родительской категории"""
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""


class ContentV2ObjectCharcsSubjectIdResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: list[ContentV2ObjectCharcsSubjectIdResponseDataItem] | None = _field(default=None)
    """Данные"""
    error: bool | None = _field(default=None)
    """Флаг наличия ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Текст ошибки"""


class ContentV2ObjectCharcsSubjectIdResponseDataItem(WBModel):
    charc_id: int | None = _field(default=None, name="charcID")
    """ID характеристики"""
    charc_type: int | None = _field(default=None, name="charcType")
    """Тип данных характеристики, который необходимо использовать при создании или редактировании
    карточек товаров:   -  `1` — массив строк …
    """
    exist_named_field: bool | None = _field(default=None, name="existNamedField")
    """Как передать характеристику в запросах на cоздание, создание с
    присоединением и редактирование карточек товара: …
    """
    has_filter: bool | None = _field(default=None, name="hasFilter")
    """Ключевая характеристика. Является ли характеристика значимой для покупателей:   - `true` —
    да   - `false` — нет
    """
    is_variable: bool | None = _field(default=None, name="isVariable")
    """Признак меняющейся характеристики. Значение размечает характеристики, по которым варианты
    отличаются друг от друга: …
    """
    max_count: int | None = _field(default=None, name="maxCount")
    """Максимальное количество значений, которое можно присвоить характеристике при создании или
    редактировании карточек товаров. …
    """
    name: str | None = _field(default=None)
    """Название характеристики"""
    popular: bool | None = _field(default=None)
    """Характеристика популярна у пользователей (true - да, false - нет)"""
    required: bool | None = _field(default=None)
    """- `true` — характеристику необходимо обязательно указать в карточке товара - `false` —
    характеристику необязательно указывать
    """
    subject_id: int | None = _field(default=None, name="subjectID")
    """ID предмета"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Название предмета"""
    unit_name: str | None = _field(default=None, name="unitName")
    """Единица измерения"""


class ContentV2ObjectParentAllResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: Any | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг наличия ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2TagCreateBody(WBModel):
    color: str | None = _field(default=None)
    """Цвет ярлыка.  Доступные цвета:   - `D1CFD7` — серый   - `FEE0E0` — красный   - `ECDAFF` —
    фиолетовый   - `E4EAFF` — синий   - `DEF1DD` — зеленый …
    """
    name: str | None = _field(default=None)
    """Имя ярлыка"""


class ContentV2TagIdUpdateBody(WBModel):
    color: str | None = _field(default=None)
    """Цвет ярлыка"""
    name: str | None = _field(default=None)
    """Имя ярлыка"""


class ContentV2TagNomenclatureLinkCreateBody(WBModel):
    nm_id: int | None = _field(default=None, name="nmID")
    """Артикул WB"""
    tags_ids: list[int] | None = _field(default=None, name="tagsIDs")
    """Массив числовых ID ярлыков. Что бы снять ярлыки с карточки товара, необходимо передать
    пустой массив. …
    """


class ContentV2TagsResponse(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: list[ContentV2TagsResponseDataItem] | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV2TagsResponseDataItem(WBModel):
    color: str | None = _field(default=None)
    """Цвет ярлыка"""
    id: int | None = _field(default=None)
    """Числовой ID ярлыка"""
    name: str | None = _field(default=None)
    """Имя ярлыка"""


class ContentV3MediaFileCreateResponse(WBModel):
    additional_errors: dict[str, Any] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: dict[str, Any] | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ContentV3MediaSaveCreateBody(WBModel):
    data: list[str] | None = _field(default=None)
    """Ссылки на изображения в том порядке, в котором они будут в карточке товара, и на видео, на
    любой позиции массива
    """
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""


class ContentV3MediaSaveCreateResponse(WBModel):
    additional_errors: dict[str, Any] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: dict[str, Any] | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class DbwWarehousesWarehouseIdContactsResponse(WBModel):
    """Список контактов склада продавца"""

    contacts: list[DbwWarehousesWarehouseIdContactsResponseContactsItem] | None = _field(default=None)


class DbwWarehousesWarehouseIdContactsResponseContactsItem(WBModel):
    comment: str | None = _field(default=None)
    """Комментарий"""
    phone: str | None = _field(default=None)
    """Номер телефона"""


class DbwWarehousesWarehouseIdContactsUpdateContactsItem(WBModel):
    comment: str | None = _field(default=None)
    """Комментарий"""
    phone: str | None = _field(default=None)
    """Номер телефона.Поддерживаются коды стран:   - `+7` — Россия, Казахстан   - `+374` — Армения
    - `+375` — Беларусь   - `+996` — Кыргызстан
    """


class GetRecomReq(WBModel):
    """Запрос для получения рекомендаций"""

    brand_names: list[str] | None = _field(default=None, name="brandNames")
    """Бренды"""
    limit: int | None = _field(default=None)
    """Количество товаров в ответе"""
    next: int | None = _field(default=None)
    """Курсор. Последний `nmId` в ответе"""
    search: str | None = _field(default=None)
    """Поиск:   - по артикулу WB `nmId` — полное совпадение   - по артикулу продавца `vendorCode` —
    частичное совпадение
    """
    subject_ids: list[int] | None = _field(default=None, name="subjectIds")
    """ID предметов"""


class GetRecomRes(WBModel):
    """Товары с рекомендациями"""

    data: list[GetRecomResDataItem] | None = _field(default=None)
    """Данные о товарах и их рекомендациях"""
    next: int | None = _field(default=None)
    """Курсор. Последний `nmId` в ответе"""


class GetRecomResDataItem(WBModel):
    brand_name: str | None = _field(default=None, name="brandName")
    """Бренд"""
    imt_id: int | None = _field(default=None, name="imtId")
    """ID для объединённых карточек товаров"""
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    pic: str | None = _field(default=None)
    """URL основного изображения в карточке товара"""
    pics_count: int | None = _field(default=None, name="picsCount")
    """Количество изображений в карточке товара"""
    recom_count: int | None = _field(default=None, name="recomCount")
    """Количество рекомендуемых товаров"""
    recom_nms: list[int] | None = _field(default=None, name="recomNms")
    """Список `nmId` рекомендуемых товаров"""
    recom_pics: list[str] | None = _field(default=None, name="recomPics")
    """Список URL основных изображений рекомендуемых товаров"""
    subject_name: str | None = _field(default=None, name="subjectName")
    """Предмет"""
    title: str | None = _field(default=None)
    """Название товара"""
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время последнего обновления рекомендаций"""
    vendor_code: str | None = _field(default=None, name="vendorCode")
    """Артикул продавца"""


class ModelsErrorTableListPublicRespV2(WBModel):
    """Данные ответа"""

    cursor: ViewerContractPublicErrorsCursorOutput | None = _field(default=None)
    items: list[ModelsErrorTableListPublicRespV2Item] | None = _field(default=None)
    """Пакеты данных"""


class ModelsErrorTableListPublicRespV2Item(WBModel):
    batch_uuid: Any | None = _field(default=None, name="batchUUID")
    """ID пакета"""
    brands: Any | None = _field(default=None)
    """Бренды. Разбивка по `vendorCodes`"""
    errors: Any | None = _field(default=None)
    """Ошибки. Разбивка по `vendorCodes`"""
    subjects: Any | None = _field(default=None)
    """Предметы. Разбивка по `vendorCodes`"""
    updated_at: Any | None = _field(default=None, name="updatedAt")
    """Дата и время создания или редактирования пакета"""
    vendor_codes: Any | None = _field(default=None, name="vendorCodes")
    """Артикулы продавца"""


class Office(WBModel):
    """Данные о складе WB"""

    address: str | None = _field(default=None)
    """Адрес"""
    cargo_type: int | None = _field(default=None, name="cargoType")
    """Тип товара, который принимает склад:   - `1` — малогабаритный товар (МГТ)   - `3` —
    крупногабаритный товар (КГТ+)
    """
    city: str | None = _field(default=None)
    """Город"""
    delivery_type: int | None = _field(default=None, name="deliveryType")
    """Тип доставки, который принимает склад:   - `1` — доставка на склад WB (FBS)   - `2` —
    доставка силами продавца (DBS)   - `3` — доставка курьером WB (DBW) …
    """
    federal_district: str | None = _field(default=None, name="federalDistrict")
    """Федеральный округ склада WB. Если `null`, склад находится за пределами РФ или федеральный
    округ не указан
    """
    id: int | None = _field(default=None)
    """ID"""
    latitude: float | None = _field(default=None)
    """Широта"""
    longitude: float | None = _field(default=None)
    """Долгота"""
    name: str | None = _field(default=None)
    """Название"""
    selected: bool | None = _field(default=None)
    """Признак того, что склад уже выбран продавцом"""


class RequestMoveNmsImtConn(WBModel):
    nm_ids: list[int] | None = _field(default=None, name="nmIDs")
    """`nmID`, которые необходимо объединить"""
    target_imt: int | None = _field(default=None, name="targetIMT")
    """Существующий `imtID`, под которым необходимо объединить карточки товаров"""


class RequestPublicViewerPublicErrorsTableListV2(WBModel):
    cursor: SwaggerPublicErrorsCursorInput | None = _field(default=None)
    order: SwaggerPublicErrorsOrderV2 | None = _field(default=None)


class ResponseContentError(WBModel):
    additional_errors: str | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: dict[str, Any] | None = _field(default=None)
    """Данные ошибки"""
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Текст ошибки"""


class ResponseItemList(WBModel):
    additional_errors: ResponseItemListAdditionalErrors | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: dict[str, Any] | None = _field(default=None)
    """Данные ответа"""
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class ResponseItemListAdditionalErrors(WBModel):
    string: str | None = _field(default=None)


class ResponsePublicViewerPublicErrorsTableListV2(WBModel):
    additional_errors: dict[str, Any] | None = _field(default=None, name="additionalErrors")
    """Дополнительные ошибки"""
    data: ModelsErrorTableListPublicRespV2 | None = _field(default=None)
    error: bool | None = _field(default=None)
    """Флаг ошибки"""
    error_text: str | None = _field(default=None, name="errorText")
    """Описание ошибки"""


class SetRecomReq(WBModel):
    """Запрос на добавление или замену рекомендаций"""

    rec_list: list[SetRecomReqRecListItem] | None = _field(default=None, name="recList")
    """Список рекомендаций для товаров"""
    replace: bool | None = _field(default=None)
    """Действие в запросе:   - `false` — добавить новые рекомендации к существующим   - `true` —
    заменить существующие рекомендации новыми
    """


class SetRecomReqRecListItem(WBModel):
    nm_id: int | None = _field(default=None, name="nmId")
    """Артикул WB"""
    recommendations: list[SetRecomReqRecListItemRecommendationsItem] | None = _field(default=None)
    """Рекомендуемые товары.  Укажите `recomNm` товаров, чтобы добавить их в рекомендации к
    указанному `nmId`. …
    """


class SetRecomReqRecListItemRecommendationsItem(WBModel):
    recom_nm: Any | None = _field(default=None, name="recomNm")
    """Артикул WB рекомендуемого товара"""
    sort: Any | None = _field(default=None)
    """Позиция товара в списке рекомендаций.   Допустимые значения:  - `1`–`20` — фиксированная
    позиция: …
    """


class SetRecomRes(WBModel):
    errors: list[SetRecomResErrorsItem] | None = _field(default=None)
    """Ошибки. При `"isError":true`"""
    is_error: bool | None = _field(default=None, name="isError")
    """Есть ли ошибки:   - `false` — ошибок нет. Запрос полностью успешен   - `true` — ошибки есть
    """


class SetRecomResErrorsItem(WBModel):
    """Ошибки установки рекомендаций"""

    main_nm: str | None = _field(default=None, name="mainNm")
    """Значение параметра `nmId`"""
    message: str | None = _field(default=None)
    """Сообщение об ошибке"""
    recom_nm: str | None = _field(default=None, name="recomNm")
    """Значение параметра `recomNm`"""


class StocksWarehouseIdBody(WBModel):
    chrt_ids: list[int] | None = _field(default=None, name="chrtIds")
    """Массив ID размеров товаров"""


class StocksWarehouseIdDeleteBody(WBModel):
    chrt_ids: list[int] | None = _field(default=None, name="chrtIds")
    """Массив ID размеров товаров"""


class StocksWarehouseIdResponse(WBModel):
    stocks: list[StocksWarehouseIdResponseStocksItem] | None = _field(default=None)


class StocksWarehouseIdResponseStocksItem(WBModel):
    amount: int | None = _field(default=None)
    """Остаток"""
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара"""


class StocksWarehouseIdUpdateBody(WBModel):
    stocks: list[StocksWarehouseIdUpdateBodyStocksItem] | None = _field(default=None)
    """Массив ID размеров товаров и их остатков"""


class StocksWarehouseIdUpdateBodyStocksItem(WBModel):
    amount: int | None = _field(default=None)
    """Остаток"""
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара"""


class StocksWarehouseIdUpdateStocksItem(WBModel):
    amount: int | None = _field(default=None)
    """Остаток"""
    chrt_id: int | None = _field(default=None, name="chrtId")
    """ID размера товара"""


class StoreContactRequestBody(WBModel):
    """Контакты склада продавца"""

    contacts: list[StoreContactRequestBodyContactsItem] | None = _field(default=None)


class StoreContactRequestBodyContactsItem(WBModel):
    comment: str | None = _field(default=None)
    """Комментарий"""
    phone: str | None = _field(default=None)
    """Номер телефона.Поддерживаются коды стран:   - `+7` — Россия, Казахстан   - `+374` — Армения
    - `+375` — Беларусь   - `+996` — Кыргызстан
    """


class SwaggerPublicErrorsCursorInput(WBModel):
    """Пагинатор"""

    batch_uuid: str | None = _field(default=None, name="batchUUID")
    """ID последнего пакета в ответе на предыдущий запрос"""
    limit: float | None = _field(default=None)
    """Количество пакетов в ответе"""
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время формирования последнего пакета в ответе на предыдущий запрос"""


class SwaggerPublicErrorsOrderV2(WBModel):
    """Порядок выдачи пакетов"""

    ascending: bool | None = _field(default=None)
    """- `false` — сортировка по убыванию - `true` — сортировка по возрастанию"""


class ViewerContractPublicErrorsCursorOutput(WBModel):
    """Пагинатор"""

    batch_uuid: str | None = _field(default=None, name="batchUUID")
    """ID последнего пакета в ответе"""
    next: bool | None = _field(default=None)
    """Есть ли ещё черновики:   - `false` — нет   - `true` — да"""
    updated_at: str | None = _field(default=None, name="updatedAt")
    """Дата и время формирования последнего пакета в ответе"""


class Warehouse(WBModel):
    """Данные о складе продавца"""

    cargo_type: int | None = _field(default=None, name="cargoType")
    """Тип товара:   - `1` — малогабаритный товар (МГТ)   - `2` — сверхгабаритный товар (СГТ)   -
    `3` — крупногабаритный товар (КГТ+)
    """
    delivery_type: int | None = _field(default=None, name="deliveryType")
    """Тип доставки, который принимает склад:   - `1` — доставка на склад WB (FBS)   - `2` —
    доставка силами продавца (DBS)   - `3` — доставка курьером WB (DBW) …
    """
    id: int | None = _field(default=None)
    """ID склада продавца"""
    is_deleting: bool | None = _field(default=None, name="isDeleting")
    """Склад удаляется:   - `false` — нет   - `true` — да  После удаления склад пропадёт из списка
    """
    is_processing: bool | None = _field(default=None, name="isProcessing")
    """Данные склада обновляются:   - `false` — нет   - `true` — да, обновление и удаление остатков
    недоступно  Обновление данных может занимать несколько минут
    """
    name: str | None = _field(default=None)
    """Название склада продавца"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада WB"""


class WarehousesCreateBody(WBModel):
    name: str | None = _field(default=None)
    """Имя склада продавца"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада WB.Нельзя привязывать склад WB, который уже используется"""


class WarehousesCreateResponse(WBModel):
    id: int | None = _field(default=None)
    """ID склада продавца"""


class WarehousesWarehouseIdUpdateBody(WBModel):
    name: str | None = _field(default=None)
    """Имя склада продавца"""
    office_id: int | None = _field(default=None, name="officeId")
    """ID склада WB.Нельзя привязывать склад WB, который уже используется.Можно менять не чаще
    одного раза в сутки
    """
