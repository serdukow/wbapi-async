import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsInTrashListItem


@pytest.mark.unit
class TestGetProductCardsInTrashList:
    async def test_get_product_cards_in_trash_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "cards": [
                    {
                        "nmID": 1,
                        "vendorCode": "vendorCode",
                        "subjectID": 1,
                        "subjectName": "subjectName",
                        "photos": [
                            {
                                "big": "big",
                                "c246x328": "c246x328",
                                "c516x688": "c516x688",
                                "square": "square",
                                "tm": "tm",
                            }
                        ],
                        "video": "video",
                        "wholesale": {"enabled": True, "quantum": 1.0},
                        "sizes": [{"chrtID": 1, "techSize": "techSize", "wbSize": "wbSize", "skus": []}],
                        "dimensions": {
                            "length": 1,
                            "width": 1,
                            "height": 1,
                            "weightBrutto": 1.0,
                            "isValid": True,
                        },
                        "characteristics": [{"id": 1, "name": "name", "value": None}],
                        "createdAt": "createdAt",
                        "trashedAt": "trashedAt",
                    }
                ]
            }
        )

        result = await api.get_product_cards_in_trash_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsInTrashListItem)
        assert result[0].nm_id == 1
        assert result[0].vendor_code == "vendorCode"
        assert result[0].subject_id == 1
        assert result[0].subject_name == "subjectName"
