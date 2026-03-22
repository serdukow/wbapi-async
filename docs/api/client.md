# WbAPI Client

The main entry point for the library.

```python
from wbapi_async import WbAPI

async with WbAPI(token="your_token") as api:
    result = await api.connection_check()
```

## Constructor

```python
WbAPI(
    token: str,                        # Wildberries API token (JWT)
    session: BaseSession | None = None, # Custom HTTP session (optional)
    **kwargs                           # Passed to BaseSession (base, timeout)
)
```

| Parameter | Default            | Description                             |
| --------- | ------------------ | --------------------------------------- |
| `token`   | required           | JWT token from WB Seller Portal         |
| `session` | `None`             | Custom `BaseSession` instance           |
| `base`    | `"wildberries.ru"` | API base domain (via kwargs)            |
| `timeout` | `60`               | Request timeout in seconds (via kwargs) |

## Custom session

```python
from wbapi_async import WbAPI
from wbapi_async.client.session import BaseSession

session = BaseSession(base="wildberries.ru", timeout=120)

async with WbAPI(token="...", session=session) as api:
    ...
```

## All methods

All 252 API methods are available as async methods on the `WbAPI` instance. Use your IDE's autocomplete to discover them, or see the full API documentation at [dev.wildberries.ru](https://dev.wildberries.ru/openapi).
