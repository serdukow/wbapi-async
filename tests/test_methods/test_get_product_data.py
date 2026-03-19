import pytest

from wbapi_async.enums.product_data_availability import ProductDataAvailability
from wbapi_async.enums.product_data_order_field import ProductDataOrderField
from wbapi_async.enums.product_data_order_mode import ProductDataOrderMode
from wbapi_async.enums.product_data_stock_type import ProductDataStockType
from wbapi_async.types.product_data import ProductDataItem

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetProductData:

    async def test_get_product_data(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "items": [
                        {
                            "nmID": 123456789,
                            "isDeleted": False,
                            "subjectName": "Принтеры",
                            "name": "Печатник 3000",
                            "vendorCode": "pechatnik3000",
                            "brandName": "Компик",
                            "mainPhoto": "https://basket-12.wbbasket.ru/vol1788/part178840/178840836/images/c246x328/1.webp",
                            "hasSizes": True,
                            "metrics": {
                                "ordersCount": 100,
                                "ordersSum": 100000,
                                "avgOrders": 200,
                                "avgOrdersByMonth": [
                                    {
                                        "start": "2025-01-01",
                                        "end": "2025-01-31",
                                        "value": 25.55,
                                    }
                                ],
                                "buyoutCount": 150,
                                "buyoutSum": 150000,
                                "buyoutPercent": 5,
                                "stockCount": 50,
                                "stockSum": 50000,
                                "saleRate": {"days": 5, "hours": 15},
                                "avgStockTurnover": {"days": 5, "hours": 15},
                                "toClientCount": 20,
                                "fromClientCount": 30,
                                "officeMissingTime": {"days": 5, "hours": 15},
                                "lostOrdersCount": 1550.52,
                                "lostOrdersSum": 155000.25,
                                "lostBuyoutsCount": 123.55,
                                "lostBuyoutsSum": 225555.15,
                                "currentPrice": {"minPrice": 50, "maxPrice": 100},
                                "availability": "deficient",
                            },
                        }
                    ],
                    "currency": "RUB",
                }
            }
        )

        result = await api.get_product_data(
            date_from="2025-01-01",
            date_to="2025-01-31",
            stock_type=ProductDataStockType.ALL,
            order_by_field=ProductDataOrderField.ORDERS_COUNT,
            order_by_mode=ProductDataOrderMode.DESC,
            availability_filters=[ProductDataAvailability.DEFICIENT],
        )

        assert isinstance(result, list)
        assert len(result) == 1

        item = result[0]
        assert isinstance(item, ProductDataItem)
        assert item.nm_id == 123456789
        assert item.name == "Печатник 3000"
        assert item.vendor_code == "pechatnik3000"
        assert item.brand_name == "Компик"
        assert item.is_deleted is False
        assert item.has_sizes is True

        metrics = item.metrics
        assert metrics is not None
        assert metrics.orders_count == 100
        assert metrics.buyout_count == 150
        assert metrics.stock_count == 50
        assert metrics.lost_orders_sum == 155000.25
        assert metrics.availability == ProductDataAvailability.DEFICIENT

        assert metrics.sale_rate is not None
        assert metrics.sale_rate.days == 5
        assert metrics.sale_rate.hours == 15

        assert metrics.current_price is not None
        assert metrics.current_price.min_price == 50
        assert metrics.current_price.max_price == 100

        assert metrics.avg_orders_by_month is not None
        assert len(metrics.avg_orders_by_month) == 1
        assert metrics.avg_orders_by_month[0].value == 25.55
