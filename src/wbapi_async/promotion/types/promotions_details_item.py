from pydantic import Field

from ...types.base import BaseType
from .ranging_item import RangingItem


class PromotionsDetailsItem(BaseType):
    """Promotions Details"""

    id_: int | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")
    description: str | None = Field(None, alias="description")
    advantages: list[str] | None = Field(None, alias="advantages")
    start_date_time: str | None = Field(None, alias="startDateTime")
    end_date_time: str | None = Field(None, alias="endDateTime")
    in_promo_action_leftovers: int | None = Field(None, alias="inPromoActionLeftovers")
    in_promo_action_total: int | None = Field(None, alias="inPromoActionTotal")
    not_in_promo_action_leftovers: int | None = Field(None, alias="notInPromoActionLeftovers")
    not_in_promo_action_total: int | None = Field(None, alias="notInPromoActionTotal")
    participation_percentage: int | None = Field(None, alias="participationPercentage")
    type_: str | None = Field(None, alias="type")
    exception_products_count: int | None = Field(None, alias="exceptionProductsCount")
    ranging: list[RangingItem] | None = Field(None, alias="ranging")
