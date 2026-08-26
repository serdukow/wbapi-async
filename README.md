<div align="center">

<a href="https://dev.wildberries.ru">
  <img src="https://raw.githubusercontent.com/serdukow/wbapi-async/main/docs/logo.jpeg"
       alt="wbapi" width="220">
</a>

<p>Асинхронный клиент WB API</p>

[![PyPI version](https://img.shields.io/pypi/v/wbapi-async.svg)](https://pypi.org/project/wbapi-async/)
[![Downloads](https://img.shields.io/pypi/dm/wbapi-async.svg)](https://pypi.python.org/pypi/wbapi-async)
[![Tests](https://github.com/serdukow/wb-api/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/serdukow/wb-api/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/serdukow/cf37fee32eccac65721c605a306aa138/raw/wb-api-coverage.json)](https://github.com/serdukow/wb-api/actions/workflows/tests.yml)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2A6DB2.svg)](https://mypy-lang.org/)
[![msgspec](https://img.shields.io/badge/msgspec-0.19-2E7D32.svg)](https://github.com/jcrist/msgspec)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://pypi.org/project/wbapi-async/)

</div>

308 сгенерированных методов с автоматической пагинацией.

## Установка

Требуется Python 3.10+.

```console
pip install wbapi-async
```

## Примеры использования

### Новые сборочные задания

```python
import asyncio
import os

from wbapi import WBApi


async def main():
    async with WBApi(token="your_token_here") as api:
        response = await api.orders_fbs.get_orders_new()
        for order in response.orders:
            print(f"{order.id}: артикул {order.nm_id}, {order.sale_price / 100:.2f} ₽")


asyncio.run(main())
```

### Поставка FBS

```python
import asyncio
import os

from wbapi import WBApi


async def main():
    async with WBApi(token="your_token_here") as api:
        supply = await api.orders_fbs.create_supply()
        print(f"Создана поставка: {supply.id}")

        new_orders = await api.orders_fbs.get_orders_new()
        order_ids = [order.id for order in new_orders.orders[:10]]
        await api.orders_fbs.update_supplies_order(supply_id=supply.id, orders=order_ids)
        print(f"Добавлено {len(order_ids)} новых сборочных заданий")

        await api.orders_fbs.update_supplies_deliver(supply_id=supply.id)
        print(f"Поставка {supply.id} передана в доставку")


asyncio.run(main())
```

### Пагинация

Клиент поддерживает все существующие схемы пагинации: токен, курсор,
`rrdId`, смещение и подбирает нужную автоматически.

`auto_paginate=True` собирает все страницы в один список:

```python
import asyncio

from wbapi import WBApi


async def main():
    async with WBApi(token="your_token_here") as api:
        rows = await api.orders_fbs.get_orders(limit=1000, next_=0, auto_paginate=True)
        print(f"Всего заказов: {len(rows)}")


asyncio.run(main())
```

На больших выборках используйте `iter_*` методы:

```python
import asyncio

from wbapi import WBApi


async def main():
    async with WBApi(token="your_token_here") as api:
        async for order in api.orders_fbs.iter_get_orders(limit=1000, next_=0):
            print(order.id, order.nm_id)


asyncio.run(main())
```

### Повторы и лимиты

429, 5xx и сетевые сбои повторяются автоматически — с
экспоненциальной задержкой, джиттером и учётом заголовка `X-Ratelimit-Retry`.
Лимиты wb соблюдаются по каждому эндпоинту отдельно.

### Обработка ошибок

```python
import asyncio
import os

from wbapi import WBApi
from wbapi.exceptions import WBAPIError, WBAuthError, WBRateLimitError


async def main():
    async with WBApi(token="your_token_here") as api:
        try:
            await api.orders_fbs.get_orders_new()
        except WBAuthError:
            print("Токен просрочен или у него нет доступа к нужной категории")
        except WBRateLimitError as error:
            print(f"Превышен лимит, повтор через {error.retry_after} с")
        except WBAPIError as error:
            print(f"{error.status_code}: {error}")


asyncio.run(main())
```

### Песочница

Вы можете протестировать методы API на случайных данных. Для этого понадобится [токен](https://dev.wildberries.ru/ru/openapi/api-information#tag/authorization/Kak-sozdat-personalnyj-bazovyj-ili-testovyj-token) с опцией Тестовый контур.

Данные в тестовом контуре сгенерированы случайным образом и не принадлежат реальным продавцам. Использование тестового контура не несёт риска непреднамеренного раскрытия информации.

```python
async with WBApi(token="your_token_here", sandbox=True) as api:
    supply = await api.orders_fbs.create_supply(name="test")
```

## Лицензия

[MIT](LICENSE)
