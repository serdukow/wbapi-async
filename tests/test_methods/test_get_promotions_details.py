import pytest

from wbapi_async.types.promotions_details_item import PromotionsDetailsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetPromotionsDetails:

    async def test_get_promotions_details(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "promotions": [{
                "id": 1,
                "name": "name",
                "description": "description",
                "advantages": [],
                "startDateTime": "startDateTime",
                "endDateTime": "endDateTime",
                "inPromoActionLeftovers": 1,
                "inPromoActionTotal": 1,
                "notInPromoActionLeftovers": 1,
                "notInPromoActionTotal": 1,
                "participationPercentage": 1,
                "type": "type",
                "exceptionProductsCount": 1,
                "ranging": [],
            }]
        }
        }
        )

        result = await api.get_promotions_details(promotion_i_ds=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PromotionsDetailsItem)
        assert result[0].id == 1
        assert result[0].name == "name"
        assert result[0].description == "description"
