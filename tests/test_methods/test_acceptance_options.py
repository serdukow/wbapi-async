import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AcceptanceOptionsItem


@pytest.mark.unit
class TestAcceptanceOptions:
    async def test_acceptance_options(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "result": [
                    {
                        "barcode": "barcode",
                        "error": {},
                        "isError": True,
                        "warehouses": [],
                    }
                ]
            }
        )

        result = await api.acceptance_options()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AcceptanceOptionsItem)
        assert result[0].barcode == "barcode"
        assert result[0].error == {}
        assert result[0].is_error
