# Changelog

## 1.0.0rc1

Библиотека переписана: вместо обёртки над HTTP-глаголами — 308 типизированных
методов, сгенерированных из официальных OpenAPI-спецификаций Wildberries.

Устанавливается как `wbapi-async`, импортируется как `wbapi`.
Требуется Python 3.10 или новее.

### Что нового

- **308 методов в 14 разделах**
- **687 моделей ответов** на msgspec
- **Постраничный обход** шести вариантов — курсор, токен, отступ, идентификатор строки
  отчёта — определяется по спецификации, а не задаётся вручную.
- **Лимиты запросов из спецификаций**, с учётом категории токена.
- **Разбор токена**
- **Повторы** при 429, 5xx и обрывах связи — с экспоненциальной задержкой и
  джиттером.
- **Песочница**: `WBApi(token=..., sandbox=True)` для методов, у которых она есть.
- Иерархия исключений и разбор `application/problem+json`: `code`, `origin`,
  `request_id` доступны как поля.

### Миграция

#### Вызов метода

```python
# было
orders = await api.get("/api/v3/orders/new", limit=10)

# стало
orders = await api.orders_fbs.orders_new()
```

Раздел и метод подсказывает редактор; путь, домен и лимит берутся из
спецификации.

#### Ответы

```python
# было
order.nmID
{**order.unwrap()}

# стало
order.nm_id
{**order.to_dict()}
```

```python
order.to_dict(by_alias=True)   # nmId, salePrice, createdAt
```

#### Постраничный обход

```python
# было
orders = await api.get("/api/v3/orders", paginate=True)

# стало — все страницы списком
orders = await api.orders_fbs.orders(limit=1000, next_=0, auto_paginate=True)

# стало — по одной записи
async for order in api.orders_fbs.iter_orders(limit=1000, next_=0):
    await save(order)
```

#### Ошибки

```python
# было
from wbapi import WBAPIError

except WBAPIError as error:
    print(error.http_status, error.detail)

# стало
from wbapi.exceptions import WBAPIError, WBAuthError, WBRateLimitError

except WBAuthError:
    ...                            # 401
except WBRateLimitError as error:
    print(error.retry_after)       # 429
except WBAPIError as error:
    print(error.status_code, error.payload)
```

### Таблица переименований

| Было | Стало |
| --- | --- |
| `WbAPI` | `WBApi` |
| `api.get("/api/v3/orders/new")` | `api.orders_fbs.orders_new()` |
| `api.get(path, paginate=True)` | `api.<раздел>.<метод>(auto_paginate=True)` |
| `WBType` | модели раздела в `wbapi.resources.<раздел>.models` |
| `response.unwrap()` | `response.to_dict()` |
| `response.to_snake()` | не нужен — поля уже в snake_case |
| `from wbapi import WBAPIError` | `from wbapi.exceptions import WBAPIError` |
| `error.http_status` | `error.status_code` |
| `error.detail` | `error.payload` |

### Исправлено

- Клиент падал, если Wildberries возвращал ошибку списком или текстом вместо
  объекта.
- При параллельных запросах токен мог не уйти с запросом.
- Ответ 429 приводил к бесконечным повторам.
- Эндпоинты с идентификатором в пути использовали чужой лимит запросов.
- Постраничный обход мог зациклиться на повторяющемся курсоре.
- Не было повторов при 5xx и обрывах связи.
