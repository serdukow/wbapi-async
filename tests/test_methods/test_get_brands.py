import pytest

from wbapi_async.types import BrandsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetBrands:

    async def test_get_brands(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "brands": [{
                "id": 1,
                "logoUrl": "logoUrl",
                "name": "name",
            }]
        }
        )

        result = await api.get_brands(subject_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BrandsItem)
        assert result[0].id_ == 1
        assert result[0].logo_url == "logoUrl"
        assert result[0].name == "name"
