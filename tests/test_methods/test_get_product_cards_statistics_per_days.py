import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsStatisticsPerDaysResponse


@pytest.mark.unit
class TestGetProductCardsStatisticsPerDays:
    async def test_get_product_cards_statistics_per_days(self, api: MockedAPI) -> None:
        api.add_response(
            [
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
                    "history": [
                        {
                            "date": "2024-10-23",
                            "openCount": 45,
                            "cartCount": 34,
                            "orderCount": 19,
                            "orderSum": 1262,
                            "buyoutCount": 19,
                            "buyoutSum": 1262,
                            "buyoutPercent": 35,
                            "addToCartConversion": 43,
                            "cartToOrderConversion": 1,
                            "addToWishlistCount": 1,
                        }
                    ],
                    "currency": "RUB",
                }
            ]
        )

        result = await api.get_product_cards_statistics_per_days(
            selected_period={"start": "2023-06-01", "end": "2024-03-01"}, nm_ids=[]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsStatisticsPerDaysResponse)
        assert result[0].currency == "RUB"
