# Error Handling

## Exceptions

```python
from wbapi_async import WbAPI, WbAPIError, TokenValidationError
```

### WbAPIError

Raised when the API returns an HTTP error (status >= 400).

```python
try:
    result = await api.get_products_with_prices()
except WbAPIError as e:
    print(e.http_status)       # 401, 403, 429, 500, ...
    print(e.error.error_text)  # Error message from API
    print(e.error.detail)      # Detailed description
    print(e.error.request_id)  # Request ID for support
```

The `e.error` object is an `Error` model with fields:

| Field        | Type                 | Description          |
| ------------ | -------------------- | -------------------- |
| `error_text` | `str \| None`        | Error message        |
| `detail`     | `str \| None`        | Detailed description |
| `code`       | `str \| None`        | Error code           |
| `status`     | `int \| str \| None` | HTTP status          |
| `request_id` | `str \| None`        | Request ID           |
| `title`      | `str \| None`        | Error title          |

### TokenValidationError

Raised when the JWT token is invalid.

```python
try:
    api = WbAPI(token="bad_token")
except TokenValidationError as e:
    print(e)  # "Token has expired", "Invalid token structure", etc.
```

## Common HTTP errors

| Status | Meaning      | Action                           |
| ------ | ------------ | -------------------------------- |
| 401    | Unauthorized | Check token                      |
| 403    | Forbidden    | Token lacks required permissions |
| 429    | Rate limited | Handled automatically (retry)    |
| 500    | Server error | Retry later                      |
