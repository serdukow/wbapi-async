<p align="center">
  <a href="https://dev.wildberries.ru/"><img src="https://upload.wikimedia.org/wikipedia/commons/4/41/Wildberries_2023_Pink.svg" alt="WbAPI"></a>
</p>

<div align="center">

## Asynchronous client for Wildberries API

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://img.shields.io/pypi/v/wild-api.svg)](https://pypi.org/project/wild-api/)
[![Downloads](https://img.shields.io/pypi/dm/wild-api.svg)](https://pypi.python.org/pypi/wild-api)
[![Docs](https://img.shields.io/badge/docs-serdukow.github.io-blue.svg)](https://serdukow.github.io/wbapi-async/)
[![Status](https://img.shields.io/badge/status-beta-8B5CF6.svg?logo=git&logoColor=white)]()

</div>

> [!CAUTION]
> The library is under active development and **is currently not recommended for use in production environments**

## Features

- **Fully async** — built on `httpx` and `asyncio`
- **Type-safe** — Pydantic v2 models with `py.typed` marker
- **Auto-pagination** — fetch all pages with a single `await paginate(...)`
- **Rate limiting** — per-method limits with `aiolimiter`
- **Auto-retry** — automatic retry on HTTP 429
- **Always up to date** — methods are [auto-generated](https://github.com/serdukow/wbapi-codegen) nightly from official OpenAPI specs

## Docs

**[wbapi-async](https://serdukow.github.io/wbapi-async/)**

**[WB API](https://dev.wildberries.ru)**
