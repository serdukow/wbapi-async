import pytest

from wbapi_async.types import ReturnTariffsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetReturnTariffs:

    async def test_get_return_tariffs(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "response": {
            "data": {
            "warehouseList": [{
                "deliveryDumpKgtOfficeBase": "deliveryDumpKgtOfficeBase",
                "deliveryDumpKgtOfficeLiter": "deliveryDumpKgtOfficeLiter",
                "deliveryDumpKgtReturnExpr": "deliveryDumpKgtReturnExpr",
                "deliveryDumpSrgOfficeExpr": "deliveryDumpSrgOfficeExpr",
                "deliveryDumpSrgReturnExpr": "deliveryDumpSrgReturnExpr",
                "deliveryDumpSupCourierBase": "deliveryDumpSupCourierBase",
                "deliveryDumpSupCourierLiter": "deliveryDumpSupCourierLiter",
                "deliveryDumpSupOfficeBase": "deliveryDumpSupOfficeBase",
                "deliveryDumpSupOfficeLiter": "deliveryDumpSupOfficeLiter",
                "deliveryDumpSupReturnExpr": "deliveryDumpSupReturnExpr",
                "warehouseName": "warehouseName",
            }]
        }
        }
        }
        )

        result = await api.get_return_tariffs(date="date")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReturnTariffsItem)
        assert result[0].delivery_dump_kgt_office_base == "deliveryDumpKgtOfficeBase"
        assert result[0].delivery_dump_kgt_office_liter == "deliveryDumpKgtOfficeLiter"
        assert result[0].delivery_dump_kgt_return_expr == "deliveryDumpKgtReturnExpr"
