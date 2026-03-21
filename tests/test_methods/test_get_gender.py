import pytest

from wbapi_async.types.gender_item import GenderItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetGender:

    async def test_get_gender(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{

            }]
        }
        )

        result = await api.get_gender()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GenderItem)
