# Pagination

## Usage

```python
from wbapi_async import WbAPI, paginate

async with WbAPI(token="...") as api:
    # Single request — use the method directly
    products = await api.get_products_with_prices(limit=100)

    # All pages — use paginate()
    all_products = await paginate(api.get_products_with_prices)

    # With parameters
    orders = await paginate(api.get_assembly_orders, date_from=1700000000)
    feedbacks = await paginate(api.get_feedbacks_list, is_answered=False)
```

`paginate()` returns a `list` with all items from all pages combined.
Methods that don't support pagination raise `TypeError`.

## Pagination patterns

Three patterns are detected automatically from the Wildberries OpenAPI spec:

| Pattern     | Parameters                | Used by                                |
| ----------- | ------------------------- | -------------------------------------- |
| `offset`    | `limit` + `offset`        | Products, reports, promotion, finances |
| `next`      | `limit` + `next` (cursor) | Orders FBS/DBW/DBS, in-store pickup    |
| `take_skip` | `take` + `skip`           | Communications (feedbacks, questions)  |

### offset — page size 1000

```
GET ...?limit=1000&offset=0     → 1000 items
GET ...?limit=1000&offset=1000  → 1000 items
GET ...?limit=1000&offset=2000  →   47 items → stop
```

### next (cursor) — page size 1000

```
GET ...?limit=1000&next=0       → 1000 items, next=99999
GET ...?limit=1000&next=99999   →   50 items, next=0   → stop
```

### take_skip — page size 5000

```
GET ...?take=5000&skip=0        → 5000 items
GET ...?take=5000&skip=5000     →  200 items → stop
```

## Adding a new pattern

1. Subclass `PaginationStrategy` in [src/wbapi_async/methods/pagination.py](../../src/wbapi_async/methods/pagination.py):

```python
class MyPagination(PaginationStrategy):
    page_size = 100

    def first_params(self) -> dict[str, Any]:
        return {"pageSize": self.page_size, "page": 1}

    def next_params(self, current_params, response, page) -> dict | None:
        if len(page) < self.page_size:
            return None
        return {"pageSize": self.page_size, "page": current_params["page"] + 1}
```

2. Register in `PAGINATION_STRATEGIES`:

```python
PAGINATION_STRATEGIES["my_pattern"] = MyPagination()
```

3. Add detection in `detect_pagination()` in [wbapi-codegen](https://github.com/serdukow/wbapi-codegen):

```python
if "pageSize" in aliases and "page" in aliases:
    return "my_pattern"
```
