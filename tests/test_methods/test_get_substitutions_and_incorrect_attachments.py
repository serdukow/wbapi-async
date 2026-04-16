import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SubstitutionsAndIncorrectAttachmentsItem


@pytest.mark.unit
class TestGetSubstitutionsAndIncorrectAttachments:
    async def test_get_substitutions_and_incorrect_attachments(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "reports": [
                        {
                            "dtBonus": "2025-06-02T00:00:00Z",
                            "nmId": 544454,
                            "oldShkId": 26624352356,
                            "oldColor": "темно-синий,голубой",
                            "oldSize": "A",
                            "oldSku": "54532562",
                            "oldVendorCode": "23535 Стемпинг 500",
                            "newShkId": 123333223,
                            "newColor": "темно-синий,голубой",
                            "newSize": "A",
                            "newSku": "12323332223",
                            "newVendorCode": "wh-service-podmena",
                            "bonusSumm": 247.5,
                            "bonusType": "Подмена FBW",
                            "photoUrls": [],
                        }
                    ]
                }
            }
        )

        result = await api.get_substitutions_and_incorrect_attachments(date_to="date_to", limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SubstitutionsAndIncorrectAttachmentsItem)
        assert result[0].dt_bonus == "2025-06-02T00:00:00Z"
        assert result[0].nm_id == 544454
        assert result[0].old_shk_id == 26624352356
        assert result[0].old_color == "темно-синий,голубой"
        assert result[0].old_size == "A"
