from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aiolimiter import AsyncLimiter


if TYPE_CHECKING:
    from .client.session.base import BaseSession

# fmt: off
# AUTO-GENERATED — DO NOT EDIT MANUALLY!!!

_PATH_TO_BASE: dict[str, str] = {
    "/adv/v0/auction/nms": "https://advert-api.wildberries.ru",
    "/adv/v0/auction/placements": "https://advert-api.wildberries.ru",
    "/adv/v0/delete": "https://advert-api.wildberries.ru",
    "/adv/v0/normquery/list": "https://advert-api.wildberries.ru",
    "/adv/v0/pause": "https://advert-api.wildberries.ru",
    "/adv/v0/rename": "https://advert-api.wildberries.ru",
    "/adv/v0/start": "https://advert-api.wildberries.ru",
    "/adv/v0/stop": "https://advert-api.wildberries.ru",
    "/adv/v1/advert": "https://advert-media-api.wildberries.ru",
    "/adv/v1/adverts": "https://advert-media-api.wildberries.ru",
    "/adv/v1/balance": "https://advert-api.wildberries.ru",
    "/adv/v1/budget": "https://advert-api.wildberries.ru",
    "/adv/v1/budget/deposit": "https://advert-api.wildberries.ru",
    "/adv/v1/count": "https://advert-media-api.wildberries.ru",
    "/adv/v1/normquery/stats": "https://advert-api.wildberries.ru",
    "/adv/v1/payments": "https://advert-api.wildberries.ru",
    "/adv/v1/promotion/count": "https://advert-api.wildberries.ru",
    "/adv/v1/stats": "https://advert-media-api.wildberries.ru",
    "/adv/v1/supplier/subjects": "https://advert-api.wildberries.ru",
    "/adv/v1/upd": "https://advert-api.wildberries.ru",
    "/adv/v2/seacat/save-ad": "https://advert-api.wildberries.ru",
    "/adv/v2/supplier/nms": "https://advert-api.wildberries.ru",
    "/adv/v3/fullstats": "https://advert-api.wildberries.ru",
    "/api/advert/v0/bids/recommendations": "https://advert-api.wildberries.ru",
    "/api/advert/v1/bids": "https://advert-api.wildberries.ru",
    "/api/advert/v1/bids/min": "https://advert-api.wildberries.ru",
    "/api/advert/v2/adverts": "https://advert-api.wildberries.ru",
    "/api/analytics/v1/deductions": "https://seller-analytics-api.wildberries.ru",
    "/api/analytics/v1/measurement-penalties": "https://seller-analytics-api.wildberries.ru",
    "/api/analytics/v1/warehouse-measurements": "https://seller-analytics-api.wildberries.ru",
    "/api/analytics/v3/sales-funnel/grouped/history": "https://seller-analytics-api.wildberries.ru",
    "/api/analytics/v3/sales-funnel/products": "https://seller-analytics-api.wildberries.ru",
    "/api/analytics/v3/sales-funnel/products/history": "https://seller-analytics-api.wildberries.ru",
    "/api/communications/v2/news": "https://common-api.wildberries.ru",
    "/api/content/v1/brands": "https://content-api.wildberries.ru",
    "/api/feedbacks/v1/pins": "https://feedbacks-api.wildberries.ru",
    "/api/feedbacks/v1/pins/count": "https://feedbacks-api.wildberries.ru",
    "/api/feedbacks/v1/pins/limits": "https://feedbacks-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/b2b/info": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/meta/customs-declaration": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/meta/delete": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/meta/gtin": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/meta/imei": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/meta/info": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/meta/sgtin": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/meta/uin": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/status/cancel": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/status/confirm": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/status/deliver": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/status/info": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/status/receive": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/status/reject": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbs/orders/stickers": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/dbw/orders/client": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/orders/meta": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/orders/{orderId}/meta/customs-declaration": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/supplies/{supplyId}/order-ids": "https://marketplace-api.wildberries.ru",
    "/api/marketplace/v3/supplies/{supplyId}/orders": "https://marketplace-api.wildberries.ru",
    "/api/tariffs/v1/acceptance/coefficients": "https://common-api.wildberries.ru",
    "/api/v1/acceptance/options": "https://supplies-api.wildberries.ru",
    "/api/v1/acceptance_report": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/acceptance_report/tasks/{task_id}/download": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/acceptance_report/tasks/{task_id}/status": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/account/balance": "https://finance-api.wildberries.ru",
    "/api/v1/analytics/antifraud-details": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/banned-products/blocked": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/banned-products/shadowed": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/brand-share": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/brand-share/brands": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/brand-share/parent-subjects": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/excise-report": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/goods-labeling": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/goods-return": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/analytics/region-sale": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/calendar/promotions": "https://dp-calendar-api.wildberries.ru",
    "/api/v1/calendar/promotions/details": "https://dp-calendar-api.wildberries.ru",
    "/api/v1/calendar/promotions/nomenclatures": "https://dp-calendar-api.wildberries.ru",
    "/api/v1/calendar/promotions/upload": "https://dp-calendar-api.wildberries.ru",
    "/api/v1/claim": "https://returns-api.wildberries.ru",
    "/api/v1/claims": "https://returns-api.wildberries.ru",
    "/api/v1/documents/categories": "https://documents-api.wildberries.ru",
    "/api/v1/documents/download": "https://documents-api.wildberries.ru",
    "/api/v1/documents/download/all": "https://documents-api.wildberries.ru",
    "/api/v1/documents/list": "https://documents-api.wildberries.ru",
    "/api/v1/feedback": "https://feedbacks-api.wildberries.ru",
    "/api/v1/feedbacks": "https://feedbacks-api.wildberries.ru",
    "/api/v1/feedbacks/answer": "https://feedbacks-api.wildberries.ru",
    "/api/v1/feedbacks/archive": "https://feedbacks-api.wildberries.ru",
    "/api/v1/feedbacks/count": "https://feedbacks-api.wildberries.ru",
    "/api/v1/feedbacks/count-unanswered": "https://feedbacks-api.wildberries.ru",
    "/api/v1/feedbacks/order/return": "https://feedbacks-api.wildberries.ru",
    "/api/v1/invite": "https://user-management-api.wildberries.ru",
    "/api/v1/new-feedbacks-questions": "https://feedbacks-api.wildberries.ru",
    "/api/v1/paid_storage": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/paid_storage/tasks/{task_id}/download": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/paid_storage/tasks/{task_id}/status": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/question": "https://feedbacks-api.wildberries.ru",
    "/api/v1/questions": "https://feedbacks-api.wildberries.ru",
    "/api/v1/questions/count": "https://feedbacks-api.wildberries.ru",
    "/api/v1/questions/count-unanswered": "https://feedbacks-api.wildberries.ru",
    "/api/v1/seller-info": "https://common-api.wildberries.ru",
    "/api/v1/supplier/orders": "https://statistics-api.wildberries.ru",
    "/api/v1/supplier/sales": "https://statistics-api.wildberries.ru",
    "/api/v1/supplier/stocks": "https://statistics-api.wildberries.ru",
    "/api/v1/supplies": "https://supplies-api.wildberries.ru",
    "/api/v1/supplies/{ID}": "https://supplies-api.wildberries.ru",
    "/api/v1/supplies/{ID}/goods": "https://supplies-api.wildberries.ru",
    "/api/v1/supplies/{ID}/package": "https://supplies-api.wildberries.ru",
    "/api/v1/tariffs/box": "https://common-api.wildberries.ru",
    "/api/v1/tariffs/commission": "https://common-api.wildberries.ru",
    "/api/v1/tariffs/pallet": "https://common-api.wildberries.ru",
    "/api/v1/tariffs/return": "https://common-api.wildberries.ru",
    "/api/v1/transit-tariffs": "https://supplies-api.wildberries.ru",
    "/api/v1/user": "https://user-management-api.wildberries.ru",
    "/api/v1/users": "https://user-management-api.wildberries.ru",
    "/api/v1/users/access": "https://user-management-api.wildberries.ru",
    "/api/v1/warehouse_remains": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/warehouse_remains/tasks/{task_id}/download": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/warehouse_remains/tasks/{task_id}/status": "https://seller-analytics-api.wildberries.ru",
    "/api/v1/warehouses": "https://supplies-api.wildberries.ru",
    "/api/v2/buffer/goods/task": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/buffer/tasks": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/history/goods/task": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/history/tasks": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/list/goods/filter": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/list/goods/size/nm": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/nm-report/downloads": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/nm-report/downloads/file/{downloadId}": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/nm-report/downloads/retry": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/quarantine/goods": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/search-report/product/orders": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/search-report/product/search-texts": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/search-report/report": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/search-report/table/details": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/search-report/table/groups": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/stocks-report/offices": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/stocks-report/products/groups": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/stocks-report/products/products": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/stocks-report/products/sizes": "https://seller-analytics-api.wildberries.ru",
    "/api/v2/upload/task": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/upload/task/club-discount": "https://discounts-prices-api.wildberries.ru",
    "/api/v2/upload/task/size": "https://discounts-prices-api.wildberries.ru",
    "/api/v3/dbs/groups/info": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/client": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/delivery-date": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/new": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/status": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/cancel": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/confirm": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/deliver": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/meta": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/meta/gtin": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/meta/imei": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/meta/sgtin": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/meta/uin": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/receive": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbs/orders/{orderId}/reject": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/courier": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/delivery-date": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/new": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/status": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/stickers": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/{orderId}/assemble": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/{orderId}/cancel": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/{orderId}/confirm": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/{orderId}/meta": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/{orderId}/meta/gtin": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/{orderId}/meta/imei": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/{orderId}/meta/sgtin": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/orders/{orderId}/meta/uin": "https://marketplace-api.wildberries.ru",
    "/api/v3/dbw/warehouses/{warehouseId}/contacts": "https://marketplace-api.wildberries.ru",
    "/api/v3/offices": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/client": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/new": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/status": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/stickers": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/stickers/cross-border": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/{orderId}/cancel": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/{orderId}/meta": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/{orderId}/meta/expiration": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/{orderId}/meta/gtin": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/{orderId}/meta/imei": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/{orderId}/meta/sgtin": "https://marketplace-api.wildberries.ru",
    "/api/v3/orders/{orderId}/meta/uin": "https://marketplace-api.wildberries.ru",
    "/api/v3/passes": "https://marketplace-api.wildberries.ru",
    "/api/v3/passes/offices": "https://marketplace-api.wildberries.ru",
    "/api/v3/passes/{passId}": "https://marketplace-api.wildberries.ru",
    "/api/v3/stocks/{warehouseId}": "https://marketplace-api.wildberries.ru",
    "/api/v3/supplies": "https://marketplace-api.wildberries.ru",
    "/api/v3/supplies/orders/reshipment": "https://marketplace-api.wildberries.ru",
    "/api/v3/supplies/{supplyId}": "https://marketplace-api.wildberries.ru",
    "/api/v3/supplies/{supplyId}/barcode": "https://marketplace-api.wildberries.ru",
    "/api/v3/supplies/{supplyId}/deliver": "https://marketplace-api.wildberries.ru",
    "/api/v3/supplies/{supplyId}/trbx": "https://marketplace-api.wildberries.ru",
    "/api/v3/supplies/{supplyId}/trbx/stickers": "https://marketplace-api.wildberries.ru",
    "/api/v3/warehouses": "https://marketplace-api.wildberries.ru",
    "/api/v3/warehouses/{warehouseId}": "https://marketplace-api.wildberries.ru",
    "/api/v5/supplier/reportDetailByPeriod": "https://statistics-api.wildberries.ru",
    "/content/v2/barcodes": "https://content-api.wildberries.ru",
    "/content/v2/cards/delete/trash": "https://content-api.wildberries.ru",
    "/content/v2/cards/error/list": "https://content-api.wildberries.ru",
    "/content/v2/cards/limits": "https://content-api.wildberries.ru",
    "/content/v2/cards/moveNm": "https://content-api.wildberries.ru",
    "/content/v2/cards/recover": "https://content-api.wildberries.ru",
    "/content/v2/cards/update": "https://content-api.wildberries.ru",
    "/content/v2/cards/upload": "https://content-api.wildberries.ru",
    "/content/v2/cards/upload/add": "https://content-api.wildberries.ru",
    "/content/v2/directory/colors": "https://content-api.wildberries.ru",
    "/content/v2/directory/countries": "https://content-api.wildberries.ru",
    "/content/v2/directory/kinds": "https://content-api.wildberries.ru",
    "/content/v2/directory/seasons": "https://content-api.wildberries.ru",
    "/content/v2/directory/tnved": "https://content-api.wildberries.ru",
    "/content/v2/directory/vat": "https://content-api.wildberries.ru",
    "/content/v2/get/cards/list": "https://content-api.wildberries.ru",
    "/content/v2/get/cards/trash": "https://content-api.wildberries.ru",
    "/content/v2/object/all": "https://content-api.wildberries.ru",
    "/content/v2/object/charcs/{subjectId}": "https://content-api.wildberries.ru",
    "/content/v2/object/parent/all": "https://content-api.wildberries.ru",
    "/content/v2/tag": "https://content-api.wildberries.ru",
    "/content/v2/tag/nomenclature/link": "https://content-api.wildberries.ru",
    "/content/v2/tag/{id}": "https://content-api.wildberries.ru",
    "/content/v2/tags": "https://content-api.wildberries.ru",
    "/content/v3/media/file": "https://content-api.wildberries.ru",
    "/content/v3/media/save": "https://content-api.wildberries.ru",
    "/ping": "https://common-api.wildberries.ru",
}

