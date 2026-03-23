# Quick Start

## Basic usage

```python
import asyncio
from wbapi_async import WbAPI

async def main():
    async with WbAPI(token="your_token_here") as api:
        # Single request — parameters match the WB API spec exactly
        products = await api.get_products_with_prices(limit=100)
        for p in products:
            print(p.nm_id, p.vendor_code)

asyncio.run(main())
```

## Pagination

Use `paginate()` to fetch all pages automatically:

```python
from wbapi_async import WbAPI, paginate

async with WbAPI(token="...") as api:
    # All products — no limit/offset needed
    all_products = await paginate(api.get_products_with_prices)

    # With parameters
    feedbacks = await paginate(api.get_feedbacks_list, is_answered=False)
```

`paginate()` returns `list[T]` with all items combined across pages.

## Working with responses

All responses are typed Pydantic models:

```python
products = await api.get_products_with_prices(limit=10)
for product in products:
    print(product.nm_id)        # int
    print(product.vendor_code)  # str
    print(product.sizes)        # list[...]
```
