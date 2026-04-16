from ..analytics.types.avg_stock_turnover import AvgStockTurnover
from ..analytics.types.comparison import Comparison
from ..analytics.types.conversions import Conversions
from ..analytics.types.create_the_report_response import CreateTheReportResponse
from ..analytics.types.current_period import CurrentPeriod
from ..analytics.types.float_graph_by_period_item import FloatGraphByPeriodItem
from ..analytics.types.group_data_item import GroupDataItem
from ..analytics.types.grouped_product_cards_statistics_per_days_item import (
    GroupedProductCardsStatisticsPerDaysItem,
)
from ..analytics.types.history import History
from ..analytics.types.main_page_response import MainPageResponse
from ..analytics.types.metrics import Metrics
from ..analytics.types.office_missing_time import OfficeMissingTime
from ..analytics.types.offices_item import OfficesItem
from ..analytics.types.order_by import OrderBy
from ..analytics.types.orders_and_positions_by_product_search_texts_response import (
    OrdersAndPositionsByProductSearchTextsResponse,
)
from ..analytics.types.pagination_by_groups_response import PaginationByGroupsResponse
from ..analytics.types.pagination_by_products_within_a_group_response import (
    PaginationByProductsWithinAGroupResponse,
)
from ..analytics.types.past import Past
from ..analytics.types.past_period import PastPeriod
from ..analytics.types.period import Period
from ..analytics.types.product import Product
from ..analytics.types.product_cards_statistics_per_days_response import ProductCardsStatisticsPerDaysResponse
from ..analytics.types.product_cards_statistics_per_period_item import ProductCardsStatisticsPerPeriodItem
from ..analytics.types.product_data_item import ProductDataItem
from ..analytics.types.regenerate_the_report_response import RegenerateTheReportResponse
from ..analytics.types.sale_rate import SaleRate
from ..analytics.types.search_texts_by_product_response import SearchTextsByProductResponse
from ..analytics.types.selected import Selected
from ..analytics.types.selected_period import SelectedPeriod
from ..analytics.types.size_data_item import SizeDataItem
from ..analytics.types.statistic import Statistic
from ..analytics.types.stocks import Stocks
from ..analytics.types.table_product_item_st import TableProductItemSt
from ..analytics.types.tag import Tag
from ..analytics.types.the_report_response import TheReportResponse
from ..analytics.types.the_reports_list_item import TheReportsListItem
from ..analytics.types.time_to_ready import TimeToReady
from ..analytics.types.time_to_ready_dynamic import TimeToReadyDynamic
from ..analytics.types.warehouse_data_item import WarehouseDataItem
from ..analytics.types.wb_club import WbClub
from ..analytics.types.wb_club_dynamic import WbClubDynamic
from ..communications.types.answer import Answer
from ..communications.types.answer_buyers_application_response import AnswerBuyersApplicationResponse
from ..communications.types.buyers_return_applications_item import BuyersReturnApplicationsItem
from ..communications.types.chat_events_item import ChatEventsItem
from ..communications.types.chat_list_item import ChatListItem
from ..communications.types.edit_response_to_feedback_response import EditResponseToFeedbackResponse
from ..communications.types.event_attachments import EventAttachments
from ..communications.types.feedbacks_list_item import FeedbacksListItem
from ..communications.types.file import File
from ..communications.types.file_from_the_message_response import FileFromTheMessageResponse
from ..communications.types.good_card import GoodCard
from ..communications.types.image import Image
from ..communications.types.last_message import LastMessage
from ..communications.types.list_of_archived_feedbacks_item import ListOfArchivedFeedbacksItem
from ..communications.types.list_of_pinned_and_unpinned_feedback_response import (
    ListOfPinnedAndUnpinnedFeedbackResponse,
)
from ..communications.types.message import Message
from ..communications.types.number_of_feedbacks_item import NumberOfFeedbacksItem
from ..communications.types.number_of_questions_item import NumberOfQuestionsItem
from ..communications.types.photo_links_item import PhotoLinksItem
from ..communications.types.pin_feedback_response import PinFeedbackResponse
from ..communications.types.pinned_and_unpinned_feedback_number_response import (
    PinnedAndUnpinnedFeedbackNumberResponse,
)
from ..communications.types.pinned_feedback_limits_response import PinnedFeedbackLimitsResponse
from ..communications.types.product_details import ProductDetails
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
from ..communications.types.video import Video
from ..communications.types.working_with_questions_item import WorkingWithQuestionsItem
from ..finances.types.document_response import DocumentResponse
from ..finances.types.documents_categories_item import DocumentsCategoriesItem
from ..finances.types.documents_list_item import DocumentsListItem
from ..finances.types.documents_response import DocumentsResponse
from ..finances.types.params_item import ParamsItem
from ..finances.types.realization_sales_report_response import RealizationSalesReportResponse
from ..finances.types.sellers_balance_response import SellersBalanceResponse
from ..general.types.a_list_of_seller_active_or_invited_users_item import (
    AListOfSellerActiveOrInvitedUsersItem,
)
from ..general.types.access_item import AccessItem
from ..general.types.connection_check_response import ConnectionCheckResponse
from ..general.types.create_an_invitation_for_a_new_user_response import CreateAnInvitationForANewUserResponse
from ..general.types.delete_user_response import DeleteUserResponse
from ..general.types.getting_seller_portal_news_item import GettingSellerPortalNewsItem
from ..general.types.invite import Invite
from ..general.types.invitee_info import InviteeInfo
from ..general.types.seller_information_response import SellerInformationResponse
from ..general.types.types_item import TypesItem
from ..general.types.update_users_access_permissions_response import UpdateUsersAccessPermissionsResponse
from ..general.types.user_access import UserAccess
from ..in_store_pickup.types.add_data_matrix_codes_to_the_assembly_orders_chestny_znak_item import (
    AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem,
)
from ..in_store_pickup.types.add_gtin_to_the_assembly_orders_item import AddGtinToTheAssemblyOrdersItem
from ..in_store_pickup.types.add_imei_to_the_assembly_orders_item import AddImeiToTheAssemblyOrdersItem
from ..in_store_pickup.types.add_uin_unique_identification_numbers_to_the_assembly_orders_item import (
    AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem,
)
from ..in_store_pickup.types.api_meta_error_response import ApiMetaErrorResponse
from ..in_store_pickup.types.api_orders_error_response import ApiOrdersErrorResponse
from ..in_store_pickup.types.assembly_order_metadata_item import AssemblyOrderMetadataItem
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
from ..orders_dbs.types.api_b2b_client_info import ApiB2BClientInfo
from ..orders_dbs.types.api_batch_error_response import ApiBatchErrorResponse
from ..orders_dbs.types.api_gtin import ApiGtin
from ..orders_dbs.types.api_imei import ApiImei
from ..orders_dbs.types.api_order_code_request import ApiOrderCodeRequest
from ..orders_dbs.types.api_sgti_ns import ApiSgtiNs
from ..orders_dbs.types.api_uin import ApiUin
from ..orders_dbs.types.assembly_order_statuses_item import AssemblyOrderStatusesItem
from ..orders_dbs.types.b2_b_buyer_information_item import B2BBuyerInformationItem
from ..orders_dbs.types.cancel_assembly_orders_item import CancelAssemblyOrdersItem
from ..orders_dbs.types.delete_assembly_orders_metadata_item import DeleteAssemblyOrdersMetadataItem
from ..orders_dbs.types.errors_item import ErrorsItem
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
from ..orders_dbs.types.orders_item import OrdersItem
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
from ..orders_dbw.types.contacts import Contacts
from ..orders_dbw.types.courier_info import CourierInfo
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
from ..orders_fbs.types.address import Address
from ..orders_fbs.types.all_assembly_orders_for_reshipment_item import AllAssemblyOrdersForReshipmentItem
from ..orders_fbs.types.assembly_orders_item import AssemblyOrdersItem
from ..orders_fbs.types.assembly_orders_metadata_item import AssemblyOrdersMetadataItem
from ..orders_fbs.types.assembly_orders_statuses_item import AssemblyOrdersStatusesItem
from ..orders_fbs.types.assembly_orders_stickers_item import AssemblyOrdersStickersItem
from ..orders_fbs.types.cancel_the_assembly_order_response import CancelTheAssemblyOrderResponse
from ..orders_fbs.types.create_a_new_supply_response import CreateANewSupplyResponse
from ..orders_fbs.types.create_pass_response import CreatePassResponse
from ..orders_fbs.types.customs_declaration import CustomsDeclaration
from ..orders_fbs.types.delete_assembly_order_metadata_response import DeleteAssemblyOrderMetadataResponse
from ..orders_fbs.types.delete_boxes_from_the_supply_response import DeleteBoxesFromTheSupplyResponse
from ..orders_fbs.types.delete_the_pass_response import DeleteThePassResponse
from ..orders_fbs.types.delete_the_supply_response import DeleteTheSupplyResponse
from ..orders_fbs.types.expiration import Expiration
from ..orders_fbs.types.gtin import Gtin
from ..orders_fbs.types.imei import Imei
from ..orders_fbs.types.meta import Meta
from ..orders_fbs.types.move_the_supply_to_the_delivery_response import MoveTheSupplyToTheDeliveryResponse
from ..orders_fbs.types.new_assembly_orders_item import NewAssemblyOrdersItem
from ..orders_fbs.types.offices_for_pass_response import OfficesForPassResponse
from ..orders_fbs.types.options import Options
from ..orders_fbs.types.orders_with_client_information_item import OrdersWithClientInformationItem
from ..orders_fbs.types.passes_response import PassesResponse
from ..orders_fbs.types.sgtin import Sgtin
from ..orders_fbs.types.status_history_for_crossborder_orders_item import (
    StatusHistoryForCrossborderOrdersItem,
)
from ..orders_fbs.types.statuses_item import StatusesItem
from ..orders_fbs.types.stickers_for_crossborder_assembly_orders_item import (
    StickersForCrossborderAssemblyOrdersItem,
)
from ..orders_fbs.types.supply_assembly_order_ids_item import SupplyAssemblyOrderIdsItem
from ..orders_fbs.types.supply_boxes_list_item import SupplyBoxesListItem
from ..orders_fbs.types.supply_details_response import SupplyDetailsResponse
from ..orders_fbs.types.the_supply_box_qr_code_stickers_item import TheSupplyBoxQrCodeStickersItem
from ..orders_fbs.types.the_supply_qr_code_response import TheSupplyQrCodeResponse
from ..orders_fbs.types.uin import Uin
from ..orders_fbs.types.update_pass_response import UpdatePassResponse
from ..orders_fbw.types.acceptance_options_item import AcceptanceOptionsItem
from ..orders_fbw.types.models_date_filter_request import ModelsDateFilterRequest
from ..orders_fbw.types.models_good_in_box import ModelsGoodInBox
from ..orders_fbw.types.models_volume_tariff import ModelsVolumeTariff
from ..orders_fbw.types.supplies_list_response import SuppliesListResponse
from ..orders_fbw.types.supply_package_response import SupplyPackageResponse
from ..orders_fbw.types.supply_products_response import SupplyProductsResponse
from ..orders_fbw.types.transit_directions_response import TransitDirectionsResponse
from ..orders_fbw.types.warehouses_item import WarehousesItem
from ..orders_fbw.types.warehouses_list_response import WarehousesListResponse
from ..products.types.brands_item import BrandsItem
from ..products.types.cards_to_add_item import CardsToAddItem
from ..products.types.characteristics_item import CharacteristicsItem
from ..products.types.club_disc_req import ClubDiscReq
from ..products.types.color_response import ColorResponse
from ..products.types.contacts_item import ContactsItem
from ..products.types.contacts_list_item import ContactsListItem
from ..products.types.country_of_origin_response import CountryOfOriginResponse
from ..products.types.create_a_tag_response import CreateATagResponse
from ..products.types.create_product_cards_response import CreateProductCardsResponse
from ..products.types.create_product_cards_with_merge_response import CreateProductCardsWithMergeResponse
from ..products.types.create_warehouse_response import CreateWarehouseResponse
from ..products.types.cursor import Cursor
from ..products.types.data import Data
from ..products.types.delete_inventory_response import DeleteInventoryResponse
from ..products.types.delete_the_tag_response import DeleteTheTagResponse
from ..products.types.delete_warehouse_response import DeleteWarehouseResponse
from ..products.types.dimensions import Dimensions
from ..products.types.filter_ import Filter
from ..products.types.gender_item import GenderItem
from ..products.types.generation_of_skus_item import GenerationOfSkusItem
from ..products.types.good import Good
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
from ..products.types.order import Order
from ..products.types.photos_item import PhotosItem
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
from ..products.types.settings import Settings
from ..products.types.size_good_req import SizeGoodReq
from ..products.types.sizes_item import SizesItem
from ..products.types.sort import Sort
from ..products.types.stocks_item import StocksItem
from ..products.types.subject_characteristics_item import SubjectCharacteristicsItem
from ..products.types.subjects_list_item import SubjectsListItem
from ..products.types.supplier_task_metadata import SupplierTaskMetadata
from ..products.types.supplier_task_metadata_buffer import SupplierTaskMetadataBuffer
from ..products.types.tag_management_in_the_product_card_response import TagManagementInTheProductCardResponse
from ..products.types.tags_item import TagsItem
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
from ..products.types.wholesale import Wholesale
from ..promotion.types.active_and_inactive_search_cluster_lists_item import (
    ActiveAndInactiveSearchClusterListsItem,
)
from ..promotion.types.add_product_to_the_promotion_response import AddProductToThePromotionResponse
from ..promotion.types.advert_list_item import AdvertListItem
from ..promotion.types.advert_n_ms_settings import AdvertNMsSettings
from ..promotion.types.advert_settings import AdvertSettings
from ..promotion.types.advert_subject import AdvertSubject
from ..promotion.types.adverts import Adverts
from ..promotion.types.balance_item import BalanceItem
from ..promotion.types.bids_item import BidsItem
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
from ..promotion.types.items_item import ItemsItem
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
from ..promotion.types.nm_bids_item import NmBidsItem
from ..promotion.types.nms import Nms
from ..promotion.types.nms_item import NmsItem
from ..promotion.types.pause_campaign_response import PauseCampaignResponse
from ..promotion.types.placements import Placements
from ..promotion.types.placements_item import PlacementsItem
from ..promotion.types.product_cards_for_campaigns_response import ProductCardsForCampaignsResponse
from ..promotion.types.promotions_details_item import PromotionsDetailsItem
from ..promotion.types.promotions_list_item import PromotionsListItem
from ..promotion.types.ranging_item import RangingItem
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
from ..promotion.types.show_hours_item import ShowHoursItem
from ..promotion.types.stop_campaign_response import StopCampaignResponse
from ..promotion.types.subjects_for_campaigns_response import SubjectsForCampaignsResponse
from ..promotion.types.timestamps import Timestamps
from ..promotion.types.topup_of_the_campaign_budget_response import TopupOfTheCampaignBudgetResponse
from ..promotion.types.v0_bid_recommendation_reach_max import V0BidRecommendationReachMax
from ..promotion.types.v0_bid_recommendation_reach_medium import V0BidRecommendationReachMedium
from ..promotion.types.v0_bid_recommendation_reach_min import V0BidRecommendationReachMin
from ..promotion.types.v0_get_norm_query_bids_request_item import V0GetNormQueryBidsRequestItem
from ..promotion.types.v0_get_norm_query_list_request_item import V0GetNormQueryListRequestItem
from ..promotion.types.v0_get_norm_query_list_response_item_norm_queries import (
    V0GetNormQueryListResponseItemNormQueries,
)
from ..promotion.types.v0_get_norm_query_minus_request_item import V0GetNormQueryMinusRequestItem
from ..promotion.types.v0_get_norm_query_stats_item_stat import V0GetNormQueryStatsItemStat
from ..promotion.types.v0_set_norm_query_bids_request_item import V0SetNormQueryBidsRequestItem
from ..promotion.types.v1_get_norm_query_stats_response_item_daily_stat import (
    V1GetNormQueryStatsResponseItemDailyStat,
)
from ..promotion.types.v1_get_norm_query_stats_response_item_stat import V1GetNormQueryStatsResponseItemStat
from ..reports.types.blocked_product_cards_item import BlockedProductCardsItem
from ..reports.types.check_the_status_response import CheckTheStatusResponse
from ..reports.types.create_task_response_data import CreateTaskResponseData
from ..reports.types.generate_the_report_response import GenerateTheReportResponse
from ..reports.types.get_tasks_response_data import GetTasksResponseData
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
    "AccessItem",
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
    "Address",
    "AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem",
    "AddUinUniqueIdentificationNumberToAssemblyOrdersItem",
    "AddUinUniqueIdentificationNumberToTheAssemblyOrderResponse",
    "AddUinUniqueIdentificationNumberToTheOrderResponse",
    "AdvertListItem",
    "AdvertNMsSettings",
    "Adverts",
    "AdvertSettings",
    "AdvertSubject",
    "AListOfSellerActiveOrInvitedUsersItem",
    "AllAssemblyOrdersForReshipmentItem",
    "Answer",
    "AnswerBuyersApplicationResponse",
    "ApiB2BClientInfo",
    "ApiBatchErrorResponse",
    "ApiGtin",
    "ApiImei",
    "ApiMetaErrorResponse",
    "ApiOrderCodeRequest",
    "ApiOrdersErrorResponse",
    "ApiSgtiNs",
    "ApiUin",
    "AssemblyOrderMetadataItem",
    "AssemblyOrdersItem",
    "AssemblyOrdersMetadataItem",
    "AssemblyOrdersStatusesItem",
    "AssemblyOrdersStickersItem",
    "AssemblyOrderStatusesItem",
    "AssignADataMatrixCodeToTheAssemblyOrderResponse",
    "ASuppliesListItem",
    "AvgStockTurnover",
    "B2BBuyerInformationItem",
    "BalanceItem",
    "BaseType",
    "BidsItem",
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
    "CardsToAddItem",
    "ChangingCampaignsBidsItem",
    "ChangingPlacementsInCampaignsWithCustomBidResponse",
    "ChangingTheListOfProductCardsInCampaignsItem",
    "CharacteristicsItem",
    "ChatEventsItem",
    "ChatListItem",
    "CheckIfTheOrderBelongsToTheBuyerResponse",
    "CheckTheStatusResponse",
    "ClubDiscReq",
    "ColorResponse",
    "Comparison",
    "ConnectionCheckResponse",
    "Contacts",
    "ContactsItem",
    "ContactsListItem",
    "Conversions",
    "CountryOfOriginResponse",
    "CourierInfo",
    "CourierInfoItem",
    "CreateANewSupplyResponse",
    "CreateAnInvitationForANewUserResponse",
    "CreateATagResponse",
    "CreateCampaignResponse",
    "CreatePassResponse",
    "CreateProductCardsResponse",
    "CreateProductCardsWithMergeResponse",
    "CreateTaskResponseData",
    "CreateTheReportResponse",
    "CreateWarehouseResponse",
    "CurrentPeriod",
    "Cursor",
    "CustomsDeclaration",
    "DailySearchClustersStatisticsItem",
    "Data",
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
    "Dimensions",
    "DocumentResponse",
    "DocumentsCategoriesItem",
    "DocumentsListItem",
    "DocumentsResponse",
    "EditResponseToFeedbackResponse",
    "Error",
    "ErrorsItem",
    "EventAttachments",
    "Expiration",
    "FeedbacksListItem",
    "File",
    "FileFromTheMessageResponse",
    "Filter",
    "FloatGraphByPeriodItem",
    "GenderItem",
    "GenerateTheReportResponse",
    "GenerationOfSkusItem",
    "GetTasksResponseData",
    "GettingSellerPortalNewsItem",
    "Good",
    "GoodCard",
    "GroupDataItem",
    "GroupedProductCardsStatisticsPerDaysItem",
    "Gtin",
    "HiddenFromTheCatalogItem",
    "History",
    "HscodesItem",
    "Image",
    "Imei",
    "InformationAboutMediaCampaignItem",
    "InformationOnCompletedOrdersItem",
    "InformationOnPaidDeliveryResponse",
    "InventoryItem",
    "Invite",
    "InviteeInfo",
    "ItemsItem",
    "LastMessage",
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
    "Message",
    "Meta",
    "Metrics",
    "MinimumBidsForProductCardsItem",
    "ModelsDateFilterRequest",
    "ModelsGoodInBox",
    "ModelsVolumeTariff",
    "MoveTheSupplyToTheDeliveryResponse",
    "NewAssemblyOrdersItem",
    "NewAssemblyOrdersListItem",
    "NewOrdersItem",
    "NewOrdersListItem",
    "NmBidsItem",
    "Nms",
    "NmsItem",
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
    "OfficeMissingTime",
    "OfficesForPassResponse",
    "OfficesItem",
    "OfficesResponse",
    "Options",
    "Order",
    "OrderBy",
    "OrderMetadataItem",
    "OrdersAndPositionsByProductSearchTextsResponse",
    "OrdersItem",
    "OrdersResponse",
    "OrdersStatusesItem",
    "OrdersStickersItem",
    "OrdersWithClientInformationItem",
    "PaginationByGroupsResponse",
    "PaginationByProductsWithinAGroupResponse",
    "PalletTariffsItem",
    "ParamsItem",
    "ParentCategoriesOfTheBrandItem",
    "PassesResponse",
    "Past",
    "PastPeriod",
    "PauseCampaignResponse",
    "Period",
    "PhotoLinksItem",
    "PhotosItem",
    "PinFeedbackResponse",
    "PinnedAndUnpinnedFeedbackNumberResponse",
    "PinnedFeedbackLimitsResponse",
    "Placements",
    "PlacementsItem",
    "ProcessedUploadDetailsItem",
    "ProcessedUploadStateResponse",
    "Product",
    "ProductCardsForCampaignsResponse",
    "ProductCardsInTrashListItem",
    "ProductCardsListItem",
    "ProductCardsStatisticsPerDaysResponse",
    "ProductCardsStatisticsPerPeriodItem",
    "ProductCategoryCommissionResponse",
    "ProductDataItem",
    "ProductDetail",
    "ProductDetailColor",
    "ProductDetailPrice",
    "ProductDetails",
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
    "RangingItem",
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
    "SaleRate",
    "SalesResponse",
    "SearchClustersStatisticsItem",
    "SearchTextsByProductResponse",
    "SeasonItem",
    "Selected",
    "SelectedPeriod",
    "SelfpurchasesItem",
    "SellerBrandsItem",
    "SellerInformationResponse",
    "SellersBalanceResponse",
    "SendMessageItem",
    "SetBidsForSearchClustersResponse",
    "SetPricesAndDiscountsResponse",
    "SetSizePricesResponse",
    "SettingAndDeletingMinusPhrasesResponse",
    "Settings",
    "SetWbClubDiscountsResponse",
    "Sgtin",
    "ShowHoursItem",
    "SizeDataItem",
    "SizeGoodReq",
    "SizesItem",
    "Sort",
    "Statistic",
    "StatusesItem",
    "StatusHistoryForCrossborderOrdersItem",
    "StickersForAssemblyOrdersWithDeliveryToPickupPointItem",
    "StickersForCrossborderAssemblyOrdersItem",
    "Stocks",
    "StocksItem",
    "StopCampaignResponse",
    "SubjectCharacteristicsItem",
    "SubjectsForCampaignsResponse",
    "SubjectsListItem",
    "SubstitutionsAndIncorrectAttachmentsItem",
    "SupplierTaskMetadata",
    "SupplierTaskMetadataBuffer",
    "SuppliesListResponse",
    "SupplyAssemblyOrderIdsItem",
    "SupplyBoxesListItem",
    "SupplyDetailsResponse",
    "SupplyPackageResponse",
    "SupplyProductsResponse",
    "SupplyTariffsResponse",
    "TableProductItemSt",
    "Tag",
    "TagManagementInTheProductCardResponse",
    "TagsItem",
    "TagsListResponse",
    "TheFeedbackByIdItem",
    "TheQuestionByIdItem",
    "TheReportResponse",
    "TheReportsListItem",
    "TheSupplyBoxQrCodeStickersItem",
    "TheSupplyQrCodeResponse",
    "Timestamps",
    "TimeToReady",
    "TimeToReadyDynamic",
    "TopupOfTheCampaignBudgetResponse",
    "TransferProductCardToTrashResponse",
    "TransferToAssemblyItem",
    "TransferToAssemblyResponse",
    "TransferToDeliveryItem",
    "TransferToDeliveryResponse",
    "TransitDirectionsResponse",
    "TypesItem",
    "Uin",
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
    "UserAccess",
    "V0BidRecommendationReachMax",
    "V0BidRecommendationReachMedium",
    "V0BidRecommendationReachMin",
    "V0GetNormQueryBidsRequestItem",
    "V0GetNormQueryListRequestItem",
    "V0GetNormQueryListResponseItemNormQueries",
    "V0GetNormQueryMinusRequestItem",
    "V0GetNormQueryStatsItemStat",
    "V0SetNormQueryBidsRequestItem",
    "V1GetNormQueryStatsResponseItemDailyStat",
    "V1GetNormQueryStatsResponseItemStat",
    "VatRateItem",
    "Video",
    "WarehouseDataItem",
    "WarehouseMeasurementsItem",
    "WarehouseResponse",
    "WarehousesItem",
    "WarehousesListResponse",
    "WarehousesResponse",
    "WbClub",
    "WbClubDynamic",
    "Wholesale",
    "WorkingWithQuestionsItem",
)
