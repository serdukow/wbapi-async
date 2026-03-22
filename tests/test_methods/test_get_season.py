import pytest

from wbapi_async.types import SeasonItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSeason:

    async def test_get_season(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{

            }]
        }
        )

        result = await api.get_season()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SeasonItem)
