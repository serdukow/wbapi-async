from ..analytics.methods.create_the_report import CreateTheReport
from ..analytics.methods.get_the_report import GetTheReport
from ..analytics.methods.get_the_reports_list import GetTheReportsList
from ..analytics.methods.group_data import GroupData
from ..analytics.methods.grouped_product_cards_statistics_per_days import GroupedProductCardsStatisticsPerDays
from ..analytics.methods.main_page import MainPage
from ..analytics.methods.orders_and_positions_by_product_search_texts import (
    OrdersAndPositionsByProductSearchTexts,
)
from ..analytics.methods.pagination_by_groups import PaginationByGroups
from ..analytics.methods.pagination_by_products_within_a_group import PaginationByProductsWithinAGroup
from ..analytics.methods.product_cards_statistics_per_days import ProductCardsStatisticsPerDays
from ..analytics.methods.product_cards_statistics_per_period import ProductCardsStatisticsPerPeriod
from ..analytics.methods.product_data import ProductData
from ..analytics.methods.regenerate_the_report import RegenerateTheReport
from ..analytics.methods.search_texts_by_product import SearchTextsByProduct
from ..analytics.methods.size_data import SizeData
from ..analytics.methods.warehouse_data import WarehouseData
from ..communications.methods.answer_buyers_application import AnswerBuyersApplication
from ..communications.methods.edit_response_to_feedback import EditResponseToFeedback
from ..communications.methods.get_buyers_return_applications import GetBuyersReturnApplications
from ..communications.methods.get_chat_events import GetChatEvents
from ..communications.methods.get_chat_list import GetChatList
from ..communications.methods.get_feedbacks_list import GetFeedbacksList
from ..communications.methods.get_file_from_the_message import GetFileFromTheMessage
from ..communications.methods.get_list_of_archived_feedbacks import GetListOfArchivedFeedbacks
from ..communications.methods.get_list_of_pinned_and_unpinned_feedback import (
    GetListOfPinnedAndUnpinnedFeedback,
)
from ..communications.methods.get_number_of_feedbacks import GetNumberOfFeedbacks
from ..communications.methods.get_number_of_questions import GetNumberOfQuestions
from ..communications.methods.get_pinned_and_unpinned_feedback_number import (
    GetPinnedAndUnpinnedFeedbackNumber,
)
from ..communications.methods.get_pinned_feedback_limits import GetPinnedFeedbackLimits
from ..communications.methods.get_question_list import GetQuestionList
from ..communications.methods.get_the_feedback_by_id import GetTheFeedbackById
from ..communications.methods.get_the_question_by_id import GetTheQuestionById
from ..communications.methods.get_unanswered_feedbacks import GetUnansweredFeedbacks
from ..communications.methods.get_unanswered_questions import GetUnansweredQuestions
from ..communications.methods.get_unseen_feedbacks_and_questions import GetUnseenFeedbacksAndQuestions
from ..communications.methods.pin_feedback import PinFeedback
from ..communications.methods.reply_to_feedback import ReplyToFeedback
from ..communications.methods.return_product_by_feedback_id import ReturnProductByFeedbackId
from ..communications.methods.send_message import SendMessage
from ..communications.methods.unpin_feedback import UnpinFeedback
from ..communications.methods.working_with_questions import WorkingWithQuestions
from ..finances.methods.get_document import GetDocument
from ..finances.methods.get_documents import GetDocuments
from ..finances.methods.get_documents_categories import GetDocumentsCategories
from ..finances.methods.get_documents_list import GetDocumentsList
from ..finances.methods.get_realization_sales_report import GetRealizationSalesReport
from ..finances.methods.get_sellers_balance import GetSellersBalance
from ..general.methods.create_an_invitation_for_a_new_user import CreateAnInvitationForANewUser
from ..general.methods.delete_user import DeleteUser
from ..general.methods.get_a_list_of_seller_active_or_invited_users import (
    GetAListOfSellerActiveOrInvitedUsers,
)
from ..general.methods.get_connection_check import GetConnectionCheck
from ..general.methods.get_getting_seller_portal_news import GetGettingSellerPortalNews
from ..general.methods.get_seller_information import GetSellerInformation
from ..general.methods.update_users_access_permissions import UpdateUsersAccessPermissions
from ..in_store_pickup.methods.add_data_matrix_codes_to_the_assembly_orders_chestny_znak import (
    AddDataMatrixCodesToTheAssemblyOrdersChestnyZnak,
)
from ..in_store_pickup.methods.add_gtin_to_the_assembly_orders import AddGtinToTheAssemblyOrders
from ..in_store_pickup.methods.add_imei_to_the_assembly_orders import AddImeiToTheAssemblyOrders
from ..in_store_pickup.methods.add_uin_unique_identification_numbers_to_the_assembly_orders import (
    AddUinUniqueIdentificationNumbersToTheAssemblyOrders,
)
from ..in_store_pickup.methods.assign_a_data_matrix_code_to_the_assembly_order import (
    AssignADataMatrixCodeToTheAssemblyOrder,
)
from ..in_store_pickup.methods.cancel_the_assembly_orders import CancelTheAssemblyOrders
from ..in_store_pickup.methods.check_if_the_order_belongs_to_the_buyer import CheckIfTheOrderBelongsToTheBuyer
from ..in_store_pickup.methods.get_assembly_order_metadata import GetAssemblyOrderMetadata
from ..in_store_pickup.methods.get_new_assembly_orders_list import GetNewAssemblyOrdersList
from ..in_store_pickup.methods.get_retrieve_information_on_completed_assembly_orders import (
    GetRetrieveInformationOnCompletedAssemblyOrders,
)
from ..in_store_pickup.methods.notify_that_the_assembly_order_is_ready_for_pickup import (
    NotifyThatTheAssemblyOrderIsReadyForPickup,
)
from ..in_store_pickup.methods.notify_that_the_assembly_orders_are_ready_for_pickup import (
    NotifyThatTheAssemblyOrdersAreReadyForPickup,
)
from ..in_store_pickup.methods.notify_that_the_buyer_refused_the_order import (
    NotifyThatTheBuyerRefusedTheOrder,
)
from ..in_store_pickup.methods.notify_that_the_orders_were_received_by_the_buyers import (
    NotifyThatTheOrdersWereReceivedByTheBuyers,
)
from ..orders_dbs.methods.add_custom_declaration_to_the_orders import AddCustomDeclarationToTheOrders
from ..orders_dbs.methods.add_data_matrix_codes_to_assembly_orders_chestny_znak import (
    AddDataMatrixCodesToAssemblyOrdersChestnyZnak,
)
from ..orders_dbs.methods.add_gtin_to_assembly_orders import AddGtinToAssemblyOrders
from ..orders_dbs.methods.add_imei_to_assembly_orders import AddImeiToAssemblyOrders
from ..orders_dbs.methods.add_uin_unique_identification_number_to_assembly_orders import (
    AddUinUniqueIdentificationNumberToAssemblyOrders,
)
from ..orders_dbs.methods.b2_b_buyer_information import B2BBuyerInformation
from ..orders_dbs.methods.cancel_assembly_orders import CancelAssemblyOrders
from ..orders_dbs.methods.delete_assembly_orders_metadata import DeleteAssemblyOrdersMetadata
from ..orders_dbs.methods.get_assembly_order_statuses import GetAssemblyOrderStatuses
from ..orders_dbs.methods.get_information_on_paid_delivery import GetInformationOnPaidDelivery
from ..orders_dbs.methods.get_new_orders_list import GetNewOrdersList
from ..orders_dbs.methods.get_stickers_for_assembly_orders_with_delivery_to_pickup_point import (
    GetStickersForAssemblyOrdersWithDeliveryToPickupPoint,
)
from ..orders_dbs.methods.notify_that_the_buyer_has_declined_the_order import (
    NotifyThatTheBuyerHasDeclinedTheOrder,
)
from ..orders_dbs.methods.notify_that_the_order_has_been_accepted_by_the_buyer import (
    NotifyThatTheOrderHasBeenAcceptedByTheBuyer,
)
from ..orders_dbs.methods.notify_that_the_orders_are_declined import NotifyThatTheOrdersAreDeclined
from ..orders_dbs.methods.notify_that_the_orders_are_received import NotifyThatTheOrdersAreReceived
from ..orders_dbw.methods.add_data_matrix_code_to_the_order import AddDataMatrixCodeToTheOrder
from ..orders_dbw.methods.add_gtin_to_the_order import AddGtinToTheOrder
from ..orders_dbw.methods.add_imei_to_the_order import AddImeiToTheOrder
from ..orders_dbw.methods.add_uin_unique_identification_number_to_the_order import (
    AddUinUniqueIdentificationNumberToTheOrder,
)
from ..orders_dbw.methods.buyer_information import BuyerInformation
from ..orders_dbw.methods.cancel_the_order import CancelTheOrder
from ..orders_dbw.methods.courier_info import CourierInfo
from ..orders_dbw.methods.delete_order_metadata import DeleteOrderMetadata
from ..orders_dbw.methods.delivery_date_and_time import DeliveryDateAndTime
from ..orders_dbw.methods.get_information_on_completed_orders import GetInformationOnCompletedOrders
from ..orders_dbw.methods.get_new_orders import GetNewOrders
from ..orders_dbw.methods.get_order_metadata import GetOrderMetadata
from ..orders_dbw.methods.get_orders_statuses import GetOrdersStatuses
from ..orders_dbw.methods.get_orders_stickers import GetOrdersStickers
from ..orders_dbw.methods.transfer_to_assembly import TransferToAssembly
from ..orders_dbw.methods.transfer_to_delivery import TransferToDelivery
from ..orders_fbs.methods.add_assembly_orders_to_the_supply import AddAssemblyOrdersToTheSupply
from ..orders_fbs.methods.add_boxes_to_the_supply import AddBoxesToTheSupply
from ..orders_fbs.methods.add_custom_declaration_number_to_the_order import (
    AddCustomDeclarationNumberToTheOrder,
)
from ..orders_fbs.methods.add_data_matrix_code_to_the_assembly_order import (
    AddDataMatrixCodeToTheAssemblyOrder,
)
from ..orders_fbs.methods.add_expiration_date_to_the_assembly_order import AddExpirationDateToTheAssemblyOrder
from ..orders_fbs.methods.add_gtin_to_the_assembly_order import AddGtinToTheAssemblyOrder
from ..orders_fbs.methods.add_imei_to_the_assembly_order import AddImeiToTheAssemblyOrder
from ..orders_fbs.methods.add_uin_unique_identification_number_to_the_assembly_order import (
    AddUinUniqueIdentificationNumberToTheAssemblyOrder,
)
from ..orders_fbs.methods.cancel_the_assembly_order import CancelTheAssemblyOrder
from ..orders_fbs.methods.create_a_new_supply import CreateANewSupply
from ..orders_fbs.methods.create_pass import CreatePass
from ..orders_fbs.methods.delete_assembly_order_metadata import DeleteAssemblyOrderMetadata
from ..orders_fbs.methods.delete_boxes_from_the_supply import DeleteBoxesFromTheSupply
from ..orders_fbs.methods.delete_the_pass import DeleteThePass
from ..orders_fbs.methods.delete_the_supply import DeleteTheSupply
from ..orders_fbs.methods.get_a_supplies_list import GetASuppliesList
from ..orders_fbs.methods.get_all_assembly_orders_for_reshipment import GetAllAssemblyOrdersForReshipment
from ..orders_fbs.methods.get_assembly_orders import GetAssemblyOrders
from ..orders_fbs.methods.get_assembly_orders_metadata import GetAssemblyOrdersMetadata
from ..orders_fbs.methods.get_assembly_orders_statuses import GetAssemblyOrdersStatuses
from ..orders_fbs.methods.get_assembly_orders_stickers import GetAssemblyOrdersStickers
from ..orders_fbs.methods.get_new_assembly_orders import GetNewAssemblyOrders
from ..orders_fbs.methods.get_offices_for_pass import GetOfficesForPass
from ..orders_fbs.methods.get_passes import GetPasses
from ..orders_fbs.methods.get_stickers_for_crossborder_assembly_orders import (
    GetStickersForCrossborderAssemblyOrders,
)
from ..orders_fbs.methods.get_supply_assembly_order_ids import GetSupplyAssemblyOrderIds
from ..orders_fbs.methods.get_supply_boxes_list import GetSupplyBoxesList
from ..orders_fbs.methods.get_supply_details import GetSupplyDetails
from ..orders_fbs.methods.get_the_supply_box_qr_code_stickers import GetTheSupplyBoxQrCodeStickers
from ..orders_fbs.methods.get_the_supply_qr_code import GetTheSupplyQrCode
from ..orders_fbs.methods.move_the_supply_to_the_delivery import MoveTheSupplyToTheDelivery
from ..orders_fbs.methods.orders_with_client_information import OrdersWithClientInformation
from ..orders_fbs.methods.status_history_for_crossborder_orders import StatusHistoryForCrossborderOrders
from ..orders_fbs.methods.update_pass import UpdatePass
from ..orders_fbw.methods.acceptance_options import AcceptanceOptions
from ..orders_fbw.methods.get_supply_package import GetSupplyPackage
from ..orders_fbw.methods.get_supply_products import GetSupplyProducts
from ..orders_fbw.methods.get_transit_directions import GetTransitDirections
from ..orders_fbw.methods.get_warehouses_list import GetWarehousesList
from ..orders_fbw.methods.supplies_list import SuppliesList
from ..products.methods.create_a_tag import CreateATag
from ..products.methods.create_product_cards import CreateProductCards
from ..products.methods.create_product_cards_with_merge import CreateProductCardsWithMerge
from ..products.methods.create_warehouse import CreateWarehouse
from ..products.methods.delete_inventory import DeleteInventory
from ..products.methods.delete_the_tag import DeleteTheTag
from ..products.methods.delete_warehouse import DeleteWarehouse
from ..products.methods.generation_of_skus import GenerationOfSkus
from ..products.methods.get_brands import GetBrands
from ..products.methods.get_color import GetColor
from ..products.methods.get_contacts_list import GetContactsList
from ..products.methods.get_country_of_origin import GetCountryOfOrigin
from ..products.methods.get_gender import GetGender
from ..products.methods.get_hscodes import GetHscodes
from ..products.methods.get_inventory import GetInventory
from ..products.methods.get_limits_for_the_product_cards import GetLimitsForTheProductCards
from ..products.methods.get_offices import GetOffices
from ..products.methods.get_processed_upload_details import GetProcessedUploadDetails
from ..products.methods.get_processed_upload_state import GetProcessedUploadState
from ..products.methods.get_product_sizes_with_prices import GetProductSizesWithPrices
from ..products.methods.get_products_in_quarantine import GetProductsInQuarantine
from ..products.methods.get_products_parent_categories import GetProductsParentCategories
from ..products.methods.get_products_with_prices import GetProductsWithPrices
from ..products.methods.get_products_with_prices_by_articles import GetProductsWithPricesByArticles
from ..products.methods.get_season import GetSeason
from ..products.methods.get_subject_characteristics import GetSubjectCharacteristics
from ..products.methods.get_subjects_list import GetSubjectsList
from ..products.methods.get_tags_list import GetTagsList
from ..products.methods.get_unprocessed_upload_details import GetUnprocessedUploadDetails
from ..products.methods.get_unprocessed_upload_state import GetUnprocessedUploadState
from ..products.methods.get_vat_rate import GetVatRate
from ..products.methods.get_warehouses import GetWarehouses
from ..products.methods.list_of_failed_product_cards_with_errors import ListOfFailedProductCardsWithErrors
from ..products.methods.merging_or_separating_of_product_cards import MergingOrSeparatingOfProductCards
from ..products.methods.product_cards_in_trash_list import ProductCardsInTrashList
from ..products.methods.product_cards_list import ProductCardsList
from ..products.methods.recover_product_card_from_trash import RecoverProductCardFromTrash
from ..products.methods.set_prices_and_discounts import SetPricesAndDiscounts
from ..products.methods.set_size_prices import SetSizePrices
from ..products.methods.set_wb_club_discounts import SetWbClubDiscounts
from ..products.methods.tag_management_in_the_product_card import TagManagementInTheProductCard
from ..products.methods.transfer_product_card_to_trash import TransferProductCardToTrash
from ..products.methods.update_contacts_list import UpdateContactsList
from ..products.methods.update_inventory import UpdateInventory
from ..products.methods.update_product_cards import UpdateProductCards
from ..products.methods.update_the_tag import UpdateTheTag
from ..products.methods.update_warehouse import UpdateWarehouse
from ..products.methods.upload_media_file import UploadMediaFile
from ..products.methods.upload_media_files_via_links import UploadMediaFilesViaLinks
from ..promotion.methods.active_and_inactive_search_cluster_lists import ActiveAndInactiveSearchClusterLists
from ..promotion.methods.add_product_to_the_promotion import AddProductToThePromotion
from ..promotion.methods.changing_campaigns_bids import ChangingCampaignsBids
from ..promotion.methods.changing_placements_in_campaigns_with_custom_bid import (
    ChangingPlacementsInCampaignsWithCustomBid,
)
from ..promotion.methods.changing_the_list_of_product_cards_in_campaigns import (
    ChangingTheListOfProductCardsInCampaigns,
)
from ..promotion.methods.create_campaign import CreateCampaign
from ..promotion.methods.daily_search_clusters_statistics import DailySearchClustersStatistics
from ..promotion.methods.delete_bids_from_search_clusters import DeleteBidsFromSearchClusters
from ..promotion.methods.get_balance import GetBalance
from ..promotion.methods.get_campaign_budget import GetCampaignBudget
from ..promotion.methods.get_campaigns_information import GetCampaignsInformation
from ..promotion.methods.get_campaigns_lists import GetCampaignsLists
from ..promotion.methods.get_campaigns_statistics import GetCampaignsStatistics
from ..promotion.methods.get_delete_campaign import GetDeleteCampaign
from ..promotion.methods.get_information_about_media_campaign import GetInformationAboutMediaCampaign
from ..promotion.methods.get_launch_campaign import GetLaunchCampaign
from ..promotion.methods.get_list_of_media_campaigns import GetListOfMediaCampaigns
from ..promotion.methods.get_list_of_products_for_participating_in_the_promotion import (
    GetListOfProductsForParticipatingInThePromotion,
)
from ..promotion.methods.get_media_campaigns_number import GetMediaCampaignsNumber
from ..promotion.methods.get_pause_campaign import GetPauseCampaign
from ..promotion.methods.get_promotions_details import GetPromotionsDetails
from ..promotion.methods.get_promotions_list import GetPromotionsList
from ..promotion.methods.get_receiving_costs_history import GetReceivingCostsHistory
from ..promotion.methods.get_receiving_the_history_of_account_topups import (
    GetReceivingTheHistoryOfAccountTopups,
)
from ..promotion.methods.get_recommended_bids_for_items_and_search_clusters import (
    GetRecommendedBidsForItemsAndSearchClusters,
)
from ..promotion.methods.get_stop_campaign import GetStopCampaign
from ..promotion.methods.get_subjects_for_campaigns import GetSubjectsForCampaigns
from ..promotion.methods.list_of_campaign_minus_phrases import ListOfCampaignMinusPhrases
from ..promotion.methods.list_of_search_clusters_bids import ListOfSearchClustersBids
from ..promotion.methods.media_campaign_statistics import MediaCampaignStatistics
from ..promotion.methods.minimum_bids_for_product_cards import MinimumBidsForProductCards
from ..promotion.methods.product_cards_for_campaigns import ProductCardsForCampaigns
from ..promotion.methods.rename_campaign import RenameCampaign
from ..promotion.methods.search_clusters_statistics import SearchClustersStatistics
from ..promotion.methods.set_bids_for_search_clusters import SetBidsForSearchClusters
from ..promotion.methods.setting_and_deleting_minus_phrases import SettingAndDeletingMinusPhrases
from ..promotion.methods.topup_of_the_campaign_budget import TopupOfTheCampaignBudget
from ..reports.methods.get_blocked_product_cards import GetBlockedProductCards
from ..reports.methods.get_check_the_status import GetCheckTheStatus
from ..reports.methods.get_create_the_report import GetCreateTheReport
from ..reports.methods.get_generate_the_report import GetGenerateTheReport
from ..reports.methods.get_goods_return import GetGoodsReturn
from ..reports.methods.get_hidden_from_the_catalog import GetHiddenFromTheCatalog
from ..reports.methods.get_logistics_and_storage_costs_multiplier import GetLogisticsAndStorageCostsMultiplier
from ..reports.methods.get_orders import GetOrders
from ..reports.methods.get_parent_categories_of_the_brand import GetParentCategoriesOfTheBrand
from ..reports.methods.get_product_labeling import GetProductLabeling
from ..reports.methods.get_report import GetReport
from ..reports.methods.get_sales import GetSales
from ..reports.methods.get_selfpurchases import GetSelfpurchases
from ..reports.methods.get_seller_brands import GetSellerBrands
from ..reports.methods.get_substitutions_and_incorrect_attachments import (
    GetSubstitutionsAndIncorrectAttachments,
)
from ..reports.methods.get_warehouse import GetWarehouse
from ..reports.methods.get_warehouse_measurements import GetWarehouseMeasurements
from ..reports.methods.report_on_products_with_mandatory_labeling import ReportOnProductsWithMandatoryLabeling
from ..tariffs.methods.get_box_tariffs import GetBoxTariffs
from ..tariffs.methods.get_pallet_tariffs import GetPalletTariffs
from ..tariffs.methods.get_product_category_commission import GetProductCategoryCommission
from ..tariffs.methods.get_return_tariffs import GetReturnTariffs
from ..tariffs.methods.get_supply_tariffs import GetSupplyTariffs
from .base import WbMethod
from .get_product_detail import GetProductDetail


