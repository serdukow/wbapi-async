import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AListOfSellerActiveOrInvitedUsersItem


@pytest.mark.unit
class TestGetAListOfSellerActiveOrInvitedUsers:
    async def test_get_a_list_of_seller_active_or_invited_users(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "users": [
                    {
                        "id": 1,
                        "role": "user",
                        "position": "position",
                        "phone": "phone",
                        "email": "email",
                        "isOwner": True,
                        "firstName": "firstName",
                        "secondName": "secondName",
                        "patronymic": "patronymic",
                        "goodsReturn": True,
                        "isInvitee": True,
                        "inviteeInfo": {
                            "phoneNumber": "phoneNumber",
                            "position": "position",
                            "inviteUuid": "inviteUuid",
                            "expiredAt": "expiredAt",
                            "isActive": True,
                        },
                        "access": [{"code": "balance", "disabled": True}],
                    }
                ]
            }
        )

        result = await api.get_a_list_of_seller_active_or_invited_users()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AListOfSellerActiveOrInvitedUsersItem)
        assert result[0].id_ == 1
        assert result[0].role == "user"
        assert result[0].position == "position"
        assert result[0].phone == "phone"
        assert result[0].email == "email"
