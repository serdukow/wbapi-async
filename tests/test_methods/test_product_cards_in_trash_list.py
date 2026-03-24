import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsInTrashListItem


@pytest.mark.unit
class TestProductCardsInTrashList:
    async def test_product_cards_in_trash_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "cards": [
                    {
                        "nmID": 1,
                        "vendorCode": "vendorCode",
                        "subjectID": 1,
                        "subjectName": "subjectName",
                        "photos": [],
                        "video": "video",
                        "wholesale": {},
                        "sizes": [],
                        "dimensions": {},
                        "characteristics": [],
                        "createdAt": "createdAt",
                        "trashedAt": "trashedAt",
                    }
                ]
            }
        )

        result = await api.product_cards_in_trash_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsInTrashListItem)
        assert result[0].nm_id == 1
        assert result[0].vendor_code == "vendorCode"
        assert result[0].subject_id == 1
