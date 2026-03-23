import pytest

from wbapi_async.types import CheckIfTheOrderBelongsToTheBuyerResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestCheckIfTheOrderBelongsToTheBuyer:

    async def test_check_if_the_order_belongs_to_the_buyer(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "ok": True,
            }]
        )

        result = await api.check_if_the_order_belongs_to_the_buyer()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CheckIfTheOrderBelongsToTheBuyerResponse)
        assert result[0].ok == True
