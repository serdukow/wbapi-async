<p align="center">
  <a href="https://dev.wildberries.ru/"><img src="https://dev.wildberries.ru/images/open-graph.png" alt="WbAPI" width="1200"></a>
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
- **Auto-pagination** — `get_all()` fetches all pages. Auto-detects all known strategies; you can easily add your own via a custom paginator — [see docs](https://serdukow.github.io/wbapi-async/advanced/pagination/)
- **Rate limiting** — per-endpoint limits from the spec, powered by `aiolimiter`
- **Auto-retry** — automatic retry on HTTP 429
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
```

Just copy the path straight from the [WB API](https://dev.wildberries.ru) — the correct base URL and subdomain are resolved automatically.
