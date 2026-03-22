from typing import Any

from ..client.session.base import BaseSession
from ..enums import (
    AggregationLevel,
    BidType,
    Height,
    Height2,
    Locale,
    Order,
    Order2,
    PaymentType,
    Period,
    PinOn,
    PositionCluster,
    Sort,
    Sort2,
    Sort3,
    Sort4,
    State,
    TopOrderBy,
    Type,
    Type2,
    Width,
    Width2,
)
from ..methods import (
    AcceptanceOptions,
    ActiveAndInactiveSearchClusterLists,
    AddAssemblyOrdersToTheSupply,
    AddBoxesToTheSupply,
    AddCustomDeclarationNumberToTheOrder,
    AddCustomDeclarationToTheOrders,
    AddDataMatrixCodesToAssemblyOrdersChestnyZnak,
    AddDataMatrixCodesToTheAssemblyOrdersChestnyZnak,
    AddDataMatrixCodeToTheAssemblyOrder,
    AddDataMatrixCodeToTheOrder,
    AddExpirationDateToTheAssemblyOrder,
    AddGtinToAssemblyOrders,
    AddGtinToTheAssemblyOrder,
    AddGtinToTheAssemblyOrders,
    AddGtinToTheOrder,
    AddImeiToAssemblyOrders,
    AddImeiToTheAssemblyOrder,
    AddImeiToTheAssemblyOrders,
    AddImeiToTheOrder,
    AddProductToThePromotion,
    AddUinUniqueIdentificationNumbersToTheAssemblyOrders,
    AddUinUniqueIdentificationNumberToAssemblyOrders,
    AddUinUniqueIdentificationNumberToTheAssemblyOrder,
    AddUinUniqueIdentificationNumberToTheOrder,
    AnswerBuyersApplication,
    AssignADataMatrixCodeToTheAssemblyOrder,
    B2BBuyerInformation,
    BuyerInformation,
    CancelAssemblyOrders,
    CancelTheAssemblyOrder,
    CancelTheAssemblyOrders,
    CancelTheOrder,
    ChangingCampaignsBids,
    ChangingPlacementsInCampaignsWithCustomBid,
    ChangingTheListOfProductCardsInCampaigns,
    CheckIfTheOrderBelongsToTheBuyer,
    CourierInfo,
    CreateANewSupply,
    CreateAnInvitationForANewUser,
    CreateATag,
    CreateCampaign,
    CreatePass,
    CreateProductCards,
    CreateProductCardsWithMerge,
    CreateTheReport,
    CreateWarehouse,
    DailySearchClustersStatistics,
    DeleteAssemblyOrderMetadata,
    DeleteAssemblyOrdersMetadata,
    DeleteBidsFromSearchClusters,
    DeleteBoxesFromTheSupply,
    DeleteInventory,
    DeleteOrderMetadata,
    DeleteThePass,
    DeleteTheSupply,
    DeleteTheTag,
    DeleteUser,
    DeleteWarehouse,
    DeliveryDateAndTime,
    EditResponseToFeedback,
    GenerationOfSkus,
    GetAListOfSellerActiveOrInvitedUsers,
    GetAllAssemblyOrdersForReshipment,
    GetAssemblyOrderMetadata,
    GetAssemblyOrders,
    GetAssemblyOrdersMetadata,
    GetAssemblyOrdersStatuses,
    GetAssemblyOrdersStickers,
    GetAssemblyOrderStatuses,
    GetASuppliesList,
    GetBalance,
    GetBlockedProductCards,
    GetBoxTariffs,
    GetBrands,
    GetBuyersReturnApplications,
    GetCampaignBudget,
    GetCampaignsInformation,
    GetCampaignsLists,
    GetCampaignsStatistics,
    GetChatEvents,
    GetChatList,
    GetCheckTheStatus,
    GetColor,
    GetConnectionCheck,
    GetContactsList,
    GetCountryOfOrigin,
    GetCreateTheReport,
    GetDeleteCampaign,
    GetDocument,
    GetDocuments,
    GetDocumentsCategories,
    GetDocumentsList,
    GetFeedbacksList,
    GetFileFromTheMessage,
    GetGender,
    GetGenerateTheReport,
    GetGettingSellerPortalNews,
    GetHiddenFromTheCatalog,
    GetHscodes,
    GetInformationAboutMediaCampaign,
    GetInformationOnCompletedOrders,
    GetInformationOnPaidDelivery,
    GetInventory,
    GetLaunchCampaign,
    GetLimitsForTheProductCards,
    GetListOfArchivedFeedbacks,
    GetListOfMediaCampaigns,
    GetListOfPinnedAndUnpinnedFeedback,
    GetListOfProductsForParticipatingInThePromotion,
    GetLogisticsAndStorageCostsMultiplier,
    GetMediaCampaignsNumber,
    GetNewAssemblyOrders,
    GetNewAssemblyOrdersList,
    GetNewOrders,
    GetNewOrdersList,
    GetNumberOfFeedbacks,
    GetNumberOfQuestions,
    GetOffices,
    GetOfficesForPass,
    GetOrderMetadata,
    GetOrders,
    GetOrdersStatuses,
    GetOrdersStickers,
    GetPalletTariffs,
    GetParentCategoriesOfTheBrand,
    GetPasses,
    GetPauseCampaign,
    GetPinnedAndUnpinnedFeedbackNumber,
    GetPinnedFeedbackLimits,
    GetProcessedUploadDetails,
    GetProcessedUploadState,
    GetProductCategoryCommission,
    GetProductDetail,
    GetProductLabeling,
    GetProductsInQuarantine,
    GetProductSizesWithPrices,
    GetProductsParentCategories,
    GetProductsWithPrices,
    GetProductsWithPricesByArticles,
    GetPromotionsDetails,
    GetPromotionsList,
    GetQuestionList,
    GetRealizationSalesReport,
    GetReceivingCostsHistory,
    GetReceivingTheHistoryOfAccountTopups,
    GetRecommendedBidsForItemsAndSearchClusters,
    GetReport,
    GetRetrieveInformationOnCompletedAssemblyOrders,
    GetReturnTariffs,
    GetSales,
    GetSeason,
    GetSelfpurchases,
    GetSellerBrands,
    GetSellerInformation,
    GetSellersBalance,
    GetStickersForAssemblyOrdersWithDeliveryToPickupPoint,
    GetStickersForCrossborderAssemblyOrders,
    GetStopCampaign,
    GetSubjectCharacteristics,
    GetSubjectsForCampaigns,
    GetSubjectsList,
    GetSubstitutionsAndIncorrectAttachments,
    GetSupplyAssemblyOrderIds,
    GetSupplyBoxesList,
    GetSupplyDetails,
    GetSupplyPackage,
    GetSupplyProducts,
    GetSupplyTariffs,
    GetTagsList,
    GetTheFeedbackById,
    GetTheQuestionById,
    GetTheReport,
    GetTheReportsList,
    GetTheSupplyBoxQrCodeStickers,
    GetTheSupplyQrCode,
    GetTransitDirections,
    GetUnansweredFeedbacks,
    GetUnansweredQuestions,
    GetUnprocessedUploadDetails,
    GetUnprocessedUploadState,
    GetUnseenFeedbacksAndQuestions,
    GetVatRate,
    GetWarehouse,
    GetWarehouseMeasurements,
    GetWarehouses,
    GetWarehousesList,
    GroupData,
    GroupedProductCardsStatisticsPerDays,
    ListOfCampaignMinusPhrases,
    ListOfFailedProductCardsWithErrors,
    ListOfSearchClustersBids,
    MainPage,
    MediaCampaignStatistics,
    MergingOrSeparatingOfProductCards,
    MinimumBidsForProductCards,
    MoveTheSupplyToTheDelivery,
    NotifyThatTheAssemblyOrderIsReadyForPickup,
    NotifyThatTheAssemblyOrdersAreReadyForPickup,
    NotifyThatTheBuyerHasDeclinedTheOrder,
    NotifyThatTheBuyerRefusedTheOrder,
    NotifyThatTheOrderHasBeenAcceptedByTheBuyer,
    NotifyThatTheOrdersAreDeclined,
    NotifyThatTheOrdersAreReceived,
    NotifyThatTheOrdersWereReceivedByTheBuyers,
    OrdersAndPositionsByProductSearchTexts,
    OrdersWithClientInformation,
    PaginationByGroups,
    PaginationByProductsWithinAGroup,
    PinFeedback,
    ProductCardsForCampaigns,
    ProductCardsInTrashList,
    ProductCardsList,
    ProductCardsStatisticsPerDays,
    ProductCardsStatisticsPerPeriod,
    ProductData,
    RecoverProductCardFromTrash,
    RegenerateTheReport,
    RenameCampaign,
    ReplyToFeedback,
    ReportOnProductsWithMandatoryLabeling,
    ReturnProductByFeedbackId,
    SearchClustersStatistics,
    SearchTextsByProduct,
    SendMessage,
    SetBidsForSearchClusters,
    SetPricesAndDiscounts,
    SetSizePrices,
    SettingAndDeletingMinusPhrases,
    SetWbClubDiscounts,
    SizeData,
    StatusHistoryForCrossborderOrders,
    SuppliesList,
    TagManagementInTheProductCard,
    TopupOfTheCampaignBudget,
    TransferProductCardToTrash,
    TransferToAssembly,
    TransferToDelivery,
    UnpinFeedback,
    UpdateContactsList,
    UpdateInventory,
    UpdatePass,
    UpdateProductCards,
    UpdateTheTag,
    UpdateUsersAccessPermissions,
    UpdateWarehouse,
    UploadMediaFile,
    UploadMediaFilesViaLinks,
    WarehouseData,
    WbMethod,
    WorkingWithQuestions,
)
from ..types import (
    AcceptanceOptionsItem,
    ActiveAndInactiveSearchClusterListsItem,
    AddBoxesToTheSupplyItem,
    AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem,
    AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem,
    AddGtinToAssemblyOrdersItem,
    AddGtinToTheAssemblyOrdersItem,
    AddImeiToAssemblyOrdersItem,
    AddImeiToTheAssemblyOrdersItem,
    AddProductToThePromotionResponse,
    AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem,
    AddUinUniqueIdentificationNumberToAssemblyOrdersItem,
    AListOfSellerActiveOrInvitedUsersItem,
    AllAssemblyOrdersForReshipmentItem,
    AssemblyOrderMetadataResponse,
    AssemblyOrdersItem,
    AssemblyOrdersMetadataItem,
    AssemblyOrdersStatusesItem,
    AssemblyOrdersStickersItem,
    AssemblyOrderStatusesItem,
    ASuppliesListItem,
    B2BBuyerInformationItem,
    BalanceItem,
    BlockedProductCardsItem,
    BoxTariffsItem,
    BrandsItem,
    BuyerInformationItem,
    BuyersReturnApplicationsItem,
    CampaignBudgetResponse,
    CampaignsInformationItem,
    CampaignsListsItem,
    CampaignsStatisticsResponse,
    CancelAssemblyOrdersItem,
    CancelTheAssemblyOrdersItem,
    ChangingCampaignsBidsItem,
    ChangingTheListOfProductCardsInCampaignsItem,
    ChatEventsItem,
    ChatListItem,
    CheckIfTheOrderBelongsToTheBuyerResponse,
    CheckTheStatusResponse,
    ColorResponse,
    ConnectionCheckResponse,
    ContactsListItem,
    CountryOfOriginResponse,
    CourierInfoItem,
    CreateANewSupplyResponse,
    CreateAnInvitationForANewUserResponse,
    CreateATagResponse,
    CreateCampaignResponse,
    CreatePassResponse,
    CreateProductCardsResponse,
    CreateProductCardsWithMergeResponse,
    CreateTheReportResponse,
    CreateWarehouseResponse,
    DailySearchClustersStatisticsItem,
    DeleteAssemblyOrdersMetadataItem,
    DeleteTheTagResponse,
    DeliveryDateAndTimeItem,
    DocumentResponse,
    DocumentsCategoriesItem,
    DocumentsListItem,
    DocumentsResponse,
    FeedbacksListItem,
    GenderItem,
    GenerateTheReportResponse,
    GenerationOfSkusItem,
    GettingSellerPortalNewsItem,
    GroupDataItem,
    GroupedProductCardsStatisticsPerDaysItem,
    HiddenFromTheCatalogItem,
    HscodesItem,
    InformationAboutMediaCampaignItem,
    InformationOnCompletedOrdersItem,
    InformationOnPaidDeliveryResponse,
    InventoryItem,
    LimitsForTheProductCardsResponse,
    ListOfArchivedFeedbacksItem,
    ListOfCampaignMinusPhrasesItem,
    ListOfFailedProductCardsWithErrorsItem,
    ListOfMediaCampaignsResponse,
    ListOfPinnedAndUnpinnedFeedbackResponse,
    ListOfProductsForParticipatingInThePromotionItem,
    ListOfSearchClustersBidsItem,
    LogisticsAndStorageCostsMultiplierItem,
    MainPageResponse,
    MediaCampaignsNumberResponse,
    MediaCampaignStatisticsResponse,
    MergingOrSeparatingOfProductCardsResponse,
    MinimumBidsForProductCardsItem,
    NewAssemblyOrdersItem,
    NewAssemblyOrdersListItem,
    NewOrdersItem,
    NewOrdersListItem,
    NotifyThatTheAssemblyOrdersAreReadyForPickupItem,
    NotifyThatTheOrdersAreDeclinedItem,
    NotifyThatTheOrdersAreReceivedItem,
    NotifyThatTheOrdersWereReceivedByTheBuyersItem,
    NumberOfFeedbacksItem,
    NumberOfQuestionsItem,
    OfficesForPassResponse,
    OfficesResponse,
    OrderMetadataItem,
    OrdersAndPositionsByProductSearchTextsResponse,
    OrdersResponse,
    OrdersStatusesItem,
    OrdersStickersItem,
    OrdersWithClientInformationItem,
    PaginationByGroupsResponse,
    PaginationByProductsWithinAGroupResponse,
    PalletTariffsItem,
    ParentCategoriesOfTheBrandItem,
    PassesResponse,
    PinFeedbackResponse,
    PinnedAndUnpinnedFeedbackNumberResponse,
    PinnedFeedbackLimitsResponse,
    ProcessedUploadDetailsItem,
    ProcessedUploadStateResponse,
    ProductCardsForCampaignsResponse,
    ProductCardsInTrashListItem,
    ProductCardsListItem,
    ProductCardsStatisticsPerDaysResponse,
    ProductCardsStatisticsPerPeriodResponse,
    ProductCategoryCommissionResponse,
    ProductDataItem,
    ProductDetail,
    ProductLabelingItem,
    ProductsInQuarantineItem,
    ProductSizesWithPricesItem,
    ProductsParentCategoriesResponse,
    ProductsWithPricesByArticlesItem,
    ProductsWithPricesItem,
    PromotionsDetailsItem,
    PromotionsListItem,
    QuestionListItem,
    RealizationSalesReportResponse,
    ReceivingCostsHistoryResponse,
    ReceivingTheHistoryOfAccountTopupsResponse,
    RecommendedBidsForItemsAndSearchClustersItem,
    RecoverProductCardFromTrashResponse,
    RegenerateTheReportResponse,
    ReportItem,
    ReportOnProductsWithMandatoryLabelingItem,
    RetrieveInformationOnCompletedAssemblyOrdersItem,
    ReturnProductByFeedbackIdItem,
    ReturnTariffsItem,
    SalesResponse,
    SearchClustersStatisticsItem,
    SearchTextsByProductResponse,
    SeasonItem,
    SelfpurchasesItem,
    SellerBrandsItem,
    SellerInformationResponse,
    SellersBalanceResponse,
    SendMessageItem,
    SetPricesAndDiscountsResponse,
    SetSizePricesResponse,
    SetWbClubDiscountsResponse,
    SizeDataItem,
    StatusHistoryForCrossborderOrdersItem,
    StickersForAssemblyOrdersWithDeliveryToPickupPointItem,
    StickersForCrossborderAssemblyOrdersItem,
    SubjectCharacteristicsItem,
    SubjectsForCampaignsResponse,
    SubjectsListItem,
    SubstitutionsAndIncorrectAttachmentsItem,
    SuppliesListResponse,
    SupplyAssemblyOrderIdsItem,
    SupplyBoxesListItem,
    SupplyDetailsResponse,
    SupplyPackageResponse,
    SupplyProductsResponse,
    SupplyTariffsResponse,
    TagManagementInTheProductCardResponse,
    TagsListResponse,
    TheFeedbackByIdItem,
    TheQuestionByIdItem,
    TheReportsListItem,
    TheSupplyBoxQrCodeStickersItem,
    TheSupplyQrCodeResponse,
    TopupOfTheCampaignBudgetResponse,
    TransferProductCardToTrashResponse,
    TransitDirectionsResponse,
    UnansweredFeedbacksItem,
    UnansweredQuestionsItem,
    UnpinFeedbackResponse,
    UnprocessedUploadDetailsItem,
    UnprocessedUploadStateResponse,
    UnseenFeedbacksAndQuestionsItem,
    UpdateProductCardsResponse,
    UpdateTheTagResponse,
    UploadMediaFileResponse,
    UploadMediaFilesViaLinksResponse,
    VatRateItem,
    WarehouseDataItem,
    WarehouseMeasurementsItem,
    WarehouseResponse,
    WarehousesListResponse,
    WarehousesResponse,
    WorkingWithQuestionsItem,
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

    async def acceptance_options(
        self,
        warehouse_id: int | None = None,
    ) -> list[AcceptanceOptionsItem]:
        """
        The method returns information about warehouses and package types available for supply. The
        warehouseslist is determined by product's barcode and quantity

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Information-for-Forming-Supplies/paths/~1api~1v1~1acceptance~1options/post

        :param warehouse_id: Warehouse ID. If the parameter is not specified, data for all
                             warehousesis returned. **Maximum is one value**
        :return: list[AcceptanceOptionsItem]
        """
        call = AcceptanceOptions(warehouse_id=warehouse_id)
        return await self(call)

    async def active_and_inactive_search_cluster_lists(
        self,
        items: list[Any] = None,
    ) -> list[ActiveAndInactiveSearchClusterListsItem]:
        """
        Returns lists of active and inactive search clusters with at least 100 views. Request limit
        perone seller's account:

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1list/post
        :return: list[ActiveAndInactiveSearchClusterListsItem]
        """
        call = ActiveAndInactiveSearchClusterLists(items=items)
        return await self(call)

    async def add_assembly_orders_to_the_supply(
        self,
        supply_id: str,
        orders: list[int] | None = None,
    ) -> None:
        """
        The method adds up to 100 [assembly
        orders](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get)to the
        supplyand moves it to the `confirm`
        [status](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1status/post).

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1marketplace~1v3~1supplies~1%7BsupplyId%7D~1orders/patch

        :param supply_id: Supply ID
        :param orders: Assembly order IDs
        :return: None
        """
        call = AddAssemblyOrdersToTheSupply(supply_id=supply_id, orders=orders)
        return await self(call)

    async def add_boxes_to_the_supply(
        self,
        supply_id: str,
        amount: int = None,
    ) -> list[AddBoxesToTheSupplyItem]:
        """
        Adds the required number of boxes to the supply. You should add boxes only to supplies
        shippedto the pickup points. You can add boxes to an open supply only. You can add as many
        boxesas there are items in the supply, plus one more box.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx/post

        :param supply_id: Supply ID
        :param amount: Boxes amount to add to the supply.
        :return: list[AddBoxesToTheSupplyItem]
        """
        call = AddBoxesToTheSupply(supply_id=supply_id, amount=amount)
        return await self(call)

    async def add_custom_declaration_number_to_the_order(
        self,
        order_id: int,
        customs_declaration: str | None = None,
    ) -> None:
        """
        The method updates the customs declaration number in the [metadata of the assembly
        order](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1meta/post).

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1%7BorderId%7D~1meta~1customs-declaration/put

        :param order_id: Assembly order ID
        :param customs_declaration: Customs declaration number
        :return: None
        """
        call = AddCustomDeclarationNumberToTheOrder(
            order_id=order_id,
            customs_declaration=customs_declaration,
        )
        return await self(call)

    async def add_custom_declaration_to_the_orders(
        self,
        orders: list[dict[str, Any]] | None = None,
    ) -> None:
        """
        Sets the cargo customs declaration number in the metadata of the assembly orders.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1customs-declaration/post
        :return: None
        """
        call = AddCustomDeclarationToTheOrders(orders=orders)
        return await self(call)

    async def add_data_matrix_code_to_the_assembly_order(
        self,
        order_id: int,
        sgtins: list[str] | None = None,
    ) -> None:
        """
        The method allows attaching a Data Matrix code [Chestny ZNAK](https://chestnyznak.ru/en) to
        anassembly order.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1sgtin/put

        :param order_id: Assembly order ID
        :param sgtins: List of Data Matrix codes.
        :return: None
        """
        call = AddDataMatrixCodeToTheAssemblyOrder(order_id=order_id, sgtins=sgtins)
        return await self(call)

    async def add_data_matrix_code_to_the_order(
        self,
        order_id: int,
        sgtins: list[str] | None = None,
    ) -> None:
        """
        This method allows you to assign a Data Matrix code (Chestny ZNAK marking) to an order. The
        assignmentof a Data Matrix code to an order is only possible if this field is returned in
        theresponse of the [Get order
        metadata](/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get)
        methodand the order is in the `confirm` status.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta~1sgtin/put

        :param order_id: Assembly order ID
        :param sgtins: List of Data Matrix codes. From 16 to 135 characters for one label
        :return: None
        """
        call = AddDataMatrixCodeToTheOrder(order_id=order_id, sgtins=sgtins)
        return await self(call)

    async def add_data_matrix_codes_to_assembly_orders_chestny_znak(
        self,
        orders: list[Any] = None,
    ) -> list[AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem]:
        """
        Sets the Data Matrix code (Chestny ZNAK marking) for the assembly orders. You can set the
        DataMatrix code only for orders in the `confirm` status and if the field `sgtin` is
        returnedin the response of the [Get order
        metadata](orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post)
        method.For more information about Data Matrix Codes please check:
        https://chestnyznak.ru/en/.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1sgtin/post
        :return: list[AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem]
        """
        call = AddDataMatrixCodesToAssemblyOrdersChestnyZnak(orders=orders)
        return await self(call)

    async def add_data_matrix_codes_to_the_assembly_orders_chestny_znak(
        self,
        orders: list[Any] = None,
    ) -> list[AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem]:
        """
        The method sets Data Matrix codes (Chestny ZNAK) to the [assembly orders
        metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).
        Youcan set the Data Matrix codes only for orders in the `confirm` status and if the field
        `sgtin`is returned in the response of the [Get order
        metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post)
        method.You can get the uploaded Data Matrix codes in the [assembly orders
        metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1sgtin/post
        :return: list[AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem]
        """
        call = AddDataMatrixCodesToTheAssemblyOrdersChestnyZnak(orders=orders)
        return await self(call)

    async def add_expiration_date_to_the_assembly_order(
        self,
        order_id: int,
        expiration: str | None = None,
    ) -> None:
        """
        Sets the expiration date for the assembly order. The expiration date can only be added for
        assemblyorders that are delivered by WB and are in the `confirm` status. You can get the
        uploadeddata in the [metadata of the assembly
        order](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1meta/post).
        Tochange the expiration date, send a request with the new date. It is impossible to remove
        theexpiration date from the metadata of the assembly order.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1expiration/put

        :param order_id: Assembly order ID
        :param expiration: The date until which the product is valid. No less than 30 days from the
                           currentdate.
        :return: None
        """
        call = AddExpirationDateToTheAssemblyOrder(order_id=order_id, expiration=expiration)
        return await self(call)

    async def add_gtin_to_assembly_orders(
        self,
        orders: list[Any] = None,
    ) -> list[AddGtinToAssemblyOrdersItem]:
        """
        Sets the GTIN, Belarus product unique identifier, for the assembly order
        metadata(./orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).
        Theassembly order can only have one GTIN. You can set the GTIN only for orders in the
        `confirmed`
        [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
        andthat are delivered by Wildberries.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1gtin/post
        :return: list[AddGtinToAssemblyOrdersItem]
        """
        call = AddGtinToAssemblyOrders(orders=orders)
        return await self(call)

    async def add_gtin_to_the_assembly_order(
        self,
        order_id: int,
        gtin: str = None,
    ) -> None:
        """
        Sets the GTIN (Belarus product unique identifier) for the assembly order. The assembly
        ordercan only have one GTIN. You can add the code only for assembly orders in the `confirm`
        status.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1gtin/put

        :param order_id: Assembly order ID
        :param gtin: GTIN
        :return: None
        """
        call = AddGtinToTheAssemblyOrder(order_id=order_id, gtin=gtin)
        return await self(call)

    async def add_gtin_to_the_assembly_orders(
        self,
        orders: list[Any] = None,
    ) -> list[AddGtinToTheAssemblyOrdersItem]:
        """
        The method sets the GTIN, Belarus product unique identifier, for the for the assembly
        orders
        [metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).
        Theassembly order can only have one GTIN. You can add the GTIN only for assembly orders in
        the`confirm`
        [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
        andthat are delivered by WB.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1gtin/post
        :return: list[AddGtinToTheAssemblyOrdersItem]
        """
        call = AddGtinToTheAssemblyOrders(orders=orders)
        return await self(call)

    async def add_gtin_to_the_order(
        self,
        order_id: int,
        gtin: str = None,
    ) -> None:
        """
        Sets the GTIN (Belarus product unique identifier) for the order. The order can only have
        oneGTIN. You can add the code only for orders in the `confirmed` status.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta~1gtin/put

        :param order_id: Assembly order ID
        :param gtin: GTIN
        :return: None
        """
        call = AddGtinToTheOrder(order_id=order_id, gtin=gtin)
        return await self(call)

    async def add_imei_to_assembly_orders(
        self,
        orders: list[Any] = None,
    ) -> list[AddImeiToAssemblyOrdersItem]:
        """
        Sets the IMEI for the [assembly orders
        metadata](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).
        Theassembly order can have only one IMEI. You can add the IMEI only for orders in the
        `confirmed`
        [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
        andthat are delivered by Wildberries.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1imei/post
        :return: list[AddImeiToAssemblyOrdersItem]
        """
        call = AddImeiToAssemblyOrders(orders=orders)
        return await self(call)

    async def add_imei_to_the_assembly_order(
        self,
        order_id: int,
        imei: str = None,
    ) -> None:
        """
        Sets the IMEI for the assembly order. The assembly order can have only one IMEI. If a
        devicehas two IMEIs — **IMEI** and **IMEI2** or **IMEI1** and **IMEI2** — you should only
        specify**IMEI** or **IMEI1**. You don't need to specify **IMEI2**. You can add the code
        onlyfor assembly orders in the `confirm` status.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1imei/put

        :param order_id: Assembly order ID
        :param imei: IMEI
        :return: None
        """
        call = AddImeiToTheAssemblyOrder(order_id=order_id, imei=imei)
        return await self(call)

    async def add_imei_to_the_assembly_orders(
        self,
        orders: list[Any] = None,
    ) -> list[AddImeiToTheAssemblyOrdersItem]:
        """
        Sets the IMEI for the [assembly orders
        metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).
        Theassembly order can have only one IMEI. You can add the IMEI only for assembly orders in
        the`confirm`
        [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
        thatare delivered by Wildberries.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1imei/post
        :return: list[AddImeiToTheAssemblyOrdersItem]
        """
        call = AddImeiToTheAssemblyOrders(orders=orders)
        return await self(call)

    async def add_imei_to_the_order(
        self,
        order_id: int,
        imei: str = None,
    ) -> None:
        """
        Sets the IMEI for the order. The order can have only one IMEI. You can add the code only
        fororders in the `confirmed` status.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta~1imei/put

        :param order_id: Assembly order ID
        :param imei: IMEI
        :return: None
        """
        call = AddImeiToTheOrder(order_id=order_id, imei=imei)
        return await self(call)

    async def add_product_to_the_promotion(
        self,
        data: dict[str, Any] | None = None,
    ) -> list[AddProductToThePromotionResponse]:
        """
        Creates a product upload for the promotion. The upload status can be checked using
        [separate
        methods](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1tasks/get).

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Promotions-Calendar/paths/~1api~1v1~1calendar~1promotions~1upload/post

        :param data: Request data
        :return: list[AddProductToThePromotionResponse]
        """
        call = AddProductToThePromotion(data=data)
        return await self(call)

    async def add_uin_unique_identification_number_to_assembly_orders(
        self,
        orders: list[Any] = None,
    ) -> list[AddUinUniqueIdentificationNumberToAssemblyOrdersItem]:
        """
        Sets the UIN to the [assembly orders
        metadata](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post).
        Theorder can only have one UIN. You can add the UIN only for assembly orders in the
        `confirmed`
        [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
        andthat are delivered by Wildberries.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1uin/post
        :return: list[AddUinUniqueIdentificationNumberToAssemblyOrdersItem]
        """
        call = AddUinUniqueIdentificationNumberToAssemblyOrders(orders=orders)
        return await self(call)

    async def add_uin_unique_identification_number_to_the_assembly_order(
        self,
        order_id: int,
        uin: str = None,
    ) -> None:
        """
        Sets the UIN for the assembly order. The assembly order can only have one UIN. You can add
        thecode only for assembly orders in the `confirm` status.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1uin/put

        :param order_id: Assembly order ID
        :param uin: UIN
        :return: None
        """
        call = AddUinUniqueIdentificationNumberToTheAssemblyOrder(order_id=order_id, uin=uin)
        return await self(call)

    async def add_uin_unique_identification_number_to_the_order(
        self,
        order_id: int,
        uin: str = None,
    ) -> None:
        """
        Sets the UIN for the order. The order can only have one UIN. You can add the code only for
        ordersin the `confirmed` status.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta~1uin/put

        :param order_id: Assembly order ID
        :param uin: UIN
        :return: None
        """
        call = AddUinUniqueIdentificationNumberToTheOrder(order_id=order_id, uin=uin)
        return await self(call)

    async def add_uin_unique_identification_numbers_to_the_assembly_orders(
        self,
        orders: list[Any] = None,
    ) -> list[AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem]:
        """
        The method sets the UIN (Unique Identification Numbers) for the [assembly orders
        metadata](/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1info/post).
        Theorder can only have one UIN. You can add the UIN only for assembly orders in the
        `confirm`
        [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
        andthat are delivered by WB.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1marketplace~1v3~1click-collect~1orders~1meta~1uin/post
        :return: list[AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem]
        """
        call = AddUinUniqueIdentificationNumbersToTheAssemblyOrders(orders=orders)
        return await self(call)

    async def answer_buyers_application(
        self,
        id: str = None,
        action: str = None,
        comment: str | None = None,
    ) -> None:
        """
        Sends an answer to the buyers application for product return.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Returns/paths/~1api~1v1~1claim/patch

        :param id: Application ID
        :param action: Application action. Use one of the `actions` array values from the response
                       ofthe getting [buyers
                       applications](./user-communication#tag/Buyers-Returns/paths/~1api~1v1~1claims/get)
                       method
        :param comment: Comment. Only when `"action":"rejectcustom"` or `"action":"approvecc1"`.
                        When`"action":"rejectcustom"` this parameter is required
        :return: None
        """
        call = AnswerBuyersApplication(id=id, action=action, comment=comment)
        return await self(call)

    async def assign_a_data_matrix_code_to_the_assembly_order(
        self,
        order_id: int,
        sgtins: list[str] | None = None,
    ) -> None:
        """
        This method is deprecated. It will be removed on [May
        19](https://dev.wildberries.ru/en/release-notes?id=474)

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1v3~1click-collect~1orders~1%7BorderId%7D~1meta~1sgtin/put

        :param order_id: Assembly order ID
        :param sgtins: List of Data Matrix codes. From 16 to 135 symbols for one Data Matrix code
        :return: None
        """
        call = AssignADataMatrixCodeToTheAssemblyOrder(order_id=order_id, sgtins=sgtins)
        return await self(call)

    async def b2b_buyer_information(
        self,
        orders_ids: list[int] | None = None,
    ) -> list[B2BBuyerInformationItem]:
        """
        The method returns B2B buyers data by assembly orders ID: - Taxpayer Identification Number
        (TINor INN in Russian) - Code of Reason for Registration (CRR or KPP in Russian) - Company
        name

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1b2b~1info/post

        :param orders_ids: List of assembly order IDs
        :return: list[B2BBuyerInformationItem]
        """
        call = B2BBuyerInformation(orders_ids=orders_ids)
        return await self(call)

    async def buyer_information(
        self,
        orders: list[int] | None = None,
    ) -> list[BuyerInformationItem]:
        """
        The method returns buyers information by order IDs.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbw~1orders~1client/post

        :param orders: Assembly order IDs list
        :return: list[BuyerInformationItem]
        """
        call = BuyerInformation(orders=orders)
        return await self(call)

    async def cancel_assembly_orders(
        self,
        orders_ids: list[int] | None = None,
    ) -> list[CancelAssemblyOrdersItem]:
        """
        The method transfers [assembly orders](/openapi/orders-dbs#tag/DBS-Assembly-Orders) with
        the
        [statuses](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
        `new`,`confirm` и `deliver` to the status `cancel` — canceled by the supplier.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1cancel/post

        :param orders_ids: List of assembly order IDs
        :return: list[CancelAssemblyOrdersItem]
        """
        call = CancelAssemblyOrders(orders_ids=orders_ids)
        return await self(call)

    async def cancel_the_assembly_order(
        self,
        order_id: int,
    ) -> None:
        """
        Moves the assembly orders to `cancel` ("Canceled by the supplier") status.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1%7BorderId%7D~1cancel/patch

        :param order_id: Assembly order ID
        :return: None
        """
        call = CancelTheAssemblyOrder(order_id=order_id)
        return await self(call)

    async def cancel_the_assembly_orders(
        self,
        orders_ids: list[int] | None = None,
    ) -> list[CancelTheAssemblyOrdersItem]:
        """
        The method transfers [assembly
        orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)from the `new`,
        `confirm`,`prepare`
        [statuses](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
        tothe `cancel` — canceled by the seller — status.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1cancel/post

        :param orders_ids: List of assembly order IDs
        :return: list[CancelTheAssemblyOrdersItem]
        """
        call = CancelTheAssemblyOrders(orders_ids=orders_ids)
        return await self(call)

    async def cancel_the_order(
        self,
        order_id: int,
    ) -> None:
        """
        Moves the assembly order to `cancel` status — canceled by the seller.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1cancel/patch

        :param order_id: Assembly order ID
        :return: None
        """
        call = CancelTheOrder(order_id=order_id)
        return await self(call)

    async def changing_campaigns_bids(
        self,
        bids: list[dict[str, Any]] = None,
    ) -> list[ChangingCampaignsBidsItem]:
        """
        The method changes the bids of product cards by WB articles in campaigns: - with standard
        bid- with custom bid - with a `cpc` payment model — per click

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1api~1advert~1v1~1bids/patch

        :param bids: Bids in campaigns, kopecks
        :return: list[ChangingCampaignsBidsItem]
        """
        call = ChangingCampaignsBids(bids=bids)
        return await self(call)

    async def changing_placements_in_campaigns_with_custom_bid(
        self,
        placements: list[dict[str, Any]] = None,
    ) -> None:
        """
        The method allows you to change placements in campaigns with custom bid and per mille
        paymentmodel — `cpm`. For campaigns in statuses `4`, `9` and `11`.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1auction~1placements/put

        :param placements: Placements in campaigns
        :return: None
        """
        call = ChangingPlacementsInCampaignsWithCustomBid(placements=placements)
        return await self(call)

    async def changing_the_list_of_product_cards_in_campaigns(
        self,
        nms: list[dict[str, Any]] = None,
    ) -> list[ChangingTheListOfProductCardsInCampaignsItem]:
        """
        The method allows you to add and remove product cards in campaigns. For campaigns in
        statuses`4`, `9` and `11`. The current minimum bid is set for the added products.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1auction~1nms/patch

        :param nms: Product cards in campaigns
        :return: list[ChangingTheListOfProductCardsInCampaignsItem]
        """
        call = ChangingTheListOfProductCardsInCampaigns(nms=nms)
        return await self(call)

    async def check_if_the_order_belongs_to_the_buyer(
        self,
        order_code: str | None = None,
        passcode: str | None = None,
    ) -> list[CheckIfTheOrderBelongsToTheBuyerResponse]:
        """
        The method indicates whether the checked order belongs to the buyer based on the provided
        code.Available if at least one assembly order from the order is in `prepare` status — ready
        forpickup.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders~1client~1identity/post

        :param order_code: Unique buyer order ID
        :param passcode: Confirmation code
        :return: list[CheckIfTheOrderBelongsToTheBuyerResponse]
        """
        call = CheckIfTheOrderBelongsToTheBuyer(order_code=order_code, passcode=passcode)
        return await self(call)

    async def courier_info(
        self,
        orders: list[int] | None = None,
    ) -> list[CourierInfoItem]:
        """
        Method provides the courier's contact information and vehicle number based on the assembly
        orderID. For assembly orders in the statuses `confirm` and `complete`.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1courier/post

        :param orders: Assembly order IDs list
        :return: list[CourierInfoItem]
        """
        call = CourierInfo(orders=orders)
        return await self(call)

    async def create_a_new_supply(
        self,
        name: str | None = None,
    ) -> list[CreateANewSupplyResponse]:
        """
        **Supplies limitations**:

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies/post

        :param name: Supply name
        :return: list[CreateANewSupplyResponse]
        """
        call = CreateANewSupply(name=name)
        return await self(call)

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

    async def create_an_invitation_for_a_new_user(
        self,
        access: list[dict[str, Any]] | None = None,
        invite: dict[str, Any] = None,
    ) -> list[CreateAnInvitationForANewUserResponse]:
        """
        Method is available by Personal token

        Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1invite/post

        :param access: Access settings for seller account sections
        :return: list[CreateAnInvitationForANewUserResponse]
        """
        call = CreateAnInvitationForANewUser(access=access, invite=invite)
        return await self(call)

    async def create_campaign(
        self,
        name: str | None = None,
        nms: list[int] | None = None,
        bid_type: BidType | None = "manual",
        payment_type: PaymentType | None = "cpm",
        placement_types: list[str] | None = ("search",),
    ) -> list[CreateCampaignResponse]:
        """
        The method creates campaign: - with custom bid for promotion products in search and/or
        recommendations- with standard bid for promotion products both in search and
        recommendations

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1adv~1v2~1seacat~1save-ad/post

        :param name: Campaign name
        :param nms: Product card for this campaign. You can available product cards with [product
                    cardsfor
                    campaigns](./promotion#tag/Campaigns-Creation/paths/~1adv~1v2~1supplier~1nms/post)
                    method.Maximum of 50 products (`nm`)
        :param bid_type: Bid type:
        :param payment_type: Payment type:
        :param placement_types: Placements:
        :return: list[CreateCampaignResponse]
        """
        call = CreateCampaign(
            name=name,
            nms=nms,
            bid_type=bid_type,
            payment_type=payment_type,
            placement_types=placement_types,
        )
        return await self(call)

    async def create_pass(
        self,
        first_name: str = None,
        last_name: str = None,
        car_model: str = None,
        car_number: str = None,
        office_id: int = None,
    ) -> list[CreatePassResponse]:
        """
        Creates a supplier pass. The pass is valid for 48 hours from the time of creation. Maximum
        of1 request per 10 minutes per one seller's account

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes/post

        :param first_name: First name
        :param last_name: Last name
        :param car_model: Car model
        :param car_number: Car number
        :param office_id: Office ID
        :return: list[CreatePassResponse]
        """
        call = CreatePass(
            first_name=first_name,
            last_name=last_name,
            car_model=car_model,
            car_number=car_number,
            office_id=office_id,
        )
        return await self(call)

    async def create_product_cards(
        self,
    ) -> list[CreateProductCardsResponse]:
        """
        Creates products cards. You can specify product description and characteristics.

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
        respectively,you can create no more than 29 product cards in one request. The dimensions of
        theproducts can only be specified in `centimeters`, and the weight of packed products must
        bespecified in `kilograms`. If this method response is Success (`200`) but product card was
        notupdated, check errors using [list of failed nomenclature with
        errors](/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1error~1list/post).
        Productcards are created asynchronously. The process of synchronizing a new card with
        servicesmay take up to 30 minutes. During this time, you can't add inventory to warehouses
        andset prices.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload~1add/post

        :param imt_id: `imtID` of an individual product card or group of merged product cards to
                       whichthe created cards are added
        :param cards_to_add: Added product cards
        :return: list[CreateProductCardsWithMergeResponse]
        """
        call = CreateProductCardsWithMerge(imt_id=imt_id, cards_to_add=cards_to_add)
        return await self(call)

    async def create_the_report(
        self,
    ) -> list[CreateTheReportResponse]:
        """
        The method creates a task for generating a report with advanced seller analytics. You can
        createa CSV-version of [sales funnel](/openapi/analytics#tag/Sales-Funnel) or [search
        parameters](/openapi/analytics#tag/Search-Queries-for-Your-Items)report with grouping:

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post
        :return: list[CreateTheReportResponse]
        """
        call = CreateTheReport()
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

    async def daily_search_clusters_statistics(
        self,
        from_: str = None,
        to: str = None,
        items: list[dict[str, Any]] = None,
    ) -> list[DailySearchClustersStatisticsItem]:
        """
        Returns statistics (views, clicks, add-to-cart, orders, CTR, CPC, CPM, etc.) by search
        clustersfor the specified period detailed by day. Request limit per one seller's account:

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v1~1normquery~1stats/post

        :param from_: Period start date
        :param to: Period end date
        :return: list[DailySearchClustersStatisticsItem]
        """
        call = DailySearchClustersStatistics(from_=from_, to=to, items=items)
        return await self(call)

    async def delete_assembly_order_metadata(
        self,
        order_id: int,
        key: str | None = None,
    ) -> None:
        """
        Removes all assembly order metadata values for the passed key. Possible metadata are: -
        `imei`—
        [IMEI](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1imei/put)
        -`uin` —
        [UIN](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1uin/put)
        -`gtin` —
        [GTIN](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1gtin/put)
        -`sgtin` — [Data matrix
        code](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1sgtin/put)
        -`customsDeclaration` — [customs declaration
        number](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1%7BorderId%7D~1meta~1customs-declaration/put)

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta/delete

        :param order_id: Assembly order ID
        :param key: Name of the metadata to remove (`imei`, `uin`, `gtin`, `sgtin`,
                    `customsDeclaration`)
        :return: None
        """
        call = DeleteAssemblyOrderMetadata(order_id=order_id, key=key)
        return await self(call)

    async def delete_assembly_orders_metadata(
        self,
        key: str = None,
        order_ids: list[int] = None,
    ) -> list[DeleteAssemblyOrdersMetadataItem]:
        """
        Removes all [assembly order
        metadata](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1info/post)
        values.You can only delete one type of metadata in one request. Specify the metadata type
        inthe request: - `imei` —
        [IMEI](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1imei/post)
        -`uin` —
        [UIN](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1uin/post)
        -`gtin` —
        [GTIN](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1gtin/post)
        -`sgtin` — [Data Matrix
        code](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1sgtin/post)
        -`customsDeclaration` — [customs declaration
        number](/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1meta~1customs-declaration/post)

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Metadata/paths/~1api~1marketplace~1v3~1dbs~1orders~1meta~1delete/post

        :param key: Name of metadata to delete (**imei**, **uin**, **gtin**, **sgtin**). Only one
                    valueis passed
        :param order_ids: Assembly orders IDs list
        :return: list[DeleteAssemblyOrdersMetadataItem]
        """
        call = DeleteAssemblyOrdersMetadata(key=key, order_ids=order_ids)
        return await self(call)

    async def delete_bids_from_search_clusters(
        self,
        bids: list[Any] = None,
    ) -> None:
        """
        The method deletes the bids from search clusters. You can use this method only for
        campaignswith: - custom bid - a `cpm` payment model — per displays

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1bids/delete
        :return: None
        """
        call = DeleteBidsFromSearchClusters(bids=bids)
        return await self(call)

    async def delete_boxes_from_the_supply(
        self,
        supply_id: str,
        trbx_ids: list[str] = None,
    ) -> None:
        """
        The method deletes boxes from the supply. Available only while the supply is being
        assembled.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx/delete

        :param supply_id: Supply ID
        :param trbx_ids: List of box IDs to delete from the supply.
        :return: None
        """
        call = DeleteBoxesFromTheSupply(supply_id=supply_id, trbx_ids=trbx_ids)
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

    async def delete_order_metadata(
        self,
        order_id: int,
        key: str | None = None,
    ) -> None:
        """
        Removes all order metadata values for the passed key. Possible metadata is `imei`, `uin`,
        `gtin`,`sgtin`.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/delete

        :param order_id: Assembly order ID
        :param key: Name of metadata to delete (`imei`, `uin`, `gtin`, `sgtin`). Only one value is
                    passed
        :return: None
        """
        call = DeleteOrderMetadata(order_id=order_id, key=key)
        return await self(call)

    async def delete_the_pass(
        self,
        pass_id: int,
    ) -> None:
        """
        Deletes the seller's pass

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes~1%7BpassId%7D/delete

        :param pass_id: Pass ID
        :return: None
        """
        call = DeleteThePass(pass_id=pass_id)
        return await self(call)

    async def delete_the_supply(
        self,
        supply_id: str,
    ) -> None:
        """
        Deleted the supply if it is active and does not contain any assembly orders.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/delete

        :param supply_id: Supply ID
        :return: None
        """
        call = DeleteTheSupply(supply_id=supply_id)
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

    async def delete_user(
        self,
        deleted_user_id: int = None,
    ) -> None:
        """
        Method is available by Personal token

        Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1user/delete

        :param deleted_user_id: ID of the user whose access will be revoked
        :return: None
        """
        call = DeleteUser(deleted_user_id=deleted_user_id)
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

    async def delivery_date_and_time(
        self,
        orders: list[int] | None = None,
    ) -> list[DeliveryDateAndTimeItem]:
        """
        Method provides information about the delivery date and time selected by the buyer for
        orders.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1delivery-date/post

        :param orders: Assembly order IDs list
        :return: list[DeliveryDateAndTimeItem]
        """
        call = DeliveryDateAndTime(orders=orders)
        return await self(call)

    async def edit_response_to_feedback(
        self,
        id: str = None,
        text: str = None,
    ) -> None:
        """
        Allows you to edit an already sent response to the feedback. You can edit the response only
        oncewithin 60 days. There is no validation by `feedback ID`: if an incorrect value is
        providedin the request, you will not receive an error.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1answer/patch

        :param id: Feedback ID
        :param text: Reply text
        :return: None
        """
        call = EditResponseToFeedback(id=id, text=text)
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

    async def get_a_list_of_seller_active_or_invited_users(
        self,
        limit: int | None = 100,
        offset: int | None = 0,
        is_invite_only: bool | None = False,
    ) -> list[AListOfSellerActiveOrInvitedUsersItem]:
        """
        Method is available by Personal token

        Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1users/get

        :param limit: The number of active or invited users in the response
        :param offset: How many results to skip. For example, for the value 10, the response will
                       startwith the 11 element
        :param is_invite_only: - `true` — the list of invited users who have not yet activated
                               access
        :return: list[AListOfSellerActiveOrInvitedUsersItem]
        """
        call = GetAListOfSellerActiveOrInvitedUsers(
            limit=limit,
            offset=offset,
            is_invite_only=is_invite_only,
        )
        return await self(call)

    async def get_a_supplies_list(
        self,
        limit: int = None,
        next: int = None,
    ) -> list[ASuppliesListItem]:
        """
        Returns the supply list.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies/get

        :param limit: Pagination parameter. Sets the limit for the amount of data returned.
        :param next: Pagination parameter. Sets the value from which to retrieve the next batch. It
                     shouldstart at 0 to get the full list of data. For the subsequent requests,
                     youmust take the value from the `next` field in the response.
        :return: list[ASuppliesListItem]
        """
        call = GetASuppliesList(limit=limit, next=next)
        return await self(call)

    async def get_all_assembly_orders_for_reshipment(
        self,
    ) -> list[AllAssemblyOrdersForReshipmentItem]:
        """
        Returns all assembly orders that require re-shipment

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1supplies~1orders~1reshipment/get
        :return: list[AllAssemblyOrdersForReshipmentItem]
        """
        call = GetAllAssemblyOrdersForReshipment()
        return await self(call)

    async def get_assembly_order_metadata(
        self,
        order_id: int,
    ) -> list[AssemblyOrderMetadataResponse]:
        """
        This method is deprecated. It will be removed on [May
        19](https://dev.wildberries.ru/en/release-notes?id=474)

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Metadata/paths/~1api~1v3~1click-collect~1orders~1%7BorderId%7D~1meta/get

        :param order_id: Assembly order ID
        :return: list[AssemblyOrderMetadataResponse]
        """
        call = GetAssemblyOrderMetadata(order_id=order_id)
        return await self(call)

    async def get_assembly_order_statuses(
        self,
        orders_ids: list[int] | None = None,
    ) -> list[AssemblyOrderStatusesItem]:
        """
        Returns the statuses of [assembly orders](/openapi/orders-dbs#tag/DBS-Assembly-Orders)
        basedon the list of assembly order IDs.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post

        :param orders_ids: List of assembly order IDs
        :return: list[AssemblyOrderStatusesItem]
        """
        call = GetAssemblyOrderStatuses(orders_ids=orders_ids)
        return await self(call)

    async def get_assembly_orders(
        self,
        limit: int = None,
        next: int = None,
        date_from: int | None = None,
        date_to: int | None = None,
    ) -> list[AssemblyOrdersItem]:
        """
        Returns assembly orders information without current status. You can get data for a
        specifiedperiod, maximum of 30 calendar days per request.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get

        :param limit: Pagination parameter. Sets the limit for the amount of data returned.
        :param next: Pagination parameter. Sets the value from which to retrieve the next batch. It
                     shouldstart at 0 to get the full list of data. For the subsequent requests,
                     youmust take the value from the `next` field in the response.
        :param date_from: Period start date in Unix timestamp format. By default date is 30 days
                          beforethe request
        :param date_to: Period end date in Unix timestamp format
        :return: list[AssemblyOrdersItem]
        """
        call = GetAssemblyOrders(limit=limit, next=next, date_from=date_from, date_to=date_to)
        return await self(call)

    async def get_assembly_orders_metadata(
        self,
        orders: list[int] = None,
    ) -> list[AssemblyOrdersMetadataItem]:
        """
        The method returns metadata for [assembly
        orders](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get)by the list
        oftheir IDs. You can get the list of metadata available for an assembly order in the
        `requiredMeta`and `optionalMeta` fields in the response of the [Get New Assembly
        Orders](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1new/get)
        method.Possible metadata: - `imei` —
        [IMEI](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1imei/put)
        -`uin` —
        [UIN](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1uin/put)
        -`gtin` —
        [GTIN](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1gtin/put)
        -`sgtin` — [Data matrix
        code](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1sgtin/put)
        -`expiration` — [Expiration
        date](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1v3~1orders~1%7BorderId%7D~1meta~1expiration/put)
        -`customsDeclaration` — [customs declaration
        number](/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1%7BorderId%7D~1meta~1customs-declaration/put)

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Metadata/paths/~1api~1marketplace~1v3~1orders~1meta/post
        :return: list[AssemblyOrdersMetadataItem]
        """
        call = GetAssemblyOrdersMetadata(orders=orders)
        return await self(call)

    async def get_assembly_orders_statuses(
        self,
        orders: list[int] = None,
    ) -> list[AssemblyOrdersStatusesItem]:
        """
        Returns the statuses of assembly orders from the request.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1status/post

        :param orders: List of assembly order IDs
        :return: list[AssemblyOrdersStatusesItem]
        """
        call = GetAssemblyOrdersStatuses(orders=orders)
        return await self(call)

    async def get_assembly_orders_stickers(
        self,
        type: Type = None,
        width: Width = None,
        height: Height = None,
        orders: list[int] | None = None,
    ) -> list[AssemblyOrdersStickersItem]:
        """
        Returns a list of stickers according to the requested assembly orders. You can request a
        stickerin `svg`, `zplv` (vertical), `zplh` (horizontal) and `png` formats.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1stickers/post

        :param type: Sticker format
        :param width: Sticker width
        :param height: Sticker height
        :param orders: List of assembly order IDs
        :return: list[AssemblyOrdersStickersItem]
        """
        call = GetAssemblyOrdersStickers(type=type, width=width, height=height, orders=orders)
        return await self(call)

    async def get_balance(
        self,
    ) -> list[BalanceItem]:
        """
        The method allows to get information about the seller's net, balance and bonuses

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1balance/get
        :return: list[BalanceItem]
        """
        call = GetBalance()
        return await self(call)

    async def get_blocked_product_cards(
        self,
        sort: Sort2 = None,
        order: Order2 = None,
    ) -> list[BlockedProductCardsItem]:
        """
        Returns the list of [blocked product
        cards](https://seller.wildberries.ru/analytics-reports/banned-products)

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Hidden-Products/paths/~1api~1v1~1analytics~1banned-products~1blocked/get

        :param sort: Sorting
        :param order: Data order
        :return: list[BlockedProductCardsItem]
        """
        call = GetBlockedProductCards(sort=sort, order=order)
        return await self(call)

    async def get_box_tariffs(
        self,
        date: str = None,
    ) -> list[BoxTariffsItem]:
        """
        For items inventory supplied to the warehouse in boxes, the method returns the
        [rates](https://seller.wildberries.ru/dynamic-product-categories):- for delivery from
        warehouseor sorting center to the buyer - for delivery from the buyer to the sorting center
        -for storage on WB warehouse

        Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Stock-Tariffs/paths/~1api~1v1~1tariffs~1box/get

        :param date: Date, YYYY-MM-DD
        :return: list[BoxTariffsItem]
        """
        call = GetBoxTariffs(date=date)
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
                     databatch
        :return: list[BrandsItem]
        """
        call = GetBrands(subject_id=subject_id, next=next)
        return await self(call)

    async def get_buyers_return_applications(
        self,
        is_archive: bool = None,
        id: str | None = None,
        limit: int | None = 50,
        offset: int | None = 0,
        nm_id: int | None = None,
    ) -> list[BuyersReturnApplicationsItem]:
        """
        Returns buyers applications for product returns for the current 14 days.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Returns/paths/~1api~1v1~1claims/get

        :param is_archive: Application status:
        :param id: Application ID
        :param limit: Number of applications in the response
        :param offset: From which element to start outputting data. `0` by default
        :param nm_id: WB article
        :return: list[BuyersReturnApplicationsItem]
        """
        call = GetBuyersReturnApplications(
            is_archive=is_archive,
            id=id,
            limit=limit,
            offset=offset,
            nm_id=nm_id,
        )
        return await self(call)

    async def get_campaign_budget(
        self,
        id: int = None,
    ) -> list[CampaignBudgetResponse]:
        """
        The method allows to get information about the budget of a campaign.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1budget/get

        :param id: Campaign ID
        :return: list[CampaignBudgetResponse]
        """
        call = GetCampaignBudget(id=id)
        return await self(call)

    async def get_campaigns_information(
        self,
        ids: str | None = None,
        statuses: str | None = None,
        payment_type: PaymentType | None = None,
    ) -> list[CampaignsInformationItem]:
        """
        The method returns information about campaigns with standard or custom bid via statuses,
        paymenttypes and IDs.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns/paths/~1api~1advert~1v2~1adverts/get

        :param ids: Campaign IDs, maximum 50
        :param statuses: Campaign statuses:
        :param payment_type: Payment type:
        :return: list[CampaignsInformationItem]
        """
        call = GetCampaignsInformation(ids=ids, statuses=statuses, payment_type=payment_type)
        return await self(call)

    async def get_campaigns_lists(
        self,
    ) -> list[CampaignsListsItem]:
        """
        Method allows to get campaigns lists grouped by type and status with information about last
        campaignchange date.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns/paths/~1adv~1v1~1promotion~1count/get
        :return: list[CampaignsListsItem]
        """
        call = GetCampaignsLists()
        return await self(call)

    async def get_campaigns_statistics(
        self,
        ids: str = None,
        begin_date: str = None,
        end_date: str = None,
    ) -> list[CampaignsStatisticsResponse]:
        """
        The method generates statistics for campaigns, regardless of their type. The maximum period
        ina request is 31 days. For campaigns in statuses `7`, `9` and `11`.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v3~1fullstats/get

        :param ids: Campaign IDs, maximum 50 values
        :param begin_date: Start date for the interval
        :param end_date: End date for the interval
        :return: list[CampaignsStatisticsResponse]
        """
        call = GetCampaignsStatistics(ids=ids, begin_date=begin_date, end_date=end_date)
        return await self(call)

    async def get_chat_events(
        self,
        next: int | None = None,
    ) -> list[ChatEventsItem]:
        """
        Returns an event list for all chats.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1events/get

        :param next: Paginator. Retrieve the next data packet starting from this moment. Format:
                     Unixtimestamp **with milliseconds**
        :return: list[ChatEventsItem]
        """
        call = GetChatEvents(next=next)
        return await self(call)

    async def get_chat_list(
        self,
    ) -> list[ChatListItem]:
        """
        Returns a list of all seller's chats.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1chats/get
        :return: list[ChatListItem]
        """
        call = GetChatList()
        return await self(call)

    async def get_check_the_status(
        self,
        task_id: str,
    ) -> list[CheckTheStatusResponse]:
        """
        Returns the status of the generation task

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Warehouses-Inventory-Report/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1status/get

        :param task_id: Generation task ID
        :return: list[CheckTheStatusResponse]
        """
        call = GetCheckTheStatus(task_id=task_id)
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

    async def get_connection_check(
        self,
    ) -> list[ConnectionCheckResponse]:
        """
        Checks: 1. Whether the request successfully reaches the WB API. 2. The validity of the
        authorizationtoken and request URL. 3. Whether the token category matches the service.

        Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/WB-API-Connection-Check/paths/~1ping/get
        :return: list[ConnectionCheckResponse]
        """
        call = GetConnectionCheck()
        return await self(call)

    async def get_contacts_list(
        self,
        warehouse_id: int,
    ) -> list[ContactsListItem]:
        """
        Returns a list of contacts linked to the seller's warehouse. Only for warehouses with
        deliverytype `3` — Delivery by WB courier (DBW).

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

    async def get_create_the_report(
        self,
        locale: str | None = "ru",
        group_by_brand: bool | None = False,
        group_by_subject: bool | None = False,
        group_by_sa: bool | None = False,
        group_by_nm: bool | None = False,
        group_by_barcode: bool | None = False,
        group_by_size: bool | None = False,
        filter_pics: int | None = 0,
        filter_volume: int | None = 0,
    ) -> list[CreateTheReportResponse]:
        """
        Creates a task for report generation. The parameters `groupBy` and `filter` can be set in
        anycombination — similar to the
        [version](https://seller.wildberries.ru/analytics-reports/warehouse-remains)in the personal
        account.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Warehouses-Inventory-Report/paths/~1api~1v1~1warehouse_remains/get

        :param locale: Language of the `subjectName` and `warehouseName` response fields:
        :param group_by_brand: Group by brand
        :param group_by_subject: Group by subject
        :param group_by_sa: Group by seller's article
        :param group_by_nm: Group by WB article. If `groupByNm=true`, there will be `volume` field
                            inthe response
        :param group_by_barcode: Group by barcode
        :param group_by_size: Group by size
        :param filter_pics: Photo filter:
        :param filter_volume: Volume filter:
        :return: list[CreateTheReportResponse]
        """
        call = GetCreateTheReport(
            locale=locale,
            group_by_brand=group_by_brand,
            group_by_subject=group_by_subject,
            group_by_sa=group_by_sa,
            group_by_nm=group_by_nm,
            group_by_barcode=group_by_barcode,
            group_by_size=group_by_size,
            filter_pics=filter_pics,
            filter_volume=filter_volume,
        )
        return await self(call)

    async def get_delete_campaign(
        self,
        id: int = None,
    ) -> None:
        """
        The method allows to delete campaigns in the status `4` — ready to launch.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1delete/get

        :param id: Campaign ID
        :return: None
        """
        call = GetDeleteCampaign(id=id)
        return await self(call)

    async def get_document(
        self,
        service_name: str = None,
        extension: str = None,
    ) -> list[DocumentResponse]:
        """
        Returns one document

        Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1download/get

        :param service_name: Unique document ID
        :param extension: Document format
        :return: list[DocumentResponse]
        """
        call = GetDocument(service_name=service_name, extension=extension)
        return await self(call)

    async def get_documents(
        self,
        params: list[dict[str, Any]] | None = None,
    ) -> list[DocumentsResponse]:
        """
        Returns more than one document.

        Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1download~1all/post
        :return: list[DocumentsResponse]
        """
        call = GetDocuments(params=params)
        return await self(call)

    async def get_documents_categories(
        self,
        locale: str | None = "en",
    ) -> list[DocumentsCategoriesItem]:
        """
        Returns documents categories

        Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1categories/get

        :param locale: `title` field language:
        :return: list[DocumentsCategoriesItem]
        """
        call = GetDocumentsCategories(locale=locale)
        return await self(call)

    async def get_documents_list(
        self,
        locale: str | None = "en",
        begin_time: str | None = None,
        end_time: str | None = None,
        sort: Sort4 | None = "date",
        order: Order2 | None = "desc",
        category: str | None = None,
        service_name: str | None = None,
        limit: int | None = 50,
        offset: int | None = 0,
    ) -> list[DocumentsListItem]:
        """
        Returns seller's documents list

        Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1list/get

        :param locale: `category` field language:
        :param begin_time: Period start. Only with `endTime`
        :param end_time: Period end. Only with `beginTime`
        :param sort: Sorting:
        :param order: Data order:
        :param category: [Document
                         category](./financial-reports-and-accounting#tag/Documents/paths/~1api~1v1~1documents~1categories/get)
                         IDfrom the `name` field
        :param service_name: Unique document ID
        :param limit: The maximum number of response rows
        :param offset: From which row to start outputting data
        :return: list[DocumentsListItem]
        """
        call = GetDocumentsList(
            locale=locale,
            begin_time=begin_time,
            end_time=end_time,
            sort=sort,
            order=order,
            category=category,
            service_name=service_name,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def get_feedbacks_list(
        self,
        is_answered: bool = None,
        nm_id: int | None = None,
        take: int = None,
        skip: int = None,
        order: Order | None = None,
        date_from: int | None = None,
        date_to: int | None = None,
    ) -> list[FeedbacksListItem]:
        """
        The method allows you to get a list of feedbacks by the specified parameters with
        paginationand sorting

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks/get

        :param is_answered: If the feedback was answered:
        :param nm_id: WB article
        :param take: Number of feedbacks (max. 5 000)
        :param skip: Number of feedbacks for skip (max. 199990)
        :param order: Sorting of feedbacks by date (dateAsc/dateDesc)
        :param date_from: The start date of the period in Unix timestamp format
        :param date_to: The end date of the period in Unix timestamp format
        :return: list[FeedbacksListItem]
        """
        call = GetFeedbacksList(
            is_answered=is_answered,
            nm_id=nm_id,
            take=take,
            skip=skip,
            order=order,
            date_from=date_from,
            date_to=date_to,
        )
        return await self(call)

    async def get_file_from_the_message(
        self,
        id: str,
    ) -> None:
        """
        The method provides a file or image from the message by its ID.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1download~1%7Bid%7D/get

        :param id: File ID from the `downloadID` field in the [chat
                   events](./user-communication#tag/Buyers-Chat/paths/~1api~1v1~1seller~1events/get)
                   method
        :return: None
        """
        call = GetFileFromTheMessage(id=id)
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

    async def get_generate_the_report(
        self,
        date_from: str = None,
        date_to: str = None,
    ) -> list[GenerateTheReportResponse]:
        """
        Create a task to generate a report. Maximum of report period — 8 days

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Paid-Storage/paths/~1api~1v1~1paid_storage/get

        :param date_from: Start of the report period, RFC3339 format. Date or date and time, for
                          example:
        :param date_to: End of the report period, RFC3339 format. Date or date and time, for
                        example:
        :return: list[GenerateTheReportResponse]
        """
        call = GetGenerateTheReport(date_from=date_from, date_to=date_to)
        return await self(call)

    async def get_getting_seller_portal_news(
        self,
        from_: str | None = None,
        from_id: int | None = None,
    ) -> list[GettingSellerPortalNewsItem]:
        """
        The method allows getting news from the seller portal. To receive a successful response,
        oneof the parameters `from` or `fromID` must be specified. You can get up to 100 news items
        perrequest.

        Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/News-API/paths/~1api~1communications~1v2~1news/get

        :param from_: Date from which to get news
        :param from_id: The news ID, starting from which — including it — you need to get the list
                        ofnews
        :return: list[GettingSellerPortalNewsItem]
        """
        call = GetGettingSellerPortalNews(from_=from_, from_id=from_id)
        return await self(call)

    async def get_hidden_from_the_catalog(
        self,
        sort: Sort3 = None,
        order: Order2 = None,
    ) -> list[HiddenFromTheCatalogItem]:
        """
        Returns the list of products [hidden from the
        catalog](https://seller.wildberries.ru/analytics-reports/banned-products/shadowed)

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Hidden-Products/paths/~1api~1v1~1analytics~1banned-products~1shadowed/get

        :param sort: Sorting
        :param order: Data order
        :return: list[HiddenFromTheCatalogItem]
        """
        call = GetHiddenFromTheCatalog(sort=sort, order=order)
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

    async def get_information_about_media_campaign(
        self,
        id: int = None,
    ) -> list[InformationAboutMediaCampaignItem]:
        """
        The method allows to get information about a media campaign

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Media/paths/~1adv~1v1~1advert/get

        :param id: Media campaign ID
        :return: list[InformationAboutMediaCampaignItem]
        """
        call = GetInformationAboutMediaCampaign(id=id)
        return await self(call)

    async def get_information_on_completed_orders(
        self,
        limit: int = None,
        next: int = None,
        date_from: int = None,
        date_to: int = None,
    ) -> list[InformationOnCompletedOrdersItem]:
        """
        Returns information on completed orders (either canceled or sold). You can get data for a
        specifiedperiod, maximum of 30 calendar days per request.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders/get

        :param limit: Pagination parameter. Sets the limit for the amount of data returned
        :param next: Pagination parameter. Sets the value from which to retrieve the next batch. It
                     shouldstart at `0` to get the full list of data. For the subsequent requests,
                     youmust take the value from the `next` field in the response
        :param date_from: Period start date in Unix timestamp format
        :param date_to: Period end date in Unix timestamp format
        :return: list[InformationOnCompletedOrdersItem]
        """
        call = GetInformationOnCompletedOrders(
            limit=limit,
            next=next,
            date_from=date_from,
            date_to=date_to,
        )
        return await self(call)

    async def get_information_on_paid_delivery(
        self,
        groups: list[str] | None = None,
    ) -> list[InformationOnPaidDeliveryResponse]:
        """
        The method provides information on paid delivery for assembly orders that have been
        receivedat a single warehouse (warehouseId) as part of a single buyer transaction
        (orderUid).

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1groups~1info/post

        :param groups: List of `groupId` values. Can be obtained from
                       [new](./orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders~1new/get)
                       and
                       [completed](./orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders/get)
                       assemblyorders.
        :return: list[InformationOnPaidDeliveryResponse]
        """
        call = GetInformationOnPaidDelivery(groups=groups)
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

    async def get_launch_campaign(
        self,
        id: int = None,
    ) -> None:
        """
        The method allows to run campaigns that are in statuses `4` — ready to launch or `11` —
        pausedcampaign. To run a campaign, check its budget. If the budget is insufficient,
        replenishit.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1start/get

        :param id: Campaign ID
        :return: None
        """
        call = GetLaunchCampaign(id=id)
        return await self(call)

    async def get_limits_for_the_product_cards(
        self,
    ) -> list[LimitsForTheProductCardsResponse]:
        """
        The method allows to get separately free and paid vendor limits for creating product cards.
        Tocalculate the number of cards that can be created, use the formula: (freeLimits +
        paidLimits)- Number of cards created. All cards that can be obtained using the [product
        cards
        list](/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post)
        and[list of product cards that are in the
        trash](/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1trash/post)
        methodsare considered created.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1limits/get
        :return: list[LimitsForTheProductCardsResponse]
        """
        call = GetLimitsForTheProductCards()
        return await self(call)

    async def get_list_of_archived_feedbacks(
        self,
        nm_id: int | None = None,
        take: int = None,
        skip: int = None,
        order: Order | None = None,
    ) -> list[ListOfArchivedFeedbacksItem]:
        """
        The method allows you to get a list of archived feedbacks. The feedback becomes archived
        if:- A response to the feedback is received. - No response to the feedback is received
        within30 days. - The feedback contains no text or photos.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1archive/get

        :param nm_id: WB article
        :param take: Number of feedbacks (max. 5 000)
        :param skip: Number of feedbacks for skip
        :param order: Sorting of feedbacks by date (dateAsc/dateDesc)
        :return: list[ListOfArchivedFeedbacksItem]
        """
        call = GetListOfArchivedFeedbacks(nm_id=nm_id, take=take, skip=skip, order=order)
        return await self(call)

    async def get_list_of_media_campaigns(
        self,
        status: int | None = None,
        type: int | None = None,
        limit: int | None = None,
        offset: int | None = None,
        order: str | None = None,
        direction: str | None = None,
    ) -> list[ListOfMediaCampaignsResponse]:
        """
        The method allows to get the list of media campaigns of the seller

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Media/paths/~1adv~1v1~1adverts/get

        :param status: Media campaign status:
        :param type: Media campaign type:
        :param limit: Number of campaigns in the response
        :param offset: Offset relative to the first media campaign
        :param order: The order in which the response is displayed:
        :param direction: Sorting order:
        :return: list[ListOfMediaCampaignsResponse]
        """
        call = GetListOfMediaCampaigns(
            status=status,
            type=type,
            limit=limit,
            offset=offset,
            order=order,
            direction=direction,
        )
        return await self(call)

    async def get_list_of_pinned_and_unpinned_feedback(
        self,
        state: State | None = None,
        pin_on: PinOn | None = None,
        imt_id: int | None = None,
        nm_id: int | None = None,
        feedback_id: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
        next: int | None = None,
        limit: int | None = 500,
    ) -> list[ListOfPinnedAndUnpinnedFeedbackResponse]:
        """
        The method allows to get the list of pinned and unpinned feedback. Only automatically
        unpinnedfeedback cause of the reasons specified in the response in the `unpinnedCause`
        fieldare considered unpinned.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/get

        :param state: If the feedback is pinned:
        :param pin_on: Feedback pinning placement:
        :param imt_id: Merged product cards ID.
        :param nm_id: WB article
        :param feedback_id: Feedback ID
        :param date_from: The date the first feedback in the list was pinned
        :param date_to: The date the last feedback in the list was pinned
        :param next: The last pinning operation ID (paginator)
        :param limit: Feedback number per page (pagination)
        :return: list[ListOfPinnedAndUnpinnedFeedbackResponse]
        """
        call = GetListOfPinnedAndUnpinnedFeedback(
            state=state,
            pin_on=pin_on,
            imt_id=imt_id,
            nm_id=nm_id,
            feedback_id=feedback_id,
            date_from=date_from,
            date_to=date_to,
            next=next,
            limit=limit,
        )
        return await self(call)

    async def get_list_of_products_for_participating_in_the_promotion(
        self,
        promotion_id: int = None,
        in_action: bool = False,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[ListOfProductsForParticipatingInThePromotionItem]:
        """
        Returns a list of products suitable for participation in the promotion.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Promotions-Calendar/paths/~1api~1v1~1calendar~1promotions~1nomenclatures/get

        :param promotion_id: Promotion ID
        :param in_action: Participates in the promotion:
        :param limit: Number of requested products
        :param offset: From which element to start outputting data
        :return: list[ListOfProductsForParticipatingInThePromotionItem]
        """
        call = GetListOfProductsForParticipatingInThePromotion(
            promotion_id=promotion_id,
            in_action=in_action,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def get_logistics_and_storage_costs_multiplier(
        self,
        date_from: str | None = None,
        date_to: str = None,
        limit: int = None,
        offset: int | None = 0,
    ) -> list[LogisticsAndStorageCostsMultiplierItem]:
        """
        The method returns a report with [logistics and storage costs
        multiplier](https://seller.wildberries.ru/analytics-reports/dimensions-penalties)

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1analytics~1v1~1measurement-penalties/get

        :param date_from: Report period start. By default the date when data for the report was
                          firstreceived is used
        :param date_to: Report period end
        :param limit: Number of retentions in the response
        :param offset: How many results to skip. For example, with value `10`, the response will
                       startwith the 11 element
        :return: list[LogisticsAndStorageCostsMultiplierItem]
        """
        call = GetLogisticsAndStorageCostsMultiplier(
            date_from=date_from,
            date_to=date_to,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def get_media_campaigns_number(
        self,
    ) -> list[MediaCampaignsNumberResponse]:
        """
        Method allows you to get the number of the seller's media campaigns.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Media/paths/~1adv~1v1~1count/get
        :return: list[MediaCampaignsNumberResponse]
        """
        call = GetMediaCampaignsNumber()
        return await self(call)

    async def get_new_assembly_orders(
        self,
    ) -> list[NewAssemblyOrdersItem]:
        """
        Returns a list of all new [assembly
        orders](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get).

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1new/get
        :return: list[NewAssemblyOrdersItem]
        """
        call = GetNewAssemblyOrders()
        return await self(call)

    async def get_new_assembly_orders_list(
        self,
    ) -> list[NewAssemblyOrdersListItem]:
        """
        The method provides a list of all new [assembly
        orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)that the seller has at
        thetime of the request.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders~1new/get
        :return: list[NewAssemblyOrdersListItem]
        """
        call = GetNewAssemblyOrdersList()
        return await self(call)

    async def get_new_orders(
        self,
    ) -> list[NewOrdersItem]:
        """
        Returns a list of all new [orders](/openapi/orders-dbw#tag/DBW-Assembly-Orders).

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1new/get
        :return: list[NewOrdersItem]
        """
        call = GetNewOrders()
        return await self(call)

    async def get_new_orders_list(
        self,
    ) -> list[NewOrdersListItem]:
        """
        Returns a list of all new orders for the seller at the moment

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders~1new/get
        :return: list[NewOrdersListItem]
        """
        call = GetNewOrdersList()
        return await self(call)

    async def get_number_of_feedbacks(
        self,
        date_from: int | None = None,
        date_to: int | None = None,
        is_answered: bool | None = True,
    ) -> list[NumberOfFeedbacksItem]:
        """
        The method allows to get the number of feedbacks

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1count/get

        :param date_from: The start date of the period in Unix timestamp format
        :param date_to: The end date of the period in Unix timestamp format
        :param is_answered: If the feedback was answered:
        :return: list[NumberOfFeedbacksItem]
        """
        call = GetNumberOfFeedbacks(date_from=date_from, date_to=date_to, is_answered=is_answered)
        return await self(call)

    async def get_number_of_questions(
        self,
        date_from: int | None = None,
        date_to: int | None = None,
        is_answered: bool | None = True,
    ) -> list[NumberOfQuestionsItem]:
        """
        The method allows to get the number of questions for requested period

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions~1count/get

        :param date_from: The start date of the period in Unix timestamp format
        :param date_to: The end date of the period in Unix timestamp format
        :param is_answered: If the question was answered:
        :return: list[NumberOfQuestionsItem]
        """
        call = GetNumberOfQuestions(date_from=date_from, date_to=date_to, is_answered=is_answered)
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

    async def get_offices_for_pass(
        self,
    ) -> list[OfficesForPassResponse]:
        """
        Returns a list of offices that require a pass.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes~1offices/get
        :return: list[OfficesForPassResponse]
        """
        call = GetOfficesForPass()
        return await self(call)

    async def get_order_metadata(
        self,
        order_id: int,
    ) -> list[OrderMetadataItem]:
        """
        Returns assembly order metadata. The list of metadata available for the assembly order can
        beobtained in the [list of new assembly
        orders](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1new/get),
        field`requiredMeta`.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Metadata/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1meta/get

        :param order_id: Assembly order ID
        :return: list[OrderMetadataItem]
        """
        call = GetOrderMetadata(order_id=order_id)
        return await self(call)

    async def get_orders(
        self,
        date_from: str = None,
        flag: int | None = 0,
    ) -> list[OrdersResponse]:
        """
        The method returns order information. The data updated every 30 minutes.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1orders/get

        :param date_from: Date and time of last change on the order.
        :param flag: If parameter `flag=0` (or it doesn't exist in requests string), then call of
                     APImethods returns data,
        :return: list[OrdersResponse]
        """
        call = GetOrders(date_from=date_from, flag=flag)
        return await self(call)

    async def get_orders_statuses(
        self,
        orders: list[int] = None,
    ) -> list[OrdersStatusesItem]:
        """
        Returns the statuses of orders based on the provided list of assembly order IDs

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1status/post

        :param orders: Orders IDs list
        :return: list[OrdersStatusesItem]
        """
        call = GetOrdersStatuses(orders=orders)
        return await self(call)

    async def get_orders_stickers(
        self,
        type: Type = None,
        width: Width = None,
        height: Height = None,
        orders: list[int] | None = None,
    ) -> list[OrdersStickersItem]:
        """
        Returns a list of stickers for the [assembly
        orders](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1new/get)
        inthe
        [statuses](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1status/post):
        -`confirm` — on assembly - `complete` — on delivery

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1stickers/post

        :param type: Sticker format
        :param width: Sticker width
        :param height: Sticker height
        :param orders: Assembly order IDs list
        :return: list[OrdersStickersItem]
        """
        call = GetOrdersStickers(type=type, width=width, height=height, orders=orders)
        return await self(call)

    async def get_pallet_tariffs(
        self,
        date: str = None,
    ) -> list[PalletTariffsItem]:
        """
        For items supplied to the WB warehouse on pallets, the method returns the
        [cost](https://seller.wildberries.ru/dynamic-product-categories):- of delivery from
        warehouseto the buyer - of delivery from the buyer to warehouse - of storage on WB
        warehouse

        Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Stock-Tariffs/paths/~1api~1v1~1tariffs~1pallet/get

        :param date: Date, YYYY-MM-DD
        :return: list[PalletTariffsItem]
        """
        call = GetPalletTariffs(date=date)
        return await self(call)

    async def get_parent_categories_of_the_brand(
        self,
        locale: str | None = "ru",
        brand: str = None,
        date_from: str = None,
        date_to: str = None,
    ) -> list[ParentCategoriesOfTheBrandItem]:
        """
        Returns parent categories of the brand.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Share-of-Brand-in-Sales/paths/~1api~1v1~1analytics~1brand-share~1parent-subjects/get

        :param locale: Language of the response field `parentName`:
        :param brand: Brand
        :param date_from: Report period start, `YYYY-MM-DD`
        :param date_to: Report period end, `YYYY-MM-DD`
        :return: list[ParentCategoriesOfTheBrandItem]
        """
        call = GetParentCategoriesOfTheBrand(
            locale=locale,
            brand=brand,
            date_from=date_from,
            date_to=date_to,
        )
        return await self(call)

    async def get_passes(
        self,
    ) -> list[PassesResponse]:
        """
        Returns a list of all seller's passes.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes/get
        :return: list[PassesResponse]
        """
        call = GetPasses()
        return await self(call)

    async def get_pause_campaign(
        self,
        id: int = None,
    ) -> None:
        """
        Campaign in status `9` — active — can be paused

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1pause/get

        :param id: Campaign ID
        :return: None
        """
        call = GetPauseCampaign(id=id)
        return await self(call)

    async def get_pinned_and_unpinned_feedback_number(
        self,
        state: State | None = None,
        pin_on: PinOn | None = None,
        imt_id: int | None = None,
        nm_id: int | None = None,
        feedback_id: int | None = None,
        date_from: str | None = None,
        date_to: str | None = None,
    ) -> list[PinnedAndUnpinnedFeedbackNumberResponse]:
        """
        The method returns the number of pinned and unpinned feedback for the period.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins~1count/get

        :param state: If the feedback is pinned:
        :param pin_on: Feedback pinning placement:
        :param imt_id: Merged product cards ID.
        :param nm_id: WB article
        :param feedback_id: Feedback ID
        :param date_from: The date the first feedback in the list was pinned
        :param date_to: The date the last feedback in the list was pinned
        :return: list[PinnedAndUnpinnedFeedbackNumberResponse]
        """
        call = GetPinnedAndUnpinnedFeedbackNumber(
            state=state,
            pin_on=pin_on,
            imt_id=imt_id,
            nm_id=nm_id,
            feedback_id=feedback_id,
            date_from=date_from,
            date_to=date_to,
        )
        return await self(call)

    async def get_pinned_feedback_limits(
        self,
    ) -> list[PinnedFeedbackLimitsResponse]:
        """
        The method returns the pinned feedback limits for a tariff and subscription.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins~1limits/get
        :return: list[PinnedFeedbackLimitsResponse]
        """
        call = GetPinnedFeedbackLimits()
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
                       startwith the 11 element
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

    async def get_product_category_commission(
        self,
        locale: str | None = None,
    ) -> list[ProductCategoryCommissionResponse]:
        """
        WB commission by parent categories of products according to sales model.

        Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Commissions/paths/~1api~1v1~1tariffs~1commission/get

        :param locale: Language of the `parentName` and `subjectName` response fields:
        :return: list[ProductCategoryCommissionResponse]
        """
        call = GetProductCategoryCommission(locale=locale)
        return await self(call)

    async def get_product_labeling(
        self,
        date_from: str = None,
        date_to: str = None,
    ) -> list[ProductLabelingItem]:
        """
        Returns a report on deductions for the absence of mandatory product labeling. The report
        containsphotos of products where the labeling is absent or cannot be read. Data can be
        obtainedfor up to 31 days, starting from March 2024

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1v1~1analytics~1goods-labeling/get

        :param date_from: Report period start, `YYYY-MM-DD`
        :param date_to: Report period end, `YYYY-MM-DD`
        :return: list[ProductLabelingItem]
        """
        call = GetProductLabeling(date_from=date_from, date_to=date_to)
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
                       startwith the 11 element
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
        Returns information about products in quarantine. If the product new price with discount
        willbe minimum 3 times less than the old price, the product will be placed in
        [quarantine](https://seller.wildberries.ru/discount-and-prices/quarantine)and will be sold
        atthe old price. An error about this will be in the [upload
        states](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1history~1tasks/get)
        methodresponse. You can change price or discount via API or release product from quarantine
        in[personal account](https://seller.wildberries.ru/discount-and-prices/quarantine). For
        productswith [size-based
        pricing](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task~1size/post),
        quarantinedoes not apply.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1quarantine~1goods/get

        :param limit: Number of elements per page (pagination)
        :param offset: How many results to skip. For example, with value `10`, the response will
                       startwith the 11 element
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
        Returns product data. You can specify only one article in one request. To get data for all
        products,do not set the article, set `limit=1000`, and use the `offset` field to set the
        dataoffset. The offset should be calculated using the formula: `offset` plus `limit` from
        theprevious request. Repeat the request until you receive a response with an empty array.
        Useseparate methods to get data: - for [more than one product by
        article](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/post)
        -for [the size of the
        product](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1size~1nm/get)

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/get

        :param limit: Number of elements per page (pagination)
        :param offset: How many results to skip. For example, with value `10`, the response will
                       startwith the 11 element
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
        Returns product data by its article. You can specify more than one article in one request.
        Useseparate methods to get data: - for [all products without specifying
        articles](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/get)
        -for [the size of the
        product](/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1size~1nm/get).

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1list~1goods~1filter/post

        :param nm_list: WB articles for search
        :return: list[ProductsWithPricesByArticlesItem]
        """
        call = GetProductsWithPricesByArticles(nm_list=nm_list)
        return await self(call)

    async def get_promotions_details(
        self,
        promotion_i_ds: list[int] = None,
    ) -> list[PromotionsDetailsItem]:
        """
        Returns detailed information about the selected promotions

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Promotions-Calendar/paths/~1api~1v1~1calendar~1promotions~1details/get

        :param promotion_i_ds: IDs of the promotions for which information should be returned
        :return: list[PromotionsDetailsItem]
        """
        call = GetPromotionsDetails(promotion_i_ds=promotion_i_ds)
        return await self(call)

    async def get_promotions_list(
        self,
        start_date_time: str = None,
        end_date_time: str = None,
        all_promo: bool = False,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[PromotionsListItem]:
        """
        Returns a promotions list with dates and times of occurrence

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Promotions-Calendar/paths/~1api~1v1~1calendar~1promotions/get

        :param start_date_time: Period start, format `YYYY-MM-DDTHH:MM:SSZ`
        :param end_date_time: Period end, format `YYYY-MM-DDTHH:MM:SSZ`
        :param all_promo: Show promotions:
        :param limit: Number of requested promotions
        :param offset: From which element to start outputting data
        :return: list[PromotionsListItem]
        """
        call = GetPromotionsList(
            start_date_time=start_date_time,
            end_date_time=end_date_time,
            all_promo=all_promo,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def get_question_list(
        self,
        is_answered: bool = None,
        nm_id: int | None = None,
        take: int = None,
        skip: int = None,
        order: str | None = None,
        date_from: int | None = None,
        date_to: int | None = None,
    ) -> list[QuestionListItem]:
        """
        The method allows you to get a list of questions by the specified parameters with
        paginationand sorting. It is possible to get a maximum of 10,000 questions per query

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions/get

        :param is_answered: The question is answered:
        :param nm_id: WB article
        :param take: Number of requested questions (the maximum possible value for the parameter is
                     10,000,and the total amount of `take` and `skip` parameters must not exceed
                     10,000)
        :param skip: Number of questions to skip (maximum possible value for the parameter is
                     10,000,and the total amount of `take` and `skip` parameters must not exceed
                     10,000)
        :param order: Sorting questions by date (`dateAsc`/`dateDesc`)
        :param date_from: The start date of the period in Unix timestamp format
        :param date_to: The end date of the period in Unix timestamp format
        :return: list[QuestionListItem]
        """
        call = GetQuestionList(
            is_answered=is_answered,
            nm_id=nm_id,
            take=take,
            skip=skip,
            order=order,
            date_from=date_from,
            date_to=date_to,
        )
        return await self(call)

    async def get_realization_sales_report(
        self,
        date_from: str = None,
        date_to: str = None,
        limit: int | None = 100000,
        rrdid: int | None = 0,
        period: Period | None = "weekly",
    ) -> list[RealizationSalesReportResponse]:
        """
        Details for the [realization
        reports](https://seller.wildberries.ru/suppliers-mutual-settlements).The report contains
        datasince 29 January 2024.

        Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Financial-Reports/paths/~1api~1v5~1supplier~1reportDetailByPeriod/get

        :param date_from: Starting date of the report. Date format: RFC3339. You may send date or
                          datewith time. Time could be specified in seconds or milliseconds. The
                          timestands in Moscow time zone (UTC+3). Examples:
        :param date_to: Report end date
        :param limit: Number of strings in the response
        :param rrdid: The unique ID of the report line. Required to receive the report in parts.
        :param period: Report periodicity:
        :return: list[RealizationSalesReportResponse]
        """
        call = GetRealizationSalesReport(
            date_from=date_from,
            date_to=date_to,
            limit=limit,
            rrdid=rrdid,
            period=period,
        )
        return await self(call)

    async def get_receiving_costs_history(
        self,
        from_: str = None,
        to: str = None,
    ) -> list[ReceivingCostsHistoryResponse]:
        """
        The method allows to get a costs history

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1upd/get

        :param from_: Beginning of the interval
        :param to: End of interval.
        :return: list[ReceivingCostsHistoryResponse]
        """
        call = GetReceivingCostsHistory(from_=from_, to=to)
        return await self(call)

    async def get_receiving_the_history_of_account_topups(
        self,
        from_: str | None = None,
        to: str | None = None,
    ) -> list[ReceivingTheHistoryOfAccountTopupsResponse]:
        """
        The method allows you to get a history of top-ups.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1payments/get

        :param from_: Beginning of the interval
        :param to: End of interval.
        :return: list[ReceivingTheHistoryOfAccountTopupsResponse]
        """
        call = GetReceivingTheHistoryOfAccountTopups(from_=from_, to=to)
        return await self(call)

    async def get_recommended_bids_for_items_and_search_clusters(
        self,
        nm_id: int = None,
        advert_id: int = None,
    ) -> list[RecommendedBidsForItemsAndSearchClustersItem]:
        """
        The method returns recommended bids for items and search clusters of the campaign. Only for
        campaignswith cpm payment type — cost per mille.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1api~1advert~1v0~1bids~1recommendations/get

        :param nm_id: WB article
        :param advert_id: Campaign ID
        :return: list[RecommendedBidsForItemsAndSearchClustersItem]
        """
        call = GetRecommendedBidsForItemsAndSearchClusters(nm_id=nm_id, advert_id=advert_id)
        return await self(call)

    async def get_report(
        self,
        date_from: str = None,
        date_to: str = None,
    ) -> list[ReportItem]:
        """
        Returns sales data grouped by regions of the countries. You can obtain a report for a
        maximumof 31 days.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Sales-by-Regions/paths/~1api~1v1~1analytics~1region-sale/get

        :param date_from: Report period start, `YYYY-MM-DD`
        :param date_to: Report period end, `YYYY-MM-DD`
        :return: list[ReportItem]
        """
        call = GetReport(date_from=date_from, date_to=date_to)
        return await self(call)

    async def get_retrieve_information_on_completed_assembly_orders(
        self,
        limit: int = None,
        next: int = None,
        date_from: int = None,
        date_to: int = None,
    ) -> list[RetrieveInformationOnCompletedAssemblyOrdersItem]:
        """
        The method provides information on completed assembly orders after the sale or cancellation
        ofan order.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders/get

        :param limit: Pagination parameter. Sets the maximum number of returned data.
        :param next: Pagination parameter. Sets the value from which the next batch of data should
                     beretrieved. To obtain the complete list of data, it should be set to 0 in the
                     firstrequest. For subsequent requests, the values should be taken from the
                     fieldwith the same name in the response.
        :param date_from: Period start date in the Unix timestamp format
        :param date_to: Period end date in the Unix timestamp format
        :return: list[RetrieveInformationOnCompletedAssemblyOrdersItem]
        """
        call = GetRetrieveInformationOnCompletedAssemblyOrders(
            limit=limit,
            next=next,
            date_from=date_from,
            date_to=date_to,
        )
        return await self(call)

    async def get_return_tariffs(
        self,
        date: str = None,
    ) -> list[ReturnTariffsItem]:
        """
        Returns [tariffs](https://seller.wildberries.ru/dynamic-product-categories/return-cost): -
        ontransfer from Wildberries warehouse or sorting center to the seller - on transfer of
        returnedproducts that were not picked up by seller

        Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Return-Cost-to-Seller/paths/~1api~1v1~1tariffs~1return/get

        :param date: Date, YYYY-MM-DD
        :return: list[ReturnTariffsItem]
        """
        call = GetReturnTariffs(date=date)
        return await self(call)

    async def get_sales(
        self,
        date_from: str = None,
        flag: int | None = 0,
    ) -> list[SalesResponse]:
        """
        The method returns sale and return information. The data updated every 30 minutes.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1sales/get

        :param date_from: Date and time of last change on the sale/return.
        :param flag: If parameter `flag=0` (or it doesn't exist in requests string), then call of
                     APImethods returns data,
        :return: list[SalesResponse]
        """
        call = GetSales(date_from=date_from, flag=flag)
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

    async def get_selfpurchases(
        self,
        date: str | None = None,
    ) -> list[SelfpurchasesItem]:
        """
        Returns report with self-purchase deductions. The report is generated on Wednesdays at 7:00
        UTC+4and contains weekly data. Also you can get all data starting from August 2023.
        Self-purchasededuction is 30% of product price. Minimum deduction is 100,000 ₽, if the
        totalproduct cost delivered to the pick-up point is more than 100,000 ₽ per one week.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1v1~1analytics~1antifraud-details/get

        :param date: Date from report period, `YYYY-MM-DD`, for example `2023-12-01`. To get all
                     datafrom August 2023 do not use this parameter
        :return: list[SelfpurchasesItem]
        """
        call = GetSelfpurchases(date=date)
        return await self(call)

    async def get_seller_brands(
        self,
    ) -> list[SellerBrandsItem]:
        """
        Returns the list of the seller brands.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Share-of-Brand-in-Sales/paths/~1api~1v1~1analytics~1brand-share~1brands/get
        :return: list[SellerBrandsItem]
        """
        call = GetSellerBrands()
        return await self(call)

    async def get_seller_information(
        self,
    ) -> list[SellerInformationResponse]:
        """
        This method allows you to obtain the seller's name and account ID. You can use any token in
        request,as long as the **Test Environment** option is not selected.

        Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-Information/paths/~1api~1v1~1seller-info/get
        :return: list[SellerInformationResponse]
        """
        call = GetSellerInformation()
        return await self(call)

    async def get_sellers_balance(
        self,
    ) -> list[SellersBalanceResponse]:
        """
        Balance widget data on [the main page](https://seller.wildberries.ru) of the sellers
        portal.

        Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Balance/paths/~1api~1v1~1account~1balance/get
        :return: list[SellersBalanceResponse]
        """
        call = GetSellersBalance()
        return await self(call)

    async def get_stickers_for_assembly_orders_with_delivery_to_pickup_point(
        self,
        type: Type2 = None,
        width: Width2 = None,
        height: Height2 = None,
        orders: list[int] = None,
    ) -> list[StickersForAssemblyOrdersWithDeliveryToPickupPointItem]:
        """
        Method is available by token types : Personal , Service

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1stickers/post

        :param type: Sticker format
        :param width: Sticker width
        :param height: Sticker height
        :param orders: Assembly orders ID list
        :return: list[StickersForAssemblyOrdersWithDeliveryToPickupPointItem]
        """
        call = GetStickersForAssemblyOrdersWithDeliveryToPickupPoint(
            type=type,
            width=width,
            height=height,
            orders=orders,
        )
        return await self(call)

    async def get_stickers_for_crossborder_assembly_orders(
        self,
        orders: list[int] | None = None,
    ) -> list[StickersForCrossborderAssemblyOrdersItem]:
        """
        Returns a list of stickers for cross-border assembly orders in PDF.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1stickers~1cross-border/post

        :param orders: List of assembly order IDs
        :return: list[StickersForCrossborderAssemblyOrdersItem]
        """
        call = GetStickersForCrossborderAssemblyOrders(orders=orders)
        return await self(call)

    async def get_stop_campaign(
        self,
        id: int = None,
    ) -> None:
        """
        The method allows to end campaigns in statuses: - `4` — ready to launch - `9` — active -
        `11`— paused

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1stop/get

        :param id: Campaign ID
        :return: None
        """
        call = GetStopCampaign(id=id)
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

    async def get_subjects_for_campaigns(
        self,
        payment_type: str | None = "cpm",
    ) -> list[SubjectsForCampaignsResponse]:
        """
        Returns subjects product cards from which are available for all campaigns

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1adv~1v1~1supplier~1subjects/get

        :param payment_type: Payment type:
        :return: list[SubjectsForCampaignsResponse]
        """
        call = GetSubjectsForCampaigns(payment_type=payment_type)
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
                     conductedin any of the supported languages
        :param limit: Number of search results, maximum 1,000
        :param offset: How many results to skip. For example, with value `10`, the response will
                       startwith the 11 element
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

    async def get_substitutions_and_incorrect_attachments(
        self,
        date_from: str | None = None,
        date_to: str = None,
        sort: Sort | None = "dtBonus",
        order: Order2 | None = "desc",
        limit: int = None,
        offset: int | None = 0,
    ) -> list[SubstitutionsAndIncorrectAttachmentsItem]:
        """
        The method returns a report with [substitutions and incorrect
        attachments](https://seller.wildberries.ru/analytics-reports/dimensions-penalties/retentions)
        retentions

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1analytics~1v1~1deductions/get

        :param date_from: Report period start. By default the date and time when data for the
                          reportwas first received is used
        :param date_to: Report period end
        :param sort: Sorting:
        :param order: Data order:
        :param limit: Number of retentions in the response
        :param offset: How many results to skip. For example, with value `10`, the response will
                       startwith the 11 element
        :return: list[SubstitutionsAndIncorrectAttachmentsItem]
        """
        call = GetSubstitutionsAndIncorrectAttachments(
            date_from=date_from,
            date_to=date_to,
            sort=sort,
            order=order,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def get_supply_assembly_order_ids(
        self,
        supply_id: str,
    ) -> list[SupplyAssemblyOrderIdsItem]:
        """
        The method returns assembly orders IDs assigned to the supply.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1marketplace~1v3~1supplies~1%7BsupplyId%7D~1order-ids/get

        :param supply_id: Supply ID
        :return: list[SupplyAssemblyOrderIdsItem]
        """
        call = GetSupplyAssemblyOrderIds(supply_id=supply_id)
        return await self(call)

    async def get_supply_boxes_list(
        self,
        supply_id: str,
    ) -> list[SupplyBoxesListItem]:
        """
        Returns supply boxes list.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx/get

        :param supply_id: Supply ID
        :return: list[SupplyBoxesListItem]
        """
        call = GetSupplyBoxesList(supply_id=supply_id)
        return await self(call)

    async def get_supply_details(
        self,
        supply_id: str,
    ) -> list[SupplyDetailsResponse]:
        """
        Returns supply details.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/get

        :param supply_id: Supply ID
        :return: list[SupplyDetailsResponse]
        """
        call = GetSupplyDetails(supply_id=supply_id)
        return await self(call)

    async def get_supply_package(
        self,
        id: int,
    ) -> list[SupplyPackageResponse]:
        """
        The method returns information about the package of the supply.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies~1%7BID%7D~1package/get

        :param id: Supply ID
        :return: list[SupplyPackageResponse]
        """
        call = GetSupplyPackage(id=id)
        return await self(call)

    async def get_supply_products(
        self,
        id: int,
        limit: int | None = 100,
        offset: int | None = 0,
        is_preorder_id: bool | None = False,
    ) -> list[SupplyProductsResponse]:
        """
        The method returns information about the products in the supply.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies~1%7BID%7D~1goods/get

        :param id: ID of the supply or the order
        :param limit: Number of objects in the response
        :param offset: From which element to start outputting data
        :param is_preorder_id: Search by:
        :return: list[SupplyProductsResponse]
        """
        call = GetSupplyProducts(id=id, limit=limit, offset=offset, is_preorder_id=is_preorder_id)
        return await self(call)

    async def get_supply_tariffs(
        self,
        warehouse_i_ds: str | None = None,
    ) -> list[SupplyTariffsResponse]:
        """
        The method returns the supply tariffs for specific warehouses for the next 14 days.

        Source: https://dev.wildberries.ru/en/docs/openapi/tariffs#tag/Supply-Tariffs/paths/~1api~1tariffs~1v1~1acceptance~1coefficients/get

        :param warehouse_i_ds: Warehouse IDs. By default, data for all warehouses is returned
        :return: list[SupplyTariffsResponse]
        """
        call = GetSupplyTariffs(warehouse_i_ds=warehouse_i_ds)
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

    async def get_the_feedback_by_id(
        self,
        id: str = None,
    ) -> list[TheFeedbackByIdItem]:
        """
        The method allows you to get a feedback by its ID

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedback/get

        :param id: Feedback ID
        :return: list[TheFeedbackByIdItem]
        """
        call = GetTheFeedbackById(id=id)
        return await self(call)

    async def get_the_question_by_id(
        self,
        id: str = None,
    ) -> list[TheQuestionByIdItem]:
        """
        The method allows you to get a question by its ID

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1question/get

        :param id: Question ID
        :return: list[TheQuestionByIdItem]
        """
        call = GetTheQuestionById(id=id)
        return await self(call)

    async def get_the_report(
        self,
        download_id: str,
    ) -> None:
        """
        The method provides a report with advanced seller analytics by [generation
        task](/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post)
        ID.You can get a report that was generated within the last 48 hours. The report will be
        downloadedinside a ZIP archive in CSV format.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads~1file~1%7BdownloadId%7D/get

        :param download_id: Report ID
        :return: None
        """
        call = GetTheReport(download_id=download_id)
        return await self(call)

    async def get_the_reports_list(
        self,
        filter_download_ids: list[str] | None = None,
    ) -> list[TheReportsListItem]:
        """
        The method provides a list of reports with advanced seller analytics. The response contains
        [report
        IDs](/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post)
        andgeneration statuses.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/get

        :param filter_download_ids: Report ID
        :return: list[TheReportsListItem]
        """
        call = GetTheReportsList(filter_download_ids=filter_download_ids)
        return await self(call)

    async def get_the_supply_box_qr_code_stickers(
        self,
        supply_id: str,
        type: Type = None,
        trbx_ids: list[str] = None,
    ) -> list[TheSupplyBoxQrCodeStickersItem]:
        """
        Returns QR-code stickers in svg, zplv (vertical), zplh (horizontal), png. Available only if
        thereare assembly orders in the box. Stickers dimensions: 580x400 px.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx~1stickers/post

        :param supply_id: Supply ID
        :param type: Sticker format
        :param trbx_ids: List of supply box IDs for the sticker generation
        :return: list[TheSupplyBoxQrCodeStickersItem]
        """
        call = GetTheSupplyBoxQrCodeStickers(supply_id=supply_id, type=type, trbx_ids=trbx_ids)
        return await self(call)

    async def get_the_supply_qr_code(
        self,
        supply_id: str,
        type: Type = None,
    ) -> list[TheSupplyQrCodeResponse]:
        """
        Returns the QR code in svg, zplv (vertical), zplh (horizontal), png. Available only after
        thesupply has been transferred to the delivery. Available dimensions: 580x400 px

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1barcode/get

        :param supply_id: Supply ID
        :param type: Sticker format
        :return: list[TheSupplyQrCodeResponse]
        """
        call = GetTheSupplyQrCode(supply_id=supply_id, type=type)
        return await self(call)

    async def get_transit_directions(
        self,
    ) -> list[TransitDirectionsResponse]:
        """
        The method returns information about available transit directions.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Information-for-Forming-Supplies/paths/~1api~1v1~1transit-tariffs/get
        :return: list[TransitDirectionsResponse]
        """
        call = GetTransitDirections()
        return await self(call)

    async def get_unanswered_feedbacks(
        self,
    ) -> list[UnansweredFeedbacksItem]:
        """
        The method allows you to get the number of unanswered feedbacks for today, for all time.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1count-unanswered/get
        :return: list[UnansweredFeedbacksItem]
        """
        call = GetUnansweredFeedbacks()
        return await self(call)

    async def get_unanswered_questions(
        self,
    ) -> list[UnansweredQuestionsItem]:
        """
        The method allows you to get the number of unanswered questions for today and for all time

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions~1count-unanswered/get
        :return: list[UnansweredQuestionsItem]
        """
        call = GetUnansweredQuestions()
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
                       startwith the 11 element
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

    async def get_unseen_feedbacks_and_questions(
        self,
    ) -> list[UnseenFeedbacksAndQuestionsItem]:
        """
        The method displays information about the seller's unseen feedbacks and questions

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1new-feedbacks-questions/get
        :return: list[UnseenFeedbacksAndQuestionsItem]
        """
        call = GetUnseenFeedbacksAndQuestions()
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

    async def get_warehouse(
        self,
        date_from: str = None,
    ) -> list[WarehouseResponse]:
        """
        The method returns WB warehouses inventory.

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1stocks/get

        :param date_from: Date and time of last change on the product.
        :return: list[WarehouseResponse]
        """
        call = GetWarehouse(date_from=date_from)
        return await self(call)

    async def get_warehouse_measurements(
        self,
        date_from: str | None = None,
        date_to: str = None,
        limit: int = None,
        offset: int | None = 0,
    ) -> list[WarehouseMeasurementsItem]:
        """
        The method returns a report with [warehouse
        measurements](https://seller.wildberries.ru/analytics-reports/dimensions-penalties/warehouse-measurements)

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1analytics~1v1~1warehouse-measurements/get

        :param date_from: Report period start. By default the date when data for the report was
                          firstreceived is used
        :param date_to: Report period end
        :param limit: Number of measurements in the response
        :param offset: How many results to skip. For example, with value `10`, the response will
                       startwith the 11 element
        :return: list[WarehouseMeasurementsItem]
        """
        call = GetWarehouseMeasurements(
            date_from=date_from,
            date_to=date_to,
            limit=limit,
            offset=offset,
        )
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

    async def get_warehouses_list(
        self,
    ) -> list[WarehousesListResponse]:
        """
        The method returns Wildberries warehouses list.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Information-for-Forming-Supplies/paths/~1api~1v1~1warehouses/get
        :return: list[WarehousesListResponse]
        """
        call = GetWarehousesList()
        return await self(call)

    async def group_data(
        self,
    ) -> list[GroupDataItem]:
        """
        Forms a dataset for inventory by product group. The product group is described by a tuple
        of`subjectID, brandName, tagID`.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1groups/post
        :return: list[GroupDataItem]
        """
        call = GroupData()
        return await self(call)

    async def grouped_product_cards_statistics_per_days(
        self,
        selected_period: Any = None,
        brand_names: list[str] | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
        skip_deleted_nm: bool | None = None,
        aggregation_level: AggregationLevel | None = "day",
    ) -> list[GroupedProductCardsStatisticsPerDaysItem]:
        """
        The method returns statistics for product cards by day or by week. Product cards are
        groupedby subjects, brands and tags. You can get data for a maximum of the last week.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1grouped~1history/post

        :param brand_names: List of brands for filtering
        :param subject_ids: List of subject IDs for filtering
        :param tag_ids: List of label IDs for filtering
        :param skip_deleted_nm: Skip deleted items
        :param aggregation_level: Aggregation Type. If not specified, the default is aggregation
        :return: list[GroupedProductCardsStatisticsPerDaysItem]
        """
        call = GroupedProductCardsStatisticsPerDays(
            selected_period=selected_period,
            brand_names=brand_names,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
            skip_deleted_nm=skip_deleted_nm,
            aggregation_level=aggregation_level,
        )
        return await self(call)

    async def list_of_campaign_minus_phrases(
        self,
        items: list[Any] = None,
    ) -> list[ListOfCampaignMinusPhrasesItem]:
        """
        The method returns a list of minus phrases by: - campaign IDs - WB articles

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1get-minus/post
        :return: list[ListOfCampaignMinusPhrasesItem]
        """
        call = ListOfCampaignMinusPhrases(items=items)
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
        encounteredduring product card creation or editing. The data is returned in batches. One
        batchcontains: - all errors for one `variants` array in one request during product cards
        [creation](/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload/post)
        -all errors in one request during product cards [creation with
        merge](/openapi/work-with-products#tag/Creating-Product-Cards/paths/~1content~1v2~1cards~1upload~1add/post)
        or
        [editing](/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1update/post).
        Toget more than 100 batches, use pagination:

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1error~1list/post

        :param locale: Language of subject names:
        :param cursor: Paginator
        :param order: The order of return of batches
        :return: list[ListOfFailedProductCardsWithErrorsItem]
        """
        call = ListOfFailedProductCardsWithErrors(locale=locale, cursor=cursor, order=order)
        return await self(call)

    async def list_of_search_clusters_bids(
        self,
        items: list[Any] = None,
    ) -> list[ListOfSearchClustersBidsItem]:
        """
        The method returns a list of search clusters with bids by: - campaign IDs - WB articles

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1get-bids/post
        :return: list[ListOfSearchClustersBidsItem]
        """
        call = ListOfSearchClustersBids(items=items)
        return await self(call)

    async def main_page(
        self,
        current_period: dict[str, Any] = None,
        past_period: dict[str, Any] | None = None,
        nm_ids: list[int] | None = None,
        subject_ids: list[int] | None = None,
        brand_names: list[str] | None = None,
        tag_ids: list[int] | None = None,
        position_cluster: PositionCluster = None,
        order_by: dict[str, Any] = None,
        include_substituted_sk_us: bool | None = True,
        include_search_texts: bool | None = True,
        limit: int = None,
        offset: int = None,
    ) -> list[MainPageResponse]:
        """
        Forms a dataset for the main report page with: - General information - Product positions -
        Dataon visibility and transitions to the product card - Data for the table by groups

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1report/post

        :param current_period: Current period
        :param past_period: Previous period for comparison. Number of days — less than or equal to
                            `currentPeriod`
        :param nm_ids: List of WB article numbers for filtering
        :param subject_ids: List of subject IDs for filtering
        :param brand_names: List of brands for filtering
        :param tag_ids: List of label IDs for filtering
        :param position_cluster: Which average search position of products to display in the
                                 report:
        :param order_by: Sorting parameters
        :param include_substituted_sk_us: Show data for direct queries with [promo
                                          items](https://seller.wildberries.ru/help-center/article/A-524)
        :param include_search_texts: Show data for search queries without promo items
        :param limit: Number of product groups in the response
        :param offset: From which element to start outputting data
        :return: list[MainPageResponse]
        """
        call = MainPage(
            current_period=current_period,
            past_period=past_period,
            nm_ids=nm_ids,
            subject_ids=subject_ids,
            brand_names=brand_names,
            tag_ids=tag_ids,
            position_cluster=position_cluster,
            order_by=order_by,
            include_substituted_sk_us=include_substituted_sk_us,
            include_search_texts=include_search_texts,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def media_campaign_statistics(
        self,
    ) -> list[MediaCampaignStatisticsResponse]:
        """
        The method allows to get statistics of [WB
        Media](https://cmp.wildberries.ru/cmpf/statistics)campaigns

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v1~1stats/post
        :return: list[MediaCampaignStatisticsResponse]
        """
        call = MediaCampaignStatistics()
        return await self(call)

    async def merging_or_separating_of_product_cards(
        self,
    ) -> list[MergingOrSeparatingOfProductCardsResponse]:
        """
        The method merges and separates product cards. Product cards are merged if they have the
        same`imtID`.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1cards~1moveNm/post
        :return: list[MergingOrSeparatingOfProductCardsResponse]
        """
        call = MergingOrSeparatingOfProductCards()
        return await self(call)

    async def minimum_bids_for_product_cards(
        self,
        advert_id: int = None,
        nm_ids: list[int] = None,
        payment_type: PaymentType = None,
        placement_types: list[str] = None,
    ) -> list[MinimumBidsForProductCardsItem]:
        """
        Method allows minimum bids for product cards in kopecks depending on the payment type and
        placements.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1api~1advert~1v1~1bids~1min/post

        :param advert_id: Campaign ID
        :param nm_ids: WB articles list
        :param payment_type: Payment type:
        :param placement_types: Placements:
        :return: list[MinimumBidsForProductCardsItem]
        """
        call = MinimumBidsForProductCards(
            advert_id=advert_id,
            nm_ids=nm_ids,
            payment_type=payment_type,
            placement_types=placement_types,
        )
        return await self(call)

    async def move_the_supply_to_the_delivery(
        self,
        supply_id: str,
    ) -> None:
        """
        Closes the supply and moves all assembly orders to `complete` (`In Delivery`) status. You
        cannotadd any assembly orders to the supply after it is closed.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1deliver/patch

        :param supply_id: Supply ID
        :return: None
        """
        call = MoveTheSupplyToTheDelivery(supply_id=supply_id)
        return await self(call)

    async def notify_that_the_assembly_order_is_ready_for_pickup(
        self,
        order_id: int,
    ) -> None:
        """
        This method is deprecated. It will be removed on [May
        19](https://dev.wildberries.ru/en/release-notes?id=474)

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders~1%7BorderId%7D~1prepare/patch

        :param order_id: Assembly order ID
        :return: None
        """
        call = NotifyThatTheAssemblyOrderIsReadyForPickup(order_id=order_id)
        return await self(call)

    async def notify_that_the_assembly_orders_are_ready_for_pickup(
        self,
        orders_ids: list[int] | None = None,
    ) -> list[NotifyThatTheAssemblyOrdersAreReadyForPickupItem]:
        """
        The method transfers [assembly
        orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)from the `confirm` —
        onassembly —
        [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
        tothe `prepare` — ready for pickup — status.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1prepare/post

        :param orders_ids: List of assembly order IDs
        :return: list[NotifyThatTheAssemblyOrdersAreReadyForPickupItem]
        """
        call = NotifyThatTheAssemblyOrdersAreReadyForPickup(orders_ids=orders_ids)
        return await self(call)

    async def notify_that_the_buyer_has_declined_the_order(
        self,
        order_id: int,
        code: str | None = None,
    ) -> None:
        """
        This method is deprecated. It will be removed on [April
        13](https://dev.wildberries.ru/en/release-notes?id=378)

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders~1%7BorderId%7D~1reject/patch

        :param order_id: Assembly order ID
        :param code: Confirmation code. Displayed to the buyer on the website and in the
                     Wildberriesapp
        :return: None
        """
        call = NotifyThatTheBuyerHasDeclinedTheOrder(order_id=order_id, code=code)
        return await self(call)

    async def notify_that_the_buyer_refused_the_order(
        self,
        order_id: int,
    ) -> None:
        """
        This method is deprecated. It will be removed on [May
        19](https://dev.wildberries.ru/en/release-notes?id=474)

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders~1%7BorderId%7D~1reject/patch

        :param order_id: Assembly order ID
        :return: None
        """
        call = NotifyThatTheBuyerRefusedTheOrder(order_id=order_id)
        return await self(call)

    async def notify_that_the_order_has_been_accepted_by_the_buyer(
        self,
        order_id: int,
        code: str | None = None,
    ) -> None:
        """
        This method is deprecated. It will be removed on [April
        13](https://dev.wildberries.ru/en/release-notes?id=378)

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders~1%7BorderId%7D~1receive/patch

        :param order_id: Assembly order ID
        :param code: Confirmation code. Displayed to the buyer on the website and in the
                     Wildberriesapp
        :return: None
        """
        call = NotifyThatTheOrderHasBeenAcceptedByTheBuyer(order_id=order_id, code=code)
        return await self(call)

    async def notify_that_the_orders_are_declined(
        self,
        orders: list[Any] = None,
    ) -> list[NotifyThatTheOrdersAreDeclinedItem]:
        """
        The method transfers [assembly orders](/openapi/orders-dbs#tag/DBS-Assembly-Orders) with
        the`deliver`
        [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
        tothe `reject` status — declined upon receipt.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1reject/post
        :return: list[NotifyThatTheOrdersAreDeclinedItem]
        """
        call = NotifyThatTheOrdersAreDeclined(orders=orders)
        return await self(call)

    async def notify_that_the_orders_are_received(
        self,
        orders: list[Any] = None,
    ) -> list[NotifyThatTheOrdersAreReceivedItem]:
        """
        The method transfers [assembly orders](/openapi/orders-dbs#tag/DBS-Assembly-Orders) with
        the`deliver`
        [status](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
        tothe `receive` status — received by the buyer.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1receive/post
        :return: list[NotifyThatTheOrdersAreReceivedItem]
        """
        call = NotifyThatTheOrdersAreReceived(orders=orders)
        return await self(call)

    async def notify_that_the_orders_were_received_by_the_buyers(
        self,
        orders_ids: list[int] | None = None,
    ) -> list[NotifyThatTheOrdersWereReceivedByTheBuyersItem]:
        """
        The method transfers [assembly
        orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)from the `prepare` —
        readyfor pickup —
        [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
        tothe `receive` — received by the buyer — status.

        Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1receive/post

        :param orders_ids: List of assembly order IDs
        :return: list[NotifyThatTheOrdersWereReceivedByTheBuyersItem]
        """
        call = NotifyThatTheOrdersWereReceivedByTheBuyers(orders_ids=orders_ids)
        return await self(call)

    async def orders_and_positions_by_product_search_texts(
        self,
        period: dict[str, Any] = None,
        nm_id: int = None,
        search_texts: list[str] = None,
    ) -> list[OrdersAndPositionsByProductSearchTextsResponse]:
        """
        Forms data for a table on the number of orders and positions by queries. The data is
        specifiedwithin a period for a specific product.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1product~1orders/post

        :param period: Current period. Maximum of 7 days
        :param nm_id: WB article
        :param search_texts: Search texts. For the
                             [Advanced](https://seller.wildberries.ru/monetization/tariffs)tariff,
                             themaximum is 100
        :return: list[OrdersAndPositionsByProductSearchTextsResponse]
        """
        call = OrdersAndPositionsByProductSearchTexts(
            period=period,
            nm_id=nm_id,
            search_texts=search_texts,
        )
        return await self(call)

    async def orders_with_client_information(
        self,
        orders: list[int] | None = None,
    ) -> list[OrdersWithClientInformationItem]:
        """
        The method allows getting information about the client by assembly order ID. Only for
        cross-borderorders from **Turkey**

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1client/post

        :param orders: Orders list
        :return: list[OrdersWithClientInformationItem]
        """
        call = OrdersWithClientInformation(orders=orders)
        return await self(call)

    async def pagination_by_groups(
        self,
        current_period: dict[str, Any] = None,
        past_period: dict[str, Any] | None = None,
        nm_ids: list[int] | None = None,
        subject_ids: list[int] | None = None,
        brand_names: list[str] | None = None,
        tag_ids: list[int] | None = None,
        order_by: dict[str, Any] = None,
        position_cluster: PositionCluster = None,
        include_substituted_sk_us: bool | None = True,
        include_search_texts: bool | None = True,
        limit: int = None,
        offset: int = None,
    ) -> list[PaginationByGroupsResponse]:
        """
        Pagination by groups in the report. It is possible only if there is a filter by brand,
        subject,or tag.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1table~1groups/post

        :param current_period: Current period
        :param past_period: Previous period for comparison. Number of days — less than or equal to
                            `currentPeriod`
        :param nm_ids: List of WB article numbers for filtering
        :param subject_ids: List of subject IDs for filtering
        :param brand_names: List of brands for filtering
        :param tag_ids: List of label IDs for filtering
        :param order_by: Sorting parameters
        :param position_cluster: Which average search position of products to display in the
                                 report:
        :param include_substituted_sk_us: Show data for direct queries with [promo
                                          items](https://seller.wildberries.ru/help-center/article/A-524)
        :param include_search_texts: Show data for search queries without promo items
        :param limit: Number of product groups in the response
        :param offset: From which element to start outputting data
        :return: list[PaginationByGroupsResponse]
        """
        call = PaginationByGroups(
            current_period=current_period,
            past_period=past_period,
            nm_ids=nm_ids,
            subject_ids=subject_ids,
            brand_names=brand_names,
            tag_ids=tag_ids,
            order_by=order_by,
            position_cluster=position_cluster,
            include_substituted_sk_us=include_substituted_sk_us,
            include_search_texts=include_search_texts,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def pagination_by_products_within_a_group(
        self,
        current_period: dict[str, Any] = None,
        past_period: dict[str, Any] | None = None,
        subject_id: int | None = None,
        brand_name: str | None = None,
        tag_id: int | None = None,
        nm_ids: list[int] | None = None,
        order_by: dict[str, Any] = None,
        position_cluster: PositionCluster = None,
        include_substituted_sk_us: bool | None = True,
        include_search_texts: bool | None = True,
        limit: int = None,
        offset: int = None,
    ) -> list[PaginationByProductsWithinAGroupResponse]:
        """
        Pagination by products within a group. It is possible regardless of the presence of
        filters.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1table~1details/post

        :param current_period: Current period
        :param past_period: Previous period for comparison. Number of days — less than or equal to
                            `currentPeriod`
        :param subject_id: Subject ID
        :param brand_name: Product name
        :param tag_id: Label ID
        :param nm_ids: WB article numbers list
        :param order_by: Sorting parameters
        :param position_cluster: Which average search position of products to display in the
                                 report:
        :param include_substituted_sk_us: Show data for direct queries with [promo
                                          items](https://seller.wildberries.ru/help-center/article/A-524)
        :param include_search_texts: Show data for search queries without promo items
        :param limit: Number of products in the response
        :param offset: From which element to start outputting data
        :return: list[PaginationByProductsWithinAGroupResponse]
        """
        call = PaginationByProductsWithinAGroup(
            current_period=current_period,
            past_period=past_period,
            subject_id=subject_id,
            brand_name=brand_name,
            tag_id=tag_id,
            nm_ids=nm_ids,
            order_by=order_by,
            position_cluster=position_cluster,
            include_substituted_sk_us=include_substituted_sk_us,
            include_search_texts=include_search_texts,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def pin_feedback(
        self,
    ) -> list[PinFeedbackResponse]:
        """
        The method allows to pin the feedback to a group of merged product cards or to a product
        card.To get feedback ID, use the [List of pinned and unpinned
        feedback](/openapi/user-communication#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/get)
        method.The method is available for [Jam
        subscription](https://seller.wildberries.ru/monetization/jam)or **Pin a feedback** option
        inthe [tariff constructor](https://seller.wildberries.ru/tariff-constructor).

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/post
        :return: list[PinFeedbackResponse]
        """
        call = PinFeedback()
        return await self(call)

    async def product_cards_for_campaigns(
        self,
    ) -> list[ProductCardsForCampaignsResponse]:
        """
        Returns product cards that are available for all campaigns.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1adv~1v2~1supplier~1nms/post
        :return: list[ProductCardsForCampaignsResponse]
        """
        call = ProductCardsForCampaigns()
        return await self(call)

    async def product_cards_in_trash_list(
        self,
        locale: Locale | None = None,
        settings: dict[str, Any] | None = None,
    ) -> list[ProductCardsInTrashListItem]:
        """
        The method is available with the token of the Promotion category

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
        The method is available with the token of the Promotion category

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post

        :param locale: Language for response of the `name`, `value` and `object` fields:
        :param settings: Settings
        :return: list[ProductCardsListItem]
        """
        call = ProductCardsList(locale=locale, settings=settings)
        return await self(call)

    async def product_cards_statistics_per_days(
        self,
        selected_period: Any = None,
        nm_ids: list[int] = None,
        skip_deleted_nm: bool | None = None,
        aggregation_level: AggregationLevel | None = "day",
    ) -> list[ProductCardsStatisticsPerDaysResponse]:
        """
        The method returns statistics for product cards by day or by week. You can get data for a
        maximumof the last week.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1products~1history/post

        :param nm_ids: WB articles to include in the report
        :param skip_deleted_nm: Skip deleted items
        :param aggregation_level: Aggregation Type. If not specified, the default is aggregation
        :return: list[ProductCardsStatisticsPerDaysResponse]
        """
        call = ProductCardsStatisticsPerDays(
            selected_period=selected_period,
            nm_ids=nm_ids,
            skip_deleted_nm=skip_deleted_nm,
            aggregation_level=aggregation_level,
        )
        return await self(call)

    async def product_cards_statistics_per_period(
        self,
        selected_period: Any = None,
        past_period: Any | None = None,
        nm_ids: list[int] | None = None,
        brand_names: list[str] | None = None,
        subject_ids: list[int] | None = None,
        tag_ids: list[int] | None = None,
        skip_deleted_nm: bool | None = None,
        order_by: dict[str, Any] | None = None,
        limit: int | None = 50,
        offset: int | None = 0,
    ) -> list[ProductCardsStatisticsPerPeriodResponse]:
        """
        The method generates a report on products by comparing key metrics for the current period
        witha similar past one.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Sales-Funnel/paths/~1api~1analytics~1v3~1sales-funnel~1products/post

        :param nm_ids: WB articles to include in the report. Leave empty to get a report for all
                       products
        :param brand_names: List of brands for filtering
        :param subject_ids: List of subject IDs for filtering
        :param tag_ids: List of label IDs for filtering
        :param skip_deleted_nm: Skip deleted items
        :param order_by: Sorting parameters
        :param limit: Number of product cards in the response
        :param offset: How many results to skip. For example, with value `10`, the response will
                       startwith the 11 element
        :return: list[ProductCardsStatisticsPerPeriodResponse]
        """
        call = ProductCardsStatisticsPerPeriod(
            selected_period=selected_period,
            past_period=past_period,
            nm_ids=nm_ids,
            brand_names=brand_names,
            subject_ids=subject_ids,
            tag_ids=tag_ids,
            skip_deleted_nm=skip_deleted_nm,
            order_by=order_by,
            limit=limit,
            offset=offset,
        )
        return await self(call)

    async def product_data(
        self,
    ) -> list[ProductDataItem]:
        """
        Forms a dataset for inventory by products. You can get data for individual products as well
        asfor the entire report if there are no filters in the query: `nmIDs`, `subjectID`,
        `brandName`,`tagID`.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post
        :return: list[ProductDataItem]
        """
        call = ProductData()
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

    async def regenerate_the_report(
        self,
        download_id: str | None = None,
    ) -> list[RegenerateTheReportResponse]:
        """
        The method creates a [repeated generation
        task](/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post)
        ofreport with advanced seller analytics. This is necessary if you [received the
        status](/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/get)
        `FAILED`when generating the report.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads~1retry/post

        :param download_id: Report ID
        :return: list[RegenerateTheReportResponse]
        """
        call = RegenerateTheReport(download_id=download_id)
        return await self(call)

    async def rename_campaign(
        self,
        advert_id: int = None,
        name: str = None,
    ) -> None:
        """
        The method allows to rename a campaign.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1rename/post

        :param advert_id: ID of the campaign where the name is changing
        :param name: New name (max 100 characters)
        :return: None
        """
        call = RenameCampaign(advert_id=advert_id, name=name)
        return await self(call)

    async def reply_to_feedback(
        self,
        id: str = None,
        text: str = None,
    ) -> None:
        """
        Allows you to respond to the feedback. There is no validation by `feedback ID`: if an
        incorrectvalue is provided in the request, you will not receive an error.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1answer/post

        :param id: Feedback ID
        :param text: Reply text
        :return: None
        """
        call = ReplyToFeedback(id=id, text=text)
        return await self(call)

    async def report_on_products_with_mandatory_labeling(
        self,
        date_from: str = None,
        date_to: str = None,
        countries: list[str] | None = None,
    ) -> list[ReportOnProductsWithMandatoryLabelingItem]:
        """
        Returns operations with labeled products

        Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Report-on-Products-with-Mandatory-Labeling/paths/~1api~1v1~1analytics~1excise-report/post

        :param date_from: Report period start, `YYYY-MM-DD`
        :param date_to: Report period end, `YYYY-MM-DD`
        :param countries: Country code in according with ISO 3166-2. Set the empty parameter to get
                          datawithout filters by country
        :return: list[ReportOnProductsWithMandatoryLabelingItem]
        """
        call = ReportOnProductsWithMandatoryLabeling(
            date_from=date_from,
            date_to=date_to,
            countries=countries,
        )
        return await self(call)

    async def return_product_by_feedback_id(
        self,
        feedback_id: str | None = None,
    ) -> list[ReturnProductByFeedbackIdItem]:
        """
        The method allows requesting a return for a product for which a feedback has been left.
        Returnis available for feedbacks with `"isAbleReturnProductOrders": true`

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1order~1return/post

        :param feedback_id: Feedback ID
        :return: list[ReturnProductByFeedbackIdItem]
        """
        call = ReturnProductByFeedbackId(feedback_id=feedback_id)
        return await self(call)

    async def search_clusters_statistics(
        self,
        from_: str = None,
        to: str = None,
        items: list[dict[str, Any]] = None,
    ) -> list[SearchClustersStatisticsItem]:
        """
        The method returns statistics for search clusters over a specified period. You can use this
        methodonly for campaigns with a `cpm` payment model — for displays.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Statistics/paths/~1adv~1v0~1normquery~1stats/post

        :param from_: Period start date
        :param to: Period end date
        :return: list[SearchClustersStatisticsItem]
        """
        call = SearchClustersStatistics(from_=from_, to=to, items=items)
        return await self(call)

    async def search_texts_by_product(
        self,
        current_period: dict[str, Any] = None,
        past_period: dict[str, Any] | None = None,
        nm_ids: list[int] = None,
        top_order_by: TopOrderBy = None,
        include_substituted_sk_us: bool | None = True,
        include_search_texts: bool | None = True,
        order_by: dict[str, Any] = None,
        limit: Any = None,
    ) -> list[SearchTextsByProductResponse]:
        """
        Forms the top search texts by product.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1product~1search-texts/post

        :param current_period: Current period
        :param past_period: Previous period for comparison. Number of days — less than or equal to
                            `currentPeriod`
        :param nm_ids: WB article numbers list
        :param top_order_by: Filtering by the search queries that brought the most:
        :param include_substituted_sk_us: Show data for direct queries with [promo
                                          items](https://seller.wildberries.ru/help-center/article/A-524)
        :param include_search_texts: Show data for search queries without promo items
        :param order_by: Sorting parameters
        :return: list[SearchTextsByProductResponse]
        """
        call = SearchTextsByProduct(
            current_period=current_period,
            past_period=past_period,
            nm_ids=nm_ids,
            top_order_by=top_order_by,
            include_substituted_sk_us=include_substituted_sk_us,
            include_search_texts=include_search_texts,
            order_by=order_by,
            limit=limit,
        )
        return await self(call)

    async def send_message(
        self,
    ) -> list[SendMessageItem]:
        """
        Sends message to the buyer.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1message/post
        :return: list[SendMessageItem]
        """
        call = SendMessage()
        return await self(call)

    async def set_bids_for_search_clusters(
        self,
        bids: list[Any] = None,
    ) -> None:
        """
        The method sets the bids for search clusters. You can use this method only for campaigns
        with:- custom bid - a `cpm` payment model — per displays

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1bids/post
        :return: None
        """
        call = SetBidsForSearchClusters(bids=bids)
        return await self(call)

    async def set_prices_and_discounts(
        self,
        data: list[Any] = None,
    ) -> list[SetPricesAndDiscountsResponse]:
        """
        Sets prices and discounts.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Prices-and-Discounts/paths/~1api~1v2~1upload~1task/post

        :param data: Products, prices and discounts. Maximum 1,000 products. Both price and
                     discountcan not be empty
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

    async def setting_and_deleting_minus_phrases(
        self,
        advert_id: int = None,
        nm_id: int = None,
        norm_queries: list[str] = None,
    ) -> None:
        """
        The method sets and deletes the minus phrases in campaigns with standard and custom bid.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Search-Clusters/paths/~1adv~1v0~1normquery~1set-minus/post

        :param advert_id: Campaign ID
        :param nm_id: WB article
        :return: None
        """
        call = SettingAndDeletingMinusPhrases(
            advert_id=advert_id,
            nm_id=nm_id,
            norm_queries=norm_queries,
        )
        return await self(call)

    async def size_data(
        self,
    ) -> list[SizeDataItem]:
        """
        Forms a dataset for inventory by the size of the product. Possible cases: 1. The product
        hasdimensions and `"includeOffice":true`, then the response body will contain data on the
        inventoryfor each of the sizes with nested details by warehouse. 2. The product has
        dimensionsand `"includeOffice":false`, then the response body will contain data on the
        inventoryfor each of the sizes without nested details by warehouse. 3. The product has no
        sizeand `"include Office":true`, then the response body will contain details by warehouse
        withoutdata on the inventory for each of the sizes. 4. The product has no size and
        `"includeOffice":false`, then the response body will be empty. `The product has no size`
        meansthe size of the product is the same and has `"techSize":"0"`. In responses of the
        methodfor getting data on
        [products](/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post),
        suchproducts have `hasSizes':false`. The data on the seller's warehouses are in an
        aggregatedform — for all of them together without detailing specific warehouses — and
        responsescontain `"regionName":"Маркетплейс"` and `"officeName":""` in such cases.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1sizes/post
        :return: list[SizeDataItem]
        """
        call = SizeData()
        return await self(call)

    async def status_history_for_crossborder_orders(
        self,
        orders: list[int] | None = None,
    ) -> list[StatusHistoryForCrossborderOrdersItem]:
        """
        Returns status history for cross-border orders

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1status~1history/post

        :param orders: Assembly orders IDs
        :return: list[StatusHistoryForCrossborderOrdersItem]
        """
        call = StatusHistoryForCrossborderOrders(orders=orders)
        return await self(call)

    async def supplies_list(
        self,
        limit: int | None = 1000,
        offset: int | None = 0,
        dates: list[Any] | None = None,
        status_i_ds: list[Any] | None = None,
    ) -> list[SuppliesListResponse]:
        """
        The method returns a list of supplies, the last 1000 supplies by default.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies/post

        :param limit: Number of objects in the response
        :param offset: From which element to start outputting data
        :param dates: Filter by dates
        :param status_i_ds: Filter the supply by statuses. Possible values:
        :return: list[SuppliesListResponse]
        """
        call = SuppliesList(limit=limit, offset=offset, dates=dates, status_i_ds=status_i_ds)
        return await self(call)

    async def tag_management_in_the_product_card(
        self,
        nm_id: int | None = None,
        tags_i_ds: list[int] | None = None,
    ) -> list[TagManagementInTheProductCardResponse]:
        """
        The method allows to add tags to the product card and remove tags from the product card.
        Whenremoving a tag from a product card, the tag itself is not removed. It is possible to
        add15 tags to a product card.

        Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Tags/paths/~1content~1v2~1tag~1nomenclature~1link/post

        :param nm_id: WB article
        :param tags_i_ds: An array of numeric tag IDs.
        :return: list[TagManagementInTheProductCardResponse]
        """
        call = TagManagementInTheProductCard(nm_id=nm_id, tags_i_ds=tags_i_ds)
        return await self(call)

    async def topup_of_the_campaign_budget(
        self,
        id: int = None,
        sum: int | None = None,
        cashback_sum: int | None = None,
        cashback_percent: int | None = None,
        type: int | None = None,
        return_: bool | None = None,
    ) -> list[TopupOfTheCampaignBudgetResponse]:
        """
        The method tops up the campaign
        [budget](/openapi/promotion#tag/Finances/paths/~1adv~1v1~1budget/get).To launch the
        campaignafter topping up the budget, use the [Launch
        campaign](/openapi/promotion#tag/Campaigns-Management/paths/~1adv~1v0~1start/get)method.

        Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Finances/paths/~1adv~1v1~1budget~1deposit/post

        :param id: Campaign ID
        :param sum: Budget top-up amount
        :param cashback_sum: Top-up budget sum paid with promo bonuses.
        :param cashback_percent: The percentage of the top-up amount that can be paid with promo
                                 bonuses.You need to specify the value of the `percent` field from
                                 theresponse for the method for getting [balance]
        :param type: Type of top-up source:
        :param return_: Response return flag (`true` means updated campaign budget size will be
                        returnedin the response, `false` or empty means nothing will be returned).
        :return: list[TopupOfTheCampaignBudgetResponse]
        """
        call = TopupOfTheCampaignBudget(
            id=id,
            sum=sum,
            cashback_sum=cashback_sum,
            cashback_percent=cashback_percent,
            type=type,
            return_=return_,
        )
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

    async def transfer_to_assembly(
        self,
        order_id: int,
    ) -> None:
        """
        Transfers the assembly order to the `confirm` status — on assembly.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1confirm/patch

        :param order_id: Assembly order ID
        :return: None
        """
        call = TransferToAssembly(order_id=order_id)
        return await self(call)

    async def transfer_to_delivery(
        self,
        order_id: int,
    ) -> None:
        """
        Transfers the [assembly
        order](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders/get)to the
        [status](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1status/post)
        `complete`— in delivery.

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1%7BorderId%7D~1assemble/patch

        :param order_id: Assembly order ID
        :return: None
        """
        call = TransferToDelivery(order_id=order_id)
        return await self(call)

    async def unpin_feedback(
        self,
    ) -> list[UnpinFeedbackResponse]:
        """
        The method allows to unpin the feedback in a group of merged product cards or a product
        card.To get `pinId` — feedback pinning operation ID, use the [List of pinned and unpinned
        feedback](/openapi/user-communication#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/get)
        method.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/delete
        :return: list[UnpinFeedbackResponse]
        """
        call = UnpinFeedback()
        return await self(call)

    async def update_contacts_list(
        self,
        warehouse_id: int,
        contacts: list[dict[str, Any]] | None = None,
    ) -> None:
        """
        Updates the seller's warehouse contact list.

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

    async def update_pass(
        self,
        pass_id: int,
        first_name: str = None,
        last_name: str = None,
        car_model: str = None,
        car_number: str = None,
        office_id: int = None,
    ) -> None:
        """
        Updates the seller's pass detail

        Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Passes/paths/~1api~1v3~1passes~1%7BpassId%7D/put

        :param pass_id: Pass ID
        :param first_name: First name
        :param last_name: Last name
        :param car_model: Car model
        :param car_number: Car number
        :param office_id: Office ID
        :return: None
        """
        call = UpdatePass(
            pass_id=pass_id,
            first_name=first_name,
            last_name=last_name,
            car_model=car_model,
            car_number=car_number,
            office_id=office_id,
        )
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

    async def update_users_access_permissions(
        self,
        users_accesses: list[Any] = None,
    ) -> None:
        """
        Method is available by Personal token

        Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Seller-User-Management/paths/~1api~1v1~1users~1access/put

        :param users_accesses: Access settings for user
        :return: None
        """
        call = UpdateUsersAccessPermissions(users_accesses=users_accesses)
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
                     positionof the array
        :return: list[UploadMediaFilesViaLinksResponse]
        """
        call = UploadMediaFilesViaLinks(nm_id=nm_id, data=data)
        return await self(call)

    async def warehouse_data(
        self,
    ) -> list[WarehouseDataItem]:
        """
        Forms a dataset for inventory by warehouses. The data on the seller's warehouses are in an
        aggregatedform — for all of them together without detailing specific warehouses — and
        responsescontain `"regionName":"Маркетплейс"` and `"offices":[]`.

        Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1offices/post
        :return: list[WarehouseDataItem]
        """
        call = WarehouseData()
        return await self(call)

    async def working_with_questions(
        self,
    ) -> list[WorkingWithQuestionsItem]:
        """
        Depending on the request body, you can: - View question. - Reject question. - Answer
        questionor edit the answer.

        Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions/patch
        :return: list[WorkingWithQuestionsItem]
        """
        call = WorkingWithQuestions()
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
