import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import WarehouseDataItem


@pytest.mark.unit
class TestGetWarehouseData:
    async def test_get_warehouse_data(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "regions": [
                        {
                            "regionName": "Центральный",
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
                            "offices": [
                                {
                                    "officeID": 123456,
                                    "officeName": "Коледино",
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
                            ],
                        }
                    ]
                }
            }
        )

        result = await api.get_warehouse_data()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WarehouseDataItem)
        assert result[0].region_name == "Центральный"
