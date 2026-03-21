from typing import Any

from ..client.session.base import BaseSession
from ..methods import (
    CreateATag,
    CreateProductCards,
    CreateProductCardsWithMerge,
    CreateWarehouse,
    DeleteInventory,
    DeleteTheTag,
    DeleteWarehouse,
    GenerationOfSkus,
    GetBrands,
    GetColor,
    GetContactsList,
    GetCountryOfOrigin,
    GetGender,
    GetHscodes,
    GetInventory,
    GetLimitsForTheProductCards,
    GetOffices,
    GetProcessedUploadDetails,
    GetProcessedUploadState,
    GetProductDetail,
    GetProductsInQuarantine,
    GetProductSizesWithPrices,
    GetProductsParentCategories,
    GetProductsWithPrices,
    GetProductsWithPricesByArticles,
    GetSeason,
    GetSubjectCharacteristics,
    GetSubjectsList,
    GetTagsList,
    GetUnprocessedUploadDetails,
    GetUnprocessedUploadState,
    GetVatRate,
    GetWarehouses,
    ListOfFailedProductCardsWithErrors,
    MergingOrSeparatingOfProductCards,
    ProductCardsInTrashList,
    ProductCardsList,
    RecoverProductCardFromTrash,
    SetPricesAndDiscounts,
    SetSizePrices,
    SetWbClubDiscounts,
    TagManagementInTheProductCard,
    TransferProductCardToTrash,
    UpdateContactsList,
    UpdateInventory,
    UpdateProductCards,
    UpdateTheTag,
    UpdateWarehouse,
    UploadMediaFile,
    UploadMediaFilesViaLinks,
    WbMethod,
)
from ..types import (
    BrandsItem,
    ColorResponse,
    ContactsListItem,
    CountryOfOriginResponse,
    CreateATagResponse,
    CreateProductCardsResponse,
    CreateProductCardsWithMergeResponse,
    CreateWarehouseResponse,
    DeleteTheTagResponse,
    GenderItem,
    GenerationOfSkusItem,
    HscodesItem,
    InventoryItem,
    LimitsForTheProductCardsResponse,
    ListOfFailedProductCardsWithErrorsItem,
    MergingOrSeparatingOfProductCardsResponse,
    OfficesResponse,
    ProcessedUploadDetailsItem,
    ProcessedUploadStateResponse,
    ProductCardsInTrashListItem,
    ProductCardsListItem,
    ProductDetail,
    ProductsInQuarantineItem,
    ProductSizesWithPricesItem,
    ProductsParentCategoriesResponse,
    ProductsWithPricesByArticlesItem,
    ProductsWithPricesItem,
    RecoverProductCardFromTrashResponse,
    SeasonItem,
    SetPricesAndDiscountsResponse,
    SetSizePricesResponse,
    SetWbClubDiscountsResponse,
    SubjectCharacteristicsItem,
    SubjectsListItem,
    TagManagementInTheProductCardResponse,
    TagsListResponse,
    TransferProductCardToTrashResponse,
    UnprocessedUploadDetailsItem,
    UnprocessedUploadStateResponse,
    UpdateProductCardsResponse,
    UpdateTheTagResponse,
    UploadMediaFileResponse,
    UploadMediaFilesViaLinksResponse,
    VatRateItem,
    WarehousesResponse,
)
from ..utils.token import validate_token
from ..utils.unofficial import unofficial


