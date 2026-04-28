# wbapi

Async Python client for the Wildberries Seller API. Pydantic-free — responses are plain `ApiResponse` objects with attribute access. No type models, no method classes. Just HTTP verbs + path.

```python
async with WbAPI(token="...") as api:
    orders = await api.get("/api/v3/orders/new", limit=10, next=0)
    print(orders.orders[0].id)
    supplies = await api.get_all("/api/v3/supplies")  # auto-pagination
    await api.post("/adv/v0/rename", body={"advertId": 123, "name": "new"})
```

## Key files (`src/wbapi_async/`)

| File                     | Role                                                                                   |
| ------------------------ | -------------------------------------------------------------------------------------- |
| `api.py`                 | `WbAPI` — get/post/put/patch/delete/get_all                                            |
| `type.py`                | `ApiResponse` — recursive dict wrapper, `.field`, `.unwrap()`, `.to_snake()`           |
| `_method.py`             | `MethodDispatcher` — dispatch, fetch_all, resolve_url                                  |
| `_registry.py`           | `_BASES`, `_LIMITS`, `_PUBLIC` — **`# fmt: off` block is auto-generated, do not edit** |
| `client/session/base.py` | httpx, rate limiting, 429 retry                                                        |
| `utils/paginate.py`      | pagination strategies                                                                  |

## Design rules

- **URL resolution**: prefix lookup in `_BASES`; dynamic segments resolve via parent prefix. Unknown path → `WBAPIError`.
- **Rate limiting**: `_LIMITS[path] = (period_ms, limit, interval_ms, burst)`; limiters shared globally by `(interval_ms, burst)`.
- **Pagination**: `get_all` auto-detects cursor (`next` field) or offset (1000-item page). Custom: `paginator=callable(resp) -> (items, next_params | None)`.
- **`_registry.py`**: everything outside the `# fmt: off` block is safe to edit.

## OpenAPI specs

Base: https://dev.wildberries.ru/api/swagger/yaml/en/ — files `01-general.yaml` through `13-finances.yaml`.
