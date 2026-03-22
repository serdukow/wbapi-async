# Rate Limiting

## How it works

Every API method has a `request_limit` defining its rate constraints:

```python
request_limit = RequestLimit(
    period=60,       # Time window (seconds)
    limit=10,        # Max requests per period
    interval=600,    # Min interval between requests (ms)
    burst=5          # Max concurrent requests
)
```

The library enforces these limits automatically using `aiolimiter`. You don't need to add delays or throttling in your code.

## Auto-retry on 429

When Wildberries returns HTTP 429 (Too Many Requests), the library automatically:

1. Reads the `X-Ratelimit-Retry` header
2. Waits for the specified time
3. Retries the request

No action needed on your side.

## Concurrent requests

Rate limiters are shared by `(burst, interval)` key. Methods with the same rate profile share a limiter, preventing overall overload.

```python
import asyncio

async with WbAPI(token="...") as api:
    # These run concurrently but respect rate limits
    results = await asyncio.gather(
        api.get_products_with_prices(limit=100),
        api.get_inventory(),
        api.get_warehouses(),
    )
```
