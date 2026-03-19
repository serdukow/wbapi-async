import pytest

from wbapi_async.types import RealizationSalesReport

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetRealizationSalesReport:

    async def test_get_realization_sales_report(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "realizationreport_id": 1234567,
                    "date_from": "2022-10-17",
                    "date_to": "2022-10-23",
                    "create_dt": "2022-10-24",
                    "currency_name": "руб",
                    "suppliercontract_code": None,
                    "rrd_id": 1232610467,
                    "gi_id": 123456,
                    "dlv_prc": 1.8,
                    "fix_tariff_date_from": "2024-10-23",
                    "fix_tariff_date_to": "2024-11-18",
                    "subject_name": "Mini ovens",
                    "nm_id": 1234567,
                    "brand_name": "BlahBlah",
                    "sa_name": "MAB123",
                    "ts_name": "0",
                    "barcode": "1231312352310",
                    "doc_type_name": "Продажа",
                    "quantity": 1,
                    "retail_price": 1249,
                    "retail_amount": 367,
                    "sale_percent": 0,
                    "commission_percent": 24,
                    "office_name": "Коледино",
                    "supplier_oper_name": "Продажа",
                    "order_dt": "2022-10-13T00:00:00Z",
                    "sale_dt": "2022-10-20T00:00:00Z",
                    "rr_dt": "2022-10-20",
                    "shk_id": 1239159661,
                    "retail_price_withdisc_rub": 399.68,
                    "delivery_amount": 0,
                    "return_amount": 0,
                    "delivery_rub": 0,
                    "gi_box_type_name": "Монопаллета",
                    "product_discount_for_report": 0,
                    "supplier_promo": 0,
                    "ppvz_spp_prc": 25.31,
                    "ppvz_kvw_prc_base": 24.15,
                    "ppvz_kvw_prc": 1.81,
                    "sup_rating_prc_up": 0,
                    "is_kgvp_v2": 0,
                    "ppvz_sales_commission": 23.74,
                    "ppvz_for_pay": 376.99,
                    "ppvz_reward": 0,
                    "acquiring_fee": 14.89,
                    "acquiring_percent": 4.06,
                    "payment_processing": "Комиссия за организацию платежа с НДС",
                    "acquiring_bank": "Тинькофф",
                    "ppvz_vw": 22.25,
                    "ppvz_vw_nds": 4.45,
                    "ppvz_office_name": "Пункт самовывоза (ПВЗ)",
                    "ppvz_office_id": 105383,
                    "ppvz_supplier_id": 186465,
                    "ppvz_supplier_name": "ИП Жасмин",
                    "ppvz_inn": "010101010101",
                    "declaration_number": "",
                    "bonus_type_name": "Штраф МП. Невыполненный заказ",
                    "sticker_id": "1964038895",
                    "site_country": "RU",
                    "srv_dbs": True,
                    "penalty": 231.35,
                    "additional_payment": 0,
                    "rebill_logistic_cost": 1.349,
                    "rebill_logistic_org": "ИП Иванов Иван Иванович(123456789012)",
                    "storage_fee": 12647.29,
                    "deduction": 6354,
                    "acceptance": 865,
                    "assembly_id": 2816993144,
                    "kiz": "some_kiz_value",
                    "srid": "0f1c3999172603062979867564654dac5b702849",
                    "report_type": 1,
                    "is_legal_entity": False,
                    "trbx_id": "WB-TRBX-1234567",
                    "installment_cofinancing_amount": 0,
                    "wibes_wb_discount_percent": 1,
                    "cashback_amount": 0,
                    "cashback_discount": 0,
                    "cashback_commission_change": 0,
                    "order_uid": "id375f16c4bec295d9995393af803ff7b",
                    "payment_schedule": 0,
                    "delivery_method": "FBS, (МГТ)",
                    "seller_promo_id": 14350,
                    "seller_promo_discount": 3,
                    "loyalty_id": 0,
                    "loyalty_discount": 0,
                    "uuid_promocode": "",
                    "sale_price_promocode_discount_prc": 0,
                }
            ]
        )

        result = await api.get_realization_sales_report(
            date_from="2022-10-17",
            date_to="2022-10-23",
        )

        assert isinstance(result, list)
        assert len(result) == 1

        report = result[0]
        assert isinstance(report, RealizationSalesReport)
        assert report.realizationreport_id == 1234567
        assert report.rrd_id == 1232610467
        assert report.nm_id == 1234567
        assert report.brand_name == "BlahBlah"
        assert report.quantity == 1
        assert report.retail_price == 1249
        assert report.commission_percent == 24
        assert report.ppvz_for_pay == 376.99
        assert report.penalty == 231.35
        assert report.storage_fee == 12647.29
        assert report.srv_dbs is True
        assert report.is_legal_entity is False
        assert report.site_country == "RU"
