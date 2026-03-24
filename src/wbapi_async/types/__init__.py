from ..analytics.types.create_the_report_response import CreateTheReportResponse
from ..analytics.types.group_data_item import GroupDataItem
from ..analytics.types.grouped_product_cards_statistics_per_days_item import (
    GroupedProductCardsStatisticsPerDaysItem,
)
from ..analytics.types.main_page_response import MainPageResponse
from ..analytics.types.orders_and_positions_by_product_search_texts_response import (
    OrdersAndPositionsByProductSearchTextsResponse,
)
from ..analytics.types.pagination_by_groups_response import PaginationByGroupsResponse
from ..analytics.types.pagination_by_products_within_a_group_response import (
    PaginationByProductsWithinAGroupResponse,
)
from ..analytics.types.product_cards_statistics_per_days_response import ProductCardsStatisticsPerDaysResponse
from ..analytics.types.product_cards_statistics_per_period_response import (
    ProductCardsStatisticsPerPeriodResponse,
)
from ..analytics.types.product_data_item import ProductDataItem
from ..analytics.types.regenerate_the_report_response import RegenerateTheReportResponse
from ..analytics.types.search_texts_by_product_response import SearchTextsByProductResponse
from ..analytics.types.size_data_item import SizeDataItem
from ..analytics.types.the_report_response import TheReportResponse
from ..analytics.types.the_reports_list_item import TheReportsListItem
from ..analytics.types.warehouse_data_item import WarehouseDataItem
from ..analytics.types.wb_warehouses_inventory_item import WbWarehousesInventoryItem
from ..communications.types.answer_buyers_application_response import AnswerBuyersApplicationResponse
from ..communications.types.buyers_return_applications_item import BuyersReturnApplicationsItem
from ..communications.types.chat_events_item import ChatEventsItem
from ..communications.types.chat_list_item import ChatListItem
from ..communications.types.edit_response_to_feedback_response import EditResponseToFeedbackResponse
from ..communications.types.feedbacks_list_item import FeedbacksListItem
from ..communications.types.file_from_the_message_response import FileFromTheMessageResponse
from ..communications.types.list_of_archived_feedbacks_item import ListOfArchivedFeedbacksItem
from ..communications.types.list_of_pinned_and_unpinned_feedback_response import (
    ListOfPinnedAndUnpinnedFeedbackResponse,
)
from ..communications.types.number_of_feedbacks_item import NumberOfFeedbacksItem
from ..communications.types.number_of_questions_item import NumberOfQuestionsItem
from ..communications.types.pin_feedback_response import PinFeedbackResponse
from ..communications.types.pinned_and_unpinned_feedback_number_response import (
    PinnedAndUnpinnedFeedbackNumberResponse,
)
from ..communications.types.pinned_feedback_limits_response import PinnedFeedbackLimitsResponse
from ..communications.types.question_list_item import QuestionListItem
from ..communications.types.reply_to_feedback_response import ReplyToFeedbackResponse
from ..communications.types.return_product_by_feedback_id_item import ReturnProductByFeedbackIdItem
from ..communications.types.send_message_item import SendMessageItem
from ..communications.types.the_feedback_by_id_item import TheFeedbackByIdItem
from ..communications.types.the_question_by_id_item import TheQuestionByIdItem
from ..communications.types.unanswered_feedbacks_item import UnansweredFeedbacksItem
from ..communications.types.unanswered_questions_item import UnansweredQuestionsItem
from ..communications.types.unpin_feedback_response import UnpinFeedbackResponse
from ..communications.types.unseen_feedbacks_and_questions_item import UnseenFeedbacksAndQuestionsItem
from ..communications.types.working_with_questions_item import WorkingWithQuestionsItem
from ..finances.types.document_response import DocumentResponse
from ..finances.types.documents_categories_item import DocumentsCategoriesItem
from ..finances.types.documents_list_item import DocumentsListItem
from ..finances.types.documents_response import DocumentsResponse
from ..finances.types.realization_sales_report_response import RealizationSalesReportResponse
from ..finances.types.sellers_balance_response import SellersBalanceResponse
from ..general.types.a_list_of_seller_active_or_invited_users_item import (
    AListOfSellerActiveOrInvitedUsersItem,
)
from ..general.types.connection_check_response import ConnectionCheckResponse
from ..general.types.create_an_invitation_for_a_new_user_response import CreateAnInvitationForANewUserResponse
from ..general.types.delete_user_response import DeleteUserResponse
from ..general.types.getting_seller_portal_news_item import GettingSellerPortalNewsItem
from ..general.types.seller_information_response import SellerInformationResponse
from ..general.types.update_users_access_permissions_response import UpdateUsersAccessPermissionsResponse
from ..in_store_pickup.types.add_data_matrix_codes_to_the_assembly_orders_chestny_znak_item import (
    AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem,
)
from ..in_store_pickup.types.add_gtin_to_the_assembly_orders_item import AddGtinToTheAssemblyOrdersItem
from ..in_store_pickup.types.add_imei_to_the_assembly_orders_item import AddImeiToTheAssemblyOrdersItem
from ..in_store_pickup.types.add_uin_unique_identification_numbers_to_the_assembly_orders_item import (
    AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem,
)
from ..in_store_pickup.types.assembly_order_metadata_response import AssemblyOrderMetadataResponse
from ..in_store_pickup.types.assign_a_data_matrix_code_to_the_assembly_order_response import (
    AssignADataMatrixCodeToTheAssemblyOrderResponse,
)
from ..in_store_pickup.types.cancel_the_assembly_orders_item import CancelTheAssemblyOrdersItem
from ..in_store_pickup.types.check_if_the_order_belongs_to_the_buyer_response import (
    CheckIfTheOrderBelongsToTheBuyerResponse,
)
from ..in_store_pickup.types.delete_assembly_order_metadata_item import DeleteAssemblyOrderMetadataItem
from ..in_store_pickup.types.new_assembly_orders_list_item import NewAssemblyOrdersListItem
from ..in_store_pickup.types.notify_that_the_assembly_order_is_ready_for_pickup_response import (
    NotifyThatTheAssemblyOrderIsReadyForPickupResponse,
)
from ..in_store_pickup.types.notify_that_the_assembly_orders_are_ready_for_pickup_item import (
    NotifyThatTheAssemblyOrdersAreReadyForPickupItem,
)
from ..in_store_pickup.types.notify_that_the_buyer_refused_the_order_response import (
    NotifyThatTheBuyerRefusedTheOrderResponse,
)
from ..in_store_pickup.types.notify_that_the_orders_were_received_by_the_buyers_item import (
    NotifyThatTheOrdersWereReceivedByTheBuyersItem,
)
from ..in_store_pickup.types.retrieve_information_on_completed_assembly_orders_item import (
    RetrieveInformationOnCompletedAssemblyOrdersItem,
)
from ..orders_dbs.types.add_custom_declaration_to_the_orders_response import (
    AddCustomDeclarationToTheOrdersResponse,
)
from ..orders_dbs.types.add_data_matrix_codes_to_assembly_orders_chestny_znak_item import (
    AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem,
)
from ..orders_dbs.types.add_gtin_to_assembly_orders_item import AddGtinToAssemblyOrdersItem
from ..orders_dbs.types.add_imei_to_assembly_orders_item import AddImeiToAssemblyOrdersItem
from ..orders_dbs.types.add_uin_unique_identification_number_to_assembly_orders_item import (
    AddUinUniqueIdentificationNumberToAssemblyOrdersItem,
)
from ..orders_dbs.types.assembly_order_statuses_item import AssemblyOrderStatusesItem
from ..orders_dbs.types.b2_b_buyer_information_item import B2BBuyerInformationItem
from ..orders_dbs.types.cancel_assembly_orders_item import CancelAssemblyOrdersItem
from ..orders_dbs.types.delete_assembly_orders_metadata_item import DeleteAssemblyOrdersMetadataItem
from ..orders_dbs.types.information_on_paid_delivery_response import InformationOnPaidDeliveryResponse
from ..orders_dbs.types.new_orders_list_item import NewOrdersListItem
from ..orders_dbs.types.notify_that_the_buyer_has_declined_the_order_response import (
    NotifyThatTheBuyerHasDeclinedTheOrderResponse,
)
from ..orders_dbs.types.notify_that_the_order_has_been_accepted_by_the_buyer_response import (
    NotifyThatTheOrderHasBeenAcceptedByTheBuyerResponse,
)
from ..orders_dbs.types.notify_that_the_orders_are_declined_item import NotifyThatTheOrdersAreDeclinedItem
from ..orders_dbs.types.notify_that_the_orders_are_received_item import NotifyThatTheOrdersAreReceivedItem
from ..orders_dbs.types.stickers_for_assembly_orders_with_delivery_to_pickup_point_item import (
    StickersForAssemblyOrdersWithDeliveryToPickupPointItem,
)
from ..orders_dbs.types.transfer_to_assembly_item import TransferToAssemblyItem
from ..orders_dbs.types.transfer_to_delivery_item import TransferToDeliveryItem
from ..orders_dbw.types.add_data_matrix_code_to_the_order_response import AddDataMatrixCodeToTheOrderResponse
from ..orders_dbw.types.add_gtin_to_the_order_response import AddGtinToTheOrderResponse
from ..orders_dbw.types.add_imei_to_the_order_response import AddImeiToTheOrderResponse
from ..orders_dbw.types.add_uin_unique_identification_number_to_the_order_response import (
    AddUinUniqueIdentificationNumberToTheOrderResponse,
)
from ..orders_dbw.types.buyer_information_item import BuyerInformationItem
from ..orders_dbw.types.cancel_the_order_response import CancelTheOrderResponse
from ..orders_dbw.types.courier_info_item import CourierInfoItem
from ..orders_dbw.types.delete_order_metadata_response import DeleteOrderMetadataResponse
from ..orders_dbw.types.delivery_date_and_time_item import DeliveryDateAndTimeItem
from ..orders_dbw.types.information_on_completed_orders_item import InformationOnCompletedOrdersItem
from ..orders_dbw.types.new_orders_item import NewOrdersItem
from ..orders_dbw.types.order_metadata_item import OrderMetadataItem
from ..orders_dbw.types.orders_statuses_item import OrdersStatusesItem
from ..orders_dbw.types.orders_stickers_item import OrdersStickersItem
from ..orders_dbw.types.transfer_to_assembly_response import TransferToAssemblyResponse
from ..orders_dbw.types.transfer_to_delivery_response import TransferToDeliveryResponse
from ..orders_fbs.types.a_supplies_list_item import ASuppliesListItem
from ..orders_fbs.types.add_assembly_orders_to_the_supply_response import AddAssemblyOrdersToTheSupplyResponse
from ..orders_fbs.types.add_boxes_to_the_supply_item import AddBoxesToTheSupplyItem
from ..orders_fbs.types.add_custom_declaration_number_to_the_order_response import (
    AddCustomDeclarationNumberToTheOrderResponse,
)
from ..orders_fbs.types.add_data_matrix_code_to_the_assembly_order_response import (
    AddDataMatrixCodeToTheAssemblyOrderResponse,
)
from ..orders_fbs.types.add_expiration_date_to_the_assembly_order_response import (
    AddExpirationDateToTheAssemblyOrderResponse,
)
from ..orders_fbs.types.add_gtin_to_the_assembly_order_response import AddGtinToTheAssemblyOrderResponse
from ..orders_fbs.types.add_imei_to_the_assembly_order_response import AddImeiToTheAssemblyOrderResponse
from ..orders_fbs.types.add_uin_unique_identification_number_to_the_assembly_order_response import (
    AddUinUniqueIdentificationNumberToTheAssemblyOrderResponse,
)
from ..orders_fbs.types.all_assembly_orders_for_reshipment_item import AllAssemblyOrdersForReshipmentItem
from ..orders_fbs.types.assembly_orders_item import AssemblyOrdersItem
from ..orders_fbs.types.assembly_orders_metadata_item import AssemblyOrdersMetadataItem
from ..orders_fbs.types.assembly_orders_statuses_item import AssemblyOrdersStatusesItem
from ..orders_fbs.types.assembly_orders_stickers_item import AssemblyOrdersStickersItem
from ..orders_fbs.types.cancel_the_assembly_order_response import CancelTheAssemblyOrderResponse
from ..orders_fbs.types.create_a_new_supply_response import CreateANewSupplyResponse
from ..orders_fbs.types.create_pass_response import CreatePassResponse
from ..orders_fbs.types.delete_assembly_order_metadata_response import DeleteAssemblyOrderMetadataResponse
from ..orders_fbs.types.delete_boxes_from_the_supply_response import DeleteBoxesFromTheSupplyResponse
from ..orders_fbs.types.delete_the_pass_response import DeleteThePassResponse
from ..orders_fbs.types.delete_the_supply_response import DeleteTheSupplyResponse
from ..orders_fbs.types.move_the_supply_to_the_delivery_response import MoveTheSupplyToTheDeliveryResponse
from ..orders_fbs.types.new_assembly_orders_item import NewAssemblyOrdersItem
from ..orders_fbs.types.offices_for_pass_response import OfficesForPassResponse
from ..orders_fbs.types.orders_with_client_information_item import OrdersWithClientInformationItem
from ..orders_fbs.types.passes_response import PassesResponse
from ..orders_fbs.types.status_history_for_crossborder_orders_item import (
    StatusHistoryForCrossborderOrdersItem,
)
from ..orders_fbs.types.stickers_for_crossborder_assembly_orders_item import (
    StickersForCrossborderAssemblyOrdersItem,
)
from ..orders_fbs.types.supply_assembly_order_ids_item import SupplyAssemblyOrderIdsItem
from ..orders_fbs.types.supply_boxes_list_item import SupplyBoxesListItem
from ..orders_fbs.types.supply_details_response import SupplyDetailsResponse
from ..orders_fbs.types.the_supply_box_qr_code_stickers_item import TheSupplyBoxQrCodeStickersItem
from ..orders_fbs.types.the_supply_qr_code_response import TheSupplyQrCodeResponse
from ..orders_fbs.types.update_pass_response import UpdatePassResponse
from ..orders_fbw.types.acceptance_options_item import AcceptanceOptionsItem
from ..orders_fbw.types.supplies_list_response import SuppliesListResponse
from ..orders_fbw.types.supply_package_response import SupplyPackageResponse
from ..orders_fbw.types.supply_products_response import SupplyProductsResponse
from ..orders_fbw.types.transit_directions_response import TransitDirectionsResponse
from ..orders_fbw.types.warehouses_list_response import WarehousesListResponse
from ..products.types.brands_item import BrandsItem
from ..products.types.color_response import ColorResponse
from ..products.types.contacts_list_item import ContactsListItem
from ..products.types.country_of_origin_response import CountryOfOriginResponse
from ..products.types.create_a_tag_response import CreateATagResponse
from ..products.types.create_product_cards_response import CreateProductCardsResponse
from ..products.types.create_product_cards_with_merge_response import CreateProductCardsWithMergeResponse
from ..products.types.create_warehouse_response import CreateWarehouseResponse
from ..products.types.delete_inventory_response import DeleteInventoryResponse
from ..products.types.delete_the_tag_response import DeleteTheTagResponse
from ..products.types.delete_warehouse_response import DeleteWarehouseResponse
from ..products.types.gender_item import GenderItem
from ..products.types.generation_of_skus_item import GenerationOfSkusItem
from ..products.types.hscodes_item import HscodesItem
from ..products.types.inventory_item import InventoryItem
from ..products.types.limits_for_the_product_cards_response import LimitsForTheProductCardsResponse
from ..products.types.list_of_failed_product_cards_with_errors_item import (
    ListOfFailedProductCardsWithErrorsItem,
)
from ..products.types.merging_or_separating_of_product_cards_response import (
    MergingOrSeparatingOfProductCardsResponse,
)
from ..products.types.offices_response import OfficesResponse
from ..products.types.processed_upload_details_item import ProcessedUploadDetailsItem
from ..products.types.processed_upload_state_response import ProcessedUploadStateResponse
from ..products.types.product_cards_in_trash_list_item import ProductCardsInTrashListItem
from ..products.types.product_cards_list_item import ProductCardsListItem
from ..products.types.product_sizes_with_prices_item import ProductSizesWithPricesItem
from ..products.types.products_in_quarantine_item import ProductsInQuarantineItem
from ..products.types.products_parent_categories_response import ProductsParentCategoriesResponse
from ..products.types.products_with_prices_by_articles_item import ProductsWithPricesByArticlesItem
from ..products.types.products_with_prices_item import ProductsWithPricesItem
from ..products.types.recover_product_card_from_trash_response import RecoverProductCardFromTrashResponse
from ..products.types.season_item import SeasonItem
from ..products.types.set_prices_and_discounts_response import SetPricesAndDiscountsResponse
from ..products.types.set_size_prices_response import SetSizePricesResponse
from ..products.types.set_wb_club_discounts_response import SetWbClubDiscountsResponse
from ..products.types.subject_characteristics_item import SubjectCharacteristicsItem
from ..products.types.subjects_list_item import SubjectsListItem
from ..products.types.tag_management_in_the_product_card_response import TagManagementInTheProductCardResponse
from ..products.types.tags_list_response import TagsListResponse
from ..products.types.transfer_product_card_to_trash_response import TransferProductCardToTrashResponse
from ..products.types.unprocessed_upload_details_item import UnprocessedUploadDetailsItem
from ..products.types.unprocessed_upload_state_response import UnprocessedUploadStateResponse
from ..products.types.update_contacts_list_response import UpdateContactsListResponse
from ..products.types.update_inventory_response import UpdateInventoryResponse
from ..products.types.update_product_cards_response import UpdateProductCardsResponse
from ..products.types.update_the_tag_response import UpdateTheTagResponse
from ..products.types.update_warehouse_response import UpdateWarehouseResponse
from ..products.types.upload_media_file_response import UploadMediaFileResponse
from ..products.types.upload_media_files_via_links_response import UploadMediaFilesViaLinksResponse
from ..products.types.vat_rate_item import VatRateItem
from ..products.types.warehouses_response import WarehousesResponse
from ..promotion.types.active_and_inactive_search_cluster_lists_item import (
    ActiveAndInactiveSearchClusterListsItem,
)
from ..promotion.types.add_product_to_the_promotion_response import AddProductToThePromotionResponse
from ..promotion.types.balance_item import BalanceItem
from ..promotion.types.campaign_budget_response import CampaignBudgetResponse
from ..promotion.types.campaigns_information_item import CampaignsInformationItem
from ..promotion.types.campaigns_lists_item import CampaignsListsItem
from ..promotion.types.campaigns_statistics_response import CampaignsStatisticsResponse
from ..promotion.types.changing_campaigns_bids_item import ChangingCampaignsBidsItem
from ..promotion.types.changing_placements_in_campaigns_with_custom_bid_response import (
    ChangingPlacementsInCampaignsWithCustomBidResponse,
)
from ..promotion.types.changing_the_list_of_product_cards_in_campaigns_item import (
    ChangingTheListOfProductCardsInCampaignsItem,
)
from ..promotion.types.create_campaign_response import CreateCampaignResponse
from ..promotion.types.daily_search_clusters_statistics_item import DailySearchClustersStatisticsItem
from ..promotion.types.delete_bids_from_search_clusters_response import DeleteBidsFromSearchClustersResponse
from ..promotion.types.delete_campaign_response import DeleteCampaignResponse
from ..promotion.types.information_about_media_campaign_item import InformationAboutMediaCampaignItem
from ..promotion.types.launch_campaign_response import LaunchCampaignResponse
from ..promotion.types.list_of_campaign_minus_phrases_item import ListOfCampaignMinusPhrasesItem
from ..promotion.types.list_of_media_campaigns_response import ListOfMediaCampaignsResponse
from ..promotion.types.list_of_products_for_participating_in_the_promotion_item import (
    ListOfProductsForParticipatingInThePromotionItem,
)
from ..promotion.types.list_of_search_clusters_bids_item import ListOfSearchClustersBidsItem
from ..promotion.types.media_campaign_statistics_response import MediaCampaignStatisticsResponse
from ..promotion.types.media_campaigns_number_response import MediaCampaignsNumberResponse
from ..promotion.types.minimum_bids_for_product_cards_item import MinimumBidsForProductCardsItem
from ..promotion.types.pause_campaign_response import PauseCampaignResponse
from ..promotion.types.product_cards_for_campaigns_response import ProductCardsForCampaignsResponse
from ..promotion.types.promotions_details_item import PromotionsDetailsItem
from ..promotion.types.promotions_list_item import PromotionsListItem
from ..promotion.types.receiving_costs_history_response import ReceivingCostsHistoryResponse
from ..promotion.types.receiving_the_history_of_account_topups_response import (
    ReceivingTheHistoryOfAccountTopupsResponse,
)
from ..promotion.types.recommended_bids_for_items_and_search_clusters_item import (
    RecommendedBidsForItemsAndSearchClustersItem,
)
from ..promotion.types.rename_campaign_response import RenameCampaignResponse
from ..promotion.types.search_clusters_statistics_item import SearchClustersStatisticsItem
from ..promotion.types.set_bids_for_search_clusters_response import SetBidsForSearchClustersResponse
from ..promotion.types.setting_and_deleting_minus_phrases_response import (
    SettingAndDeletingMinusPhrasesResponse,
)
from ..promotion.types.stop_campaign_response import StopCampaignResponse
from ..promotion.types.subjects_for_campaigns_response import SubjectsForCampaignsResponse
from ..promotion.types.topup_of_the_campaign_budget_response import TopupOfTheCampaignBudgetResponse
from ..reports.types.blocked_product_cards_item import BlockedProductCardsItem
from ..reports.types.check_the_status_response import CheckTheStatusResponse
from ..reports.types.generate_the_report_response import GenerateTheReportResponse
from ..reports.types.hidden_from_the_catalog_item import HiddenFromTheCatalogItem
from ..reports.types.logistics_and_storage_costs_multiplier_item import LogisticsAndStorageCostsMultiplierItem
from ..reports.types.orders_response import OrdersResponse
from ..reports.types.parent_categories_of_the_brand_item import ParentCategoriesOfTheBrandItem
from ..reports.types.product_labeling_item import ProductLabelingItem
from ..reports.types.report_item import ReportItem
from ..reports.types.report_on_products_with_mandatory_labeling_item import (
    ReportOnProductsWithMandatoryLabelingItem,
)
from ..reports.types.sales_response import SalesResponse
from ..reports.types.selfpurchases_item import SelfpurchasesItem
from ..reports.types.seller_brands_item import SellerBrandsItem
from ..reports.types.substitutions_and_incorrect_attachments_item import (
    SubstitutionsAndIncorrectAttachmentsItem,
)
from ..reports.types.warehouse_measurements_item import WarehouseMeasurementsItem
from ..reports.types.warehouse_response import WarehouseResponse
from ..tariffs.types.box_tariffs_item import BoxTariffsItem
from ..tariffs.types.pallet_tariffs_item import PalletTariffsItem
from ..tariffs.types.product_category_commission_response import ProductCategoryCommissionResponse
from ..tariffs.types.return_tariffs_item import ReturnTariffsItem
from ..tariffs.types.supply_tariffs_response import SupplyTariffsResponse
from .base import BaseType
from .error import Error
from .product_detail import (
    ProductDetail,
    ProductDetailColor,
    ProductDetailPrice,
    ProductDetailSize,
    ProductDetailStock,
)
from .request_limit import RequestLimit


