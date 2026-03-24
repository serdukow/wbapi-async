import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import HiddenFromTheCatalogItem


@pytest.mark.unit
class TestGetHiddenFromTheCatalog:
    async def test_get_hidden_from_the_catalog(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "report": [
                    {
                        "brand": "brand",
                        "nmId": 1,
                        "title": "title",
                        "vendorCode": "vendorCode",
                        "nmRating": 1.0,
                    }
                ]
            }
        )

        result = await api.get_hidden_from_the_catalog(sort="brand", order="desc")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], HiddenFromTheCatalogItem)
        assert result[0].brand == "brand"
        assert result[0].nm_id == 1
        assert result[0].title == "title"
