import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DeleteTheTagResponse


@pytest.mark.unit
class TestDeleteTheTag:
    async def test_delete_the_tag(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "error": True,
                    "errorText": "errorText",
                    "additionalErrors": "additionalErrors",
                }
            ]
        )

        result = await api.delete_the_tag(id_=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DeleteTheTagResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
