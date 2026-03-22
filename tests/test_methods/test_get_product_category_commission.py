import pytest

from wbapi_async.types.product_category_commission_response import ProductCategoryCommissionResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetProductCategoryCommission:

    async def test_get_product_category_commission(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.get_product_category_commission()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCategoryCommissionResponse)
