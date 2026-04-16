import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CheckTheStatusResponse


@pytest.mark.unit
class TestGetCheckTheStatus:
    async def test_get_check_the_status(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {"id": "id", "status": "status"},
                }
            ]
        )

        result = await api.get_check_the_status(task_id="task_id")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CheckTheStatusResponse)
