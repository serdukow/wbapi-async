import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import BlockedProductCardsItem


@pytest.mark.unit
class TestGetBlockedProductCards:
    async def test_get_blocked_product_cards(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "report": [
                    {
                        "brand": "brand",
                        "nmId": 1,
                        "title": "title",
                        "vendorCode": "vendorCode",
                        "reason": "reason",
                    }
                ]
            }
        )

        result = await api.get_blocked_product_cards(sort="brand", order="desc")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BlockedProductCardsItem)
        assert result[0].brand == "brand"
        assert result[0].nm_id == 1
        assert result[0].title == "title"
