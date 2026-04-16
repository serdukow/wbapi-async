import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import TheSupplyBoxQrCodeStickersItem


@pytest.mark.unit
class TestGetTheSupplyBoxQrCodeStickers:
    async def test_get_the_supply_box_qr_code_stickers(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "stickers": [
                    {
                        "barcode": "$WBMP:1:123:1234567",
                        "file": "U3dhZ2dlciByb2Nrcw==",
                    }
                ]
            }
        )

        result = await api.get_the_supply_box_qr_code_stickers(
            supply_id="supply_id", type_="svg", trbx_ids=[]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TheSupplyBoxQrCodeStickersItem)
        assert result[0].barcode == "$WBMP:1:123:1234567"
        assert result[0].file == "U3dhZ2dlciByb2Nrcw=="
