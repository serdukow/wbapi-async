import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SetWbClubDiscountsResponse


@pytest.mark.unit
class TestSetWbClubDiscounts:
    async def test_set_wb_club_discounts(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {"id": 1, "alreadyExists": False},
                    "error": False,
                    "errorText": "",
                }
            ]
        )

        result = await api.set_wb_club_discounts(data=[{"nmID": 123, "clubDiscount": 5}])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SetWbClubDiscountsResponse)
        assert not result[0].error
        assert result[0].error_text == ""
