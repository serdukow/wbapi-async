import pytest

from wbapi_async.types.product_cards_statistics import ProductCardStatistics

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetProductCardsStatistics:

    async def test_get_product_cards_statistics(self, api: MockedAPI) -> None:
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
                                    "period": {
                                        "start": "2023-06-01",
                                        "end": "2024-03-01",
                                    },
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
                                        "buyoutPercent": 0,
                                    },
                                },
                                "past": None,
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
                                        "orderCount": -100,
                                        "orderSum": -100,
                                        "buyoutSum": -100,
                                        "buyoutCount": -100,
                                        "cancelSum": 0,
                                        "cancelCount": 0,
                                        "avgPrice": -100,
                                        "buyoutPercent": 43,
                                        "avgOrderCountPerDay": 0.04,
                                    },
                                    "conversions": {
                                        "addToCartPercent": 19,
                                        "cartToOrderPercent": 65,
                                        "buyoutPercent": 0,
                                    },
                                },
                            },
                        }
                    ],
                    "currency": "RUB",
                }
            }
        )

        result = await api.get_product_cards_statistics_per_period(
            date_from="2023-06-01",
            date_to="2024-03-01",
        )

        assert isinstance(result, list)
        assert len(result) == 1

        item = result[0]
        assert isinstance(item, ProductCardStatistics)

        product = item.product
        assert product is not None
        assert product.nm_id == 268913787
        assert product.title == "Кроссовки для бега"
        assert product.brand_name == "Demix"
        assert product.product_rating == 4.5
        assert product.tags is not None
        assert product.tags[0].name == "Обувь"

        statistic = item.statistic
        assert statistic is not None

        selected = statistic.selected
        assert selected is not None
        assert selected.open_count == 45
        assert selected.order_count == 19
        assert selected.buyout_sum == 1262
        assert selected.time_to_ready is not None
        assert selected.time_to_ready.days == 1
        assert selected.time_to_ready.hours == 8
        assert selected.wb_club is not None
        assert selected.wb_club.buyout_percent == 43
        assert selected.conversions is not None
        assert selected.conversions.cart_to_order_percent == 65

        comparison = statistic.comparison
        assert comparison is not None
        assert comparison.open_count_dynamic == 10
        assert comparison.order_count_dynamic == -100
        assert comparison.wb_club_dynamic is not None
        assert comparison.wb_club_dynamic.avg_order_count_per_day == 0.04
