import pytest

from wbapi_async.types.substitutions_and_incorrect_attachments_item import SubstitutionsAndIncorrectAttachmentsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSubstitutionsAndIncorrectAttachments:

    async def test_get_substitutions_and_incorrect_attachments(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "reports": [{
                "dtBonus": "dtBonus",
                "nmId": 1,
                "oldShkId": 1,
                "oldColor": "oldColor",
                "oldSize": "oldSize",
                "oldSku": "oldSku",
                "oldVendorCode": "oldVendorCode",
                "newShkId": 1,
                "newColor": "newColor",
                "newSize": "newSize",
                "newSku": "newSku",
                "newVendorCode": "newVendorCode",
                "bonusSumm": 1.0,
                "bonusType": "bonusType",
                "photoUrls": [],
            }]
        }
        }
        )

        result = await api.get_substitutions_and_incorrect_attachments(date_to="date_to", limit=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SubstitutionsAndIncorrectAttachmentsItem)
        assert result[0].dt_bonus == "dtBonus"
        assert result[0].nm_id == 1
        assert result[0].old_shk_id == 1
