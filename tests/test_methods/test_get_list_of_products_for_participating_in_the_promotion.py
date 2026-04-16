import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ListOfProductsForParticipatingInThePromotionItem


@pytest.mark.unit
class TestGetListOfProductsForParticipatingInThePromotion:
    async def test_get_list_of_products_for_participating_in_the_promotion(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "nomenclatures": [
                        {
                            "id": 162579635,
                            "inAction": True,
                            "price": 1500,
                            "currencyCode": "RUB",
                            "planPrice": 1000,
                            "discount": 15,
                            "planDiscount": 34,
                        }
                    ]
                }
            }
        )

        result = await api.get_list_of_products_for_participating_in_the_promotion(promotion_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfProductsForParticipatingInThePromotionItem)
        assert result[0].id_ == 162579635
        assert result[0].in_action
        assert result[0].price == 1500
        assert result[0].currency_code == "RUB"
        assert result[0].plan_price == 1000
