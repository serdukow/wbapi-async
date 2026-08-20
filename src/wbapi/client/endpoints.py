"""Known Wildberries API endpoints: which host serves them, and how fast.

The ``ENDPOINTS`` table below is generated from the official OpenAPI specs by
``scripts/generate_endpoints.py``. It exists for convenience — short paths get
their host and rate limit filled in automatically:

    await api.get("/api/v3/supplies")

A path missing from the table is not a dead end. Pass the full URL and the
request goes through with a conservative default rate limit, so endpoints
Wildberries adds after a release are usable immediately:

    await api.get("https://content-api.wildberries.ru/content/v3/whatever")
"""

from __future__ import annotations

from functools import lru_cache
from urllib.parse import urlparse

from .exceptions import WBConfigurationError


__all__ = ("resolve_url", "rate_limit_for", "page_size_for")

# Hosts that serve unauthenticated data; the token is never sent to them.
PUBLIC_HOSTS: frozenset[str] = frozenset({"card.wb.ru"})

# Endpoints whose natural page size differs from the API-wide default.
PAGE_SIZES: dict[str, int] = {
    "/content/v2/get/cards/list": 100,
    "/api/v1/documents/list": 50,
    "/api/finance/v1/sales-reports/detailed": 100_000,
}

DEFAULT_PAGE_SIZE = 1000
DEFAULT_RATE_LIMIT = (1000, 5)  # (interval_ms, burst) — 5 requests per second

# --- BEGIN GENERATED ---