class WbAPI:
    def __init__(self, token: str, session: BaseSession | None = None, **kwargs: Any) -> None:
        """
        WbAPI class.

        Attributes:

            token: Access token

            Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Authorization/How-to-create-a-personal-access-base-or-test-token
        """
        validate_token(token)
        if session is None:
            read_timeout = kwargs.get("read_timeout", 60)
            base = kwargs.get("base", "wildberries.ru")
            session = BaseSession(
                base=base,
                timeout=read_timeout,
            )

        self._token = token
        self.session = session

    async def __aenter__(self) -> "WbAPI":
        return self

    async def __aexit__(self, exc_type: Any, _exc: Any, _tb: Any) -> None:
        await self.session.close()

    async def __call__(self, method: WbMethod) -> Any:
        return await method.emit(self)

    async def create_a_tag(
        self,
        color: str | None = None,
        name: str | None = None,
    ) -> list[CreateATagResponse]:
        """
        Creates a tag.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag/post

        :param color: Tag color.
        :param name: Tag name
        :return: list[CreateATagResponse]
        """
        call = CreateATag(color=color, name=name)
        return await self(call)

    async def create_product_cards(
        self,
    ) -> list[CreateProductCardsResponse]:
        """
        Creates products cards. You can specify product description and characteristics.<br>

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload/post
        :return: list[CreateProductCardsResponse]
        """
        call = CreateProductCards()
        return await self(call)

    async def create_product_cards_with_merge(
        self,
        imt_id: int | None = None,
        cards_to_add: list[dict[str, Any]] | None = None,
    ) -> list[CreateProductCardsWithMergeResponse]:
        """
        The method creates product cards by merging it with existing individual cards and groups of
        mergedcards. There can be no more than 30 cards in one group of merged product cards,
        respectively,you can create no more than 29 product cards in one request.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload~1add/post

        :param imt_id: `imtID` of an individual product card or group of merged product cards to
                       :param imt_id: whichthe created cards are added
        :param cards_to_add: Added product cards
        :return: list[CreateProductCardsWithMergeResponse]
        """
        call = CreateProductCardsWithMerge(imt_id=imt_id, cards_to_add=cards_to_add)
        return await self(call)

    async def create_warehouse(
        self,
        name: str = None,
        office_id: int = None,
    ) -> list[CreateWarehouseResponse]:
        """
        Creates a seller's warehouse. You cannot link an office that is already in use.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses/post

        :param name: Seller's warehouse name
        :param office_id: Office ID
        :return: list[CreateWarehouseResponse]
        """
        call = CreateWarehouse(name=name, office_id=office_id)
        return await self(call)

    async def delete_inventory(
        self,
        warehouse_id: int,
        chrt_ids: list[int] = None,
    ) -> None:
        """
        Deletes product inventory.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/delete

        :param warehouse_id: The seller's warehouse ID
        :param chrt_ids: Size IDs array
        :return: None
        """
        call = DeleteInventory(warehouse_id=warehouse_id, chrt_ids=chrt_ids)
        return await self(call)

    async def delete_the_tag(
        self,
        id: int,
    ) -> list[DeleteTheTagResponse]:
        """
        Deletes the tag

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1%7Bid%7D/delete

        :param id: Numeric tag ID
        :return: list[DeleteTheTagResponse]
        """
        call = DeleteTheTag(id=id)
        return await self(call)

    async def delete_warehouse(
        self,
        warehouse_id: int,
    ) -> None:
        """
        Deletes the seller's warehouse.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses~1%7BwarehouseId%7D/delete

        :param warehouse_id: The seller's warehouse ID
        :return: None
        """
        call = DeleteWarehouse(warehouse_id=warehouse_id)
        return await self(call)

    async def generation_of_skus(
        self,
        count: int | None = None,
    ) -> list[GenerationOfSkusItem]:
        """
        Generates array of unique SKUs to create size of the product card

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1barcodes/post

        :param count: Number of SKUs to be generated, maximum 5,000
        :return: list[GenerationOfSkusItem]
        """
        call = GenerationOfSkus(count=count)
        return await self(call)

    async def get_brands(
        self,
        subject_id: int = None,
        next: int | None = None,
    ) -> list[BrandsItem]:
        """
        The method returns list of brands by subject ID.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1api~1content~1v1~1brands/get

        :param subject_id: Subject ID
        :param next: Pagination parameter. Use the `next` value from the response to get the next
                     :param next: databatch
        :return: list[BrandsItem]
        """
        call = GetBrands(subject_id=subject_id, next=next)
        return await self(call)

    async def get_color(
        self,
        locale: str | None = None,
    ) -> list[ColorResponse]:
        """
        Provides values of color characteristic.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1colors/get

        :param locale: Language for response of the `subjectName` and `name` fields:
        :return: list[ColorResponse]
        """
        call = GetColor(locale=locale)
        return await self(call)

    async def get_contacts_list(
        self,
        warehouse_id: int,
    ) -> list[ContactsListItem]:
        """
        Returns a list of contacts linked to the seller's warehouse.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1dbw~1warehouses~1%7BwarehouseId%7D~1contacts/get

        :param warehouse_id: The seller's warehouse ID
        :return: list[ContactsListItem]
        """
        call = GetContactsList(warehouse_id=warehouse_id)
        return await self(call)

    async def get_country_of_origin(
        self,
        locale: str | None = None,
    ) -> list[CountryOfOriginResponse]:
        """
        Provides value of characteristic country of origin.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1countries/get

        :param locale: Language for response of the `subjectName` and `name` fields:
        :return: list[CountryOfOriginResponse]
        """
        call = GetCountryOfOrigin(locale=locale)
        return await self(call)

    async def get_gender(
        self,
        locale: str | None = None,
    ) -> list[GenderItem]:
        """
        Provides values of gender characteristic.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1kinds/get

        :param locale: Language for response of the `subjectName` and `name` fields:
        :return: list[GenderItem]
        """
        call = GetGender(locale=locale)
        return await self(call)

    async def get_hscodes(
        self,
        subject_id: int = None,
        search: int | None = None,
        locale: str | None = None,
    ) -> list[HscodesItem]:
        """
        The method provides list of HS-codes by category name and filter by HS-code.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1tnved/get

        :param subject_id: Subject ID
        :param search: Search by HS-code. Works only with the subjectID parameter
        :param locale: Language for response of the `subjectName` and `name` fields:
        :return: list[HscodesItem]
        """
        call = GetHscodes(subject_id=subject_id, search=search, locale=locale)
        return await self(call)

    async def get_inventory(
        self,
        warehouse_id: int,
        chrt_ids: list[int] = None,
    ) -> list[InventoryItem]:
        """
        Returns product inventory.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/post

        :param warehouse_id: The seller's warehouse ID
        :param chrt_ids: Size IDs array
        :return: list[InventoryItem]
        """
        call = GetInventory(warehouse_id=warehouse_id, chrt_ids=chrt_ids)
        return await self(call)

    async def get_limits_for_the_product_cards(
        self,
    ) -> list[LimitsForTheProductCardsResponse]:
        """
        The method allows to get separately free and paid vendor limits for creating product
        cards.<br>

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1limits/get
        :return: list[LimitsForTheProductCardsResponse]
        """
        call = GetLimitsForTheProductCards()
        return await self(call)

    async def get_offices(
        self,
    ) -> list[OfficesResponse]:
        """
        Returns a list of all offices to link to seller warehouse.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1offices/get
        :return: list[OfficesResponse]
        """
        call = GetOffices()
        return await self(call)

    async def get_processed_upload_details(
        self,
        limit: int = None,
        offset: int | None = None,
        upload_id: int = None,
    ) -> list[ProcessedUploadDetailsItem]:
        """
        Returns products in processed upload including product errors.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1goods~1task/get

        :param limit: Number of elements per page (pagination)
        :param offset: How many results to skip. For example, with value `10`, the response will
                       :param offset: startwith the 11 element
        :param upload_id: Download ID
        :return: list[ProcessedUploadDetailsItem]
        """
        call = GetProcessedUploadDetails(limit=limit, offset=offset, upload_id=upload_id)
        return await self(call)

    async def get_processed_upload_state(
        self,
        upload_id: int = None,
    ) -> list[ProcessedUploadStateResponse]:
        """
        Returns the processed upload data.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1tasks/get

        :param upload_id: Download ID
        :return: list[ProcessedUploadStateResponse]
        """
        call = GetProcessedUploadState(upload_id=upload_id)
        return await self(call)

    async def get_product_sizes_with_prices(
        self,
        limit: int = None,
        offset: int | None = None,
        nm_id: int = None,
    ) -> list[ProductSizesWithPricesItem]:
        """
        Returns sizes data for the product. Only for products from categories where size price
        settingis available. For these products `"editableSizePrice":true`.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1size~1nm/get

        :param limit: Number of elements per page (pagination)
        :param offset: How many results to skip. For example, with value `10`, the response will
                       :param offset: startwith the 11 element
        :param nm_id: WB article
        :return: list[ProductSizesWithPricesItem]
        """
        call = GetProductSizesWithPrices(limit=limit, offset=offset, nm_id=nm_id)
        return await self(call)

    async def get_products_in_quarantine(
        self,
        limit: int = None,
        offset: int | None = None,
    ) -> list[ProductsInQuarantineItem]:
        """
        Returns information about products in quarantine.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1quarantine~1goods/get

        :param limit: Number of elements per page (pagination)
        :param offset: How many results to skip. For example, with value `10`, the response will
                       :param offset: startwith the 11 element
        :return: list[ProductsInQuarantineItem]
        """
        call = GetProductsInQuarantine(limit=limit, offset=offset)
        return await self(call)

    async def get_products_parent_categories(
        self,
        locale: str | None = None,
    ) -> list[ProductsParentCategoriesResponse]:
        """
        Returns the list of all products parent categories

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1object~1parent~1all/get

        :param locale: Language for response of the `name` field:
        :return: list[ProductsParentCategoriesResponse]
        """
        call = GetProductsParentCategories(locale=locale)
        return await self(call)

    async def get_products_with_prices(
        self,
        limit: int = None,
        offset: int | None = None,
        filter_nm_id: int | None = None,
    ) -> list[ProductsWithPricesItem]:
        """
        Returns product data.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/get

        :param limit: Number of elements per page (pagination)
        :param offset: How many results to skip. For example, with value `10`, the response will
                       :param offset: startwith the 11 element
        :param filter_nm_id: WB article for search
        :return: list[ProductsWithPricesItem]
        """
        call = GetProductsWithPrices(limit=limit, offset=offset, filter_nm_id=filter_nm_id)
        return await self(call)

    async def get_products_with_prices_by_articles(
        self,
        nm_list: list[int] = None,
    ) -> list[ProductsWithPricesByArticlesItem]:
        """
        Returns product data by its article.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/post

        :param nm_list: WB articles for search
        :return: list[ProductsWithPricesByArticlesItem]
        """
        call = GetProductsWithPricesByArticles(nm_list=nm_list)
        return await self(call)

    async def get_season(
        self,
        locale: str | None = None,
    ) -> list[SeasonItem]:
        """
        Provide values of season characteristic

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1seasons/get

        :param locale: Language for response of the `subjectName` and `name` fields:
        :return: list[SeasonItem]
        """
        call = GetSeason(locale=locale)
        return await self(call)

    async def get_subject_characteristics(
        self,
        subject_id: int,
        locale: str | None = None,
    ) -> list[SubjectCharacteristicsItem]:
        """
        Returns list of the subject characteristics by its ID

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get

        :param subject_id: Subject ID
        :param locale: Language for response of the `subjectName` and `name` fields:
        :return: list[SubjectCharacteristicsItem]
        """
        call = GetSubjectCharacteristics(subject_id=subject_id, locale=locale)
        return await self(call)

    async def get_subjects_list(
        self,
        locale: str | None = None,
        name: str | None = None,
        limit: int | None = 30,
        offset: int | None = 0,
        parent_id: int | None = None,
    ) -> list[SubjectsListItem]:
        """
        Returns the list of all available subjects, subjects parent categories and their IDs

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1object~1all/get

        :param locale: Language for response of the `name` field:
        :param name: Search by item name (Socks), the search works by substring and can be
                     :param name: conductedin any of the supported languages
        :param limit: Number of search results, maximum 1,000
        :param offset: How many results to skip. For example, with value `10`, the response will
                       :param offset: startwith the 11 element
        :param parent_id: Subject parent category ID
        :return: list[SubjectsListItem]
        """
        call = GetSubjectsList(
            locale=locale,
            name=name,
            limit=limit,
            offset=offset,
            parent_id=parent_id,
        )
        return await self(call)

    async def get_tags_list(
        self,
    ) -> list[TagsListResponse]:
        """
        Returns seller's tags list

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tags/get
        :return: list[TagsListResponse]
        """
        call = GetTagsList()
        return await self(call)

    async def get_unprocessed_upload_details(
        self,
        limit: int = None,
        offset: int | None = None,
        upload_id: int = None,
    ) -> list[UnprocessedUploadDetailsItem]:
        """
        Returns products in processing upload including product errors.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1buffer~1goods~1task/get

        :param limit: Number of elements per page (pagination)
        :param offset: How many results to skip. For example, with value `10`, the response will
                       :param offset: startwith the 11 element
        :param upload_id: Download ID
        :return: list[UnprocessedUploadDetailsItem]
        """
        call = GetUnprocessedUploadDetails(limit=limit, offset=offset, upload_id=upload_id)
        return await self(call)

    async def get_unprocessed_upload_state(
        self,
        upload_id: int = None,
    ) -> list[UnprocessedUploadStateResponse]:
        """
        Returns the processing upload data.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1buffer~1tasks/get

        :param upload_id: Download ID
        :return: list[UnprocessedUploadStateResponse]
        """
        call = GetUnprocessedUploadState(upload_id=upload_id)
        return await self(call)

    async def get_vat_rate(
        self,
        locale: str | None = None,
    ) -> list[VatRateItem]:
        """
        Returns a list of values for the **VAT rate** characteristic

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories-Subjects-and-Characteristics/paths/~1content~1v2~1directory~1vat/get

        :param locale: Language for response of the `subjectName` and `name` fields:
        :return: list[VatRateItem]
        """
        call = GetVatRate(locale=locale)
        return await self(call)

    async def get_warehouses(
        self,
    ) -> list[WarehousesResponse]:
        """
        Returns a list of all seller's warehouses.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses/get
        :return: list[WarehousesResponse]
        """
        call = GetWarehouses()
        return await self(call)

    async def list_of_failed_product_cards_with_errors(
        self,
        locale: str | None = None,
        cursor: dict[str, Any] | None = None,
        order: dict[str, Any] | None = None,
    ) -> list[ListOfFailedProductCardsWithErrorsItem]:
        """
        Returns the list of product cards
        ([drafts](https://seller.wildberries.ru/new-goods/error-cards))and the list of errors
        encounteredduring product card creation or editing.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1error~1list/post

        :param locale: Language of subject names:
        :param cursor: Paginator
        :param order: The order of return of batches
        :return: list[ListOfFailedProductCardsWithErrorsItem]
        """
        call = ListOfFailedProductCardsWithErrors(locale=locale, cursor=cursor, order=order)
        return await self(call)

    async def merging_or_separating_of_product_cards(
        self,
    ) -> list[MergingOrSeparatingOfProductCardsResponse]:
        """
        The method merges and separates product cards. Product cards are merged if they have the
        same`imtID`.<br><br>

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1moveNm/post
        :return: list[MergingOrSeparatingOfProductCardsResponse]
        """
        call = MergingOrSeparatingOfProductCards()
        return await self(call)

    async def product_cards_in_trash_list(
        self,
        locale: str | None = None,
        settings: dict[str, Any] | None = None,
    ) -> list[ProductCardsInTrashListItem]:
        """
        <div class="description_auth">

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1trash/post

        :param locale: Language for response of the `name`, `value` and `object` fields:
        :param settings: Settings
        :return: list[ProductCardsInTrashListItem]
        """
        call = ProductCardsInTrashList(locale=locale, settings=settings)
        return await self(call)

    async def product_cards_list(
        self,
        locale: str | None = None,
        settings: dict[str, Any] | None = None,
    ) -> list[ProductCardsListItem]:
        """
        <div class="description_auth">

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post

        :param locale: Language for response of the `name`, `value` and `object` fields:
        :param settings: Settings
        :return: list[ProductCardsListItem]
        """
        call = ProductCardsList(locale=locale, settings=settings)
        return await self(call)

    async def recover_product_card_from_trash(
        self,
        nm_i_ds: list[int] | None = None,
    ) -> list[RecoverProductCardFromTrashResponse]:
        """
        Returns the product card from trash

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1recover/post

        :param nm_i_ds: Wildberries articles
        :return: list[RecoverProductCardFromTrashResponse]
        """
        call = RecoverProductCardFromTrash(nm_i_ds=nm_i_ds)
        return await self(call)

    async def set_prices_and_discounts(
        self,
        data: list[Any] = None,
    ) -> list[SetPricesAndDiscountsResponse]:
        """
        Sets prices and discounts.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task/post

        :param data: Products, prices and discounts. Maximum 1,000 products. Both price and
                     :param data: discountcan not be empty
        :return: list[SetPricesAndDiscountsResponse]
        """
        call = SetPricesAndDiscounts(data=data)
        return await self(call)

    async def set_size_prices(
        self,
        data: list[Any] = None,
    ) -> list[SetSizePricesResponse]:
        """
        Sets different prices for different sizes.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task~1size/post

        :param data: Sizes and prices. Maximum 1,000 sizes
        :return: list[SetSizePricesResponse]
        """
        call = SetSizePrices(data=data)
        return await self(call)

    async def set_wb_club_discounts(
        self,
        data: list[Any] = None,
    ) -> list[SetWbClubDiscountsResponse]:
        """
        Sets WB Club subscription discounts.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task~1club-discount/post

        :param data: Products and WB Club discounts. Maximum 1,000 products.
        :return: list[SetWbClubDiscountsResponse]
        """
        call = SetWbClubDiscounts(data=data)
        return await self(call)

    async def tag_management_in_the_product_card(
        self,
        nm_id: int | None = None,
        tags_i_ds: list[int] | None = None,
    ) -> list[TagManagementInTheProductCardResponse]:
        """
        The method allows to add tags to the product card and remove tags from the product
        card.<br>

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1nomenclature~1link/post

        :param nm_id: WB article
        :param tags_i_ds: An array of numeric tag IDs.<br>
        :return: list[TagManagementInTheProductCardResponse]
        """
        call = TagManagementInTheProductCard(nm_id=nm_id, tags_i_ds=tags_i_ds)
        return await self(call)

    async def transfer_product_card_to_trash(
        self,
        nm_i_ds: list[int] | None = None,
    ) -> list[TransferProductCardToTrashResponse]:
        """
        Transfers the product card to the trash. In doing so, the product card would not be
        deleted.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1delete~1trash/post

        :param nm_i_ds: Wildberries articles
        :return: list[TransferProductCardToTrashResponse]
        """
        call = TransferProductCardToTrash(nm_i_ds=nm_i_ds)
        return await self(call)

    async def update_contacts_list(
        self,
        warehouse_id: int,
        contacts: list[dict[str, Any]] | None = None,
    ) -> None:
        """
        Updates the seller's warehouse contact list. <br>

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1dbw~1warehouses~1%7BwarehouseId%7D~1contacts/put

        :param warehouse_id: The seller's warehouse ID
        :return: None
        """
        call = UpdateContactsList(warehouse_id=warehouse_id, contacts=contacts)
        return await self(call)

    async def update_inventory(
        self,
        warehouse_id: int,
        stocks: list[dict[str, Any]] = None,
    ) -> None:
        """
        Updates product inventory.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/put

        :param warehouse_id: The seller's warehouse ID
        :param stocks: Array of size IDs and amounts
        :return: None
        """
        call = UpdateInventory(warehouse_id=warehouse_id, stocks=stocks)
        return await self(call)

    async def update_product_cards(
        self,
    ) -> list[UpdateProductCardsResponse]:
        """
        Edits product cards. Also use it to add new sizes.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1update/post
        :return: list[UpdateProductCardsResponse]
        """
        call = UpdateProductCards()
        return await self(call)

    async def update_the_tag(
        self,
        id: int,
        color: str | None = None,
        name: str | None = None,
    ) -> list[UpdateTheTagResponse]:
        """
        Changes tag data: name and color

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1%7Bid%7D/patch

        :param id: Numeric tag ID
        :param color: Tag color
        :param name: Tag name
        :return: list[UpdateTheTagResponse]
        """
        call = UpdateTheTag(id=id, color=color, name=name)
        return await self(call)

    async def update_warehouse(
        self,
        warehouse_id: int,
        name: str = None,
        office_id: int = None,
    ) -> None:
        """
        Updates the seller's warehouse details. Changing the linked office is allowed once per day.
        Youcannot link an office that is already in use.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses~1%7BwarehouseId%7D/put

        :param warehouse_id: The seller's warehouse ID
        :param name: Seller's warehouse name
        :param office_id: Office ID
        :return: None
        """
        call = UpdateWarehouse(warehouse_id=warehouse_id, name=name, office_id=office_id)
        return await self(call)

    async def upload_media_file(
        self,
        x_nm_id: str = None,
        x_photo_number: int = None,
    ) -> list[UploadMediaFileResponse]:
        """
        Uploads and adds one media file for the product card.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Media-Files/paths/~1content~1v3~1media~1file/post

        :param x_nm_id: Wildberries article
        :param x_photo_number: Number of media file, starting from `1`. To add the video set `1`.
        :return: list[UploadMediaFileResponse]
        """
        call = UploadMediaFile(x_nm_id=x_nm_id, x_photo_number=x_photo_number)
        return await self(call)

    async def upload_media_files_via_links(
        self,
        nm_id: int | None = None,
        data: list[str] | None = None,
    ) -> list[UploadMediaFilesViaLinksResponse]:
        """
        The method uploads a set of media files to a product card by specifying links in the
        request.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Media-Files/paths/~1content~1v3~1media~1save/post

        :param nm_id: Wildberries article
        :param data: Links to images in the order that they are on the card, and a video at any
                     :param data: positionof the array
        :return: list[UploadMediaFilesViaLinksResponse]
        """
        call = UploadMediaFilesViaLinks(nm_id=nm_id, data=data)
        return await self(call)

    # --- unofficial methods (hand-written, not generated) ---

    @unofficial
    async def get_product_detail(
        self,
        nm: int,
        dest: int,
        spp: int | None = None,
        rate: int | None = None,
    ) -> list[ProductDetail]:
        """
        Returns product detail by WB article. No official documentation available.

        :param nm: WB article (nmID)
        :param dest: Destination region ID
        :param spp: SPP discount
        :param rate: Rate
        :return: List of :class:`ProductDetail`
        """
        call = GetProductDetail(nm=nm, dest=dest, spp=spp, rate=rate)
        return await self(call)
