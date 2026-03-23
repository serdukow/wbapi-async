import pytest

from wbapi_async.types import ProductCardsStatisticsPerDaysResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestProductCardsStatisticsPerDays:

    async def test_product_cards_statistics_per_days(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "product": None,
                "history": [],
                "currency": "currency",
            }]
        )

        result = await api.product_cards_statistics_per_days(selected_period=None, nm_ids=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsStatisticsPerDaysResponse)
        assert result[0].history == []
        assert result[0].currency == "currency"
