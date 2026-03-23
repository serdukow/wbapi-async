import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import TransferProductCardToTrashResponse


@pytest.mark.unit
class TestTransferProductCardToTrash:
    async def test_transfer_product_card_to_trash(self, api: MockedAPI) -> None:
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

        result = await api.transfer_product_card_to_trash()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TransferProductCardToTrashResponse)
        assert result[0].data == {}
        assert result[0].error
        assert result[0].error_text == "errorText"
