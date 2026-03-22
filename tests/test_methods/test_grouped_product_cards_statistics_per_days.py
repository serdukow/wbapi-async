import pytest

from wbapi_async.types import GroupedProductCardsStatisticsPerDaysItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGroupedProductCardsStatisticsPerDays:

    async def test_grouped_product_cards_statistics_per_days(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{
                "product": None,
                "history": [],
                "currency": "currency",
            }]
        }
        )

        result = await api.grouped_product_cards_statistics_per_days(selected_period=None)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GroupedProductCardsStatisticsPerDaysItem)
        assert result[0].history == []
        assert result[0].currency == "currency"