ENDPOINTS: dict[str, dict[str, tuple[int, int]]] = {
    "https://marketplace-api.wildberries.ru": {
        "/api/marketplace/v3/dbs/orders/b2b/info": (200, 20),
        "/api/marketplace/v3/dbs/orders/meta/customs-declaration": (120, 20),
        "/api/marketplace/v3/dbs/orders/meta/delete": (400, 20),
        "/api/marketplace/v3/dbs/orders/meta/gtin": (120, 20),
        "/api/marketplace/v3/dbs/orders/meta/imei": (120, 20),
        "/api/marketplace/v3/dbs/orders/meta/info": (400, 20),
        "/api/marketplace/v3/dbs/orders/meta/sgtin": (120, 20),
        "/api/marketplace/v3/dbs/orders/meta/uin": (120, 20),
        "/api/marketplace/v3/dbs/orders/status/cancel": (1000, 10),
        "/api/marketplace/v3/dbs/orders/status/confirm": (1000, 10),
        "/api/marketplace/v3/dbs/orders/status/deliver": (1000, 10),
        "/api/marketplace/v3/dbs/orders/status/info": (200, 20),
        "/api/marketplace/v3/dbs/orders/status/receive": (1000, 10),
        "/api/marketplace/v3/dbs/orders/status/reject": (1000, 10),
        "/api/marketplace/v3/dbs/orders/stickers": (200, 20),
        "/api/marketplace/v3/dbw/orders/client": (200, 20),
        "/api/marketplace/v3/orders/meta": (200, 20),
        "/api/marketplace/v3/orders/{orderId}/meta/customs-declaration": (60, 20),
        "/api/marketplace/v3/supplies/{supplyId}/order-ids": (200, 20),
        "/api/marketplace/v3/supplies/{supplyId}/orders": (200, 20),
        "/api/v3/dbs/groups/info": (200, 20),
        "/api/v3/dbs/orders": (200, 20),
        "/api/v3/dbs/orders/client": (200, 20),
        "/api/v3/dbs/orders/delivery-date": (200, 20),
        "/api/v3/dbs/orders/new": (200, 20),
        "/api/v3/dbs/orders/status": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/cancel": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/confirm": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/deliver": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/meta": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/meta/gtin": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/meta/imei": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/meta/sgtin": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/meta/uin": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/receive": (1000, 5),
        "/api/v3/dbs/orders/{orderId}/reject": (1000, 5),
        "/api/v3/dbw/orders": (200, 20),
        "/api/v3/dbw/orders/courier": (200, 20),
        "/api/v3/dbw/orders/delivery-date": (200, 20),
        "/api/v3/dbw/orders/new": (200, 20),
        "/api/v3/dbw/orders/status": (200, 20),
        "/api/v3/dbw/orders/stickers": (200, 20),
        "/api/v3/dbw/orders/{orderId}/assemble": (200, 20),
        "/api/v3/dbw/orders/{orderId}/cancel": (200, 20),
        "/api/v3/dbw/orders/{orderId}/confirm": (200, 20),
        "/api/v3/dbw/orders/{orderId}/meta": (200, 20),
        "/api/v3/dbw/orders/{orderId}/meta/gtin": (60, 20),
        "/api/v3/dbw/orders/{orderId}/meta/imei": (60, 20),
        "/api/v3/dbw/orders/{orderId}/meta/sgtin": (60, 20),
        "/api/v3/dbw/orders/{orderId}/meta/uin": (60, 20),
        "/api/v3/dbw/warehouses/{warehouseId}/contacts": (200, 20),
        "/api/v3/offices": (200, 20),
        "/api/v3/orders": (200, 20),
        "/api/v3/orders/client": (200, 20),
        "/api/v3/orders/new": (200, 20),
        "/api/v3/orders/status": (200, 20),
        "/api/v3/orders/stickers": (200, 20),
        "/api/v3/orders/stickers/cross-border": (200, 20),
        "/api/v3/orders/{orderId}/cancel": (600, 20),
        "/api/v3/orders/{orderId}/meta": (200, 20),
        "/api/v3/orders/{orderId}/meta/expiration": (60, 20),
        "/api/v3/orders/{orderId}/meta/gtin": (60, 20),
        "/api/v3/orders/{orderId}/meta/imei": (60, 20),
        "/api/v3/orders/{orderId}/meta/sgtin": (60, 20),
        "/api/v3/orders/{orderId}/meta/uin": (60, 20),
        "/api/v3/passes": (200, 20),
        "/api/v3/passes/offices": (200, 20),
        "/api/v3/passes/{passId}": (200, 20),
        "/api/v3/stocks/{warehouseId}": (200, 20),
        "/api/v3/supplies": (200, 20),
        "/api/v3/supplies/orders/reshipment": (200, 20),
        "/api/v3/supplies/{supplyId}": (200, 20),
        "/api/v3/supplies/{supplyId}/barcode": (200, 20),
        "/api/v3/supplies/{supplyId}/deliver": (200, 20),
        "/api/v3/supplies/{supplyId}/trbx": (200, 20),
        "/api/v3/supplies/{supplyId}/trbx/stickers": (200, 20),
        "/api/v3/warehouses": (200, 20),
        "/api/v3/warehouses/{warehouseId}": (200, 20),
    },
    "https://seller-analytics-api.wildberries.ru": {
        "/api/analytics/v1/deductions": (60000, 1),
        "/api/analytics/v1/measurement-penalties": (60000, 1),
        "/api/analytics/v1/warehouse-measurements": (60000, 1),
        "/api/analytics/v3/sales-funnel/grouped/history": (20000, 3),
        "/api/analytics/v3/sales-funnel/products": (20000, 3),
        "/api/analytics/v3/sales-funnel/products/history": (20000, 3),
        "/api/v1/acceptance_report": (60000, 1),
        "/api/v1/acceptance_report/tasks/{task_id}/download": (60000, 1),
        "/api/v1/acceptance_report/tasks/{task_id}/status": (5000, 1),
        "/api/v1/analytics/antifraud-details": (600000, 10),
        "/api/v1/analytics/banned-products/blocked": (10000, 6),
        "/api/v1/analytics/banned-products/shadowed": (10000, 6),
        "/api/v1/analytics/brand-share": (5000, 20),
        "/api/v1/analytics/brand-share/brands": (60000, 10),
        "/api/v1/analytics/brand-share/parent-subjects": (5000, 20),
        "/api/v1/analytics/excise-report": (1800000, 10),
        "/api/v1/analytics/goods-labeling": (60000, 10),
        "/api/v1/analytics/goods-return": (60000, 10),
        "/api/v1/analytics/region-sale": (10000, 5),
        "/api/v1/paid_storage": (60000, 5),
        "/api/v1/paid_storage/tasks/{task_id}/download": (60000, 1),
        "/api/v1/paid_storage/tasks/{task_id}/status": (5000, 5),
        "/api/v1/warehouse_remains": (60000, 5),
        "/api/v1/warehouse_remains/tasks/{task_id}/download": (60000, 1),
        "/api/v1/warehouse_remains/tasks/{task_id}/status": (5000, 5),
        "/api/v2/nm-report/downloads": (20000, 3),
        "/api/v2/nm-report/downloads/file/{downloadId}": (20000, 3),
        "/api/v2/nm-report/downloads/retry": (20000, 3),
        "/api/v2/search-report/product/orders": (20000, 3),
        "/api/v2/search-report/product/search-texts": (20000, 3),
        "/api/v2/search-report/report": (20000, 3),
        "/api/v2/search-report/table/details": (20000, 3),
        "/api/v2/search-report/table/groups": (20000, 3),
        "/api/v2/stocks-report/offices": (20000, 3),
        "/api/v2/stocks-report/products/groups": (20000, 3),
        "/api/v2/stocks-report/products/products": (20000, 3),
        "/api/v2/stocks-report/products/sizes": (20000, 3),
    },
    "https://content-api.wildberries.ru": {
        "/api/content/v1/brands": (1000, 5),
        "/content/v2/barcodes": (600, 5),
        "/content/v2/cards/delete/trash": (20000, 5),
        "/content/v2/cards/error/list": (6000, 5),
        "/content/v2/cards/limits": (600, 5),
        "/content/v2/cards/moveNm": (600, 5),
        "/content/v2/cards/recover": (20000, 5),
        "/content/v2/cards/update": (6000, 5),
        "/content/v2/cards/upload": (6000, 5),
        "/content/v2/cards/upload/add": (6000, 5),
        "/content/v2/directory/colors": (600, 5),
        "/content/v2/directory/countries": (600, 5),
        "/content/v2/directory/kinds": (600, 5),
        "/content/v2/directory/seasons": (600, 5),
        "/content/v2/directory/tnved": (600, 5),
        "/content/v2/directory/vat": (600, 5),
        "/content/v2/get/cards/list": (600, 5),
        "/content/v2/get/cards/trash": (600, 5),
        "/content/v2/object/all": (600, 5),
        "/content/v2/object/charcs/{subjectId}": (600, 5),
        "/content/v2/object/parent/all": (600, 5),
        "/content/v2/tag": (600, 5),
        "/content/v2/tag/nomenclature/link": (600, 5),
        "/content/v2/tag/{id}": (600, 5),
        "/content/v2/tags": (600, 5),
        "/content/v3/media/file": (600, 5),
        "/content/v3/media/save": (600, 5),
    },
    "https://advert-api.wildberries.ru": {
        "/adv/v0/auction/nms": (1000, 1),
        "/adv/v0/auction/placements": (1000, 1),
        "/adv/v0/delete": (200, 5),
        "/adv/v0/normquery/list": (200, 10),
        "/adv/v0/pause": (200, 5),
        "/adv/v0/rename": (200, 5),
        "/adv/v0/start": (200, 5),
        "/adv/v0/stop": (200, 5),
        "/adv/v1/balance": (1000, 5),
        "/adv/v1/budget": (250, 4),
        "/adv/v1/budget/deposit": (1000, 5),
        "/adv/v1/normquery/stats": (6000, 20),
        "/adv/v1/payments": (1000, 5),
        "/adv/v1/promotion/count": (200, 5),
        "/adv/v1/supplier/subjects": (12000, 5),
        "/adv/v1/upd": (1000, 5),
        "/adv/v2/seacat/save-ad": (12000, 5),
        "/adv/v2/supplier/nms": (12000, 5),
        "/adv/v3/fullstats": (20000, 1),
        "/api/advert/v0/bids/recommendations": (12000, 5),
        "/api/advert/v1/bids": (200, 5),
        "/api/advert/v1/bids/min": (3000, 5),
        "/api/advert/v2/adverts": (200, 5),
    },
    "https://feedbacks-api.wildberries.ru": {
        "/api/feedbacks/v1/pins": (333, 6),
        "/api/feedbacks/v1/pins/count": (333, 6),
        "/api/feedbacks/v1/pins/limits": (333, 6),
        "/api/v1/feedback": (333, 6),
        "/api/v1/feedbacks": (333, 6),
        "/api/v1/feedbacks/answer": (333, 6),
        "/api/v1/feedbacks/archive": (333, 6),
        "/api/v1/feedbacks/count": (333, 6),
        "/api/v1/feedbacks/count-unanswered": (333, 6),
        "/api/v1/feedbacks/order/return": (333, 6),
        "/api/v1/new-feedbacks-questions": (333, 6),
        "/api/v1/question": (333, 6),
        "/api/v1/questions": (333, 6),
        "/api/v1/questions/count": (333, 6),
        "/api/v1/questions/count-unanswered": (333, 6),
    },
    "https://discounts-prices-api.wildberries.ru": {
        "/api/v2/buffer/goods/task": (600, 5),
        "/api/v2/buffer/tasks": (600, 5),
        "/api/v2/history/goods/task": (600, 5),
        "/api/v2/history/tasks": (600, 5),
        "/api/v2/list/goods/filter": (600, 5),
        "/api/v2/list/goods/size/nm": (600, 5),
        "/api/v2/quarantine/goods": (600, 5),
        "/api/v2/upload/task": (600, 5),
        "/api/v2/upload/task/club-discount": (600, 5),
        "/api/v2/upload/task/size": (600, 5),
    },
    "https://common-api.wildberries.ru": {
        "/api/communications/v2/news": (60000, 10),
        "/api/tariffs/v1/acceptance/coefficients": (10000, 6),
        "/api/v1/seller-info": (60000, 10),
        "/api/v1/tariffs/box": (1000, 5),
        "/api/v1/tariffs/commission": (60000, 2),
        "/api/v1/tariffs/pallet": (1000, 5),
        "/api/v1/tariffs/return": (1000, 5),
        "/ping": (1000, 5),
    },
    "https://supplies-api.wildberries.ru": {
        "/api/v1/acceptance/options": (10000, 6),
        "/api/v1/supplies": (2000, 10),
        "/api/v1/supplies/{ID}": (2000, 10),
        "/api/v1/supplies/{ID}/goods": (2000, 10),
        "/api/v1/supplies/{ID}/package": (2000, 10),
        "/api/v1/transit-tariffs": (10000, 10),
        "/api/v1/warehouses": (10000, 6),
    },
    "https://advert-media-api.wildberries.ru": {
        "/adv/v1/advert": (100, 10),
        "/adv/v1/adverts": (100, 10),
        "/adv/v1/count": (100, 10),
        "/adv/v1/stats": (100, 10),
    },
    "https://documents-api.wildberries.ru": {
        "/api/v1/documents/categories": (10000, 5),
        "/api/v1/documents/download": (10000, 5),
        "/api/v1/documents/download/all": (300000, 5),
        "/api/v1/documents/list": (10000, 5),
    },
    "https://dp-calendar-api.wildberries.ru": {
        "/api/v1/calendar/promotions": (600, 5),
        "/api/v1/calendar/promotions/details": (600, 5),
        "/api/v1/calendar/promotions/nomenclatures": (600, 5),
        "/api/v1/calendar/promotions/upload": (600, 5),
    },
    "https://statistics-api.wildberries.ru": {
        "/api/v1/supplier/orders": (60000, 1),
        "/api/v1/supplier/sales": (60000, 1),
        "/api/v1/supplier/stocks": (60000, 1),
        "/api/v5/supplier/reportDetailByPeriod": (60000, 1),
    },
    "https://user-management-api.wildberries.ru": {
        "/api/v1/invite": (1000, 5),
        "/api/v1/user": (1000, 10),
        "/api/v1/users": (1000, 5),
        "/api/v1/users/access": (1000, 5),
    },
    "https://finance-api.wildberries.ru": {
        "/api/finance/v1/sales-reports/detailed": (60000, 1),
        "/api/v1/account/balance": (60000, 1),
    },
    "https://returns-api.wildberries.ru": {
        "/api/v1/claim": (3000, 10),
        "/api/v1/claims": (3000, 10),
    },
}

