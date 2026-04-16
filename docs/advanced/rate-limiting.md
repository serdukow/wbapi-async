# Rate Limiting

Rate limits are applied automatically per endpoint from the WB OpenAPI spec.
No configuration needed — just make requests normally.

## How it works

Each path in `_PATH_TO_LIMIT` stores `(period_ms, limit, interval_ms, burst)` parsed
from the spec. `MethodDispatcher` builds a shared `AsyncLimiter` keyed by `(interval_ms, burst)`
and acquires it before every request.

## Auto-retry on 429

When WB returns HTTP 429, the library automatically:

1. Reads `X-Ratelimit-Retry` header
2. Sleeps for the specified time
3. Retries the request

## Concurrent requests

Limiters are shared globally — parallel calls to the same endpoint share one bucket:

```python
import asyncio
from wbapi_async import WbAPI

async with WbAPI(token="...") as api:
    results = await asyncio.gather(
        api.get("/api/v3/warehouses"),
        api.get("/api/v3/supplies"),
        api.get("/api/v1/feedbacks/count"),
    )
```
