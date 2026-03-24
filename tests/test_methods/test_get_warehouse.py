import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import WarehouseResponse


@pytest.mark.unit
class TestGetWarehouse:
    async def test_get_warehouse(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "lastChangeDate": "lastChangeDate",
                    "warehouseName": "warehouseName",
                    "supplierArticle": "supplierArticle",
                    "nmId": 1,
                    "barcode": "barcode",
                    "quantity": 1,
                    "inWayToClient": 1,
                    "inWayFromClient": 1,
                    "quantityFull": 1,
                    "category": "category",
                    "subject": "subject",
                    "brand": "brand",
                    "techSize": "techSize",
                    "Price": 1.0,
                    "Discount": 1.0,
                    "isSupply": True,
                    "isRealization": True,
                    "SCCode": "SCCode",
                }
            ]
        )

        result = await api.get_warehouse(date_from="date_from")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WarehouseResponse)
        assert result[0].last_change_date == "lastChangeDate"
        assert result[0].warehouse_name == "warehouseName"
        assert result[0].supplier_article == "supplierArticle"
