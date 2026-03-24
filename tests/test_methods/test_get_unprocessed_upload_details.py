import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import UnprocessedUploadDetailsItem


@pytest.mark.unit
class TestGetUnprocessedUploadDetails:
    async def test_get_unprocessed_upload_details(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "bufferGoods": [
                        {
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
                        }
                    ]
                }
            }
        )

        result = await api.get_unprocessed_upload_details(limit=1, upload_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], UnprocessedUploadDetailsItem)
        assert result[0].nm_id == 1
        assert result[0].vendor_code == "vendorCode"
        assert result[0].size_id == 1
