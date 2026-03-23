# wbapi-async

**Asynchronous Python client for Wildberries API**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/wbapi-async.svg)](https://pypi.org/project/wbapi-async/)
[![Python](https://img.shields.io/pypi/pyversions/wbapi-async.svg)](https://pypi.org/project/wbapi-async/)

---

!!! warning "Beta"
The library is under active development. API may change between minor versions.

## Features

- **Fully async** — built on `httpx` and `asyncio`
- **Type-safe** — Pydantic v2 models with `py.typed` marker
- **Auto-pagination** — fetch all pages with a single `await paginate(...)`
- **Rate limiting** — per-method limits with `aiolimiter`
- **Auto-retry** — automatic retry on HTTP 429
- **Always up to date** — methods are [auto-generated](https://github.com/serdukow/wbapi-codegen) nightly from official OpenAPI specs

## Quick Start

```python
import asyncio
from wbapi_async import WbAPI, paginate

async def main():
    async with WbAPI(token="your_token_here") as api:
        # Single request
        products = await api.get_products_with_prices(limit=100)

        # All pages at once
        all_products = await paginate(api.get_products_with_prices)

asyncio.run(main())
```

## API Domains

13 domains: Products, Orders (FBS/FBW/DBS/DBW), Analytics, Reports, Finances, Promotion, Communications, Tariffs, General, In-Store Pickup.

Full API reference: [dev.wildberries.ru](https://dev.wildberries.ru)
