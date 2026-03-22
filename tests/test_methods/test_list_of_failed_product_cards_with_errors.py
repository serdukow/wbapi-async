import pytest

from wbapi_async.types import ListOfFailedProductCardsWithErrorsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestListOfFailedProductCardsWithErrors:

    async def test_list_of_failed_product_cards_with_errors(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "items": [{
                "batchUUID": "batchUUID",
                "subjects": {},
                "brands": {},
                "vendorCodes": [],
                "errors": {},
            }]
        }
        }
        )

        result = await api.list_of_failed_product_cards_with_errors()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfFailedProductCardsWithErrorsItem)
        assert result[0].batch_uuid == "batchUUID"
        assert result[0].subjects == {}
        assert result[0].brands == {}
