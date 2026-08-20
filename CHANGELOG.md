# Changelog

## [1.0.0](https://github.com/serdukow/wbapi-async/compare/v0.10.0...v1.0.0) (2026-08-20)


### ⚠ BREAKING CHANGES

* api.get("/api/v3/orders/new") becomes api.orders_fbs.orders_new(); WbAPI becomes WBApi; WBType is replaced by the generated models; response.unwrap() becomes response.to_dict(); exceptions moved to wbapi.exceptions.
* WbAPI is now WBApi and WBType is now WBDict/WBList. Query parameters move from **kwargs to params={...}; path ids are interpolated by the caller. Pagination is the async iterator paginate() instead of paginate=True. Exceptions live in wbapi.exceptions and the root package no longer re-exports them. unwrap() and to_snake() are gone: responses subclass dict and list, so no conversion is needed.

### Features

* generate a typed client from the OpenAPI specs ([348e18e](https://github.com/serdukow/wbapi-async/commit/348e18eff3be5a0cda4e97c678be387e3a7228e4))
* rewrite the client for 1.0 ([e569f35](https://github.com/serdukow/wbapi-async/commit/e569f35acee370484717055029a8fbcf16de71e0))


### Documentation

* describe the generated client ([483ba8c](https://github.com/serdukow/wbapi-async/commit/483ba8c905aebca023eb7865bf30fa6928e46f9e))
* rewrite README, CHANGELOG and AGENTS for 1.0 ([041e040](https://github.com/serdukow/wbapi-async/commit/041e040fdd37c7c6791cd81c6e2b9b87f9bcfed9))

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

## [0.10.0](https://github.com/serdukow/wbapi-async/compare/v0.9.0...v0.10.0) (2026-05-04)


### Features

* add offset_body paginator for POST endpoints ([0e19009](https://github.com/serdukow/wbapi-async/commit/0e190093d5b873a49593e3f3f1204a27ca74ea74))
* add offset_body paginator for POST endpoints ([fcd7b50](https://github.com/serdukow/wbapi-async/commit/fcd7b506979d891d6062a32f92a36eadf86bd49a))

## [0.9.0](https://github.com/serdukow/wbapi-async/compare/v0.8.0...v0.9.0) (2026-04-28)


### Features

* remove session param from WbAPI class ([b31faef](https://github.com/serdukow/wbapi-async/commit/b31faefd589c43dcb37588ebb3248c7b543f40d9))


### Bug Fixes

* use page size threshold to detect pagination end ([e4f62e9](https://github.com/serdukow/wbapi-async/commit/e4f62e9d5a2a32efa06fdbe21c47a974f14204a3))


### Documentation

* update methods docs ([780dd13](https://github.com/serdukow/wbapi-async/commit/780dd13dc8082c50f4223b77763e3b9b85f95b23))
