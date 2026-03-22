import pytest

from wbapi_async.types import TagsListResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetTagsList:

    async def test_get_tags_list(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": None,
                "error": True,
                "errorText": "errorText",
                "additionalErrors": "additionalErrors",
            }]
        )

        result = await api.get_tags_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TagsListResponse)
        assert result[0].error == True
        assert result[0].error_text == "errorText"
