from .base import BaseType
from .brands_item import BrandsItem
from .campaign_statistics import AppStat, BoosterStat, CampaignStatistics, DayStat, NmStat
from .campaigns_list import CampaignGroup, CampaignItem, CampaignsList
from .color_response import ColorResponse
from .connection_check import ConnectionCheck
from .contacts_list_item import ContactsListItem
from .country_of_origin_response import CountryOfOriginResponse
from .create_a_tag_response import CreateATagResponse
from .create_product_cards_response import CreateProductCardsResponse
from .create_product_cards_with_merge_response import CreateProductCardsWithMergeResponse
from .create_warehouse_response import CreateWarehouseResponse
from .delete_inventory_response import DeleteInventoryResponse
from .delete_the_tag_response import DeleteTheTagResponse
from .delete_warehouse_response import DeleteWarehouseResponse
from .error import Error
from .gender_item import GenderItem
from .generation_of_skus_item import GenerationOfSkusItem
from .hscodes_item import HscodesItem
from .inventory_item import InventoryItem
from .limits_for_the_product_cards_response import LimitsForTheProductCardsResponse
from .list_of_failed_product_cards_with_errors_item import ListOfFailedProductCardsWithErrorsItem
from .merging_or_separating_of_product_cards_response import (
    MergingOrSeparatingOfProductCardsResponse,
)
from .offices_response import OfficesResponse
from .processed_upload_details_item import ProcessedUploadDetailsItem
from .processed_upload_details_response import ProcessedUploadDetailsResponse
from .processed_upload_state_response import ProcessedUploadStateResponse
from .product_card import (
    ProductCard,
    ProductCardCharacteristic,
    ProductCardDimensions,
    ProductCardPhoto,
    ProductCardSize,
    ProductCardTag,
    ProductCardWholesale,
)
from .product_cards_in_trash_list_item import ProductCardsInTrashListItem
from .product_cards_list_item import ProductCardsListItem
from .product_cards_statistics import (
    ComparisonStats,
    Conversions,
    DaysHoursMinutes,
    PeriodStats,
    ProductCardStatistics,
    ProductInfo,
    ProductStatistic,
    Stocks,
    Tag,
    WbClubStats,
)
from .product_data import (
    AvgOrdersByMonth,
    CurrentPrice,
    DaysHours,
    ProductDataItem,
    ProductMetrics,
)
from .product_detail import (
    ProductDetail,
    ProductDetailColor,
    ProductDetailPrice,
    ProductDetailSize,
    ProductDetailStock,
)
from .product_sizes_with_prices_item import ProductSizesWithPricesItem
from .product_with_price import ProductWithPrice, Size
from .products_in_quarantine_item import ProductsInQuarantineItem
from .products_parent_categories_response import ProductsParentCategoriesResponse
from .products_with_prices_by_articles_item import ProductsWithPricesByArticlesItem
from .products_with_prices_item import ProductsWithPricesItem
from .realization_sales_report import RealizationSalesReport
from .recover_product_card_from_trash_response import RecoverProductCardFromTrashResponse
from .request_limit import RequestLimit
from .sale import Sale
from .season_item import SeasonItem
from .set_prices_and_discounts_response import SetPricesAndDiscountsResponse
from .set_size_prices_response import SetSizePricesResponse
from .set_wb_club_discounts_response import SetWbClubDiscountsResponse
from .subject_characteristics_item import SubjectCharacteristicsItem
from .subjects_list_item import SubjectsListItem
from .supply import Supply
from .supply_product import SupplyProduct
from .tag_management_in_the_product_card_response import TagManagementInTheProductCardResponse
from .tags_list_response import TagsListResponse
from .transfer_product_card_to_trash_response import TransferProductCardToTrashResponse
from .unprocessed_upload_details_item import UnprocessedUploadDetailsItem
from .unprocessed_upload_details_response import UnprocessedUploadDetailsResponse
from .unprocessed_upload_state_response import UnprocessedUploadStateResponse
from .update_contacts_list_response import UpdateContactsListResponse
from .update_inventory_response import UpdateInventoryResponse
from .update_product_cards_response import UpdateProductCardsResponse
from .update_the_tag_response import UpdateTheTagResponse
from .update_warehouse_response import UpdateWarehouseResponse
from .upload_media_file_response import UploadMediaFileResponse
from .upload_media_files_via_links_response import UploadMediaFilesViaLinksResponse
from .vat_rate_item import VatRateItem
from .warehouses_response import WarehousesResponse


__all__ = (
    "AppStat",
    "AvgOrdersByMonth",
    "BaseType",
    "BoosterStat",
    "BrandsItem",
    "CampaignGroup",
    "CampaignItem",
    "CampaignStatistics",
    "CampaignsList",
    "ColorResponse",
    "ComparisonStats",
    "ConnectionCheck",
    "ContactsListItem",
    "Conversions",
    "CountryOfOriginResponse",
    "CreateATagResponse",
    "CreateProductCardsResponse",
    "CreateProductCardsWithMergeResponse",
    "CreateWarehouseResponse",
    "CurrentPrice",
    "DayStat",
    "DaysHours",
    "DaysHoursMinutes",
    "DeleteInventoryResponse",
    "DeleteTheTagResponse",
    "DeleteWarehouseResponse",
    "Error",
    "GenderItem",
    "GenerationOfSkusItem",
    "HscodesItem",
    "InventoryItem",
    "LimitsForTheProductCardsResponse",
    "ListOfFailedProductCardsWithErrorsItem",
    "MergingOrSeparatingOfProductCardsResponse",
    "NmStat",
    "OfficesResponse",
    "PeriodStats",
    "ProcessedUploadDetailsItem",
    "ProcessedUploadDetailsResponse",
    "ProcessedUploadStateResponse",
    "ProductCard",
    "ProductCardCharacteristic",
    "ProductCardDimensions",
    "ProductCardPhoto",
    "ProductCardSize",
    "ProductCardStatistics",
    "ProductCardTag",
    "ProductCardWholesale",
    "ProductCardsInTrashListItem",
    "ProductCardsListItem",
    "ProductDataItem",
    "ProductDetail",
    "ProductDetailColor",
    "ProductDetailPrice",
    "ProductDetailSize",
    "ProductDetailStock",
    "ProductInfo",
    "ProductMetrics",
    "ProductSizesWithPricesItem",
    "ProductStatistic",
    "ProductWithPrice",
    "ProductsInQuarantineItem",
    "ProductsParentCategoriesResponse",
    "ProductsWithPricesByArticlesItem",
    "ProductsWithPricesItem",
    "RealizationSalesReport",
    "RecoverProductCardFromTrashResponse",
    "RequestLimit",
    "Sale",
    "SeasonItem",
    "SetPricesAndDiscountsResponse",
    "SetSizePricesResponse",
    "SetWbClubDiscountsResponse",
    "Size",
    "Stocks",
    "SubjectCharacteristicsItem",
    "SubjectsListItem",
    "Supply",
    "SupplyProduct",
    "Tag",
    "TagManagementInTheProductCardResponse",
    "TagsListResponse",
    "TransferProductCardToTrashResponse",
    "UnprocessedUploadDetailsItem",
    "UnprocessedUploadDetailsResponse",
    "UnprocessedUploadStateResponse",
    "UpdateContactsListResponse",
    "UpdateInventoryResponse",
    "UpdateProductCardsResponse",
    "UpdateTheTagResponse",
    "UpdateWarehouseResponse",
    "UploadMediaFileResponse",
    "UploadMediaFilesViaLinksResponse",
    "VatRateItem",
    "WarehousesResponse",
    "WbClubStats",
)
