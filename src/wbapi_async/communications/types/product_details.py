from pydantic import Field

from ...types.base import BaseType


class ProductDetails(BaseType):
    """Product information"""

    nm_id: int | None = Field(None, alias="nmId")
    imt_id: int | None = Field(None, alias="imtId")
    product_name: str | None = Field(None, alias="productName")
    supplier_article: str | None = Field(None, alias="supplierArticle")
    supplier_name: str | None = Field(None, alias="supplierName")
    brand_name: str | None = Field(None, alias="brandName")
