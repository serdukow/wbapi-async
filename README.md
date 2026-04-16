<p align="center">
  <a href="https://dev.wildberries.ru/"><img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Wildberries_2023_Pink.svg" alt="WbAPI"></a>
</p>

<div align="center">

## Async client for Wildberries Seller API

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/wild-api.svg)](https://pypi.org/project/wild-api/)
[![Downloads](https://img.shields.io/pypi/dm/wild-api.svg)](https://pypi.python.org/pypi/wild-api)
[![Docs](https://img.shields.io/badge/docs-serdukow.github.io-blue.svg)](https://serdukow.github.io/wbapi-async/)

</div>

Lightweight async Python client for the [Wildberries Seller API](https://dev.wildberries.ru).
Just pass the path from the docs and get data back.

## Install

```bash
pip install wbapi-async
```

## Usage

```python
from wbapi_async import WbAPI

async with WbAPI(token="...") as api:
    orders = await api.get("/api/v3/orders/new", limit=10, next=0)
    print(f"orders: {orders.orders!r}")

    supplies = await api.get_all("/api/v3/supplies")
    print(f"supplies: {supplies!r}")

    result = await api.post("/adv/v0/rename", body={"advertId": 2233344, "name": "newname"})
    print(f"rename: {result!r}")

    await api.put("/api/v3/stocks/507", body={"stocks": [{"sku": "WB007", "amount": 10}]})
    await api.delete("/content/v2/tag/99")
```

Paths are used exactly as they appear in the [wb api](https://dev.wildberries.ru) —
no need to know which subdomain serves which endpoint, it's resolved automatically.

## Features

- **Zero boilerplate** — no type models, no method classes, just `api.get(path, **params)`
- **Auto-pagination** — `get_all()` fetches all page. Currently auto-detects cursor or offset style
- **Rate limiting** — per-endpoint limits from the spec, powered by `aiolimiter`
- **Auto-retry** — automatic retry on HTTP 429 with `X-Ratelimit-Retry` backoff
- **Always up to date** — path registry is [auto-generated](https://github.com/serdukow/wbapi-codegen) from WB OpenAPI specs daily
- **Fully async** — built on `httpx` + `asyncio`

## Custom pagination

For endpoints with non-standard pagination, pass a `paginator=` callable.
If you've figured out a pattern that works well — feel free to open a [PR](https://github.com/serdukow/wbapi-async/pulls):

```python
def my_paginator(response):
    items = response.get("result", [])
    cursor = response.get("cursor") or None
    return items, {"cursor": cursor} if cursor else None

all_items = await api.get_all("/api/v3/custom", paginator=my_paginator)
```
