import pytest

from wbapi_async.types import Sale

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSales:

    async def test_get_sales(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "date": "2022-03-04T18:08:31",
                    "lastChangeDate": "2022-03-06T10:11:07",
                    "warehouseName": "Подольск",
                    "warehouseType": "Склад продавца",
                    "countryName": "Россия",
                    "oblastOkrugName": "Центральный федеральный округ",
                    "regionName": "Московская",
                    "supplierArticle": "12345",
                    "nmId": 1234567,
                    "barcode": "123453559000",
                    "category": "Бытовая техника",
                    "subject": "Мультистайлеры",
                    "brand": "Тест",
                    "techSize": "0",
                    "incomeID": 56735459,
                    "isSupply": False,
                    "isRealization": True,
                    "totalPrice": 1887,
                    "discountPercent": 18,
                    "spp": 20,
                    "paymentSaleAmount": 93,
                    "forPay": 1284.01,
                    "finishedPrice": 1145,
                    "priceWithDisc": 1547,
                    "saleID": "S9993700024",
                    "sticker": "926912515",
                    "gNumber": "34343462218572569531",
                    "srid": "11.rf9ef11fce1684117b0nhj96222982382.3.0",
                }
            ]
        )

        api.add_response([])

        result = await api.get_sales(date_from="2022-03-04")

        assert isinstance(result, list)
        assert len(result) == 1

        sale = result[0]
        assert isinstance(sale, Sale)
        assert sale.nm_id == 1234567
        assert sale.supplier_article == "12345"
        assert sale.warehouse_name == "Подольск"
        assert sale.total_price == 1887
        assert sale.discount_percent == 18
        assert sale.for_pay == 1284.01
        assert sale.finished_price == 1145
        assert sale.price_with_disc == 1547
        assert sale.sale_id == "S9993700024"
        assert sale.is_supply is False
        assert sale.is_realization is True
        assert sale.srid == "11.rf9ef11fce1684117b0nhj96222982382.3.0"
