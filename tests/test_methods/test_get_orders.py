import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import OrdersResponse


@pytest.mark.unit
class TestGetOrders:
    async def test_get_orders(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "date": "date",
                    "lastChangeDate": "lastChangeDate",
                    "warehouseName": "warehouseName",
                    "warehouseType": "Склад WB",
                    "countryName": "countryName",
                    "oblastOkrugName": "oblastOkrugName",
                    "regionName": "regionName",
                    "supplierArticle": "supplierArticle",
                    "nmId": 1,
                    "barcode": "barcode",
                    "category": "category",
                    "subject": "subject",
                    "brand": "brand",
                    "techSize": "techSize",
                    "incomeID": 1,
                    "isSupply": True,
                    "isRealization": True,
                    "totalPrice": 1.0,
                    "discountPercent": 1,
                    "spp": 1.0,
                    "finishedPrice": 1.0,
                    "priceWithDisc": 1.0,
                    "isCancel": True,
                    "cancelDate": "cancelDate",
                    "sticker": "sticker",
                    "gNumber": "gNumber",
                    "srid": "srid",
                }
            ]
        )

        result = await api.get_orders(date_from="date_from")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdersResponse)
        assert result[0].date == "date"
        assert result[0].last_change_date == "lastChangeDate"
        assert result[0].warehouse_name == "warehouseName"
        assert result[0].warehouse_type == "Склад WB"
        assert result[0].country_name == "countryName"
