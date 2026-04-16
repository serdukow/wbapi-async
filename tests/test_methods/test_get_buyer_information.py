import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import BuyerInformationItem


@pytest.mark.unit
class TestGetBuyerInformation:
    async def test_get_buyer_information(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "replacementPhone": "79871234567",
                        "phone": "+79871234567",
                        "firstName": "Иван",
                        "fullName": "Иванов Иван Иванович",
                        "additionalPhones": [],
                        "additionalPhoneCodes": [],
                        "orderId": 1345678910,
                        "phoneCode": 0,
                    }
                ]
            }
        )

        result = await api.get_buyer_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BuyerInformationItem)
        assert result[0].replacement_phone == "79871234567"
        assert result[0].phone == "+79871234567"
        assert result[0].first_name == "Иван"
        assert result[0].full_name == "Иванов Иван Иванович"
