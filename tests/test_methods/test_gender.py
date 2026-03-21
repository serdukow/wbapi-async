import pytest

from wbapi_async.types.gender_item import GenderItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGender:

    async def test_gender(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{

            }]
        }
        )

        result = await api.gender()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GenderItem)
