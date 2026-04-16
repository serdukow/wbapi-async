import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AcceptanceOptionsItem


@pytest.mark.unit
class TestGetAcceptanceOptions:
    async def test_get_acceptance_options(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "result": [
                    {
                        "barcode": "barcode",
                        "error": {"title": "title", "detail": "detail"},
                        "isError": True,
                        "warehouses": [
                            {
                                "warehouseID": 1,
                                "canBox": True,
                                "canMonopallet": True,
                                "canSupersafe": True,
                                "isBoxOnPallet": True,
                            }
                        ],
                    }
                ]
            }
        )

        result = await api.get_acceptance_options()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AcceptanceOptionsItem)
        assert result[0].barcode == "barcode"
        assert result[0].is_error
