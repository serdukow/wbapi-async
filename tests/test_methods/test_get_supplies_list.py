import pytest

from wbapi_async.enums.supply_dates_type import SupplyDatesType
from wbapi_async.enums.supply_status import SupplyStatus
from wbapi_async.methods.get_supplies_list import SupplyDateFilter
from wbapi_async.types.supply import Supply

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSuppliesList:

    async def test_get_supplies_list(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "phone": "+7 916 *** 44 44",
                    "supplyID": None,
                    "preorderID": 34597755,
                    "createDate": "2024-12-29T16:58:26+03:00",
                    "supplyDate": None,
                    "factDate": None,
                    "updatedDate": None,
                    "statusID": 1,
                    "boxTypeID": 1,
                },
                {
                    "phone": "+7 916 *** 33 33",
                    "supplyID": 26596368,
                    "preorderID": 34601223,
                    "createDate": "2024-12-29T16:57:59+03:00",
                    "supplyDate": "2024-12-29T00:00:00+03:00",
                    "factDate": None,
                    "updatedDate": None,
                    "statusID": 2,
                    "boxTypeID": 5,
                },
                {
                    "phone": "+7 000 *** 36 76",
                    "supplyID": 22677736,
                    "preorderID": 27363170,
                    "createDate": "2024-08-22T18:10:59+03:00",
                    "supplyDate": "2024-08-22T00:00:00+03:00",
                    "factDate": "2024-08-22T12:24:14+03:00",
                    "updatedDate": "2024-08-22T18:33:45+03:00",
                    "statusID": 6,
                    "boxTypeID": 2,
                    "isBoxOnPallet": False,
                },
            ]
        )

        result = await api.get_supplies_list(
            dates=[
                SupplyDateFilter(**{"from": "2024-01-01", "till": "2024-12-31", "type": SupplyDatesType.CREATE_DATE})
            ],
        )

        assert isinstance(result, list)
        assert len(result) == 3

        first = result[0]
        assert isinstance(first, Supply)
        assert first.phone == "+7 916 *** 44 44"
        assert first.supply_id is None
        assert first.preorder_id == 34597755
        assert first.status_id == SupplyStatus.NOT_PLANNED
        assert first.box_type_id == 1

        second = result[1]
        assert second.supply_id == 26596368
        assert second.status_id == SupplyStatus.PLANNED

        third = result[2]
        assert third.supply_id == 22677736
        assert third.status_id == SupplyStatus.UNLOADED_AT_GATE
        assert third.is_box_on_pallet is False
        assert third.fact_date == "2024-08-22T12:24:14+03:00"
