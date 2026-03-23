import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SellerBrandsItem


@pytest.mark.unit
class TestGetSellerBrands:
    async def test_get_seller_brands(self, api: MockedAPI) -> None:
        api.add_response({"data": [{}]})

        result = await api.get_seller_brands()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SellerBrandsItem)
