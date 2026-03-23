import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import BrandsItem


@pytest.mark.unit
class TestGetBrands:
    async def test_get_brands(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "brands": [
                    {
                        "id": 1,
                        "logoUrl": "logoUrl",
                        "name": "name",
                    }
                ]
            }
        )

        result = await api.get_brands(subject_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BrandsItem)
        assert result[0].id == 1
        assert result[0].logo_url == "logoUrl"
        assert result[0].name == "name"
