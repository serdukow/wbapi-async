import pytest

from wbapi_async.types.recover_product_card_from_trash_response import RecoverProductCardFromTrashResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestRecoverProductCardFromTrash:

    async def test_recover_product_card_from_trash(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": {},
                "error": True,
                "errorText": "errorText",
                "additionalErrors": {},
            }]
        )

        result = await api.recover_product_card_from_trash()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], RecoverProductCardFromTrashResponse)
        assert result[0].data == {}
        assert result[0].error == True
        assert result[0].error_text == "errorText"
