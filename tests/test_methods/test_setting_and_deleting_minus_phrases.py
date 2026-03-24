import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSettingAndDeletingMinusPhrases:
    async def test_setting_and_deleting_minus_phrases(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.setting_and_deleting_minus_phrases(advert_id=1, nm_id=1, norm_queries=[])

        assert result is None
