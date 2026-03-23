import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import RecoverProductCardFromTrashResponse


@pytest.mark.unit
class TestRecoverProductCardFromTrash:
    async def test_recover_product_card_from_trash(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                    "error": True,
                    "errorText": "errorText",
                    "additionalErrors": {},
                }
            ]
        )

        result = await api.recover_product_card_from_trash()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], RecoverProductCardFromTrashResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
