import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductCardsListItem


@pytest.mark.unit
class TestGetProductCardsList:
    async def test_get_product_cards_list(self, api: MockedAPI) -> None:
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
                        "dimensions": {
                            "length": 1,
                            "width": 1,
                            "height": 1,
                            "weightBrutto": 1.0,
                            "isValid": True,
                        },
                        "characteristics": [{"id": 1, "name": "name", "value": None}],
                        "sizes": [{"chrtID": 1, "techSize": "techSize", "wbSize": "wbSize", "skus": []}],
                        "tags": [{"id": 1, "name": "name", "color": "color"}],
                        "createdAt": "createdAt",
                        "updatedAt": "updatedAt",
                    }
                ]
            }
        )

        result = await api.get_product_cards_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductCardsListItem)
        assert result[0].nm_id == 1
        assert result[0].imt_id == 1
        assert result[0].nm_uuid == "nmUUID"
        assert result[0].subject_id == 1
        assert result[0].subject_name == "subjectName"
