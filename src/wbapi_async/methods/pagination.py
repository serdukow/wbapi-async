"""Pagination strategies for WbMethod.

Each strategy handles one pagination pattern:
- OffsetPagination:    limit + offset  (products, promotion, reports)
- NextCursorPagination: limit + next   (orders FBS/DBW/DBS, in-store pickup)
- TakeSkipPagination:  take + skip     (communications feedbacks/questions)

To add a new pattern:
1. Subclass PaginationStrategy
2. Implement first_params(), next_params(), extract_page()
3. Register in PAGINATION_STRATEGIES
4. Add the pattern name to codegen detect_pagination()
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any


if TYPE_CHECKING:
    from .base import WbMethod


class PaginationStrategy(ABC):
    """Base class for all pagination strategies."""

    page_size: int = 1000

    @abstractmethod
    def first_params(self) -> dict[str, Any]:
        """Return API params for the first page."""

    @abstractmethod
    def next_params(
        self,
        current_params: dict[str, Any],
        response: Any,
        page: list[Any],
    ) -> dict[str, Any] | None:
        """Return API params for the next page, or None if done.

        :param current_params: the params used for the current page
        :param response: raw API response
        :param page: extracted list of items from current page
        """

    def extract_page(self, method: WbMethod, response: Any) -> list[Any]:
        """Extract the list of items from a raw response."""
        result = method._extract(response)
        return result if isinstance(result, list) else []


class OffsetPagination(PaginationStrategy):
    """limit + offset — products, promotion, reports, finances, FBW."""

    page_size = 1000

    def first_params(self) -> dict[str, Any]:
        return {"limit": self.page_size, "offset": 0}

    def next_params(
        self,
        current_params: dict[str, Any],
        response: Any,
        page: list[Any],
    ) -> dict[str, Any] | None:
        if len(page) < self.page_size:
            return None
        current_offset = current_params.get("offset", 0)
        return {"limit": self.page_size, "offset": current_offset + self.page_size}


class NextCursorPagination(PaginationStrategy):
    """limit + next — orders FBS/DBW/DBS, in-store pickup, communications events."""

    page_size = 1000

    def first_params(self) -> dict[str, Any]:
        return {"limit": self.page_size, "next": 0}

    def next_params(
        self,
        current_params: dict[str, Any],
        response: Any,
        page: list[Any],
    ) -> dict[str, Any] | None:
        cursor = response.get("next", 0) if isinstance(response, dict) else 0
        if not cursor:
            return None
        return {"limit": self.page_size, "next": cursor}


class TakeSkipPagination(PaginationStrategy):
    """take + skip — communications feedbacks and questions."""

    page_size = 5000

    def first_params(self) -> dict[str, Any]:
        return {"take": self.page_size, "skip": 0}

    def next_params(
        self,
        current_params: dict[str, Any],
        response: Any,
        page: list[Any],
    ) -> dict[str, Any] | None:
        if len(page) < self.page_size:
            return None
        current_skip = current_params.get("skip", 0)
        return {"take": self.page_size, "skip": current_skip + self.page_size}


PAGINATION_STRATEGIES: dict[str, PaginationStrategy] = {
    "offset": OffsetPagination(),
    "next": NextCursorPagination(),
    "take_skip": TakeSkipPagination(),
}
