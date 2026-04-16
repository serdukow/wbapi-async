import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CheckIfTheOrderBelongsToTheBuyerResponse


@pytest.mark.unit
class TestGetCheckIfTheOrderBelongsToTheBuyer:
    async def test_get_check_if_the_order_belongs_to_the_buyer(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "ok": True,
                }
            ]
        )

        result = await api.get_check_if_the_order_belongs_to_the_buyer()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CheckIfTheOrderBelongsToTheBuyerResponse)
        assert result[0].ok
