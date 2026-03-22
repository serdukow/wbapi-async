# wbapi-async

**Asynchronous Python client for Wildberries API**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/wbapi-async.svg)](https://pypi.org/project/wbapi-async/)
[![Python](https://img.shields.io/pypi/pyversions/wbapi-async.svg)](https://pypi.org/project/wbapi-async/)

---

!!! warning "Beta"
The library is under active development. API may change between minor versions.

!!! info "Auto-generated"
API methods, types, and tests are [automatically generated](https://github.com/serdukow/wbapi-codegen) from the official [Wildberries OpenAPI specs](https://dev.wildberries.ru/openapi) — so the library is always up to date.

## Features

- **252 API methods** across 13 domains (products, orders, analytics, etc.)
- **Fully async** — built on `httpx` and `asyncio`
- **Type-safe** — Pydantic v2 models with `py.typed` marker
- **Auto-pagination** — list endpoints fetch all pages automatically
- **Rate limiting** — per-method limits with `aiolimiter`
- **Auto-retry** — automatic retry on HTTP 429

## Quick Start

```python
import asyncio
from wbapi_async import WbAPI

async def main():
    async with WbAPI(token="your_token_here") as api:
        # Connection check
        check = await api.connection_check()

        # Get products with prices
        products = await api.get_products_with_prices(limit=100)

        # Get sales report
        sales = await api.get_sales(date_from="2026-01-01")

asyncio.run(main())
```

## API Domains

252 methods across 13 domains: Products, Orders (FBS/FBW/DBS/DBW), Analytics, Reports, Finances, Promotion, Communications, Tariffs, General, In-Store Pickup.

Full API documentation is available at [dev.wildberries.ru](https://dev.wildberries.ru/openapi).