# (period_ms, limit, interval_ms, burst)
_PATH_TO_LIMIT: dict[str, tuple[int, int, int, int]] = {
    "/adv/v0/auction/nms": (1000, 1, 1000, 1),
    "/adv/v0/auction/placements": (1000, 1, 1000, 1),
    "/adv/v0/delete": (1000, 5, 200, 5),
    "/adv/v0/normquery/list": (1000, 5, 200, 10),
    "/adv/v0/pause": (1000, 5, 200, 5),
    "/adv/v0/rename": (1000, 5, 200, 5),
    "/adv/v0/start": (1000, 5, 200, 5),
    "/adv/v0/stop": (1000, 5, 200, 5),
    "/adv/v1/advert": (1000, 10, 100, 10),
    "/adv/v1/adverts": (1000, 10, 100, 10),
    "/adv/v1/balance": (1000, 1, 1000, 5),
    "/adv/v1/budget": (1000, 4, 250, 4),
    "/adv/v1/budget/deposit": (1000, 1, 1000, 5),
    "/adv/v1/count": (1000, 10, 100, 10),
    "/adv/v1/normquery/stats": (60000, 10, 6000, 20),
    "/adv/v1/payments": (1000, 1, 1000, 5),
    "/adv/v1/promotion/count": (1000, 5, 200, 5),
    "/adv/v1/stats": (1000, 10, 100, 10),
    "/adv/v1/supplier/subjects": (12000, 1, 12000, 5),
    "/adv/v1/upd": (1000, 1, 1000, 5),
    "/adv/v2/seacat/save-ad": (60000, 5, 12000, 5),
    "/adv/v2/supplier/nms": (60000, 5, 12000, 5),
    "/adv/v3/fullstats": (60000, 3, 20000, 1),
    "/api/advert/v0/bids/recommendations": (60000, 5, 12000, 5),
    "/api/advert/v1/bids": (1000, 5, 200, 5),
    "/api/advert/v1/bids/min": (60000, 20, 3000, 5),
    "/api/advert/v2/adverts": (1000, 5, 200, 5),
    "/api/analytics/v1/deductions": (60000, 1, 60000, 1),
    "/api/analytics/v1/measurement-penalties": (60000, 1, 60000, 1),
    "/api/analytics/v1/warehouse-measurements": (60000, 1, 60000, 1),
    "/api/analytics/v3/sales-funnel/grouped/history": (60000, 3, 20000, 3),
    "/api/analytics/v3/sales-funnel/products": (60000, 3, 20000, 3),
    "/api/analytics/v3/sales-funnel/products/history": (60000, 3, 20000, 3),
    "/api/communications/v2/news": (60000, 1, 60000, 10),
    "/api/content/v1/brands": (1000, 1, 1000, 5),
    "/api/feedbacks/v1/pins": (1000, 3, 333, 6),
    "/api/feedbacks/v1/pins/count": (1000, 3, 333, 6),
    "/api/feedbacks/v1/pins/limits": (1000, 3, 333, 6),
    "/api/marketplace/v3/dbs/orders/b2b/info": (60000, 300, 200, 20),
    "/api/marketplace/v3/dbs/orders/meta/customs-declaration": (60000, 500, 120, 20),
    "/api/marketplace/v3/dbs/orders/meta/delete": (60000, 150, 400, 20),
    "/api/marketplace/v3/dbs/orders/meta/gtin": (60000, 500, 120, 20),
    "/api/marketplace/v3/dbs/orders/meta/imei": (60000, 500, 120, 20),
    "/api/marketplace/v3/dbs/orders/meta/info": (60000, 150, 400, 20),
    "/api/marketplace/v3/dbs/orders/meta/sgtin": (60000, 500, 120, 20),
    "/api/marketplace/v3/dbs/orders/meta/uin": (60000, 500, 120, 20),
    "/api/marketplace/v3/dbs/orders/status/cancel": (1000, 1, 1000, 10),
    "/api/marketplace/v3/dbs/orders/status/confirm": (1000, 1, 1000, 10),
    "/api/marketplace/v3/dbs/orders/status/deliver": (1000, 1, 1000, 10),
    "/api/marketplace/v3/dbs/orders/status/info": (60000, 300, 200, 20),
    "/api/marketplace/v3/dbs/orders/status/receive": (1000, 1, 1000, 10),
    "/api/marketplace/v3/dbs/orders/status/reject": (1000, 1, 1000, 10),
    "/api/marketplace/v3/dbs/orders/stickers": (60000, 300, 200, 20),
    "/api/marketplace/v3/dbw/orders/client": (60000, 300, 200, 20),
    "/api/marketplace/v3/orders/meta": (60000, 300, 200, 20),
    "/api/marketplace/v3/orders/{orderId}/meta/customs-declaration": (60000, 1000, 60, 20),
    "/api/marketplace/v3/supplies/{supplyId}/order-ids": (60000, 300, 200, 20),
    "/api/marketplace/v3/supplies/{supplyId}/orders": (60000, 300, 200, 20),
    "/api/tariffs/v1/acceptance/coefficients": (60000, 6, 10000, 6),
    "/api/v1/acceptance/options": (60000, 6, 10000, 6),
    "/api/v1/acceptance_report": (60000, 1, 60000, 1),
    "/api/v1/acceptance_report/tasks/{task_id}/download": (60000, 1, 60000, 1),
    "/api/v1/acceptance_report/tasks/{task_id}/status": (5000, 1, 5000, 1),
    "/api/v1/account/balance": (60000, 1, 60000, 1),
    "/api/v1/analytics/antifraud-details": (600000, 1, 600000, 10),
    "/api/v1/analytics/banned-products/blocked": (10000, 1, 10000, 6),
    "/api/v1/analytics/banned-products/shadowed": (10000, 1, 10000, 6),
    "/api/v1/analytics/brand-share": (5000, 1, 5000, 20),
    "/api/v1/analytics/brand-share/brands": (60000, 1, 60000, 10),
    "/api/v1/analytics/brand-share/parent-subjects": (5000, 1, 5000, 20),
    "/api/v1/analytics/excise-report": (18000000, 10, 1800000, 10),
    "/api/v1/analytics/goods-labeling": (60000, 1, 60000, 10),
    "/api/v1/analytics/goods-return": (60000, 1, 60000, 10),
    "/api/v1/analytics/region-sale": (10000, 1, 10000, 5),
    "/api/v1/calendar/promotions": (6000, 10, 600, 5),
    "/api/v1/calendar/promotions/details": (6000, 10, 600, 5),
    "/api/v1/calendar/promotions/nomenclatures": (6000, 10, 600, 5),
    "/api/v1/calendar/promotions/upload": (6000, 10, 600, 5),
    "/api/v1/claim": (60000, 20, 3000, 10),
    "/api/v1/claims": (60000, 20, 3000, 10),
    "/api/v1/documents/categories": (10000, 1, 10000, 5),
    "/api/v1/documents/download": (10000, 1, 10000, 5),
    "/api/v1/documents/download/all": (300000, 1, 300000, 5),
    "/api/v1/documents/list": (10000, 1, 10000, 5),
    "/api/v1/feedback": (1000, 3, 333, 6),
    "/api/v1/feedbacks": (1000, 3, 333, 6),
    "/api/v1/feedbacks/answer": (1000, 3, 333, 6),
    "/api/v1/feedbacks/archive": (1000, 3, 333, 6),
    "/api/v1/feedbacks/count": (1000, 3, 333, 6),
    "/api/v1/feedbacks/count-unanswered": (1000, 3, 333, 6),
    "/api/v1/feedbacks/order/return": (1000, 3, 333, 6),
    "/api/v1/invite": (1000, 1, 1000, 5),
    "/api/v1/new-feedbacks-questions": (1000, 3, 333, 6),
    "/api/v1/paid_storage": (60000, 1, 60000, 5),
    "/api/v1/paid_storage/tasks/{task_id}/download": (60000, 1, 60000, 1),
    "/api/v1/paid_storage/tasks/{task_id}/status": (5000, 1, 5000, 5),
    "/api/v1/question": (1000, 3, 333, 6),
    "/api/v1/questions": (1000, 3, 333, 6),
    "/api/v1/questions/count": (1000, 3, 333, 6),
    "/api/v1/questions/count-unanswered": (1000, 3, 333, 6),
    "/api/v1/seller-info": (60000, 1, 60000, 10),
    "/api/v1/supplier/orders": (60000, 1, 60000, 1),
    "/api/v1/supplier/sales": (60000, 1, 60000, 1),
    "/api/v1/supplier/stocks": (60000, 1, 60000, 1),
    "/api/v1/supplies": (60000, 30, 2000, 10),
    "/api/v1/supplies/{ID}": (60000, 30, 2000, 10),
    "/api/v1/supplies/{ID}/goods": (60000, 30, 2000, 10),
    "/api/v1/supplies/{ID}/package": (60000, 30, 2000, 10),
    "/api/v1/tariffs/box": (60000, 60, 1000, 5),
    "/api/v1/tariffs/commission": (60000, 1, 60000, 2),
    "/api/v1/tariffs/pallet": (60000, 60, 1000, 5),
    "/api/v1/tariffs/return": (60000, 60, 1000, 5),
    "/api/v1/transit-tariffs": (60000, 6, 10000, 10),
    "/api/v1/user": (1000, 1, 1000, 10),
    "/api/v1/users": (1000, 1, 1000, 5),
    "/api/v1/users/access": (1000, 1, 1000, 5),
    "/api/v1/warehouse_remains": (60000, 1, 60000, 5),
    "/api/v1/warehouse_remains/tasks/{task_id}/download": (60000, 1, 60000, 1),
    "/api/v1/warehouse_remains/tasks/{task_id}/status": (5000, 1, 5000, 5),
    "/api/v1/warehouses": (60000, 6, 10000, 6),
    "/api/v2/buffer/goods/task": (6000, 10, 600, 5),
    "/api/v2/buffer/tasks": (6000, 10, 600, 5),
    "/api/v2/history/goods/task": (6000, 10, 600, 5),
    "/api/v2/history/tasks": (6000, 10, 600, 5),
    "/api/v2/list/goods/filter": (6000, 10, 600, 5),
    "/api/v2/list/goods/size/nm": (6000, 10, 600, 5),
    "/api/v2/nm-report/downloads": (60000, 3, 20000, 3),
    "/api/v2/nm-report/downloads/file/{downloadId}": (60000, 3, 20000, 3),
    "/api/v2/nm-report/downloads/retry": (60000, 3, 20000, 3),
    "/api/v2/quarantine/goods": (6000, 10, 600, 5),
    "/api/v2/search-report/product/orders": (60000, 3, 20000, 3),
    "/api/v2/search-report/product/search-texts": (60000, 3, 20000, 3),
    "/api/v2/search-report/report": (60000, 3, 20000, 3),
    "/api/v2/search-report/table/details": (60000, 3, 20000, 3),
    "/api/v2/search-report/table/groups": (60000, 3, 20000, 3),
    "/api/v2/stocks-report/offices": (60000, 3, 20000, 3),
    "/api/v2/stocks-report/products/groups": (60000, 3, 20000, 3),
    "/api/v2/stocks-report/products/products": (60000, 3, 20000, 3),
    "/api/v2/stocks-report/products/sizes": (60000, 3, 20000, 3),
    "/api/v2/upload/task": (6000, 10, 600, 5),
    "/api/v2/upload/task/club-discount": (6000, 10, 600, 5),
    "/api/v2/upload/task/size": (6000, 10, 600, 5),
    "/api/v3/dbs/groups/info": (60000, 300, 200, 20),
    "/api/v3/dbs/orders": (60000, 300, 200, 20),
    "/api/v3/dbs/orders/client": (60000, 300, 200, 20),
    "/api/v3/dbs/orders/delivery-date": (60000, 300, 200, 20),
    "/api/v3/dbs/orders/new": (60000, 300, 200, 20),
    "/api/v3/dbw/orders": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/courier": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/delivery-date": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/new": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/status": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/stickers": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/{orderId}/assemble": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/{orderId}/cancel": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/{orderId}/confirm": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/{orderId}/meta": (60000, 300, 200, 20),
    "/api/v3/dbw/orders/{orderId}/meta/gtin": (60000, 1000, 60, 20),
    "/api/v3/dbw/orders/{orderId}/meta/imei": (60000, 1000, 60, 20),
    "/api/v3/dbw/orders/{orderId}/meta/sgtin": (60000, 1000, 60, 20),
    "/api/v3/dbw/orders/{orderId}/meta/uin": (60000, 1000, 60, 20),
    "/api/v3/dbw/warehouses/{warehouseId}/contacts": (60000, 300, 200, 20),
    "/api/v3/offices": (60000, 300, 200, 20),
    "/api/v3/orders": (60000, 300, 200, 20),
    "/api/v3/orders/client": (60000, 300, 200, 20),
    "/api/v3/orders/new": (60000, 300, 200, 20),
    "/api/v3/orders/status": (60000, 300, 200, 20),
    "/api/v3/orders/stickers": (60000, 300, 200, 20),
    "/api/v3/orders/stickers/cross-border": (60000, 300, 200, 20),
    "/api/v3/orders/{orderId}/cancel": (60000, 100, 600, 20),
    "/api/v3/orders/{orderId}/meta": (60000, 300, 200, 20),
    "/api/v3/orders/{orderId}/meta/expiration": (60000, 1000, 60, 20),
    "/api/v3/orders/{orderId}/meta/gtin": (60000, 1000, 60, 20),
    "/api/v3/orders/{orderId}/meta/imei": (60000, 1000, 60, 20),
    "/api/v3/orders/{orderId}/meta/sgtin": (60000, 1000, 60, 20),
    "/api/v3/orders/{orderId}/meta/uin": (60000, 1000, 60, 20),
    "/api/v3/passes": (60000, 300, 200, 20),
    "/api/v3/passes/offices": (60000, 300, 200, 20),
    "/api/v3/passes/{passId}": (60000, 300, 200, 20),
    "/api/v3/stocks/{warehouseId}": (60000, 300, 200, 20),
    "/api/v3/supplies": (60000, 300, 200, 20),
    "/api/v3/supplies/orders/reshipment": (60000, 300, 200, 20),
    "/api/v3/supplies/{supplyId}": (60000, 300, 200, 20),
    "/api/v3/supplies/{supplyId}/barcode": (60000, 300, 200, 20),
    "/api/v3/supplies/{supplyId}/deliver": (60000, 300, 200, 20),
    "/api/v3/supplies/{supplyId}/trbx": (60000, 300, 200, 20),
    "/api/v3/supplies/{supplyId}/trbx/stickers": (60000, 300, 200, 20),
    "/api/v3/warehouses": (60000, 300, 200, 20),
    "/api/v3/warehouses/{warehouseId}": (60000, 300, 200, 20),
    "/api/v5/supplier/reportDetailByPeriod": (60000, 1, 60000, 1),
    "/content/v2/barcodes": (60000, 100, 600, 5),
    "/content/v2/cards/delete/trash": (60000, 3, 20000, 5),
    "/content/v2/cards/error/list": (60000, 10, 6000, 5),
    "/content/v2/cards/limits": (60000, 100, 600, 5),
    "/content/v2/cards/moveNm": (60000, 100, 600, 5),
    "/content/v2/cards/recover": (60000, 3, 20000, 5),
    "/content/v2/cards/update": (60000, 10, 6000, 5),
    "/content/v2/cards/upload": (60000, 10, 6000, 5),
    "/content/v2/cards/upload/add": (60000, 10, 6000, 5),
    "/content/v2/directory/colors": (60000, 100, 600, 5),
    "/content/v2/directory/countries": (60000, 100, 600, 5),
    "/content/v2/directory/kinds": (60000, 100, 600, 5),
    "/content/v2/directory/seasons": (60000, 100, 600, 5),
    "/content/v2/directory/tnved": (60000, 100, 600, 5),
    "/content/v2/directory/vat": (60000, 100, 600, 5),
    "/content/v2/get/cards/list": (60000, 100, 600, 5),
    "/content/v2/get/cards/trash": (60000, 100, 600, 5),
    "/content/v2/object/all": (60000, 100, 600, 5),
    "/content/v2/object/charcs/{subjectId}": (60000, 100, 600, 5),
    "/content/v2/object/parent/all": (60000, 100, 600, 5),
    "/content/v2/tag": (60000, 100, 600, 5),
    "/content/v2/tag/nomenclature/link": (60000, 100, 600, 5),
    "/content/v2/tag/{id}": (60000, 100, 600, 5),
    "/content/v2/tags": (60000, 100, 600, 5),
    "/content/v3/media/file": (60000, 100, 600, 5),
    "/content/v3/media/save": (60000, 100, 600, 5),
}
# fmt: on

