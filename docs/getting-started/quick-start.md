# Quick Start

```python
import asyncio
from wbapi_async import WbAPI

async def main():
    async with WbAPI(token="your_token_here") as api:
        # GET — kwargs become query params
        orders = await api.get("/api/v3/orders/new", limit=10, next=0)
        print(f"orders: {orders.orders!r}")

        # Fetch all pages automatically
        supplies = await api.get_all("/api/v3/supplies")
        print(f"supplies: {supplies!r}")

        # POST with JSON body
        result = await api.post("/adv/v0/rename", body={"advertId": 2233344, "name": "newname"})
        print(f"rename: {result!r}")

asyncio.run(main())
```

Use paths exactly as they appear in the [WB API docs](https://dev.wildberries.ru) —
base URL is resolved automatically.

## Attribute access

Responses support attribute access with field names as returned by the API (camelCase):

```python
orders = await api.get("/api/v3/orders/new", limit=10)
for order in orders.orders:
    print(order.id, order.article, order.convertedPrice)
```

Use `.unwrap()` to get the raw dict/list:

```python
raw = orders.unwrap()
```
