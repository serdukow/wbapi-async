import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CreateAnInvitationForANewUserResponse


@pytest.mark.unit
class TestCreateAnInvitationForANewUser:
    async def test_create_an_invitation_for_a_new_user(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "inviteID": "inviteID",
                    "expiredAt": "expiredAt",
                    "isSuccess": True,
                    "inviteUrl": "inviteUrl",
                }
            ]
        )

        result = await api.create_an_invitation_for_a_new_user(invite={})

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreateAnInvitationForANewUserResponse)
        assert result[0].invite_id == "inviteID"
        assert result[0].expired_at == "expiredAt"
        assert result[0].is_success
