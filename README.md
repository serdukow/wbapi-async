<p align="center">
  <a href="https://dev.wildberries.ru/"><img src="https://dev.wildberries.ru/images/open-graph.png" alt="WbAPI" width="600"></a>
</p>

<div align="center">

#### Fast, lightweight async client for the Wildberries Seller API

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/wbapi-async.svg)](https://pypi.org/project/wild-api/)
[![Downloads](https://img.shields.io/pypi/dm/wbapi-async.svg)](https://pypi.python.org/pypi/wild-api)
[![Docs](https://img.shields.io/badge/docs-serdukow.github.io-blue.svg)](https://serdukow.github.io/wbapi-async/)

</div>

## Features

- **Zero boilerplate** — responses are plain attribute-accessible dicts
- **Auto-pagination** — `get_all()` fetches all pages. Auto-detects all known strategies; you can easily add your own via a custom paginator — [see docs](https://github.com/serdukow/wbapi-async/blob/dev/docs/advanced/pagination.md)
- **Rate limiting** — per-endpoint limits powered by `aiolimiter`
- **Auto-retry** — automatic retry
- **Always up to date** — path registry is updated every monday
- **Fully async** — built on `httpx` + `asyncio`

## Install

```bash
pip install wbapi-async
```

## Quick start

```python
import asyncio
from wbapi_async import WbAPI

async def main():
    async with WbAPI(token="YOUR_TOKEN") as api:
        body = {
            "settings": {
                "sort": {"ascending": True},
                "cursor": {"limit": 100},
                "filter": {"withPhoto": -1},
            }
        }

        cards = await api.get_all("/content/v2/get/cards/list", body=body)
        print(f"cards: {cards!r}")

asyncio.run(main())
```
