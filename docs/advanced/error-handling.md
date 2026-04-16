# Error Handling

## WbAPIError

Raised when the API returns HTTP >= 400.

```python
from wbapi_async import WbAPI, WbAPIError

try:
    result = await api.get("/api/v3/orders/new")
except WbAPIError as e:
    print(e.http_status)      # 401, 403, 429, 500, ...
    print(e.detail)           # raw dict from API response
    print(str(e))             # errorText or detail from response
```

| Status | Meaning      | Action                        |
| ------ | ------------ | ----------------------------- |
| 401    | Unauthorized | Check token                   |
| 403    | Forbidden    | Token lacks permissions       |
| 429    | Rate limited | Handled automatically (retry) |
| 500    | Server error | Retry later                   |

## TokenValidationError

Raised on `WbAPI(token=...)` if the token is malformed or expired.

```python
from wbapi_async import WbAPI, TokenValidationError

try:
    api = WbAPI(token="bad_token")
except TokenValidationError as e:
    print(e)  # "Token has expired", "JWT must have 3 parts", etc.
```

## PaginationNotSupported

Raised by `get_all()` if the endpoint doesn't appear to paginate.

```python
from wbapi_async import WbAPI, PaginationNotSupported

try:
    result = await api.get_all("/api/v3/warehouses")
except PaginationNotSupported:
    result = await api.get("/api/v3/warehouses")
```
