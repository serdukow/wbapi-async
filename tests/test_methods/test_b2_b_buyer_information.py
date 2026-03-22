import pytest

from wbapi_async.types import B2BBuyerInformationItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestB2BBuyerInformation:

    async def test_b2b_buyer_information(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "results": [{
                "data": {},
                "errors": [],
                "isError": True,
                "orderId": 1,
            }]
        }
        )

        result = await api.b2b_buyer_information()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], B2BBuyerInformationItem)
        assert result[0].data == {}
        assert result[0].errors == []
        assert result[0].is_error == True
