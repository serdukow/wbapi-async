import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import MinimumBidsForProductCardsItem


@pytest.mark.unit
class TestMinimumBidsForProductCards:
    async def test_minimum_bids_for_product_cards(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "bids": [
                    {
                        "bids": [],
                        "nm_id": 1,
                    }
                ]
            }
        )

        result = await api.minimum_bids_for_product_cards(
            advert_id=1, nm_ids=[], payment_type="cpm", placement_types=[]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MinimumBidsForProductCardsItem)
        assert result[0].bids == []
        assert result[0].nm_id == 1
