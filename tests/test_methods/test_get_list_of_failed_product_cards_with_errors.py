import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ListOfFailedProductCardsWithErrorsItem


@pytest.mark.unit
class TestGetListOfFailedProductCardsWithErrors:
    async def test_get_list_of_failed_product_cards_with_errors(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "items": [
                        {
                            "batchUUID": "batchUUID",
                            "subjects": {},
                            "brands": {},
                            "vendorCodes": [],
                            "errors": {},
                        }
                    ]
                }
            }
        )

        result = await api.get_list_of_failed_product_cards_with_errors()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfFailedProductCardsWithErrorsItem)
        assert result[0].batch_uuid == "batchUUID"