# --- END GENERATED ---


@lru_cache(maxsize=1)
def _path_index() -> dict[str, str]:
    return {path: host for host, paths in ENDPOINTS.items() for path in paths}


@lru_cache(maxsize=1)
def _rate_index() -> dict[str, tuple[int, int]]:
    return {path: rate for paths in ENDPOINTS.values() for path, rate in paths.items()}


@lru_cache(maxsize=1)
def _known_hosts() -> frozenset[str]:
    hosts = {urlparse(host).netloc for host in ENDPOINTS}
    return frozenset(hosts | PUBLIC_HOSTS)


@lru_cache(maxsize=1)
def _templates() -> tuple[tuple[str, tuple[str, ...]], ...]:
    """Every templated path, pre-split, longest first."""
    templated = [p for p in _path_index() if "{" in p]
    templated.sort(key=lambda p: -p.count("/"))
    return tuple((p, tuple(p.strip("/").split("/"))) for p in templated)


@lru_cache(maxsize=2048)
def _match_template(path: str) -> str | None:
    """Map a concrete path back to its template.

    Callers interpolate ids themselves (``f"/api/v3/orders/{order_id}/cancel"``),
    but the host and rate limit are registered under the template
    (``/api/v3/orders/{orderId}/cancel``). Recovering the template keeps each
    endpoint on its own quota instead of falling back to its parent's.
    """
    if "{" in path:
        return path if path in _path_index() else None

    segments = path.strip("/").split("/")
    for template, parts in _templates():
        if len(parts) != len(segments):
            continue
        if all(
            expected.startswith("{") or expected == actual
            for expected, actual in zip(parts, segments, strict=True)
        ):
            return template
    return None


