# Types & Enums

## Response types

All API responses are deserialized into Pydantic models. Types can be imported from the flat package or from domain modules:

```python
# Flat import (any type)
from wbapi_async.types import ProductCardsListItem, BalanceItem

# Domain import
from wbapi_async.products.types import ProductCardsListItem
from wbapi_async.promotion.types import BalanceItem
```

All types inherit from `BaseType` which is configured with:

- `extra="allow"` — unknown fields from the API are kept, not rejected
- `populate_by_name=True` — fields can be set by Python name or JSON alias

## Enums

Enum parameters use Python's `StrEnum`:

```python
from wbapi_async.enums import Locale, AggregationLevel

# Pass enum values to API methods
products = await api.get_products_with_prices(locale=Locale.RU)
stats = await api.product_cards_statistics_per_days(
    aggregation_level=AggregationLevel.DAY,
)
```

Available enums:

| Enum                                  | Domain         | Values                       |
| ------------------------------------- | -------------- | ---------------------------- |
| `Locale`                              | Products       | `RU`, `EN`, `ZH`             |
| `AggregationLevel`                    | Analytics      | `DAY`, `WEEK`, `MONTH`       |
| `BidType`                             | Promotion      | `MANUAL`, `UNIFIED`          |
| `PaymentType`                         | Promotion      | `CPM`, `CPC`                 |
| `Period`                              | Finances       | `WEEK`, `TWO_WEEKS`, `MONTH` |
| `Sort`, `SortBlocked`, `SortShadowed` | Reports        | Various sort fields          |
| `State`                               | Communications | Feedback states              |
| `Order`                               | Communications | Sort order                   |

See `wbapi_async.enums` for the full list.
