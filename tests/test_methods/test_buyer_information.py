import pytest

from wbapi_async.types.buyer_information_item import BuyerInformationItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestBuyerInformation:

    async def test_buyer_information(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "orders": [{
                "replacementPhone": "replacementPhone",
                "phone": "phone",
                "firstName": "firstName",
                "fullName": "fullName",
                "additionalPhones": [],
                "additionalPhoneCodes": [],
                "orderId": 1,
                "phoneCode": 1,
            }]
        }
        )

        result = await api.buyer_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BuyerInformationItem)
        assert result[0].replacement_phone == "replacementPhone"
        assert result[0].phone == "phone"
        assert result[0].first_name == "firstName"
