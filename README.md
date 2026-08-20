<div align="center">

<h1>wbapi</h1>

<p>Асинхронная библиотека для работы с API Wildberries Seller</p>

[![PyPI version](https://img.shields.io/pypi/v/wbapi-async.svg)](https://pypi.org/project/wbapi-async/)
[![Downloads](https://img.shields.io/pypi/dm/wbapi-async.svg)](https://pypi.python.org/pypi/wbapi-async)
[![Tests](https://github.com/serdukow/wb-api/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/serdukow/wb-api/actions/workflows/tests.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/serdukow/cf37fee32eccac65721c605a306aa138/raw/wb-api-coverage.json)](https://github.com/serdukow/wb-api/actions/workflows/tests.yml)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2A6DB2.svg)](https://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12%20%7C%203.13-blue.svg)](https://pypi.org/project/wbapi-async/)

</div>

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
        orders = await api.get("/api/v3/orders/new", params={"limit": 10})
        print(orders.orders[0].id)


asyncio.run(main())
```

Домен подставляется автоматически: `/api/v3/orders/new` уходит на
`marketplace-api.wildberries.ru`, `/content/v2/get/cards/list` — на
`content-api.wildberries.ru`.

## Запросы

```python
# GET с query-параметрами
await api.get("/api/v1/supplier/orders", params={"dateFrom": "2026-04-28", "flag": 1})

# POST с телом
await api.post("/adv/v0/rename", body={"advertId": 123, "name": "Новая кампания"})

# Идентификаторы в пути — обычная f-строка
await api.patch(f"/api/v3/orders/{order_id}/cancel")

await api.put(
    f"/api/v3/stocks/{warehouse_id}",
    body={"stocks": [{"sku": "WB007", "amount": 10}]},
)

await api.delete(f"/content/v2/tag/{tag_id}")
```

## Ответы

Ответ — обычный `dict` или `list`, к которому добавлен доступ через точку.
Никакой конверсии не нужно: он сериализуется, распаковывается и проходит
проверки типов как есть.

```python
response = await api.get("/api/v3/orders/new")

response.orders[0].id                    # доступ через точку, на любую глубину
response["orders"]
response.get("total", 0)

json.dumps(response) 
isinstance(response.orders, list)        # True
sorted(response.orders, key=lambda o: o.id)
```

## Пагинация

`paginate()` возвращает асинхронный итератор и сам определяет схему
постраничного обхода по первому ответу — offset, курсор, `next`-токен
или `rrdid`.

```python
# по одной записи, память не растёт
async for order in api.paginate("/api/v3/orders"):
    await save(order)

# всё сразу
supplies = [s async for s in api.paginate("/api/v3/supplies")]

# POST-эндпоинты — тот же метод, отличается наличием body
cards = [
    c
    async for c in api.paginate(
        "/content/v2/get/cards/list",
        body={"settings": {"filter": {"withPhoto": -1}}},
    )
]
```

## Лимиты и повторные запросы

Лимиты берутся из таблицы эндпоинтов для каждого пути. Запросы к 429, 5xx и
сетевым сбоям повторяются автоматически — с экспоненциальной задержкой и
джиттером, с учётом заголовка `X-Ratelimit-Retry`.

```python
api = WBApi(
    token=...,
    timeout=60,           # или httpx.Timeout(connect=5, read=60)
    max_retries=3,
    retry_backoff=0.5,
    max_retry_wait=60,
    user_agent="myapp/1.0",
)
```

## Новые эндпоинты

Таблица эндпоинтов обновляется автоматически из OpenAPI-спецификаций
Wildberries. Если нужный путь ещё не попал в релиз, передайте полный URL:

```python
await api.get("https://content-api.wildberries.ru/content/v3/new-endpoint")
```

## Лицензия

[MIT](LICENSE)
