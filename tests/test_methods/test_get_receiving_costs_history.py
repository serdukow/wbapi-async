import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ReceivingCostsHistoryResponse


@pytest.mark.unit
class TestGetReceivingCostsHistory:
    async def test_get_receiving_costs_history(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "updNum": 1,
                    "updTime": "updTime",
                    "updSum": 1,
                    "advertId": 1,
                    "campName": "campName",
                    "advertType": 1,
                    "paymentType": "paymentType",
                    "advertStatus": 1,
                }
            ]
        )

        result = await api.get_receiving_costs_history(from_="from_", to="to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReceivingCostsHistoryResponse)
        assert result[0].upd_num == 1
        assert result[0].upd_time == "updTime"
        assert result[0].upd_sum == 1
