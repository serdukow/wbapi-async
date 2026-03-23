from ..orders_fbw.methods.acceptance_options import AcceptanceOptions
from ..promotion.methods.active_and_inactive_search_cluster_lists import ActiveAndInactiveSearchClusterLists
from ..orders_fbs.methods.add_assembly_orders_to_the_supply import AddAssemblyOrdersToTheSupply
from ..orders_fbs.methods.add_boxes_to_the_supply import AddBoxesToTheSupply
from ..orders_fbs.methods.add_custom_declaration_number_to_the_order import (
    AddCustomDeclarationNumberToTheOrder,
)
from ..orders_dbs.methods.add_custom_declaration_to_the_orders import AddCustomDeclarationToTheOrders
from ..orders_fbs.methods.add_data_matrix_code_to_the_assembly_order import (
    AddDataMatrixCodeToTheAssemblyOrder,
)
from ..orders_dbw.methods.add_data_matrix_code_to_the_order import AddDataMatrixCodeToTheOrder
from ..orders_dbs.methods.add_data_matrix_codes_to_assembly_orders_chestny_znak import (
    AddDataMatrixCodesToAssemblyOrdersChestnyZnak,
)
from ..in_store_pickup.methods.add_data_matrix_codes_to_the_assembly_orders_chestny_znak import (
    AddDataMatrixCodesToTheAssemblyOrdersChestnyZnak,
)
from ..orders_fbs.methods.add_expiration_date_to_the_assembly_order import AddExpirationDateToTheAssemblyOrder
from ..orders_dbs.methods.add_gtin_to_assembly_orders import AddGtinToAssemblyOrders
from ..orders_fbs.methods.add_gtin_to_the_assembly_order import AddGtinToTheAssemblyOrder
from ..in_store_pickup.methods.add_gtin_to_the_assembly_orders import AddGtinToTheAssemblyOrders
from ..orders_dbw.methods.add_gtin_to_the_order import AddGtinToTheOrder
from ..orders_dbs.methods.add_imei_to_assembly_orders import AddImeiToAssemblyOrders
from ..orders_fbs.methods.add_imei_to_the_assembly_order import AddImeiToTheAssemblyOrder
from ..in_store_pickup.methods.add_imei_to_the_assembly_orders import AddImeiToTheAssemblyOrders
from ..orders_dbw.methods.add_imei_to_the_order import AddImeiToTheOrder
from ..promotion.methods.add_product_to_the_promotion import AddProductToThePromotion
from ..orders_dbs.methods.add_uin_unique_identification_number_to_assembly_orders import (
    AddUinUniqueIdentificationNumberToAssemblyOrders,
)
from ..orders_fbs.methods.add_uin_unique_identification_number_to_the_assembly_order import (
    AddUinUniqueIdentificationNumberToTheAssemblyOrder,
)
from ..orders_dbw.methods.add_uin_unique_identification_number_to_the_order import (
    AddUinUniqueIdentificationNumberToTheOrder,
)
from ..in_store_pickup.methods.add_uin_unique_identification_numbers_to_the_assembly_orders import (
    AddUinUniqueIdentificationNumbersToTheAssemblyOrders,
)
from ..communications.methods.answer_buyers_application import AnswerBuyersApplication
from ..in_store_pickup.methods.assign_a_data_matrix_code_to_the_assembly_order import (
    AssignADataMatrixCodeToTheAssemblyOrder,
)
from ..orders_dbs.methods.b2_b_buyer_information import B2BBuyerInformation
from ..orders_dbw.methods.buyer_information import BuyerInformation
from ..orders_dbs.methods.cancel_assembly_orders import CancelAssemblyOrders
from ..orders_fbs.methods.cancel_the_assembly_order import CancelTheAssemblyOrder
from ..in_store_pickup.methods.cancel_the_assembly_orders import CancelTheAssemblyOrders
from ..orders_dbw.methods.cancel_the_order import CancelTheOrder
from ..promotion.methods.changing_campaigns_bids import ChangingCampaignsBids
from ..promotion.methods.changing_placements_in_campaigns_with_custom_bid import (
    ChangingPlacementsInCampaignsWithCustomBid,
)
from ..promotion.methods.changing_the_list_of_product_cards_in_campaigns import (
    ChangingTheListOfProductCardsInCampaigns,
)
from ..in_store_pickup.methods.check_if_the_order_belongs_to_the_buyer import CheckIfTheOrderBelongsToTheBuyer
from ..orders_dbw.methods.courier_info import CourierInfo
from ..orders_fbs.methods.create_a_new_supply import CreateANewSupply
from ..products.methods.create_a_tag import CreateATag
from ..general.methods.create_an_invitation_for_a_new_user import CreateAnInvitationForANewUser
from ..promotion.methods.create_campaign import CreateCampaign
from ..orders_fbs.methods.create_pass import CreatePass
from ..products.methods.create_product_cards import CreateProductCards
from ..products.methods.create_product_cards_with_merge import CreateProductCardsWithMerge
from ..analytics.methods.create_the_report import CreateTheReport
from ..products.methods.create_warehouse import CreateWarehouse
from ..promotion.methods.daily_search_clusters_statistics import DailySearchClustersStatistics
from ..orders_fbs.methods.delete_assembly_order_metadata import DeleteAssemblyOrderMetadata
from ..orders_dbs.methods.delete_assembly_orders_metadata import DeleteAssemblyOrdersMetadata
from ..promotion.methods.delete_bids_from_search_clusters import DeleteBidsFromSearchClusters
from ..orders_fbs.methods.delete_boxes_from_the_supply import DeleteBoxesFromTheSupply
from ..products.methods.delete_inventory import DeleteInventory
from ..orders_dbw.methods.delete_order_metadata import DeleteOrderMetadata
from ..orders_fbs.methods.delete_the_pass import DeleteThePass
from ..orders_fbs.methods.delete_the_supply import DeleteTheSupply
from ..products.methods.delete_the_tag import DeleteTheTag
from ..general.methods.delete_user import DeleteUser
from ..products.methods.delete_warehouse import DeleteWarehouse
from ..orders_dbw.methods.delivery_date_and_time import DeliveryDateAndTime
from ..communications.methods.edit_response_to_feedback import EditResponseToFeedback
from ..products.methods.generation_of_skus import GenerationOfSkus
from ..general.methods.get_a_list_of_seller_active_or_invited_users import (
    GetAListOfSellerActiveOrInvitedUsers,
)
from ..orders_fbs.methods.get_a_supplies_list import GetASuppliesList
from ..orders_fbs.methods.get_all_assembly_orders_for_reshipment import GetAllAssemblyOrdersForReshipment
from ..in_store_pickup.methods.get_assembly_order_metadata import GetAssemblyOrderMetadata
from ..orders_dbs.methods.get_assembly_order_statuses import GetAssemblyOrderStatuses
from ..orders_fbs.methods.get_assembly_orders import GetAssemblyOrders
from ..orders_fbs.methods.get_assembly_orders_metadata import GetAssemblyOrdersMetadata
from ..orders_fbs.methods.get_assembly_orders_statuses import GetAssemblyOrdersStatuses
from ..orders_fbs.methods.get_assembly_orders_stickers import GetAssemblyOrdersStickers
from ..promotion.methods.get_balance import GetBalance
from ..reports.methods.get_blocked_product_cards import GetBlockedProductCards
from ..tariffs.methods.get_box_tariffs import GetBoxTariffs
from ..products.methods.get_brands import GetBrands
from ..communications.methods.get_buyers_return_applications import GetBuyersReturnApplications
from ..promotion.methods.get_campaign_budget import GetCampaignBudget
from ..promotion.methods.get_campaigns_information import GetCampaignsInformation
from ..promotion.methods.get_campaigns_lists import GetCampaignsLists
from ..promotion.methods.get_campaigns_statistics import GetCampaignsStatistics
from ..communications.methods.get_chat_events import GetChatEvents
from ..communications.methods.get_chat_list import GetChatList
from ..reports.methods.get_check_the_status import GetCheckTheStatus
from ..products.methods.get_color import GetColor
from ..general.methods.get_connection_check import GetConnectionCheck
from ..products.methods.get_contacts_list import GetContactsList
from ..products.methods.get_country_of_origin import GetCountryOfOrigin
from ..reports.methods.get_create_the_report import GetCreateTheReport
from ..promotion.methods.get_delete_campaign import GetDeleteCampaign
from ..finances.methods.get_document import GetDocument
from ..finances.methods.get_documents import GetDocuments
from ..finances.methods.get_documents_categories import GetDocumentsCategories
from ..finances.methods.get_documents_list import GetDocumentsList
from ..communications.methods.get_feedbacks_list import GetFeedbacksList
from ..communications.methods.get_file_from_the_message import GetFileFromTheMessage
from ..products.methods.get_gender import GetGender
from ..reports.methods.get_generate_the_report import GetGenerateTheReport
from ..general.methods.get_getting_seller_portal_news import GetGettingSellerPortalNews
from ..reports.methods.get_hidden_from_the_catalog import GetHiddenFromTheCatalog
from ..products.methods.get_hscodes import GetHscodes
from ..promotion.methods.get_information_about_media_campaign import GetInformationAboutMediaCampaign
from ..orders_dbw.methods.get_information_on_completed_orders import GetInformationOnCompletedOrders
from ..orders_dbs.methods.get_information_on_paid_delivery import GetInformationOnPaidDelivery
from ..products.methods.get_inventory import GetInventory
from ..promotion.methods.get_launch_campaign import GetLaunchCampaign
from ..products.methods.get_limits_for_the_product_cards import GetLimitsForTheProductCards
from ..communications.methods.get_list_of_archived_feedbacks import GetListOfArchivedFeedbacks
from ..promotion.methods.get_list_of_media_campaigns import GetListOfMediaCampaigns
from ..communications.methods.get_list_of_pinned_and_unpinned_feedback import (
    GetListOfPinnedAndUnpinnedFeedback,
)
from ..promotion.methods.get_list_of_products_for_participating_in_the_promotion import (
    GetListOfProductsForParticipatingInThePromotion,
)
from ..reports.methods.get_logistics_and_storage_costs_multiplier import GetLogisticsAndStorageCostsMultiplier
from ..promotion.methods.get_media_campaigns_number import GetMediaCampaignsNumber
from ..orders_fbs.methods.get_new_assembly_orders import GetNewAssemblyOrders
from ..in_store_pickup.methods.get_new_assembly_orders_list import GetNewAssemblyOrdersList
from ..orders_dbw.methods.get_new_orders import GetNewOrders
from ..orders_dbs.methods.get_new_orders_list import GetNewOrdersList
from ..communications.methods.get_number_of_feedbacks import GetNumberOfFeedbacks
from ..communications.methods.get_number_of_questions import GetNumberOfQuestions
from ..products.methods.get_offices import GetOffices
from ..orders_fbs.methods.get_offices_for_pass import GetOfficesForPass
from ..orders_dbw.methods.get_order_metadata import GetOrderMetadata
from ..reports.methods.get_orders import GetOrders
from ..orders_dbw.methods.get_orders_statuses import GetOrdersStatuses
from ..orders_dbw.methods.get_orders_stickers import GetOrdersStickers
from ..tariffs.methods.get_pallet_tariffs import GetPalletTariffs
from ..reports.methods.get_parent_categories_of_the_brand import GetParentCategoriesOfTheBrand
from ..orders_fbs.methods.get_passes import GetPasses
from ..promotion.methods.get_pause_campaign import GetPauseCampaign
from ..communications.methods.get_pinned_and_unpinned_feedback_number import (
    GetPinnedAndUnpinnedFeedbackNumber,
)
from ..communications.methods.get_pinned_feedback_limits import GetPinnedFeedbackLimits
from ..products.methods.get_processed_upload_details import GetProcessedUploadDetails
from ..products.methods.get_processed_upload_state import GetProcessedUploadState
from ..tariffs.methods.get_product_category_commission import GetProductCategoryCommission
from .get_product_detail import GetProductDetail
from ..reports.methods.get_product_labeling import GetProductLabeling
from ..products.methods.get_product_sizes_with_prices import GetProductSizesWithPrices
from ..products.methods.get_products_in_quarantine import GetProductsInQuarantine
from ..products.methods.get_products_parent_categories import GetProductsParentCategories
from ..products.methods.get_products_with_prices import GetProductsWithPrices
from ..products.methods.get_products_with_prices_by_articles import GetProductsWithPricesByArticles
from ..promotion.methods.get_promotions_details import GetPromotionsDetails
from ..promotion.methods.get_promotions_list import GetPromotionsList
from ..communications.methods.get_question_list import GetQuestionList
from ..finances.methods.get_realization_sales_report import GetRealizationSalesReport
from ..promotion.methods.get_receiving_costs_history import GetReceivingCostsHistory
from ..promotion.methods.get_receiving_the_history_of_account_topups import (
    GetReceivingTheHistoryOfAccountTopups,
)
from ..promotion.methods.get_recommended_bids_for_items_and_search_clusters import (
    GetRecommendedBidsForItemsAndSearchClusters,
)
from ..reports.methods.get_report import GetReport
from ..in_store_pickup.methods.get_retrieve_information_on_completed_assembly_orders import (
    GetRetrieveInformationOnCompletedAssemblyOrders,
)
from ..tariffs.methods.get_return_tariffs import GetReturnTariffs
from ..reports.methods.get_sales import GetSales
from ..products.methods.get_season import GetSeason
from ..reports.methods.get_selfpurchases import GetSelfpurchases
from ..reports.methods.get_seller_brands import GetSellerBrands
from ..general.methods.get_seller_information import GetSellerInformation
from ..finances.methods.get_sellers_balance import GetSellersBalance
from ..orders_dbs.methods.get_stickers_for_assembly_orders_with_delivery_to_pickup_point import (
    GetStickersForAssemblyOrdersWithDeliveryToPickupPoint,
)
from ..orders_fbs.methods.get_stickers_for_crossborder_assembly_orders import (
    GetStickersForCrossborderAssemblyOrders,
)
from ..promotion.methods.get_stop_campaign import GetStopCampaign
from ..products.methods.get_subject_characteristics import GetSubjectCharacteristics
from ..promotion.methods.get_subjects_for_campaigns import GetSubjectsForCampaigns
from ..products.methods.get_subjects_list import GetSubjectsList
from ..reports.methods.get_substitutions_and_incorrect_attachments import (
    GetSubstitutionsAndIncorrectAttachments,
)
from ..orders_fbs.methods.get_supply_assembly_order_ids import GetSupplyAssemblyOrderIds
from ..orders_fbs.methods.get_supply_boxes_list import GetSupplyBoxesList
from ..orders_fbs.methods.get_supply_details import GetSupplyDetails
from ..orders_fbw.methods.get_supply_package import GetSupplyPackage
from ..orders_fbw.methods.get_supply_products import GetSupplyProducts
from ..tariffs.methods.get_supply_tariffs import GetSupplyTariffs
from ..products.methods.get_tags_list import GetTagsList
from ..communications.methods.get_the_feedback_by_id import GetTheFeedbackById
from ..communications.methods.get_the_question_by_id import GetTheQuestionById
from ..analytics.methods.get_the_report import GetTheReport
from ..analytics.methods.get_the_reports_list import GetTheReportsList
from ..orders_fbs.methods.get_the_supply_box_qr_code_stickers import GetTheSupplyBoxQrCodeStickers
from ..orders_fbs.methods.get_the_supply_qr_code import GetTheSupplyQrCode
from ..orders_fbw.methods.get_transit_directions import GetTransitDirections
from ..communications.methods.get_unanswered_feedbacks import GetUnansweredFeedbacks
from ..communications.methods.get_unanswered_questions import GetUnansweredQuestions
from ..products.methods.get_unprocessed_upload_details import GetUnprocessedUploadDetails
from ..products.methods.get_unprocessed_upload_state import GetUnprocessedUploadState
from ..communications.methods.get_unseen_feedbacks_and_questions import GetUnseenFeedbacksAndQuestions
from ..products.methods.get_vat_rate import GetVatRate
from ..reports.methods.get_warehouse import GetWarehouse
from ..reports.methods.get_warehouse_measurements import GetWarehouseMeasurements
from ..products.methods.get_warehouses import GetWarehouses
from ..orders_fbw.methods.get_warehouses_list import GetWarehousesList
from ..analytics.methods.group_data import GroupData
from ..analytics.methods.grouped_product_cards_statistics_per_days import GroupedProductCardsStatisticsPerDays
from ..promotion.methods.list_of_campaign_minus_phrases import ListOfCampaignMinusPhrases
from ..products.methods.list_of_failed_product_cards_with_errors import ListOfFailedProductCardsWithErrors
from ..promotion.methods.list_of_search_clusters_bids import ListOfSearchClustersBids
from ..analytics.methods.main_page import MainPage
from ..promotion.methods.media_campaign_statistics import MediaCampaignStatistics
from ..products.methods.merging_or_separating_of_product_cards import MergingOrSeparatingOfProductCards
from ..promotion.methods.minimum_bids_for_product_cards import MinimumBidsForProductCards
from ..orders_fbs.methods.move_the_supply_to_the_delivery import MoveTheSupplyToTheDelivery
from ..in_store_pickup.methods.notify_that_the_assembly_order_is_ready_for_pickup import (
    NotifyThatTheAssemblyOrderIsReadyForPickup,
)
from ..in_store_pickup.methods.notify_that_the_assembly_orders_are_ready_for_pickup import (
    NotifyThatTheAssemblyOrdersAreReadyForPickup,
)
from ..orders_dbs.methods.notify_that_the_buyer_has_declined_the_order import (
    NotifyThatTheBuyerHasDeclinedTheOrder,
)
from ..in_store_pickup.methods.notify_that_the_buyer_refused_the_order import (
    NotifyThatTheBuyerRefusedTheOrder,
)
from ..orders_dbs.methods.notify_that_the_order_has_been_accepted_by_the_buyer import (
    NotifyThatTheOrderHasBeenAcceptedByTheBuyer,
)
from ..orders_dbs.methods.notify_that_the_orders_are_declined import NotifyThatTheOrdersAreDeclined
from ..orders_dbs.methods.notify_that_the_orders_are_received import NotifyThatTheOrdersAreReceived
from ..in_store_pickup.methods.notify_that_the_orders_were_received_by_the_buyers import (
    NotifyThatTheOrdersWereReceivedByTheBuyers,
)
from ..analytics.methods.orders_and_positions_by_product_search_texts import (
    OrdersAndPositionsByProductSearchTexts,
)
from ..orders_fbs.methods.orders_with_client_information import OrdersWithClientInformation
from ..analytics.methods.pagination_by_groups import PaginationByGroups
from ..analytics.methods.pagination_by_products_within_a_group import PaginationByProductsWithinAGroup
from ..communications.methods.pin_feedback import PinFeedback
from ..promotion.methods.product_cards_for_campaigns import ProductCardsForCampaigns
from ..products.methods.product_cards_in_trash_list import ProductCardsInTrashList
from ..products.methods.product_cards_list import ProductCardsList
from ..analytics.methods.product_cards_statistics_per_days import ProductCardsStatisticsPerDays
from ..analytics.methods.product_cards_statistics_per_period import ProductCardsStatisticsPerPeriod
from ..analytics.methods.product_data import ProductData
from ..products.methods.recover_product_card_from_trash import RecoverProductCardFromTrash
from ..analytics.methods.regenerate_the_report import RegenerateTheReport
from ..promotion.methods.rename_campaign import RenameCampaign
from ..communications.methods.reply_to_feedback import ReplyToFeedback
from ..reports.methods.report_on_products_with_mandatory_labeling import ReportOnProductsWithMandatoryLabeling
from ..communications.methods.return_product_by_feedback_id import ReturnProductByFeedbackId
from ..promotion.methods.search_clusters_statistics import SearchClustersStatistics
from ..analytics.methods.search_texts_by_product import SearchTextsByProduct
from ..communications.methods.send_message import SendMessage
from ..promotion.methods.set_bids_for_search_clusters import SetBidsForSearchClusters
from ..products.methods.set_prices_and_discounts import SetPricesAndDiscounts
from ..products.methods.set_size_prices import SetSizePrices
from ..products.methods.set_wb_club_discounts import SetWbClubDiscounts
from ..promotion.methods.setting_and_deleting_minus_phrases import SettingAndDeletingMinusPhrases
from ..analytics.methods.size_data import SizeData
from ..orders_fbs.methods.status_history_for_crossborder_orders import StatusHistoryForCrossborderOrders
from ..orders_fbw.methods.supplies_list import SuppliesList
from ..products.methods.tag_management_in_the_product_card import TagManagementInTheProductCard
from ..promotion.methods.topup_of_the_campaign_budget import TopupOfTheCampaignBudget
from ..products.methods.transfer_product_card_to_trash import TransferProductCardToTrash
from ..orders_dbw.methods.transfer_to_assembly import TransferToAssembly
from ..orders_dbw.methods.transfer_to_delivery import TransferToDelivery
from ..communications.methods.unpin_feedback import UnpinFeedback
from ..products.methods.update_contacts_list import UpdateContactsList
from ..products.methods.update_inventory import UpdateInventory
from ..orders_fbs.methods.update_pass import UpdatePass
from ..products.methods.update_product_cards import UpdateProductCards
from ..products.methods.update_the_tag import UpdateTheTag
from ..general.methods.update_users_access_permissions import UpdateUsersAccessPermissions
from ..products.methods.update_warehouse import UpdateWarehouse
from ..products.methods.upload_media_file import UploadMediaFile
from ..products.methods.upload_media_files_via_links import UploadMediaFilesViaLinks
from ..analytics.methods.warehouse_data import WarehouseData
from .base import WbMethod
from ..communications.methods.working_with_questions import WorkingWithQuestions


