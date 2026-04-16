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
                        "brand": "Трикотаж",
                        "nmId": 166658151,
                        "title": "ВАЗ",
                        "vendorCode": "DP02/черный",
                        "nmRating": 3.1,
                    }
                ]
            }
        )

        result = await api.get_hidden_from_the_catalog(sort="brand", order="asc")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], HiddenFromTheCatalogItem)
        assert result[0].brand == "Трикотаж"
        assert result[0].nm_id == 166658151
        assert result[0].title == "ВАЗ"
        assert result[0].vendor_code == "DP02/черный"
        assert result[0].nm_rating == 3.1
