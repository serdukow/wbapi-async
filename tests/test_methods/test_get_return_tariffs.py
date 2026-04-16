import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ReturnTariffsItem


@pytest.mark.unit
class TestGetReturnTariffs:
    async def test_get_return_tariffs(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "response": {
                    "data": {
                        "warehouseList": [
                            {
                                "deliveryDumpKgtOfficeBase": "1 039",
                                "deliveryDumpKgtOfficeLiter": "9,1",
                                "deliveryDumpKgtReturnExpr": "1 050",
                                "deliveryDumpSrgOfficeExpr": "170",
                                "deliveryDumpSrgReturnExpr": "170",
                                "deliveryDumpSupCourierBase": "229",
                                "deliveryDumpSupCourierLiter": "9,1",
                                "deliveryDumpSupOfficeBase": "129",
                                "deliveryDumpSupOfficeLiter": "9,1",
                                "deliveryDumpSupReturnExpr": "250",
                                "warehouseName": "Электросталь",
                            }
                        ]
                    }
                }
            }
        )

        result = await api.get_return_tariffs(date="date")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReturnTariffsItem)
        assert result[0].delivery_dump_kgt_office_base == "1 039"
        assert result[0].delivery_dump_kgt_office_liter == "9,1"
        assert result[0].delivery_dump_kgt_return_expr == "1 050"
        assert result[0].delivery_dump_srg_office_expr == "170"
        assert result[0].delivery_dump_srg_return_expr == "170"
