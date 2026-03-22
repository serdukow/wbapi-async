from typing import Any

from pydantic import Field

from .base import BaseType


class ListOfArchivedFeedbacksItem(BaseType):
    """List of Archived Feedbacks"""

    id: str | None = Field(None)
    text: str | None = Field(None)
    pros: str | None = Field(None)
    cons: str | None = Field(None)
    product_valuation: int | None = Field(None, alias="productValuation")
    created_date: str | None = Field(None, alias="createdDate")
    answer: dict[str, Any] | None = Field(None)
    state: str | None = Field(None)
    product_details: dict[str, Any] | None = Field(None, alias="productDetails")
    photo_links: list[dict[str, Any]] | None = Field(None, alias="photoLinks")
    video: dict[str, Any] | None = Field(None)
    was_viewed: bool | None = Field(None, alias="wasViewed")
    user_name: str | None = Field(None, alias="userName")
    order_status: str | None = Field(None, alias="orderStatus")
    matching_size: str | None = Field(None, alias="matchingSize")
    is_able_supplier_feedback_valuation: bool | None = Field(None, alias="isAbleSupplierFeedbackValuation")
    supplier_feedback_valuation: int | None = Field(None, alias="supplierFeedbackValuation")
    is_able_supplier_product_valuation: bool | None = Field(None, alias="isAbleSupplierProductValuation")
    supplier_product_valuation: int | None = Field(None, alias="supplierProductValuation")
    is_able_return_product_orders: bool | None = Field(None, alias="isAbleReturnProductOrders")
    return_product_orders_date: str | None = Field(None, alias="returnProductOrdersDate")
    bables: list[str] | None = Field(None)
    last_order_shk_id: int | None = Field(None, alias="lastOrderShkId")
    last_order_created_at: str | None = Field(None, alias="lastOrderCreatedAt")
    color: str | None = Field(None)
    subject_id: int | None = Field(None, alias="subjectId")
    subject_name: str | None = Field(None, alias="subjectName")
    parent_feedback_id: str | None = Field(None, alias="parentFeedbackId")
    child_feedback_id: str | None = Field(None, alias="childFeedbackId")
