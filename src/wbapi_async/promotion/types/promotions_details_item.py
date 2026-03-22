from typing import Any

from pydantic import Field

from ...types.base import BaseType


class PromotionsDetailsItem(BaseType):
    """Promotions Details"""

    id: int | None = Field(None)
    name: str | None = Field(None)
    description: str | None = Field(None)
    advantages: list[str] | None = Field(None)
    start_date_time: str | None = Field(None, alias="startDateTime")
    end_date_time: str | None = Field(None, alias="endDateTime")
    in_promo_action_leftovers: int | None = Field(None, alias="inPromoActionLeftovers")
    in_promo_action_total: int | None = Field(None, alias="inPromoActionTotal")
    not_in_promo_action_leftovers: int | None = Field(None, alias="notInPromoActionLeftovers")
    not_in_promo_action_total: int | None = Field(None, alias="notInPromoActionTotal")
    participation_percentage: int | None = Field(None, alias="participationPercentage")
    type: str | None = Field(None)
    exception_products_count: int | None = Field(None, alias="exceptionProductsCount")
    ranging: list[dict[str, Any]] | None = Field(None)
