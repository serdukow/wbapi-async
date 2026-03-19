from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import Field

from ..types.base import BaseType
from ..types.product_card import ProductCard
from ..types.request_limit import RequestLimit
from .base import WbMethod


if TYPE_CHECKING:
    from ..client.api import WbAPI


class CardListSort(BaseType):
    ascending: bool = Field(False, alias="ascending")


class CardListFilter(BaseType):
    with_photo: int = Field(-1, alias="withPhoto")
    text_search: str | None = Field(None, alias="textSearch")
    tag_ids: list[int] | None = Field(None, alias="tagIDs")
    allowed_categories_only: bool | None = Field(None, alias="allowedCategoriesOnly")
    object_ids: list[int] | None = Field(None, alias="objectIDs")
    brands: list[str] | None = Field(None, alias="brands")
    imt_id: int | None = Field(None, alias="imtID")


class CardListCursor(BaseType):
    limit: int = Field(100, alias="limit")
    updated_at: str | None = Field(None, alias="updatedAt")
    nm_id: int | None = Field(None, alias="nmID")


class CardListSettings(BaseType):
    sort: CardListSort | None = Field(None, alias="sort")
    filter: CardListFilter | None = Field(None, alias="filter")
    cursor: CardListCursor | None = Field(None, alias="cursor")


class GetProductCardsList(WbMethod):
    """
    Returns the list of created product cards.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Product-Cards/paths/~1content~1v2~1get~1cards~1list/post
    """

    __return__ = ProductCard
    __api__ = "content-api"
    __method__ = "content/v2/get/cards/list"
    __data_key__ = "cards"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=100, interval=600, burst=5)

    locale: str | None = Field(None)
    settings: CardListSettings

    async def emit(self, wb_api: WbAPI) -> list[ProductCard]:
        wb_api.session.headers.set_token(wb_api._token)
        url = wb_api.session.build_url(self.__api__, self.__method__)
        request_limit: RequestLimit | None = getattr(self, "request_limit", None)

        params: dict[str, Any] | None = {"locale": self.locale} if self.locale else None
        all_cards: list[ProductCard] = []

        current_settings = self.settings.model_copy()

        while True:
            body = {"settings": current_settings.model_dump(by_alias=True, exclude_none=True)}
            data = await wb_api.session._request(
                "POST",
                url,
                params=params,
                json=body,
                limit=request_limit,
            )

            cards_raw = data.get("cards", []) if data else []
            cursor_raw = data.get("cursor", {}) if data else {}

            from pydantic import TypeAdapter

            cards = TypeAdapter(list[ProductCard]).validate_python(cards_raw)
            all_cards.extend(cards)

            total = cursor_raw.get("total", 0)
            limit = cursor_raw.get("limit", 100)

            if total < limit:
                break

            updated_at = cursor_raw.get("updatedAt")
            nm_id = cursor_raw.get("nmID")

            current_cursor = current_settings.cursor or CardListCursor()
            current_settings = current_settings.model_copy(
                update={
                    "cursor": current_cursor.model_copy(
                        update={"updated_at": updated_at, "nm_id": nm_id}
                    )
                }
            )

        return all_cards
