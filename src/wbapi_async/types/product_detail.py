from pydantic import Field

from .base import BaseType


class ProductDetailStock(BaseType):
    wh: int | None = Field(None, alias="wh")
    dtype: int | None = Field(None, alias="dtype")
    dist: int | None = Field(None, alias="dist")
    qty: int | None = Field(None, alias="qty")
    priority: int | None = Field(None, alias="priority")
    time1: int | None = Field(None, alias="time1")
    time2: int | None = Field(None, alias="time2")


class ProductDetailPrice(BaseType):
    basic: int | None = Field(None, alias="basic")
    product: int | None = Field(None, alias="product")
    logistics: int | None = Field(None, alias="logistics")
    return_: int | None = Field(None, alias="return")


class ProductDetailSize(BaseType):
    name: str | None = Field(None, alias="name")
    orig_name: str | None = Field(None, alias="origName")
    rank: int | None = Field(None, alias="rank")
    option_id: int | None = Field(None, alias="optionId")
    stocks: list[ProductDetailStock] | None = Field(None, alias="stocks")
    time1: int | None = Field(None, alias="time1")
    time2: int | None = Field(None, alias="time2")
    wh: int | None = Field(None, alias="wh")
    dtype: int | None = Field(None, alias="dtype")
    dist: int | None = Field(None, alias="dist")
    price: ProductDetailPrice | None = Field(None, alias="price")
    sale_conditions: int | None = Field(None, alias="saleConditions")
    payload: str | None = Field(None, alias="payload")


class ProductDetailColor(BaseType):
    name: str | None = Field(None, alias="name")
    id: int | None = Field(None, alias="id")


class ProductDetail(BaseType):
    id: int | None = Field(None, alias="id")
    root: int | None = Field(None, alias="root")
    kind_id: int | None = Field(None, alias="kindId")
    brand: str | None = Field(None, alias="brand")
    brand_id: int | None = Field(None, alias="brandId")
    site_brand_id: int | None = Field(None, alias="siteBrandId")
    colors: list[ProductDetailColor] | None = Field(None, alias="colors")
    subject_id: int | None = Field(None, alias="subjectId")
    subject_parent_id: int | None = Field(None, alias="subjectParentId")
    name: str | None = Field(None, alias="name")
    entity: str | None = Field(None, alias="entity")
    match_id: int | None = Field(None, alias="matchId")
    supplier: str | None = Field(None, alias="supplier")
    supplier_id: int | None = Field(None, alias="supplierId")
    supplier_rating: float | None = Field(None, alias="supplierRating")
    supplier_flags: int | None = Field(None, alias="supplierFlags")
    pics: int | None = Field(None, alias="pics")
    rating: int | None = Field(None, alias="rating")
    review_rating: float | None = Field(None, alias="reviewRating")
    nm_review_rating: float | None = Field(None, alias="nmReviewRating")
    feedbacks: int | None = Field(None, alias="feedbacks")
    nm_feedbacks: int | None = Field(None, alias="nmFeedbacks")
    volume: int | None = Field(None, alias="volume")
    weight: float | None = Field(None, alias="weight")
    view_flags: int | None = Field(None, alias="viewFlags")
    promotions: list[int] | None = Field(None, alias="promotions")
    sizes: list[ProductDetailSize] | None = Field(None, alias="sizes")
    total_quantity: int | None = Field(None, alias="totalQuantity")
    time1: int | None = Field(None, alias="time1")
    time2: int | None = Field(None, alias="time2")
    wh: int | None = Field(None, alias="wh")
    dtype: int | None = Field(None, alias="dtype")
    dist: int | None = Field(None, alias="dist")
