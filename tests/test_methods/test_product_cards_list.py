import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsListItem


@pytest.mark.unit
class TestProductCardsList:
    async def test_product_cards_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "cards": [
                    {
                        "nmID": 1,
                        "imtID": 1,
                        "nmUUID": "nmUUID",
                        "subjectID": 1,
                        "subjectName": "subjectName",
                        "vendorCode": "vendorCode",
                        "brand": "brand",
                        "title": "title",
                        "description": "description",
                        "needKiz": True,
                        "kizMarked": True,
                        "photos": [],
                        "video": "video",
                        "wholesale": {},
                        "dimensions": {},
                        "characteristics": [],
                        "sizes": [],
                        "tags": [],
                        "createdAt": "createdAt",
                        "updatedAt": "updatedAt",
                    }
                ]
            }
        )

        result = await api.product_cards_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsListItem)
        assert result[0].nm_id == 1
        assert result[0].imt_id == 1
        assert result[0].nm_uuid == "nmUUID"
