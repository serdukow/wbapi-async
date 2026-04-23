# WbAPI Client

::: wbapi.api.WbAPI

## Custom session

Useful for testing or custom timeouts:

```python
from wbapi import WbAPI
from wbapi.client.session.base import BaseSession

session = BaseSession(base="https://wildberries.ru", timeout=120)

async with WbAPI(token="...", session=session) as api:
    ...
```