__all__ = (
    "AcceptanceOptions",
    "ActiveAndInactiveSearchClusterLists",
    "AddAssemblyOrdersToTheSupply",
    "AddBoxesToTheSupply",
    "AddCustomDeclarationNumberToTheOrder",
    "AddCustomDeclarationToTheOrders",
    "AddDataMatrixCodesToAssemblyOrdersChestnyZnak",
    "AddDataMatrixCodesToTheAssemblyOrdersChestnyZnak",
    "AddDataMatrixCodeToTheAssemblyOrder",
    "AddDataMatrixCodeToTheOrder",
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
    "AddUinUniqueIdentificationNumbersToTheAssemblyOrders",
    "AddUinUniqueIdentificationNumberToAssemblyOrders",
    "AddUinUniqueIdentificationNumberToTheAssemblyOrder",
    "AddUinUniqueIdentificationNumberToTheOrder",
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
    "CreateAnInvitationForANewUser",
    "CreateATag",
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
    "GetAllAssemblyOrdersForReshipment",
    "GetAssemblyOrderMetadata",
    "GetAssemblyOrders",
    "GetAssemblyOrdersMetadata",
    "GetAssemblyOrdersStatuses",
    "GetAssemblyOrdersStickers",
    "GetAssemblyOrderStatuses",
    "GetASuppliesList",
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
    "GetGoodsReturn",
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
    "GetProductsInQuarantine",
    "GetProductSizesWithPrices",
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
    "SettingAndDeletingMinusPhrases",
    "SetWbClubDiscounts",
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
