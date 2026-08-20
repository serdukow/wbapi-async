<div align="center">

<h1>wbapi</h1>

<p>Асинхронный клиент Wildberries Seller API</p>

[![PyPI version](https://img.shields.io/pypi/v/wbapi-async.svg)](https://pypi.org/project/wbapi-async/)
[![Downloads](https://img.shields.io/pypi/dm/wbapi-async.svg)](https://pypi.python.org/pypi/wbapi-async)
[![Tests](https://github.com/serdukow/wb-api/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/serdukow/wb-api/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/serdukow/cf37fee32eccac65721c605a306aa138/raw/wb-api-coverage.json)](https://github.com/serdukow/wb-api/actions/workflows/tests.yml)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2A6DB2.svg)](https://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://pypi.org/project/wbapi-async/)

</div>

308 методов и 687 моделей, сгенерированных из официальных спецификаций
Wildberries. Автодополнение в редакторе, повторы при сбоях, лимиты запросов и
постраничный обход из коробки.

## Установка

Требуется Python 3.10+.

```console
pip install wbapi-async
```

## Быстрый старт

```python
import asyncio
import os

from wbapi import WBApi


async def main() -> None:
    async with WBApi(token=os.environ["WB_TOKEN"]) as api:
        orders = await api.orders_fbs.orders_new()
        for order in orders.orders:
            print(order.id, order.nm_id, order.sale_price)


asyncio.run(main())
```

## Разделы

```python
await api.general.seller_info()
await api.items.content_v2_cards_limits()
await api.orders_fbs.orders_new()
await api.promotion.adv_v1_promotion_count()
await api.finances.account_balance()
```

| Раздел | Что внутри |
| --- | --- |
| `general` | Общее: подключение, продавец, пользователи |
| `items` | Работа с товарами: карточки, категории, медиа |
| `orders_fbs` | Заказы FBS: задания, поставки, пропуска |
| `orders_dbs` | Заказы DBS |
| `orders_dbw` | Заказы DBW |
| `orders_fbw` | Поставки FBW |
| `in_store_pickup` | Самовывоз |
| `promotion` | Маркетинг и продвижение |
| `communications` | Отзывы, вопросы, чат с покупателями |
| `analytics` | Аналитика и данные |
| `reports` | Отчёты |
| `finances` | Документы и бухгалтерия |
| `rates` | Тарифы |
| `wbd` | Wildberries Цифровой |

## Ответы

```python
response = await api.orders_fbs.orders_new()

order = response.orders[0]
order.nm_id
order.sale_price
order.created_at

order.to_dict()
order.to_dict(by_alias=True)
order.to_json()
```

## Постраничный обход

```python
# одна страница
page = await api.orders_fbs.orders(limit=1000, next_=0)

# все страницы списком
rows = await api.orders_fbs.orders(limit=1000, next_=0, auto_paginate=True)

# по одной записи — память не растёт с размером выборки
async for order in api.orders_fbs.iter_orders(limit=1000, next_=0):
    await save(order)
```

## Повторы и лимиты

Запросы к 429, 5xx и сетевым сбоям повторяются автоматически — с
экспоненциальной задержкой, джиттером и учётом заголовка `X-Ratelimit-Retry`.

```python
api = WBApi(
    token=...,
    timeout=60,            # или httpx.Timeout(connect=5, read=60)
    max_retries=3,
    retry_backoff=0.5,
    max_retry_wait=60,
    user_agent="myapp/1.0",
)
```

## Песочница

Нужен токен с опцией «Тестовый контур» — данные там случайные.

```python
async with WBApi(token=..., sandbox=True) as api:
    supply = await api.orders_fbs.supplies_create(name="test")
```

Если у метода песочницы нет, запрос не уйдёт — клиент сообщит об этом.

## Лицензия

[MIT](LICENSE)
