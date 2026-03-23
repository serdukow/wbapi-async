import pytest

from wbapi_async.types import TheSupplyQrCodeResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetTheSupplyQrCode:

    async def test_get_the_supply_qr_code(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "barcode": "barcode",
                "file": "file",
            }]
        )

        result = await api.get_the_supply_qr_code(supply_id="supply_id", type_="svg")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TheSupplyQrCodeResponse)
        assert result[0].barcode == "barcode"
        assert result[0].file == "file"
