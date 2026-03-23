import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestUpdateUsersAccessPermissions:

    async def test_update_users_access_permissions(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.update_users_access_permissions(users_accesses=[])

        assert result is None
