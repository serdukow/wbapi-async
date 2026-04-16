# WbAPI Client

::: wbapi_async.api.WbAPI

## Custom session

Useful for testing or custom timeouts:

```python
from wbapi_async import WbAPI
from wbapi_async.client.session.base import BaseSession

session = BaseSession(base="https://wildberries.ru", timeout=120)

async with WbAPI(token="...", session=session) as api:
    ...
```
