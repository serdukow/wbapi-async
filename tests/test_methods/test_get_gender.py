import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import GenderItem


@pytest.mark.unit
class TestGetGender:
    async def test_get_gender(self, api: MockedAPI) -> None:
        api.add_response({"data": [{}]})

        result = await api.get_gender()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GenderItem)
