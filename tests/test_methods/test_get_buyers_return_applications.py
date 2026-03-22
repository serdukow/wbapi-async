import pytest

from wbapi_async.types import BuyersReturnApplicationsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetBuyersReturnApplications:

    async def test_get_buyers_return_applications(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "claims": [{
                "id": "id",
                "claim_type": 1,
                "status": 1,
                "status_ex": 1,
                "nm_id": 1,
                "user_comment": "user_comment",
                "wb_comment": "wb_comment",
                "dt": "dt",
                "imt_name": "imt_name",
                "order_dt": "order_dt",
                "dt_update": "dt_update",
                "photos": [],
                "video_paths": [],
                "actions": [],
                "price": 1.0,
                "currency_code": "currency_code",
                "srid": "srid",
                "origin_id_info": "origin_id_info",
                "delivery_dt": "delivery_dt",
            }]
        }
        )

        result = await api.get_buyers_return_applications(is_archive=True)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BuyersReturnApplicationsItem)
        assert result[0].id == "id"
        assert result[0].claim_type == 1
        assert result[0].status == 1
