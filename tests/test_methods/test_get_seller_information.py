import pytest

from wbapi_async.types import SellerInformationResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSellerInformation:

    async def test_get_seller_information(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "name": "name",
                "sid": "sid",
                "tin": "tin",
                "tradeMark": "tradeMark",
            }]
        )

        result = await api.get_seller_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SellerInformationResponse)
        assert result[0].name == "name"
        assert result[0].sid == "sid"
        assert result[0].tin == "tin"
