import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsStatisticsPerPeriodResponse


@pytest.mark.unit
class TestProductCardsStatisticsPerPeriod:
    async def test_product_cards_statistics_per_period(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": None,
                }
            ]
        )

        result = await api.product_cards_statistics_per_period(selected_period=None)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsStatisticsPerPeriodResponse)
