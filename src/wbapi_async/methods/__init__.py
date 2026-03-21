from .base import WbMethod
from .brands import Brands
from .color import Color
from .connection_check import ConnectionCheck
from .contacts_list import ContactsList
from .country_of_origin import CountryOfOrigin
from .create_a_tag import CreateATag
from .create_product_cards import CreateProductCards
from .create_product_cards_with_merge import CreateProductCardsWithMerge
from .create_warehouse import CreateWarehouse
from .delete_inventory import DeleteInventory
from .delete_the_tag import DeleteTheTag
from .delete_warehouse import DeleteWarehouse
from .gender import Gender
from .generation_of_skus import GenerationOfSkus
from .get_campaigns_lists import GetCampaignsLists
from .get_campaigns_statistics import GetCampaignsStatistics
from .get_inventory import GetInventory
from .get_offices import GetOffices
from .get_product_cards_list import (
    CardListCursor,
    CardListFilter,
    CardListSettings,
    CardListSort,
    GetProductCardsList,
)
from .get_product_cards_statistics_per_period import (
    GetProductCardsStatisticsPerPeriod,
    SalesFunnelOrderBy,
    SalesFunnelPeriod,
)
from .get_product_data import GetProductData, OrderBy, Period
from .get_product_detail import GetProductDetail
from .get_product_sizes_with_prices import GetProductSizesWithPrices
from .get_products_in_quarantine import GetProductsInQuarantine
from .get_products_with_prices import GetProductsWithPrices
from .get_products_with_prices_by_articles import GetProductsWithPricesByArticles
from .get_realization_sales_report import GetRealizationSalesReport
from .get_sales import GetSales
from .get_supplies_list import GetSuppliesList, SupplyDateFilter
from .get_supply_products import GetSupplyProducts
from .get_warehouses import GetWarehouses
from .hscodes import Hscodes
from .limits_for_the_product_cards import LimitsForTheProductCards
from .list_of_failed_product_cards_with_errors import ListOfFailedProductCardsWithErrors
from .merging_or_separating_of_product_cards import MergingOrSeparatingOfProductCards
from .processed_upload_details import ProcessedUploadDetails
from .processed_upload_state import ProcessedUploadState
from .product_cards_in_trash_list import ProductCardsInTrashList
from .product_cards_list import ProductCardsList
from .products_parent_categories import ProductsParentCategories
from .recover_product_card_from_trash import RecoverProductCardFromTrash
from .season import Season
from .set_prices_and_discounts import SetPricesAndDiscounts
from .set_size_prices import SetSizePrices
from .set_wb_club_discounts import SetWbClubDiscounts
from .subject_characteristics import SubjectCharacteristics
from .subjects_list import SubjectsList
from .tag_management_in_the_product_card import TagManagementInTheProductCard
from .tags_list import TagsList
from .transfer_product_card_to_trash import TransferProductCardToTrash
from .unprocessed_upload_details import UnprocessedUploadDetails
from .unprocessed_upload_state import UnprocessedUploadState
from .update_contacts_list import UpdateContactsList
from .update_inventory import UpdateInventory
from .update_product_cards import UpdateProductCards
from .update_the_tag import UpdateTheTag
from .update_warehouse import UpdateWarehouse
from .upload_media_file import UploadMediaFile
from .upload_media_files_via_links import UploadMediaFilesViaLinks
from .vat_rate import VatRate


__all__ = (
    "WbMethod",
    "Brands",
    "CardListCursor",
    "CardListFilter",
    "CardListSettings",
    "CardListSort",
    "Color",
    "ConnectionCheck",
    "ContactsList",
    "CountryOfOrigin",
    "CreateATag",
    "CreateProductCards",
    "CreateProductCardsWithMerge",
    "CreateWarehouse",
    "DeleteInventory",
    "DeleteTheTag",
    "DeleteWarehouse",
    "Gender",
    "GenerationOfSkus",
    "GetCampaignsLists",
    "GetCampaignsStatistics",
    "GetInventory",
    "GetOffices",
    "GetProductCardsList",
    "GetProductCardsStatisticsPerPeriod",
    "GetProductData",
    "GetProductDetail",
    "GetProductSizesWithPrices",
    "GetProductsInQuarantine",
    "GetProductsWithPrices",
    "GetProductsWithPricesByArticles",
    "GetRealizationSalesReport",
    "GetSales",
    "GetSuppliesList",
    "GetSupplyProducts",
    "GetWarehouses",
    "Hscodes",
    "LimitsForTheProductCards",
    "ListOfFailedProductCardsWithErrors",
    "MergingOrSeparatingOfProductCards",
    "OrderBy",
    "Period",
    "ProcessedUploadDetails",
    "ProcessedUploadState",
    "ProductCardsInTrashList",
    "ProductCardsList",
    "ProductsParentCategories",
    "RecoverProductCardFromTrash",
    "SalesFunnelOrderBy",
    "SalesFunnelPeriod",
    "Season",
    "SetPricesAndDiscounts",
    "SetSizePrices",
    "SetWbClubDiscounts",
    "SubjectCharacteristics",
    "SubjectsList",
    "SupplyDateFilter",
    "TagManagementInTheProductCard",
    "TagsList",
    "TransferProductCardToTrash",
    "UnprocessedUploadDetails",
    "UnprocessedUploadState",
    "UpdateContactsList",
    "UpdateInventory",
    "UpdateProductCards",
    "UpdateTheTag",
    "UpdateWarehouse",
    "UploadMediaFile",
    "UploadMediaFilesViaLinks",
    "VatRate",
)