_DEFAULT_LIMIT: tuple[int, int, int, int] = (60000, 60, 1000, 5)

# Shared AsyncLimiter instances keyed by (interval_ms, burst).
_limiters: dict[tuple[int, int], AsyncLimiter] = {}


def _get_limiter(path: str) -> AsyncLimiter:
    period_ms, limit, interval_ms, burst = _PATH_TO_LIMIT.get(path, _DEFAULT_LIMIT)
    key = (interval_ms, burst)
    if key not in _limiters:
        _limiters[key] = AsyncLimiter(max_rate=burst, time_period=interval_ms / 1000)
    return _limiters[key]


def resolve_url(path: str) -> str:
    """Resolve full URL for a spec path like /api/v3/supplies."""
    base = _PATH_TO_BASE.get(path)
    if base:
        return base + path
    # Path may contain dynamic segments (e.g. /api/v3/supplies/WB-123/orders).
    # Walk up the path until we find a match.
    parts = path.rstrip("/").split("/")
    for i in range(len(parts) - 1, 0, -1):
        candidate = "/".join(parts[:i])
        if candidate in _PATH_TO_BASE:
            return _PATH_TO_BASE[candidate] + path
    from .exceptions import WbAPIError

    raise WbAPIError(detail=f"Unknown path {path!r}. Check available paths at https://dev.wildberries.ru")


