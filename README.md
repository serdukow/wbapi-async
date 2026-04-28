<p align="center">
  <a href="https://dev.wildberries.ru"><img src="https://i.postimg.cc/q7qHdnRF/svgviewer-output-2-1-3.png" alt="wbapi"></a>
</p>

<p align="center">
<a href="https://img.shields.io/pypi/v/wbapi-async.svg">
<img src="https://img.shields.io/pypi/v/wbapi-async.svg" alt="Version">
</a>
<a href="https://pypi.python.org/pypi/wbapi-async">
<img src="https://img.shields.io/pypi/dm/wbapi-async.svg" alt="Downloads">
</a>
<a href="https://pypi.python.org/pypi/wbapi-async">
<img src="https://img.shields.io/badge/status-stable-52C72D.svg?logo=git&logoColor=52C72D" alt="Status">
</a>
<a href="https://pypi.org/project/wbapi-async">
<img src="https://img.shields.io/pypi/pyversions/wbapi-async.svg" alt="Python">
</a>
</p>

---

**Documentation**: [https://dev.wildberries.ru](https://dev.wildberries.ru)

**Source Code**: [https://github.com/serdukow/wbapi-async](https://github.com/serdukow/wbapi-async)

---

**wbapi** is a lightweight async client for the Wildberries Seller API, built on top of [httpx](https://www.python-httpx.org/).

It handles pagination, rate limiting, and base URL resolution automatically — so you can focus on your business logic instead of HTTP boilerplate.

## Requirements

Python 3.10+

wbapi stands on the shoulders of giants:

- [httpx](https://www.python-httpx.org/) for async HTTP.
- [aiolimiter](https://github.com/mjpieters/aiolimiter) for rate limiting.

## Installation

```bash
pip install wbapi-async
```

## How to use

1. Register in the Wildberries seller [personal account](https://seller.wildberries.ru/) if you haven't already.
2. Go to store settings and [create an API token](https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Authorization/How-to-create-a-personal-access-base-or-test-token).

## Quick start

```python
import asyncio
from wbapi import WbAPI

async def main():
    async with WbAPI(token="your_api_token") as api:
        # Simple request
        warehouses = await api.get("/api/v3/warehouses")

        # Auto-paginated — fetches all pages automatically
        all_cards = await api.post(
            "/content/v2/get/cards/list",
            body={
                "settings": {
                    "sort": {"ascending": True},
                    "cursor": {"limit": 100},
                    "filter": {"withPhoto": -1},
                }
            },
            paginate=True,
        )
        print(all_cards)

asyncio.run(main())
```

Pass `paginate=True` to any `get` or `post` call and the library fetches all pages automatically. Pagination strategy (cursor, token, or offset) is detected from the first response.

Base URL resolution and per-endpoint rate limiting are handled transparently.

## License

This project is licensed under the terms of the [MIT license](https://github.com/serdukow/wbapi-async/blob/main/LICENSE).
