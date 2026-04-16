import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ReceivingTheHistoryOfAccountTopupsResponse


@pytest.mark.unit
class TestGetReceivingTheHistoryOfAccountTopups:
    async def test_get_receiving_the_history_of_account_topups(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "id": 1,
                    "date": "date",
                    "sum": 1,
                    "type": 1,
                    "statusId": 1,
                    "cardStatus": "cardStatus",
                }
            ]
        )

        result = await api.get_receiving_the_history_of_account_topups()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReceivingTheHistoryOfAccountTopupsResponse)
        assert result[0].id_ == 1
        assert result[0].date == "date"
        assert result[0].sum_ == 1
        assert result[0].type_ == 1
        assert result[0].status_id == 1
