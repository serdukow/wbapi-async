import pytest

from wbapi_async.types import ProcessedUploadDetailsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetProcessedUploadDetails:

    async def test_get_processed_upload_details(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "historyGoods": [{
                "nmID": 1,
                "vendorCode": "vendorCode",
                "sizeID": 1,
                "techSizeName": "techSizeName",
                "price": 1,
                "currencyIsoCode4217": "currencyIsoCode4217",
                "discount": 1,
                "clubDiscount": 1,
                "status": 1,
                "errorText": "errorText",
            }]
        }
        }
        )

        result = await api.get_processed_upload_details(limit=1, upload_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProcessedUploadDetailsItem)
        assert result[0].nm_id == 1
        assert result[0].vendor_code == "vendorCode"
        assert result[0].size_id == 1
