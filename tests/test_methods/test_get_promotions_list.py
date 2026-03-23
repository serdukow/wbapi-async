import pytest

from wbapi_async.types import PromotionsListItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetPromotionsList:

    async def test_get_promotions_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "promotions": [{
                "id": 1,
                "name": "name",
                "startDateTime": "startDateTime",
                "endDateTime": "endDateTime",
                "type": "type",
            }]
        }
        }
        )

        result = await api.get_promotions_list(start_date_time="start_date_time", end_date_time="end_date_time")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PromotionsListItem)
        assert result[0].id_ == 1
        assert result[0].name == "name"
        assert result[0].start_date_time == "startDateTime"
