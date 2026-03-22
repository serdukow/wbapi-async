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
> The library is under active development and **is not recommended for use in production environments**

> [!NOTE]
> API methods, types, and tests are [automatically generated](https://github.com/serdukow/wbapi-codegen) from the official [Wildberries OpenAPI specs](https://dev.wildberries.ru/openapi) — so the library is always up to date with the latest endpoints and changes.

## Install

```console
pip install wbapi-async
```

## Quick Start

```python
import asyncio
from wbapi_async import WbAPI

async def main():
    async with WbAPI(token="your_token_here") as api:
        # Connection check
        check = await api.connection_check()
        print(check)

        # Get products with prices
        products = await api.get_products_with_prices(limit=100)
        print(products)

        # Get sales report
        sales = await api.get_sales(date_from="2026-01-01")
        print(sales)

        # Get realization report
        report = await api.get_realization_sales_report(
            date_from="2026-01-01",
            date_to="2026-01-31",
        )
        print(report)

asyncio.run(main())
```
