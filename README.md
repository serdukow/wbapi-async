<p align="center">
  <a href="https://dev.wildberries.ru/"><img src="docs/assets/logo.svg" alt="WbAPI" width="200"></a>
</p>

<div align="center">

#### Lightweight async client for Wildberries Seller API

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/wild-api.svg)](https://pypi.org/project/wild-api/)
[![Downloads](https://img.shields.io/pypi/dm/wild-api.svg)](https://pypi.python.org/pypi/wild-api)
[![Docs](https://img.shields.io/badge/docs-serdukow.github.io-blue.svg)](https://serdukow.github.io/wbapi-async/)

</div>

Lightweight async Python client for the [Wildberries Seller API](https://dev.wildberries.ru).
Just pass the path from the docs and get data back.

## Features

- **Zero boilerplate** — WB API changes constantly; typed models break on every schema update. Instead, responses are plain attribute-accessible dicts — `result.fieldName` just works, no models to maintain
- **Auto-pagination** — `get_all()` fetches all page. Auto-detect for all known strategies
- **Rate limiting** — per-endpoint limits from the spec, powered by `aiolimiter`
- **Auto-retry** — automatic retry on HTTP 429 with `X-Ratelimit-Retry` backoff
- **Always up to date** — path registry is [auto-generated](https://github.com/serdukow/wbapi-codegen) from WB OpenAPI specs daily
- **Fully async** — built on `httpx` + `asyncio`

## Install

```bash
pip install wbapi-async
```

## Quick start

```python
from wbapi_async import WbAPI

async with WbAPI(token="...") as api:

    supplies = await api.get_all("/api/v3/supplies")
    print(f"supplies: {supplies!r}")

    result = await api.post("/adv/v0/rename", body={"advertId": 2233344, "name": "newname"})
    print(f"rename: {result!r}")

    await api.put("/api/v3/stocks/507", body={"stocks": [{"sku": "WB007", "amount": 10}]})
    await api.delete("/content/v2/tag/99")
```

Just copy the path straight from the [WB API](https://dev.wildberries.ru) — the correct base URL and subdomain are resolved automatically.
