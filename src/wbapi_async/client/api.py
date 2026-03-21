from typing import Any

from ..client.session.base import BaseSession
from ..methods import (
    Brands,
    Color,
    ContactsList,
    CountryOfOrigin,
    CreateATag,
    CreateProductCards,
    CreateProductCardsWithMerge,
    CreateWarehouse,
    DeleteInventory,
    DeleteTheTag,
    DeleteWarehouse,
    Gender,
    GenerationOfSkus,
    GetInventory,
    GetOffices,
    GetProductDetail,
    GetProductsInQuarantine,
    GetProductSizesWithPrices,
    GetProductsWithPrices,
    GetProductsWithPricesByArticles,
    GetWarehouses,
    Hscodes,
    LimitsForTheProductCards,
    ListOfFailedProductCardsWithErrors,
    MergingOrSeparatingOfProductCards,
    ProcessedUploadDetails,
    ProcessedUploadState,
    ProductCardsInTrashList,
    ProductCardsList,
    ProductsParentCategories,
    RecoverProductCardFromTrash,
    Season,
    SetPricesAndDiscounts,
    SetSizePrices,
    SetWbClubDiscounts,
    SubjectCharacteristics,
    SubjectsList,
    TagManagementInTheProductCard,
    TagsList,
    TransferProductCardToTrash,
    UnprocessedUploadDetails,
    UnprocessedUploadState,
    UpdateContactsList,
    UpdateInventory,
    UpdateProductCards,
    UpdateTheTag,
    UpdateWarehouse,
    UploadMediaFile,
    UploadMediaFilesViaLinks,
    VatRate,
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
    GetInventoryItem,
    GetOfficesResponse,
    GetProductsInQuarantineItem,
    GetProductSizesWithPricesItem,
    GetProductsWithPricesByArticlesItem,
    GetProductsWithPricesItem,
    GetWarehousesResponse,
    HscodesItem,
    LimitsForTheProductCardsResponse,
    ListOfFailedProductCardsWithErrorsItem,
    MergingOrSeparatingOfProductCardsResponse,
    ProcessedUploadDetailsItem,
    ProcessedUploadStateResponse,
    ProductCardsInTrashListItem,
    ProductCardsListItem,
    ProductDetail,
    ProductsParentCategoriesResponse,
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

    async def brands(
        self,
        subject_id: int = None,
        next: int | None = None,
    ) -> list[BrandsItem]:
        """Brands

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1api~1content~1v1~1brands/get
        """
        call = Brands(subject_id=subject_id, next=next)
        return await self(call)

    async def color(
        self,
        locale: str | None = None,
    ) -> list[ColorResponse]:
        """Color

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1directory~1colors/get
        """
        call = Color(locale=locale)
        return await self(call)

    async def contacts_list(
        self,
        warehouse_id: int,
    ) -> list[ContactsListItem]:
        """Contacts List

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1dbw~1warehouses~1%7BwarehouseId%7D~1contacts/get
        """
        call = ContactsList(warehouse_id=warehouse_id)
        return await self(call)

    async def country_of_origin(
        self,
        locale: str | None = None,
    ) -> list[CountryOfOriginResponse]:
        """Country of Origin

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1directory~1countries/get
        """
        call = CountryOfOrigin(locale=locale)
        return await self(call)

    async def create_a_tag(
        self,
        color: str | None = None,
        name: str | None = None,
    ) -> list[CreateATagResponse]:
        """Create a Tag

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag/post
        """
        call = CreateATag(color=color, name=name)
        return await self(call)

    async def create_product_cards(
        self,
    ) -> list[CreateProductCardsResponse]:
        """Create Product Cards

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload/post
        """
        call = CreateProductCards()
        return await self(call)

    async def create_product_cards_with_merge(
        self,
        imt_id: int | None = None,
        cards_to_add: list[dict[str, Any]] | None = None,
    ) -> list[CreateProductCardsWithMergeResponse]:
        """Create Product Cards with Merge

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload~1add/post
        """
        call = CreateProductCardsWithMerge(imt_id=imt_id, cards_to_add=cards_to_add)
        return await self(call)

    async def create_warehouse(
        self,
        name: str = None,
        office_id: int = None,
    ) -> list[CreateWarehouseResponse]:
        """Create Warehouse

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses/post
        """
        call = CreateWarehouse(name=name, office_id=office_id)
        return await self(call)

    async def delete_inventory(
        self,
        warehouse_id: int,
        chrt_ids: list[int] = None,
    ) -> None:
        """Delete Inventory

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/delete
        """
        call = DeleteInventory(warehouse_id=warehouse_id, chrt_ids=chrt_ids)
        return await self(call)

    async def delete_the_tag(
        self,
        id: int,
    ) -> list[DeleteTheTagResponse]:
        """Delete the Tag

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1%7Bid%7D/delete
        """
        call = DeleteTheTag(id=id)
        return await self(call)

    async def delete_warehouse(
        self,
        warehouse_id: int,
    ) -> None:
        """Delete Warehouse

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses~1%7BwarehouseId%7D/delete
        """
        call = DeleteWarehouse(warehouse_id=warehouse_id)
        return await self(call)

    async def gender(
        self,
        locale: str | None = None,
    ) -> list[GenderItem]:
        """Gender

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1directory~1kinds/get
        """
        call = Gender(locale=locale)
        return await self(call)

    async def generation_of_skus(
        self,
        count: int | None = None,
    ) -> list[GenerationOfSkusItem]:
        """Generation of SKUs

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1barcodes/post
        """
        call = GenerationOfSkus(count=count)
        return await self(call)

    async def get_inventory(
        self,
        warehouse_id: int,
        chrt_ids: list[int] = None,
    ) -> list[GetInventoryItem]:
        """Get Inventory

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/post
        """
        call = GetInventory(warehouse_id=warehouse_id, chrt_ids=chrt_ids)
        return await self(call)

    async def get_offices(
        self,
    ) -> list[GetOfficesResponse]:
        """Get Offices

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1offices/get
        """
        call = GetOffices()
        return await self(call)

    async def get_product_sizes_with_prices(
        self,
        limit: int = None,
        offset: int | None = None,
        nm_id: int = None,
    ) -> list[GetProductSizesWithPricesItem]:
        """Get Product Sizes with Prices

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1size~1nm/get
        """
        call = GetProductSizesWithPrices(limit=limit, offset=offset, nm_id=nm_id)
        return await self(call)

    async def get_products_in_quarantine(
        self,
        limit: int = None,
        offset: int | None = None,
    ) -> list[GetProductsInQuarantineItem]:
        """Get Products in Quarantine

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1quarantine~1goods/get
        """
        call = GetProductsInQuarantine(limit=limit, offset=offset)
        return await self(call)

    async def get_products_with_prices(
        self,
        limit: int = None,
        offset: int | None = None,
        filter_nm_id: int | None = None,
    ) -> list[GetProductsWithPricesItem]:
        """Get Products with Prices

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/get
        """
        call = GetProductsWithPrices(limit=limit, offset=offset, filter_nm_id=filter_nm_id)
        return await self(call)

    async def get_products_with_prices_by_articles(
        self,
        nm_list: list[int] = None,
    ) -> list[GetProductsWithPricesByArticlesItem]:
        """Get Products with Prices by Articles

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/post
        """
        call = GetProductsWithPricesByArticles(nm_list=nm_list)
        return await self(call)

    async def get_warehouses(
        self,
    ) -> list[GetWarehousesResponse]:
        """Get Warehouses

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses/get
        """
        call = GetWarehouses()
        return await self(call)

    async def hscodes(
        self,
        subject_id: int = None,
        search: int | None = None,
        locale: str | None = None,
    ) -> list[HscodesItem]:
        """HS-codes

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1directory~1tnved/get
        """
        call = Hscodes(subject_id=subject_id, search=search, locale=locale)
        return await self(call)

    async def limits_for_the_product_cards(
        self,
    ) -> list[LimitsForTheProductCardsResponse]:
        """Limits for the Product Cards

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1limits/get
        """
        call = LimitsForTheProductCards()
        return await self(call)

    async def list_of_failed_product_cards_with_errors(
        self,
        locale: str | None = None,
        cursor: dict[str, Any] | None = None,
        order: dict[str, Any] | None = None,
    ) -> list[ListOfFailedProductCardsWithErrorsItem]:
        """List of Failed Product Cards with Errors

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1error~1list/post
        """
        call = ListOfFailedProductCardsWithErrors(locale=locale, cursor=cursor, order=order)
        return await self(call)

    async def merging_or_separating_of_product_cards(
        self,
    ) -> list[MergingOrSeparatingOfProductCardsResponse]:
        """Merging or Separating of Product Cards

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1moveNm/post
        """
        call = MergingOrSeparatingOfProductCards()
        return await self(call)

    async def processed_upload_details(
        self,
        limit: int = None,
        offset: int | None = None,
        upload_id: int = None,
    ) -> list[ProcessedUploadDetailsItem]:
        """Processed Upload Details

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1goods~1task/get
        """
        call = ProcessedUploadDetails(limit=limit, offset=offset, upload_id=upload_id)
        return await self(call)

    async def processed_upload_state(
        self,
        upload_id: int = None,
    ) -> list[ProcessedUploadStateResponse]:
        """Processed Upload State

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1tasks/get
        """
        call = ProcessedUploadState(upload_id=upload_id)
        return await self(call)

    async def product_cards_in_trash_list(
        self,
        locale: str | None = None,
        settings: dict[str, Any] | None = None,
    ) -> list[ProductCardsInTrashListItem]:
        """Product Cards in Trash List

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1trash/post
        """
        call = ProductCardsInTrashList(locale=locale, settings=settings)
        return await self(call)

    async def product_cards_list(
        self,
        locale: str | None = None,
        settings: dict[str, Any] | None = None,
    ) -> list[ProductCardsListItem]:
        """Product Cards List

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post
        """
        call = ProductCardsList(locale=locale, settings=settings)
        return await self(call)

    async def products_parent_categories(
        self,
        locale: str | None = None,
    ) -> list[ProductsParentCategoriesResponse]:
        """Products Parent Categories

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1object~1parent~1all/get
        """
        call = ProductsParentCategories(locale=locale)
        return await self(call)

    async def recover_product_card_from_trash(
        self,
        nm_i_ds: list[int] | None = None,
    ) -> list[RecoverProductCardFromTrashResponse]:
        """Recover Product Card from Trash

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1recover/post
        """
        call = RecoverProductCardFromTrash(nm_i_ds=nm_i_ds)
        return await self(call)

    async def season(
        self,
        locale: str | None = None,
    ) -> list[SeasonItem]:
        """Season

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1directory~1seasons/get
        """
        call = Season(locale=locale)
        return await self(call)

    async def set_prices_and_discounts(
        self,
        data: list[Any] = None,
    ) -> list[SetPricesAndDiscountsResponse]:
        """Set Prices and Discounts

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task/post
        """
        call = SetPricesAndDiscounts(data=data)
        return await self(call)

    async def set_size_prices(
        self,
        data: list[Any] = None,
    ) -> list[SetSizePricesResponse]:
        """Set Size Prices

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task~1size/post
        """
        call = SetSizePrices(data=data)
        return await self(call)

    async def set_wb_club_discounts(
        self,
        data: list[Any] = None,
    ) -> list[SetWbClubDiscountsResponse]:
        """Set WB Club Discounts

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task~1club-discount/post
        """
        call = SetWbClubDiscounts(data=data)
        return await self(call)

    async def subject_characteristics(
        self,
        subject_id: int,
        locale: str | None = None,
    ) -> list[SubjectCharacteristicsItem]:
        """Subject Characteristics

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1object~1charcs~1%7BsubjectId%7D/get
        """
        call = SubjectCharacteristics(subject_id=subject_id, locale=locale)
        return await self(call)

    async def subjects_list(
        self,
        locale: str | None = None,
        name: str | None = None,
        limit: int | None = 30,
        offset: int | None = 0,
        parent_id: int | None = None,
    ) -> list[SubjectsListItem]:
        """Subjects List

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1object~1all/get
        """
        call = SubjectsList(
            locale=locale, name=name, limit=limit, offset=offset, parent_id=parent_id
        )
        return await self(call)

    async def tag_management_in_the_product_card(
        self,
        nm_id: int | None = None,
        tags_i_ds: list[int] | None = None,
    ) -> list[TagManagementInTheProductCardResponse]:
        """Tag Management in the Product Card

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1nomenclature~1link/post
        """
        call = TagManagementInTheProductCard(nm_id=nm_id, tags_i_ds=tags_i_ds)
        return await self(call)

    async def tags_list(
        self,
    ) -> list[TagsListResponse]:
        """Tags List

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tags/get
        """
        call = TagsList()
        return await self(call)

    async def transfer_product_card_to_trash(
        self,
        nm_i_ds: list[int] | None = None,
    ) -> list[TransferProductCardToTrashResponse]:
        """Transfer Product Card to Trash

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1delete~1trash/post
        """
        call = TransferProductCardToTrash(nm_i_ds=nm_i_ds)
        return await self(call)

    async def unprocessed_upload_details(
        self,
        limit: int = None,
        offset: int | None = None,
        upload_id: int = None,
    ) -> list[UnprocessedUploadDetailsItem]:
        """Unprocessed Upload Details

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1buffer~1goods~1task/get
        """
        call = UnprocessedUploadDetails(limit=limit, offset=offset, upload_id=upload_id)
        return await self(call)

    async def unprocessed_upload_state(
        self,
        upload_id: int = None,
    ) -> list[UnprocessedUploadStateResponse]:
        """Unprocessed Upload State

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1buffer~1tasks/get
        """
        call = UnprocessedUploadState(upload_id=upload_id)
        return await self(call)

    async def update_contacts_list(
        self,
        warehouse_id: int,
        contacts: list[dict[str, Any]] | None = None,
    ) -> None:
        """Update Contacts List

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1dbw~1warehouses~1%7BwarehouseId%7D~1contacts/put
        """
        call = UpdateContactsList(warehouse_id=warehouse_id, contacts=contacts)
        return await self(call)

    async def update_inventory(
        self,
        warehouse_id: int,
        stocks: list[dict[str, Any]] = None,
    ) -> None:
        """Update Inventory

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/put
        """
        call = UpdateInventory(warehouse_id=warehouse_id, stocks=stocks)
        return await self(call)

    async def update_product_cards(
        self,
    ) -> list[UpdateProductCardsResponse]:
        """Update Product Cards

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1update/post
        """
        call = UpdateProductCards()
        return await self(call)

    async def update_the_tag(
        self,
        id: int,
        color: str | None = None,
        name: str | None = None,
    ) -> list[UpdateTheTagResponse]:
        """Update the Tag

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1%7Bid%7D/patch
        """
        call = UpdateTheTag(id=id, color=color, name=name)
        return await self(call)

    async def update_warehouse(
        self,
        warehouse_id: int,
        name: str = None,
        office_id: int = None,
    ) -> None:
        """Update Warehouse

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses~1%7BwarehouseId%7D/put
        """
        call = UpdateWarehouse(warehouse_id=warehouse_id, name=name, office_id=office_id)
        return await self(call)

    async def upload_media_file(
        self,
        x_nm_id: str = None,
        x_photo_number: int = None,
    ) -> list[UploadMediaFileResponse]:
        """Upload Media File

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Media-Files/paths/~1content~1v3~1media~1file/post
        """
        call = UploadMediaFile(x_nm_id=x_nm_id, x_photo_number=x_photo_number)
        return await self(call)

    async def upload_media_files_via_links(
        self,
        nm_id: int | None = None,
        data: list[str] | None = None,
    ) -> list[UploadMediaFilesViaLinksResponse]:
        """Upload Media Files via Links

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Media-Files/paths/~1content~1v3~1media~1save/post
        """
        call = UploadMediaFilesViaLinks(nm_id=nm_id, data=data)
        return await self(call)

    async def vat_rate(
        self,
        locale: str | None = None,
    ) -> list[VatRateItem]:
        """VAT Rate

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Categories--Subjects--and-Characteristics/paths/~1content~1v2~1directory~1vat/get
        """
        call = VatRate(locale=locale)
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
