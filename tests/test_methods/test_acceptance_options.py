import pytest

from wbapi_async.types.acceptance_options_item import AcceptanceOptionsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAcceptanceOptions:

    async def test_acceptance_options(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "result": [{
                "barcode": "barcode",
                "error": {},
                "isError": True,
                "warehouses": [],
            }]
        }
        )

        result = await api.acceptance_options()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AcceptanceOptionsItem)
        assert result[0].barcode == "barcode"
        assert result[0].error == {}
        assert result[0].is_error == True
