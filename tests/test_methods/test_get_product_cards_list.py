import pytest

from wbapi_async.types.product_cards_list_item import ProductCardsListItem

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetProductCardsList:

    async def test_get_product_cards_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "cards": [
                    {
                        "nmID": 12345678,
                        "imtID": 123654789,
                        "nmUUID": "01bda0b1-0000-0000-0000-000000000000",
                        "subjectID": 7771,
                        "subjectName": "AKF системы",
                        "vendorCode": "wb7f6mumjr1",
                        "brand": "Тест",
                        "title": "Тест-система",
                        "description": "Тестовое описание",
                        "needKiz": False,
                        "photos": [{"big": "https://example.com/big.jpg"}],
                        "video": "https://example.com/video.mp4",
                        "wholesale": {"enabled": True, "quantum": 112},
                        "dimensions": {"length": 55, "weightBrutto": 6.24, "isValid": False},
                        "characteristics": [{"id": 14177449, "name": "Цвет", "value": ["красно-сиреневый"]}],
                        "sizes": [{"chrtID": 316399238, "techSize": "0", "skus": ["987456321654"]}],
                        "tags": [{"id": 592569, "name": "Популярный", "color": "D1CFD7"}],
                        "createdAt": "2023-12-06T11:17:00.96577Z",
                        "updatedAt": "2023-12-06T11:17:00.96577Z",
                    }
                ],
                "cursor": {"total": 1, "limit": 100, "updatedAt": "2023-12-06T11:17:00.96577Z", "nmID": 12345678},
            }
        )

        result = await api.product_cards_list()

        assert isinstance(result, list)
        assert len(result) == 1

        card = result[0]
        assert isinstance(card, ProductCardsListItem)
        assert card.nm_id == 12345678
        assert card.imt_id == 123654789
        assert card.nm_uuid == "01bda0b1-0000-0000-0000-000000000000"
        assert card.subject_id == 7771
        assert card.subject_name == "AKF системы"
        assert card.vendor_code == "wb7f6mumjr1"
        assert card.brand == "Тест"
        assert card.title == "Тест-система"
        assert card.description == "Тестовое описание"
        assert card.need_kiz is False
        assert card.created_at == "2023-12-06T11:17:00.96577Z"
        assert card.updated_at == "2023-12-06T11:17:00.96577Z"

        assert card.photos is not None
        assert len(card.photos) == 1
        assert card.photos[0]["big"] == "https://example.com/big.jpg"

        assert card.wholesale is not None
        assert card.wholesale["enabled"] is True
        assert card.wholesale["quantum"] == 112

        assert card.dimensions is not None
        assert card.dimensions["length"] == 55

        assert card.characteristics is not None
        assert len(card.characteristics) == 1
        assert card.characteristics[0]["name"] == "Цвет"

        assert card.sizes is not None
        assert len(card.sizes) == 1
        assert card.sizes[0]["chrtID"] == 316399238

        assert card.tags is not None
        assert len(card.tags) == 1
        assert card.tags[0]["name"] == "Популярный"

    async def test_get_product_cards_list_with_locale(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "cards": [{"nmID": 99999999, "vendorCode": "sku-en"}],
                "cursor": {"total": 1, "limit": 100},
            }
        )

        result = await api.product_cards_list(locale="en")

        assert isinstance(result, list)
        assert len(result) == 1

        last_request = api.get_last_request()
        assert last_request.json is not None
        assert last_request.json.get("locale") == "en"
