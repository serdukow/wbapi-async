# Changelog

## 1.0.0rc1

Изменились имена, способ передачи параметров и работа с
пагинацией. Сетевой слой переписан: клиент повторяет запросы при 429, 5xx и
обрывах связи, корректно разбирает любые ответы Wildberries и не теряет токен
при параллельных запросах.

Устанавливается как `wbapi-async`, импортируется как `wbapi`.
Требуется Python 3.10 или новее.

### Миграция

#### Клиент и параметры

```python
# было
from wbapi import WbAPI

async with WbAPI(token=token) as api:
    orders = await api.get("/api/v3/orders/new", limit=10, next=0)

# стало
from wbapi import WBApi

async with WBApi(token=token) as api:
    orders = await api.get("/api/v3/orders/new", params={"limit": 10, "next": 0})
```

Идентификаторы в пути подставляются f-строкой:

```python
# было
await api.patch("/api/v3/orders/{orderId}/cancel", orderId=13833711)

# стало
await api.patch(f"/api/v3/orders/{order_id}/cancel")
```

#### Пагинация

`paginate=True` возвращал весь список сразу. Теперь `paginate()` — асинхронный
итератор: записи приходят по одной, вся выгрузка не держится в памяти.

```python
# было
orders = await api.get("/api/v3/orders", paginate=True)
for order in orders:
    await save(order)

# стало
async for order in api.paginate("/api/v3/orders"):
    await save(order)

# если нужен список целиком
orders = [o async for o in api.paginate("/api/v3/orders")]
```

POST-эндпоинты — тот же метод, достаточно передать `body`:

```python
# было
cards = await api.post(
    "/content/v2/get/cards/list",
    body={"settings": {"filter": {"withPhoto": -1}}},
    paginate=True,
)

# стало
cards = [
    c
    async for c in api.paginate(
        "/content/v2/get/cards/list",
        body={"settings": {"filter": {"withPhoto": -1}}},
    )
]
```

#### Ответы

Ответ — обычный `dict` или `list` с доступом через точку. Разворачивать нечего,
`unwrap()` удалён.

```python
# было
data = order.unwrap()

# стало
data = order
```

Заодно заработало без конверсии:

```python
json.dumps(response)
isinstance(response.orders, list)
sorted(response.orders, key=lambda o: o.id)
```

#### Ошибки

Исключения переехали в `wbapi.exceptions` и делятся по типу — конкретную
ошибку можно поймать вместо сравнения кода.

```python
# было
from wbapi import WBAPIError

except WBAPIError as e:
    print(e.http_status, e.detail)

# стало
from wbapi.exceptions import WBAPIError, WBAuthError, WBRateLimitError

except WBAuthError:
    ...                       # 401 — токен не подошёл
except WBRateLimitError as e:
    print(e.retry_after)      # 429 — лимит запросов
except WBAPIError as e:
    print(e.status_code, e.payload)
```

### Таблица переименований

| Было | Стало |
| --- | --- |
| `WbAPI` | `WBApi` |
| `WBType` | `WBDict` / `WBList` |
| `api.get(path, limit=10)` | `api.get(path, params={"limit": 10})` |
| `api.get(path, paginate=True)` | `api.paginate(path)` |
| `response.unwrap()` | не нужен — это уже `dict` / `list` |
| `response.to_snake()` | удалён |
| `from wbapi import WBAPIError` | `from wbapi.exceptions import WBAPIError` |
| `error.http_status` | `error.status_code` |
| `error.detail` | `error.payload` |
| `TokenValidationError` | `WBConfigurationError` |
| `BaseWBAPIError` | `WBError` |

### Исправлено

- Клиент падал с `TypeError`, если Wildberries возвращал ошибку списком или
  текстом вместо объекта.
- Ответ 429 приводил к бесконечным повторам.
- Эндпоинты с идентификатором в пути использовали чужой лимит запросов.
- Пагинация останавливалась на первой странице, если в ответе был пустой
  список `errors`, и могла зациклиться при повторяющемся курсоре.
- Не было повторов при 5xx и обрывах связи.
