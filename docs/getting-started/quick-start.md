# Quick Start

## Basic usage

```python
import asyncio
from wbapi_async import WbAPI

async def main():
    async with WbAPI(token="your_token_here") as api:
        # Check connection
        check = await api.connection_check()
        print(check)

        # Get products
        products = await api.get_products_with_prices(limit=100)
        for p in products:
            print(p.nm_id, p.vendor_code)

asyncio.run(main())
```

## Auto-pagination

Methods with `limit`/`offset` parameters automatically fetch all pages when `limit` is not set:

```python
# Fetches ALL products (auto-pagination)
all_products = await api.get_products_with_prices()

# Fetches only first 100
first_page = await api.get_products_with_prices(limit=100)
```

## Working with responses

All responses are typed Pydantic models with attribute access:

```python
products = await api.get_products_with_prices(limit=10)
for product in products:
    print(product.nm_id)        # int
    print(product.vendor_code)  # str
    print(product.sizes)        # list[...]
```

## Context manager

Always use `WbAPI` as an async context manager to ensure the HTTP session is properly closed:

```python
async with WbAPI(token="...") as api:
    # session opens
    result = await api.connection_check()
# session closes automatically
```

Or manage the lifecycle manually:

```python
api = WbAPI(token="...")
try:
    result = await api.connection_check()
finally:
    await api.close()
```
