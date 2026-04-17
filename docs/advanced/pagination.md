# Pagination

## Auto-pagination

`get_all()` fetches all pages automatically. The pagination strategy is detected from the first response:

- **cursor (`next`)** — response has a `next` field
- **offset** — first page is full (1000 items)
- **body cursor** — POST endpoint with a `cursor` field in the response body
- **`rrd_id` cursor** — response items have an `rrd_id` field
- **`lastChangeDate` cursor** — response items have a `lastChangeDate` field

```python
async with WbAPI(token="...") as api:
    supplies = await api.get_all("/api/v3/supplies")
    orders = await api.get_all("/api/v3/orders/new")
```

Raises `PaginationNotSupported` if the endpoint doesn't paginate.

## POST endpoints

For endpoints that paginate via POST body, pass `body=`:

```python
cards = await api.get_all(
    "/content/v2/get/cards/list",
    body={"settings": {"sort": {"ascending": False}}},
)
```

## Custom paginator

For non-standard pagination, pass a `paginator=` callable.
It receives the raw response and returns `(items, next_params | None)`:

```python
def my_paginator(response):
    items = response.get("result", [])
    cursor = response.get("cursor") or None
    return items, {"cursor": cursor} if cursor else None

all_items = await api.get_all("/api/v3/custom", paginator=my_paginator)
```

If you've figured out a pattern that works well — feel free to open a [PR](https://github.com/serdukow/wbapi-async/pulls).