__all__ = (
    "AcceptanceOptionsItem",
    "ActiveAndInactiveSearchClusterListsItem",
    "AddAssemblyOrdersToTheSupplyResponse",
    "AddBoxesToTheSupplyItem",
    "AddCustomDeclarationNumberToTheOrderResponse",
    "AddCustomDeclarationToTheOrdersResponse",
    "AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem",
    "AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem",
    "AddDataMatrixCodeToTheAssemblyOrderResponse",
    "AddDataMatrixCodeToTheOrderResponse",
    "AddExpirationDateToTheAssemblyOrderResponse",
    "AddGtinToAssemblyOrdersItem",
    "AddGtinToTheAssemblyOrderResponse",
    "AddGtinToTheAssemblyOrdersItem",
    "AddGtinToTheOrderResponse",
    "AddImeiToAssemblyOrdersItem",
    "AddImeiToTheAssemblyOrderResponse",
    "AddImeiToTheAssemblyOrdersItem",
    "AddImeiToTheOrderResponse",
    "AddProductToThePromotionResponse",
    "AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem",
    "AddUinUniqueIdentificationNumberToAssemblyOrdersItem",
    "AddUinUniqueIdentificationNumberToTheAssemblyOrderResponse",
    "AddUinUniqueIdentificationNumberToTheOrderResponse",
    "AListOfSellerActiveOrInvitedUsersItem",
    "AllAssemblyOrdersForReshipmentItem",
    "AnswerBuyersApplicationResponse",
    "AssemblyOrderMetadataResponse",
    "AssemblyOrdersItem",
    "AssemblyOrdersMetadataItem",
    "AssemblyOrdersStatusesItem",
    "AssemblyOrdersStickersItem",
    "AssemblyOrderStatusesItem",
    "AssignADataMatrixCodeToTheAssemblyOrderResponse",
    "ASuppliesListItem",
    "B2BBuyerInformationItem",
    "BalanceItem",
    "BaseType",
    "BlockedProductCardsItem",
    "BoxTariffsItem",
    "BrandsItem",
    "BuyerInformationItem",
    "BuyersReturnApplicationsItem",
    "CampaignBudgetResponse",
    "CampaignsInformationItem",
    "CampaignsListsItem",
    "CampaignsStatisticsResponse",
    "CancelAssemblyOrdersItem",
    "CancelTheAssemblyOrderResponse",
    "CancelTheAssemblyOrdersItem",
    "CancelTheOrderResponse",
    "ChangingCampaignsBidsItem",
    "ChangingPlacementsInCampaignsWithCustomBidResponse",
    "ChangingTheListOfProductCardsInCampaignsItem",
    "ChatEventsItem",
    "ChatListItem",
    "CheckIfTheOrderBelongsToTheBuyerResponse",
    "CheckTheStatusResponse",
    "ColorResponse",
    "ConnectionCheckResponse",
    "ContactsListItem",
    "CountryOfOriginResponse",
    "CourierInfoItem",
    "CreateANewSupplyResponse",
    "CreateAnInvitationForANewUserResponse",
    "CreateATagResponse",
    "CreateCampaignResponse",
    "CreatePassResponse",
    "CreateProductCardsResponse",
    "CreateProductCardsWithMergeResponse",
    "CreateTheReportResponse",
    "CreateWarehouseResponse",
    "DailySearchClustersStatisticsItem",
    "DeleteAssemblyOrderMetadataItem",
    "DeleteAssemblyOrderMetadataResponse",
    "DeleteAssemblyOrdersMetadataItem",
    "DeleteBidsFromSearchClustersResponse",
    "DeleteBoxesFromTheSupplyResponse",
    "DeleteCampaignResponse",
    "DeleteInventoryResponse",
    "DeleteOrderMetadataResponse",
    "DeleteThePassResponse",
    "DeleteTheSupplyResponse",
    "DeleteTheTagResponse",
    "DeleteUserResponse",
    "DeleteWarehouseResponse",
    "DeliveryDateAndTimeItem",
    "DocumentResponse",
    "DocumentsCategoriesItem",
    "DocumentsListItem",
    "DocumentsResponse",
    "EditResponseToFeedbackResponse",
    "Error",
    "FeedbacksListItem",
    "FileFromTheMessageResponse",
    "GenderItem",
    "GenerateTheReportResponse",
    "GenerationOfSkusItem",
    "GettingSellerPortalNewsItem",
    "GroupDataItem",
    "GroupedProductCardsStatisticsPerDaysItem",
    "HiddenFromTheCatalogItem",
    "HscodesItem",
    "InformationAboutMediaCampaignItem",
    "InformationOnCompletedOrdersItem",
    "InformationOnPaidDeliveryResponse",
    "InventoryItem",
    "LaunchCampaignResponse",
    "LimitsForTheProductCardsResponse",
    "ListOfArchivedFeedbacksItem",
    "ListOfCampaignMinusPhrasesItem",
    "ListOfFailedProductCardsWithErrorsItem",
    "ListOfMediaCampaignsResponse",
    "ListOfPinnedAndUnpinnedFeedbackResponse",
    "ListOfProductsForParticipatingInThePromotionItem",
    "ListOfSearchClustersBidsItem",
    "LogisticsAndStorageCostsMultiplierItem",
    "MainPageResponse",
    "MediaCampaignsNumberResponse",
    "MediaCampaignStatisticsResponse",
    "MergingOrSeparatingOfProductCardsResponse",
    "MinimumBidsForProductCardsItem",
    "MoveTheSupplyToTheDeliveryResponse",
    "NewAssemblyOrdersItem",
    "NewAssemblyOrdersListItem",
    "NewOrdersItem",
    "NewOrdersListItem",
    "NotifyThatTheAssemblyOrderIsReadyForPickupResponse",
    "NotifyThatTheAssemblyOrdersAreReadyForPickupItem",
    "NotifyThatTheBuyerHasDeclinedTheOrderResponse",
    "NotifyThatTheBuyerRefusedTheOrderResponse",
    "NotifyThatTheOrderHasBeenAcceptedByTheBuyerResponse",
    "NotifyThatTheOrdersAreDeclinedItem",
    "NotifyThatTheOrdersAreReceivedItem",
    "NotifyThatTheOrdersWereReceivedByTheBuyersItem",
    "NumberOfFeedbacksItem",
    "NumberOfQuestionsItem",
    "OfficesForPassResponse",
    "OfficesResponse",
    "OrderMetadataItem",
    "OrdersAndPositionsByProductSearchTextsResponse",
    "OrdersResponse",
    "OrdersStatusesItem",
    "OrdersStickersItem",
    "OrdersWithClientInformationItem",
    "PaginationByGroupsResponse",
    "PaginationByProductsWithinAGroupResponse",
    "PalletTariffsItem",
    "ParentCategoriesOfTheBrandItem",
    "PassesResponse",
    "PauseCampaignResponse",
    "PinFeedbackResponse",
    "PinnedAndUnpinnedFeedbackNumberResponse",
    "PinnedFeedbackLimitsResponse",
    "ProcessedUploadDetailsItem",
    "ProcessedUploadStateResponse",
    "ProductCardsForCampaignsResponse",
    "ProductCardsInTrashListItem",
    "ProductCardsListItem",
    "ProductCardsStatisticsPerDaysResponse",
    "ProductCardsStatisticsPerPeriodResponse",
    "ProductCategoryCommissionResponse",
    "ProductDataItem",
    "ProductDetail",
    "ProductDetailColor",
    "ProductDetailPrice",
    "ProductDetailSize",
    "ProductDetailStock",
    "ProductLabelingItem",
    "ProductsInQuarantineItem",
    "ProductSizesWithPricesItem",
    "ProductsParentCategoriesResponse",
    "ProductsWithPricesByArticlesItem",
    "ProductsWithPricesItem",
    "PromotionsDetailsItem",
    "PromotionsListItem",
    "QuestionListItem",
    "RealizationSalesReportResponse",
    "ReceivingCostsHistoryResponse",
    "ReceivingTheHistoryOfAccountTopupsResponse",
    "RecommendedBidsForItemsAndSearchClustersItem",
    "RecoverProductCardFromTrashResponse",
    "RegenerateTheReportResponse",
    "RenameCampaignResponse",
    "ReplyToFeedbackResponse",
    "ReportItem",
    "ReportOnProductsWithMandatoryLabelingItem",
    "RequestLimit",
    "RetrieveInformationOnCompletedAssemblyOrdersItem",
    "ReturnProductByFeedbackIdItem",
    "ReturnTariffsItem",
    "SalesResponse",
    "SearchClustersStatisticsItem",
    "SearchTextsByProductResponse",
    "SeasonItem",
    "SelfpurchasesItem",
    "SellerBrandsItem",
    "SellerInformationResponse",
    "SellersBalanceResponse",
    "SendMessageItem",
    "SetBidsForSearchClustersResponse",
    "SetPricesAndDiscountsResponse",
    "SetSizePricesResponse",
    "SettingAndDeletingMinusPhrasesResponse",
    "SetWbClubDiscountsResponse",
    "SizeDataItem",
    "StatusHistoryForCrossborderOrdersItem",
    "StickersForAssemblyOrdersWithDeliveryToPickupPointItem",
    "StickersForCrossborderAssemblyOrdersItem",
    "StopCampaignResponse",
    "SubjectCharacteristicsItem",
    "SubjectsForCampaignsResponse",
    "SubjectsListItem",
    "SubstitutionsAndIncorrectAttachmentsItem",
    "SuppliesListResponse",
    "SupplyAssemblyOrderIdsItem",
    "SupplyBoxesListItem",
    "SupplyDetailsResponse",
    "SupplyPackageResponse",
    "SupplyProductsResponse",
    "SupplyTariffsResponse",
    "TagManagementInTheProductCardResponse",
    "TagsListResponse",
    "TheFeedbackByIdItem",
    "TheQuestionByIdItem",
    "TheReportResponse",
    "TheReportsListItem",
    "TheSupplyBoxQrCodeStickersItem",
    "TheSupplyQrCodeResponse",
    "TopupOfTheCampaignBudgetResponse",
    "TransferProductCardToTrashResponse",
    "TransferToAssemblyItem",
    "TransferToAssemblyResponse",
    "TransferToDeliveryItem",
    "TransferToDeliveryResponse",
    "TransitDirectionsResponse",
    "UnansweredFeedbacksItem",
    "UnansweredQuestionsItem",
    "UnpinFeedbackResponse",
    "UnprocessedUploadDetailsItem",
    "UnprocessedUploadStateResponse",
    "UnseenFeedbacksAndQuestionsItem",
    "UpdateContactsListResponse",
    "UpdateInventoryResponse",
    "UpdatePassResponse",
    "UpdateProductCardsResponse",
    "UpdateTheTagResponse",
    "UpdateUsersAccessPermissionsResponse",
    "UpdateWarehouseResponse",
    "UploadMediaFileResponse",
    "UploadMediaFilesViaLinksResponse",
    "VatRateItem",
    "WarehouseDataItem",
    "WarehouseMeasurementsItem",
    "WarehouseResponse",
    "WarehousesListResponse",
    "WarehousesResponse",
    "WbWarehousesInventoryItem",
    "WorkingWithQuestionsItem",
)
