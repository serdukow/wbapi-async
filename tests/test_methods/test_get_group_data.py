import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import GroupDataItem


@pytest.mark.unit
class TestGetGroupData:
    async def test_get_group_data(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "groups": [
                        {
                            "subjectID": 123456789,
                            "subjectName": "Кружка",
                            "brandName": "Крутая посуда",
                            "tagID": 12345,
                            "tagName": "Человек-Паук",
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
                            ],
                        }
                    ]
                }
            }
        )

        result = await api.get_group_data(
            current_period={},
            stock_type="stock_type",
            skip_deleted_nm=True,
            availability_filters=[],
            order_by={},
            offset=1,
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GroupDataItem)
        assert result[0].subject_id == 123456789
        assert result[0].subject_name == "Кружка"
        assert result[0].brand_name == "Крутая посуда"
        assert result[0].tag_id == 12345
        assert result[0].tag_name == "Человек-Паук"
