import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteUser:
    async def test_delete_user(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.delete_user(deleted_user_id=1)

        assert result is None
