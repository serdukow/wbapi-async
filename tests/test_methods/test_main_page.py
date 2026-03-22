import pytest

from wbapi_async.types.main_page_response import MainPageResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestMainPage:

    async def test_main_page(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.main_page(current_period={}, position_cluster="position_cluster", order_by={}, limit=1, offset=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MainPageResponse)
