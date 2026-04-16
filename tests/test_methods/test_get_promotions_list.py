import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PromotionsListItem


@pytest.mark.unit
class TestGetPromotionsList:
    async def test_get_promotions_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "promotions": [
                        {
                            "id": 123,
                            "name": "скидки",
                            "startDateTime": "2023-06-05T21:00:00Z",
                            "endDateTime": "2023-06-05T21:00:00Z",
                            "type": "type",
                        }
                    ]
                }
            }
        )

        result = await api.get_promotions_list(
            start_date_time="start_date_time", end_date_time="end_date_time"
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PromotionsListItem)
        assert result[0].id_ == 123
        assert result[0].name == "скидки"
        assert result[0].start_date_time == "2023-06-05T21:00:00Z"
        assert result[0].end_date_time == "2023-06-05T21:00:00Z"
        assert result[0].type_ == "type"
