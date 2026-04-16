import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddProductToThePromotionResponse


@pytest.mark.unit
class TestAddProductToThePromotion:
    async def test_add_product_to_the_promotion(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {"alreadyExists": False, "uploadID": 11},
                }
            ]
        )

        result = await api.add_product_to_the_promotion()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddProductToThePromotionResponse)
