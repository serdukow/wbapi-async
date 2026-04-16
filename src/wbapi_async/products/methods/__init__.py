from .create_atag import CreateATag
from .create_product_cards import CreateProductCards
from .create_product_cards_with_merge import CreateProductCardsWithMerge
from .create_warehouse import CreateWarehouse
from .delete_inventory import DeleteInventory
from .delete_the_tag import DeleteTheTag
from .delete_warehouse import DeleteWarehouse
from .generation_of_skus import GenerationOfSkus
from .get_brands import GetBrands
from .get_color import GetColor
from .get_contacts_list import GetContactsList
from .get_country_of_origin import GetCountryOfOrigin
from .get_gender import GetGender
from .get_hscodes import GetHscodes
from .get_inventory import GetInventory
from .get_limits_for_the_product_cards import GetLimitsForTheProductCards
from .get_list_of_failed_product_cards_with_errors import GetListOfFailedProductCardsWithErrors
from .get_offices import GetOffices
from .get_processed_upload_details import GetProcessedUploadDetails
from .get_processed_upload_state import GetProcessedUploadState
from .get_product_cards_in_trash_list import GetProductCardsInTrashList
from .get_product_cards_list import GetProductCardsList
from .get_product_sizes_with_prices import GetProductSizesWithPrices
from .get_products_in_quarantine import GetProductsInQuarantine
from .get_products_parent_categories import GetProductsParentCategories
from .get_products_with_prices import GetProductsWithPrices
from .get_products_with_prices_by_articles import GetProductsWithPricesByArticles
from .get_season import GetSeason
from .get_subject_characteristics import GetSubjectCharacteristics
from .get_subjects_list import GetSubjectsList
from .get_tags_list import GetTagsList
from .get_unprocessed_upload_details import GetUnprocessedUploadDetails
from .get_unprocessed_upload_state import GetUnprocessedUploadState
from .get_vat_rate import GetVatRate
from .get_warehouses import GetWarehouses
from .merging_or_separating_of_product_cards import MergingOrSeparatingOfProductCards
from .recover_product_card_from_trash import RecoverProductCardFromTrash
from .set_prices_and_discounts import SetPricesAndDiscounts
from .set_size_prices import SetSizePrices
from .set_wb_club_discounts import SetWbClubDiscounts
from .tag_management_in_the_product_card import TagManagementInTheProductCard
from .transfer_product_card_to_trash import TransferProductCardToTrash
from .update_contacts_list import UpdateContactsList
from .update_inventory import UpdateInventory
from .update_product_cards import UpdateProductCards
from .update_the_tag import UpdateTheTag
from .update_warehouse import UpdateWarehouse
from .upload_media_file import UploadMediaFile
from .upload_media_files_via_links import UploadMediaFilesViaLinks


__all__ = (
    "CreateATag",
    "CreateProductCards",
    "CreateProductCardsWithMerge",
    "CreateWarehouse",
    "DeleteInventory",
    "DeleteTheTag",
    "DeleteWarehouse",
    "GenerationOfSkus",
    "GetBrands",
    "GetColor",
    "GetContactsList",
    "GetCountryOfOrigin",
    "GetGender",
    "GetHscodes",
    "GetInventory",
    "GetLimitsForTheProductCards",
    "GetListOfFailedProductCardsWithErrors",
    "GetOffices",
    "GetProcessedUploadDetails",
    "GetProcessedUploadState",
    "GetProductCardsInTrashList",
    "GetProductCardsList",
    "GetProductsInQuarantine",
    "GetProductSizesWithPrices",
    "GetProductsParentCategories",
    "GetProductsWithPrices",
    "GetProductsWithPricesByArticles",
    "GetSeason",
    "GetSubjectCharacteristics",
    "GetSubjectsList",
    "GetTagsList",
    "GetUnprocessedUploadDetails",
    "GetUnprocessedUploadState",
    "GetVatRate",
    "GetWarehouses",
    "MergingOrSeparatingOfProductCards",
    "RecoverProductCardFromTrash",
    "SetPricesAndDiscounts",
    "SetSizePrices",
    "SetWbClubDiscounts",
    "TagManagementInTheProductCard",
    "TransferProductCardToTrash",
    "UpdateContactsList",
    "UpdateInventory",
    "UpdateProductCards",
    "UpdateTheTag",
    "UpdateWarehouse",
    "UploadMediaFile",
    "UploadMediaFilesViaLinks",
)
