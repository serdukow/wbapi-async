import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductDataItem


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
                                    {"start": "2025-01-01", "end": "2025-01-31", "value": 25.55}
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
                            },
                        }
                    ]
                }
            }
        )

        result = await api.get_product_data(
            current_period={"start": "2024-02-10", "end": "2024-02-10"},
            stock_type="",
            skip_deleted_nm=True,
            order_by={"field": "openCard", "mode": "asc"},
            availability_filters=[],
            offset=1,
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductDataItem)
        assert result[0].nm_id == 123456789
        assert not result[0].is_deleted
        assert result[0].subject_name == "Принтеры"
        assert result[0].name == "Печатник 3000"
        assert result[0].vendor_code == "pechatnik3000"
