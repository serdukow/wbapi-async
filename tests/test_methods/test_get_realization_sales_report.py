import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import RealizationSalesReportResponse


@pytest.mark.unit
class TestGetRealizationSalesReport:
    async def test_get_realization_sales_report(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "realizationreport_id": 1,
                    "date_from": "date_from",
                    "date_to": "date_to",
                    "create_dt": "create_dt",
                    "currency_name": "currency_name",
                    "suppliercontract_code": {},
                    "rrd_id": 1,
                    "gi_id": 1,
                    "dlv_prc": 1.0,
                    "fix_tariff_date_from": "fix_tariff_date_from",
                    "fix_tariff_date_to": "fix_tariff_date_to",
                    "subject_name": "subject_name",
                    "nm_id": 1,
                    "brand_name": "brand_name",
                    "sa_name": "sa_name",
                    "ts_name": "ts_name",
                    "barcode": "barcode",
                    "doc_type_name": "doc_type_name",
                    "quantity": 1,
                    "retail_price": 1.0,
                    "retail_amount": 1.0,
                    "sale_percent": 1,
                    "commission_percent": 1.0,
                    "office_name": "office_name",
                    "supplier_oper_name": "supplier_oper_name",
                    "order_dt": "order_dt",
                    "sale_dt": "sale_dt",
                    "rr_dt": "rr_dt",
                    "shk_id": 1,
                    "retail_price_withdisc_rub": 1.0,
                    "delivery_amount": 1,
                    "return_amount": 1,
                    "delivery_rub": 1.0,
                    "gi_box_type_name": "gi_box_type_name",
                    "product_discount_for_report": 1.0,
                    "supplier_promo": 1.0,
                    "ppvz_spp_prc": 1.0,
                    "ppvz_kvw_prc_base": 1.0,
                    "ppvz_kvw_prc": 1.0,
                    "sup_rating_prc_up": 1.0,
                    "is_kgvp_v2": 1.0,
                    "ppvz_sales_commission": 1.0,
                    "ppvz_for_pay": 1.0,
                    "ppvz_reward": 1.0,
                    "acquiring_fee": 1.0,
                    "acquiring_percent": 1.0,
                    "payment_processing": "payment_processing",
                    "acquiring_bank": "acquiring_bank",
                    "ppvz_vw": 1.0,
                    "ppvz_vw_nds": 1.0,
                    "ppvz_office_name": "ppvz_office_name",
                    "ppvz_office_id": 1,
                    "ppvz_supplier_id": 1,
                    "ppvz_supplier_name": "ppvz_supplier_name",
                    "ppvz_inn": "ppvz_inn",
                    "declaration_number": "declaration_number",
                    "bonus_type_name": "bonus_type_name",
                    "sticker_id": "sticker_id",
                    "site_country": "site_country",
                    "srv_dbs": True,
                    "penalty": 1.0,
                    "additional_payment": 1.0,
                    "rebill_logistic_cost": 1.0,
                    "rebill_logistic_org": "rebill_logistic_org",
                    "storage_fee": 1.0,
                    "deduction": 1.0,
                    "acceptance": 1.0,
                    "assembly_id": 1,
                    "kiz": "kiz",
                    "srid": "srid",
                    "report_type": 1,
                    "is_legal_entity": True,
                    "trbx_id": "trbx_id",
                    "installment_cofinancing_amount": 1.0,
                    "wibes_wb_discount_percent": 1.0,
                    "cashback_amount": 1.0,
                    "cashback_discount": 1.0,
                    "cashback_commission_change": 1.0,
                    "order_uid": "order_uid",
                    "payment_schedule": 1.0,
                    "delivery_method": "delivery_method",
                    "seller_promo_id": 1,
                    "seller_promo_discount": 1.0,
                    "loyalty_id": 1,
                    "loyalty_discount": 1.0,
                    "uuid_promocode": "uuid_promocode",
                    "sale_price_promocode_discount_prc": 1.0,
                    "article_substitution": "article_substitution",
                    "sale_price_affiliated_discount_prc": 1.0,
                    "agency_vat": 1.0,
                    "sale_price_wholesale_discount_prc": 1.0,
                }
            ]
        )

        result = await api.get_realization_sales_report(date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], RealizationSalesReportResponse)
        assert result[0].realizationreport_id == 1
        assert result[0].date_from == "date_from"
        assert result[0].date_to == "date_to"
