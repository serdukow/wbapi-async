import pytest

from wbapi_async.types import SetWbClubDiscountsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSetWbClubDiscounts:

    async def test_set_wb_club_discounts(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "data": {},
                "error": True,
                "errorText": "errorText",
            }]
        )

        result = await api.set_wb_club_discounts(data=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SetWbClubDiscountsResponse)
        assert result[0].data == {}
        assert result[0].error == True
        assert result[0].error_text == "errorText"
