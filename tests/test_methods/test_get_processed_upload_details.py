import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProcessedUploadDetailsItem


@pytest.mark.unit
class TestGetProcessedUploadDetails:
    async def test_get_processed_upload_details(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "historyGoods": [
                        {
                            "nmID": 544833232,
                            "vendorCode": "34552332",
                            "sizeID": 54483342,
                            "techSizeName": "42",
                            "price": 1500,
                            "currencyIsoCode4217": "RUB",
                            "discount": 25,
                            "clubDiscount": 5,
                            "status": 1,
                            "errorText": "You can't change the item price. Item was added to the Sale due to high inventory",
                        }
                    ]
                }
            }
        )

        result = await api.get_processed_upload_details(limit=1, upload_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProcessedUploadDetailsItem)
        assert result[0].nm_id == 544833232
        assert result[0].vendor_code == "34552332"
        assert result[0].size_id == 54483342
        assert result[0].tech_size_name == "42"
        assert result[0].price == 1500
