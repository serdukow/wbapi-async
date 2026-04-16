import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import MainPageResponse


@pytest.mark.unit
class TestGetMainPage:
    async def test_get_main_page(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                }
            ]
        )

        result = await api.get_main_page(
            current_period={}, position_cluster="position_cluster", order_by={}, limit=1, offset=1
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MainPageResponse)