_PAGE_SIZE = 1000


def _extract_list(raw: Any) -> list[Any] | None:
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        for v in raw.values():
            if isinstance(v, list):
                return v
    return None


class MethodDispatcher:
    def __init__(self, session: BaseSession, token: str) -> None:
        self._session = session
        self._token = token

    async def dispatch(
        self,
        http_method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
        unofficial: bool = False,
    ) -> Any:
        if not unofficial:
            self._session.headers.set_token(self._token)
        url = resolve_url(path)
        limiter = _get_limiter(path)
        return await self._session._request(http_method, url, params=params, json=json, limit=limiter)

    async def fetch_all(self, path: str, **kwargs: Any) -> list[Any]:
        """Fetch all pages. Accepts an optional ``paginator`` kwarg —
        a callable ``(response) -> (items, next_params | None)`` for custom pagination logic.

        Example::

            def my_paginator(raw):
                items = raw.get("result", [])
                cursor = raw.get("cursor") or None
                next_params = {"cursor": cursor} if cursor else None
                return items, next_params


            all_items = await api.get_all(
                "/api/v3/custom", paginator=my_paginator
            )
        """
        from .exceptions import PaginationNotSupported

        paginator = kwargs.pop("paginator", None)

        if paginator is not None:
            result: list[Any] = []
            params: dict[str, Any] = dict(kwargs)
            while True:
                raw = await self.dispatch("GET", path, params=params or None)
                items, next_params = paginator(raw)
                result.extend(items)
                if not next_params:
                    break
                params = {**kwargs, **next_params}
            return result

        raw = await self.dispatch("GET", path, params={**kwargs, "limit": _PAGE_SIZE})
        page = _extract_list(raw)

        if page is None:
            raise PaginationNotSupported(f"No list data found in response for {path!r}")

        result: list[Any] = list(page)

        # Cursor pagination
        if isinstance(raw, dict) and "next" in raw:
            cursor = raw["next"]
            while cursor:
                raw = await self.dispatch("GET", path, params={**kwargs, "limit": _PAGE_SIZE, "next": cursor})
                page = _extract_list(raw)
                if not page:
                    break
                result.extend(page)
                cursor = raw.get("next") if isinstance(raw, dict) else None
            return result

        # Offset pagination — first page was full
        if len(page) < _PAGE_SIZE:
            if not result:
                raise PaginationNotSupported(f"{path!r} returned empty first page — pagination not supported")
            return result

        offset = _PAGE_SIZE
        while True:
            raw = await self.dispatch("GET", path, params={**kwargs, "limit": _PAGE_SIZE, "offset": offset})
            page = _extract_list(raw)
            if not page:
                break
            result.extend(page)
            if len(page) < _PAGE_SIZE:
                break
            offset += _PAGE_SIZE

        return result
