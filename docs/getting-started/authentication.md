# Authentication

## Getting a token

1. Go to [Wildberries Seller Portal](https://seller.wildberries.ru/)
2. Navigate to **Settings** -> **API access**
3. Create a new token with the required permissions

## Token types

Wildberries issues tokens with different access levels (`acc` field in JWT):

| Type | Description  |
| ---- | ------------ |
| 1    | Read-only    |
| 2    | Read + Write |
| 3    | Full access  |
| 4    | Statistics   |

## Using the token

```python
from wbapi_async import WbAPI

async with WbAPI(token="your_token_here") as api:
    ...
```

## Token validation

The library validates your token on client creation:

- JWT structure (header, payload, signature)
- Required fields (`id`, `sid`, `acc`, `exp`)
- Expiry check

If the token is invalid, `TokenValidationError` is raised:

```python
from wbapi_async import WbAPI, TokenValidationError

try:
    api = WbAPI(token="invalid")
except TokenValidationError as e:
    print(f"Bad token: {e}")
```
