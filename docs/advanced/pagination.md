# Pagination

## Auto-pagination

`get_all()` fetches all pages automatically. Pagination style is detected from the first response:

- **cursor** — response has a `next` field with non-zero value
- **offset** — first page is full (1000 items)

```python
async with WbAPI(token="...") as api:
    supplies = await api.get_all("/api/v3/supplies")
    orders = await api.get_all("/api/v3/orders/new")
```

Raises `PaginationNotSupported` if the endpoint doesn't paginate.

## Custom paginator

For endpoints with non-standard pagination, pass a `paginator=` callable.
It receives the raw response and returns `(items, next_params | None)`:

```python
def my_paginator(response):
    items = response.get("result", [])
    cursor = response.get("cursor") or None
    return items, {"cursor": cursor} if cursor else None

all_items = await api.get_all("/api/v3/custom", paginator=my_paginator)
```

If you've figured out a pattern that works well — feel free to open a [PR](https://github.com/serdukow/wbapi-async/pulls).
