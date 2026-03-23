import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SupplyPackageResponse


@pytest.mark.unit
class TestGetSupplyPackage:
    async def test_get_supply_package(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "packageCode": "packageCode",
                    "quantity": 1,
                    "barcodes": [],
                }
            ]
        )

        result = await api.get_supply_package(id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SupplyPackageResponse)
        assert result[0].package_code == "packageCode"
        assert result[0].quantity == 1
        assert result[0].barcodes == []
