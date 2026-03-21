import pytest

from wbapi_async.types.season_item import SeasonItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSeason:

    async def test_season(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{

            }]
        }
        )

        result = await api.season()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SeasonItem)