@lru_cache(maxsize=2048)
def _host_for(path: str) -> str | None:
    """Exact match, then template match, then longest-prefix lookup."""
    index = _path_index()
    host = index.get(path)
    if host is not None:
        return host

    template = _match_template(path)
    if template is not None:
        return index[template]

    parts = path.rstrip("/").split("/")
    for i in range(len(parts) - 1, 0, -1):
        host = index.get("/".join(parts[:i]))
        if host is not None:
            return host
    return None


def resolve_url(path: str) -> str:
    """Return the absolute URL for a spec path or a full URL.

    Args:
        path: Either a spec path (``/api/v3/supplies``) or a complete URL on a
            known Wildberries host.

    Returns:
        The absolute URL to request.

    Raises:
        WBConfigurationError: The URL points at an unrecognised host, or the
            path is not in the table and cannot be resolved to a host.
    """
    if path.startswith(("https://", "http://")):
        host = urlparse(path).netloc
        if host not in _known_hosts():
            raise WBConfigurationError(
                f"Refusing to send a request to unknown host {host!r}. Expected a wildberries.ru API host."
            )
        return path

    if not path.startswith("/"):
        raise WBConfigurationError(f"Path must start with '/' or be a full URL, got {path!r}.")

    resolved = _host_for(path)
    if resolved is None:
        raise WBConfigurationError(
            f"Unknown API path {path!r}. If Wildberries has added this endpoint "
            f"recently, pass the full URL instead, e.g. "
            f"'https://content-api.wildberries.ru{path}'. "
            f"See https://dev.wildberries.ru/release-notes"
        )
    return resolved + path


def rate_limit_for(path: str) -> tuple[int, int]:
    """Return ``(interval_ms, burst)`` governing ``path``.

    Falls back to a conservative default for paths outside the table, including
    full URLs, so an unknown endpoint is throttled rather than hammered.
    """
    rates = _rate_index()
    rate = rates.get(path)
    if rate is not None:
        return rate

    template = _match_template(path)
    if template is not None:
        return rates[template]

    parts = path.rstrip("/").split("/")
    for i in range(len(parts) - 1, 0, -1):
        rate = rates.get("/".join(parts[:i]))
        if rate is not None:
            return rate
    return DEFAULT_RATE_LIMIT


def page_size_for(path: str) -> int:
    size = PAGE_SIZES.get(path)
    if size is not None:
        return size

    template = _match_template(path)
    if template is not None:
        return PAGE_SIZES.get(template, DEFAULT_PAGE_SIZE)
    return DEFAULT_PAGE_SIZE
