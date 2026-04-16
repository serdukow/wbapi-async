import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import TagsListResponse


@pytest.mark.unit
class TestGetTagsList:
    async def test_get_tags_list(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": None,
                    "error": False,
                    "errorText": "",
                    "additionalErrors": "",
                }
            ]
        )

        result = await api.get_tags_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TagsListResponse)
        assert not result[0].error
        assert result[0].error_text == ""
        assert result[0].additional_errors == ""
