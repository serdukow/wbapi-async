import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import TheSupplyQrCodeResponse


@pytest.mark.unit
class TestGetTheSupplyQrCode:
    async def test_get_the_supply_qr_code(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "barcode": "WB-GI-12345678",
                    "file": "U3dhZ2dlciByb2Nrcw==",
                }
            ]
        )

        result = await api.get_the_supply_qr_code(supply_id="supply_id", type_="svg")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TheSupplyQrCodeResponse)
        assert result[0].barcode == "WB-GI-12345678"
        assert result[0].file == "U3dhZ2dlciByb2Nrcw=="
