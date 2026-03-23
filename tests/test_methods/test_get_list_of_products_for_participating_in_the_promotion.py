import pytest

from wbapi_async.types import ListOfProductsForParticipatingInThePromotionItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetListOfProductsForParticipatingInThePromotion:

    async def test_get_list_of_products_for_participating_in_the_promotion(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "nomenclatures": [{
                "id": 1,
                "inAction": True,
                "price": 1.0,
                "currencyCode": "currencyCode",
                "planPrice": 1.0,
                "discount": 1,
                "planDiscount": 1,
            }]
        }
        }
        )

        result = await api.get_list_of_products_for_participating_in_the_promotion(promotion_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfProductsForParticipatingInThePromotionItem)
        assert result[0].id_ == 1
        assert result[0].in_action == True
        assert result[0].price == 1.0