__all__ = (
    "AcceptanceOptions",
    "ActiveAndInactiveSearchClusterLists",
    "AddAssemblyOrdersToTheSupply",
    "AddBoxesToTheSupply",
    "AddCustomDeclarationNumberToTheOrder",
    "AddCustomDeclarationToTheOrders",
    "AddDataMatrixCodeToTheAssemblyOrder",
    "AddDataMatrixCodeToTheOrder",
    "AddDataMatrixCodesToAssemblyOrdersChestnyZnak",
    "AddDataMatrixCodesToTheAssemblyOrdersChestnyZnak",
    "AddExpirationDateToTheAssemblyOrder",
    "AddGtinToAssemblyOrders",
    "AddGtinToTheAssemblyOrder",
    "AddGtinToTheAssemblyOrders",
    "AddGtinToTheOrder",
    "AddImeiToAssemblyOrders",
    "AddImeiToTheAssemblyOrder",
    "AddImeiToTheAssemblyOrders",
    "AddImeiToTheOrder",
    "AddProductToThePromotion",
    "AddUinUniqueIdentificationNumberToAssemblyOrders",
    "AddUinUniqueIdentificationNumberToTheAssemblyOrder",
    "AddUinUniqueIdentificationNumberToTheOrder",
    "AddUinUniqueIdentificationNumbersToTheAssemblyOrders",
    "AnswerBuyersApplication",
    "AssignADataMatrixCodeToTheAssemblyOrder",
    "B2BBuyerInformation",
    "BuyerInformation",
    "CancelAssemblyOrders",
    "CancelTheAssemblyOrder",
    "CancelTheAssemblyOrders",
    "CancelTheOrder",
    "ChangingCampaignsBids",
    "ChangingPlacementsInCampaignsWithCustomBid",
    "ChangingTheListOfProductCardsInCampaigns",
    "CheckIfTheOrderBelongsToTheBuyer",
    "CourierInfo",
    "CreateANewSupply",
    "CreateATag",
    "CreateAnInvitationForANewUser",
    "CreateCampaign",
    "CreatePass",
    "CreateProductCards",
    "CreateProductCardsWithMerge",
    "CreateTheReport",
    "CreateWarehouse",
    "DailySearchClustersStatistics",
    "DeleteAssemblyOrderMetadata",
    "DeleteAssemblyOrdersMetadata",
    "DeleteBidsFromSearchClusters",
    "DeleteBoxesFromTheSupply",
    "DeleteInventory",
    "DeleteOrderMetadata",
    "DeleteThePass",
    "DeleteTheSupply",
    "DeleteTheTag",
    "DeleteUser",
    "DeleteWarehouse",
    "DeliveryDateAndTime",
    "EditResponseToFeedback",
    "GenerationOfSkus",
    "GetAListOfSellerActiveOrInvitedUsers",
    "GetASuppliesList",
    "GetAllAssemblyOrdersForReshipment",
    "GetAssemblyOrderMetadata",
    "GetAssemblyOrderStatuses",
    "GetAssemblyOrders",
    "GetAssemblyOrdersMetadata",
    "GetAssemblyOrdersStatuses",
    "GetAssemblyOrdersStickers",
    "GetBalance",
    "GetBlockedProductCards",
    "GetBoxTariffs",
    "GetBrands",
    "GetBuyersReturnApplications",
    "GetCampaignBudget",
    "GetCampaignsInformation",
    "GetCampaignsLists",
    "GetCampaignsStatistics",
    "GetChatEvents",
    "GetChatList",
    "GetCheckTheStatus",
    "GetColor",
    "GetConnectionCheck",
    "GetContactsList",
    "GetCountryOfOrigin",
    "GetCreateTheReport",
    "GetDeleteCampaign",
    "GetDocument",
    "GetDocuments",
    "GetDocumentsCategories",
    "GetDocumentsList",
    "GetFeedbacksList",
    "GetFileFromTheMessage",
    "GetGender",
    "GetGenerateTheReport",
    "GetGettingSellerPortalNews",
    "GetHiddenFromTheCatalog",
    "GetHscodes",
    "GetInformationAboutMediaCampaign",
    "GetInformationOnCompletedOrders",
    "GetInformationOnPaidDelivery",
    "GetInventory",
    "GetLaunchCampaign",
    "GetLimitsForTheProductCards",
    "GetListOfArchivedFeedbacks",
    "GetListOfMediaCampaigns",
    "GetListOfPinnedAndUnpinnedFeedback",
    "GetListOfProductsForParticipatingInThePromotion",
    "GetLogisticsAndStorageCostsMultiplier",
    "GetMediaCampaignsNumber",
    "GetNewAssemblyOrders",
    "GetNewAssemblyOrdersList",
    "GetNewOrders",
    "GetNewOrdersList",
    "GetNumberOfFeedbacks",
    "GetNumberOfQuestions",
    "GetOffices",
    "GetOfficesForPass",
    "GetOrderMetadata",
    "GetOrders",
    "GetOrdersStatuses",
    "GetOrdersStickers",
    "GetPalletTariffs",
    "GetParentCategoriesOfTheBrand",
    "GetPasses",
    "GetPauseCampaign",
    "GetPinnedAndUnpinnedFeedbackNumber",
    "GetPinnedFeedbackLimits",
    "GetProcessedUploadDetails",
    "GetProcessedUploadState",
    "GetProductCategoryCommission",
    "GetProductDetail",
    "GetProductLabeling",
    "GetProductSizesWithPrices",
    "GetProductsInQuarantine",
    "GetProductsParentCategories",
    "GetProductsWithPrices",
    "GetProductsWithPricesByArticles",
    "GetPromotionsDetails",
    "GetPromotionsList",
    "GetQuestionList",
    "GetRealizationSalesReport",
    "GetReceivingCostsHistory",
    "GetReceivingTheHistoryOfAccountTopups",
    "GetRecommendedBidsForItemsAndSearchClusters",
    "GetReport",
    "GetRetrieveInformationOnCompletedAssemblyOrders",
    "GetReturnTariffs",
    "GetSales",
    "GetSeason",
    "GetSelfpurchases",
    "GetSellerBrands",
    "GetSellerInformation",
    "GetSellersBalance",
    "GetStickersForAssemblyOrdersWithDeliveryToPickupPoint",
    "GetStickersForCrossborderAssemblyOrders",
    "GetStopCampaign",
    "GetSubjectCharacteristics",
    "GetSubjectsForCampaigns",
    "GetSubjectsList",
    "GetSubstitutionsAndIncorrectAttachments",
    "GetSupplyAssemblyOrderIds",
    "GetSupplyBoxesList",
    "GetSupplyDetails",
    "GetSupplyPackage",
    "GetSupplyProducts",
    "GetSupplyTariffs",
    "GetTagsList",
    "GetTheFeedbackById",
    "GetTheQuestionById",
    "GetTheReport",
    "GetTheReportsList",
    "GetTheSupplyBoxQrCodeStickers",
    "GetTheSupplyQrCode",
    "GetTransitDirections",
    "GetUnansweredFeedbacks",
    "GetUnansweredQuestions",
    "GetUnprocessedUploadDetails",
    "GetUnprocessedUploadState",
    "GetUnseenFeedbacksAndQuestions",
    "GetVatRate",
    "GetWarehouse",
    "GetWarehouseMeasurements",
    "GetWarehouses",
    "GetWarehousesList",
    "GroupData",
    "GroupedProductCardsStatisticsPerDays",
    "ListOfCampaignMinusPhrases",
    "ListOfFailedProductCardsWithErrors",
    "ListOfSearchClustersBids",
    "MainPage",
    "MediaCampaignStatistics",
    "MergingOrSeparatingOfProductCards",
    "MinimumBidsForProductCards",
    "MoveTheSupplyToTheDelivery",
    "NotifyThatTheAssemblyOrderIsReadyForPickup",
    "NotifyThatTheAssemblyOrdersAreReadyForPickup",
    "NotifyThatTheBuyerHasDeclinedTheOrder",
    "NotifyThatTheBuyerRefusedTheOrder",
    "NotifyThatTheOrderHasBeenAcceptedByTheBuyer",
    "NotifyThatTheOrdersAreDeclined",
    "NotifyThatTheOrdersAreReceived",
    "NotifyThatTheOrdersWereReceivedByTheBuyers",
    "OrdersAndPositionsByProductSearchTexts",
    "OrdersWithClientInformation",
    "PaginationByGroups",
    "PaginationByProductsWithinAGroup",
    "PinFeedback",
    "ProductCardsForCampaigns",
    "ProductCardsInTrashList",
    "ProductCardsList",
    "ProductCardsStatisticsPerDays",
    "ProductCardsStatisticsPerPeriod",
    "ProductData",
    "RecoverProductCardFromTrash",
    "RegenerateTheReport",
    "RenameCampaign",
    "ReplyToFeedback",
    "ReportOnProductsWithMandatoryLabeling",
    "ReturnProductByFeedbackId",
    "SearchClustersStatistics",
    "SearchTextsByProduct",
    "SendMessage",
    "SetBidsForSearchClusters",
    "SetPricesAndDiscounts",
    "SetSizePrices",
    "SetWbClubDiscounts",
    "SettingAndDeletingMinusPhrases",
    "SizeData",
    "StatusHistoryForCrossborderOrders",
    "SuppliesList",
    "TagManagementInTheProductCard",
    "TopupOfTheCampaignBudget",
    "TransferProductCardToTrash",
    "TransferToAssembly",
    "TransferToDelivery",
    "UnpinFeedback",
    "UpdateContactsList",
    "UpdateInventory",
    "UpdatePass",
    "UpdateProductCards",
    "UpdateTheTag",
    "UpdateUsersAccessPermissions",
    "UpdateWarehouse",
    "UploadMediaFile",
    "UploadMediaFilesViaLinks",
    "WarehouseData",
    "WbMethod",
    "WorkingWithQuestions",
)
