import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsStatisticsPerPeriodItem


@pytest.mark.unit
class TestGetProductCardsStatisticsPerPeriod:
    async def test_get_product_cards_statistics_per_period(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "products": [
                        {
                            "product": {
                                "nmId": 268913787,
                                "title": "Кроссовки для бега",
                                "vendorCode": "12345456",
                                "brandName": "Demix",
                                "subjectId": 105,
                                "subjectName": "Кроссовки",
                                "tags": [{"id": 1, "name": "Обувь"}],
                                "productRating": 4.5,
                                "feedbackRating": 4,
                                "stocks": {"wb": 0, "mp": 0, "balanceSum": 0},
                            },
                            "statistic": {
                                "selected": {
                                    "period": {"start": "2023-06-01", "end": "2024-03-01"},
                                    "openCount": 45,
                                    "cartCount": 34,
                                    "orderCount": 19,
                                    "orderSum": 1262,
                                    "buyoutCount": 19,
                                    "buyoutSum": 1262,
                                    "cancelCount": 0,
                                    "cancelSum": 0,
                                    "avgPrice": 1262,
                                    "avgOrdersCountPerDay": 0.04,
                                    "shareOrderPercent": 3,
                                    "addToWishlist": 455,
                                    "timeToReady": {"days": 1, "hours": 8, "mins": 34},
                                    "localizationPercent": 46,
                                    "wbClub": {
                                        "orderCount": 19,
                                        "orderSum": 1262,
                                        "buyoutSum": 1262,
                                        "buyoutCount": 19,
                                        "cancelSum": 0,
                                        "cancelCount": 0,
                                        "avgPrice": 1262,
                                        "buyoutPercent": 43,
                                        "avgOrderCountPerDay": 0.04,
                                    },
                                    "conversions": {
                                        "addToCartPercent": 19,
                                        "cartToOrderPercent": 65,
                                        "buyoutPercent": 1,
                                    },
                                },
                                "past": {
                                    "period": {"start": "2023-06-01", "end": "2024-03-01"},
                                    "openCount": 45,
                                    "cartCount": 34,
                                    "orderCount": 19,
                                    "orderSum": 1262,
                                    "buyoutCount": 19,
                                    "buyoutSum": 1262,
                                    "cancelCount": 0,
                                    "cancelSum": 0,
                                    "avgPrice": 1262,
                                    "avgOrdersCountPerDay": 0.04,
                                    "shareOrderPercent": 3,
                                    "addToWishlist": 455,
                                    "timeToReady": {"days": 1, "hours": 8, "mins": 34},
                                    "localizationPercent": 46,
                                    "wbClub": {
                                        "orderCount": 19,
                                        "orderSum": 1262,
                                        "buyoutSum": 1262,
                                        "buyoutCount": 19,
                                        "cancelSum": 0,
                                        "cancelCount": 0,
                                        "avgPrice": 1262,
                                        "buyoutPercent": 43,
                                        "avgOrderCountPerDay": 0.04,
                                    },
                                    "conversions": {
                                        "addToCartPercent": 19,
                                        "cartToOrderPercent": 65,
                                        "buyoutPercent": 1,
                                    },
                                },
                                "comparison": {
                                    "openCountDynamic": 10,
                                    "cartCountDynamic": 30,
                                    "orderCountDynamic": -100,
                                    "orderSumDynamic": -100,
                                    "buyoutCountDynamic": -100,
                                    "buyoutSumDynamic": -100,
                                    "cancelCountDynamic": 0,
                                    "cancelSumDynamic": 0,
                                    "avgOrdersCountPerDayDynamic": 0,
                                    "avgPriceDynamic": -100,
                                    "shareOrderPercentDynamic": -80,
                                    "addToWishlistDynamic": 60,
                                    "timeToReadyDynamic": {"days": 1, "hours": 8, "mins": 34},
                                    "localizationPercentDynamic": 46,
                                    "wbClubDynamic": {
                                        "orderCount": 19,
                                        "orderSum": 1262,
                                        "buyoutSum": 1262,
                                        "buyoutCount": 19,
                                        "cancelSum": 0,
                                        "cancelCount": 0,
                                        "avgPrice": 1262,
                                        "buyoutPercent": 43,
                                        "avgOrderCountPerDay": 0.04,
                                    },
                                    "conversions": {
                                        "addToCartPercent": 19,
                                        "cartToOrderPercent": 65,
                                        "buyoutPercent": 1,
                                    },
                                },
                            },
                        }
                    ]
                }
            }
        )

        result = await api.get_product_cards_statistics_per_period(selected_period={})

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsStatisticsPerPeriodItem)
