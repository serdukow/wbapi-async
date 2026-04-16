from pydantic import Field

from ...types.base import BaseType
from ..enums.type__2 import Type2
from .ranging_item import RangingItem


class PromotionsDetailsItem(BaseType):
    """Promotions Details"""

    id_: int | None = Field(None, alias="id")
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
    type_: Type2 | None = Field(None, alias="type")
    exception_products_count: int | None = Field(None, alias="exceptionProductsCount")
    ranging: list[RangingItem] | None = Field(None)
