import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DetailsForTheSalesReportsByReportIdResponse


@pytest.mark.unit
class TestDetailsForTheSalesReportsByReportId:
    async def test_details_for_the_sales_reports_by_report_id(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "reportId": 1,
                    "dateFrom": "dateFrom",
                    "dateTo": "dateTo",
                    "createDate": "createDate",
                    "currency": "currency",
                    "reportType": 1,
                    "rrdId": 1,
                    "giId": 1,
                    "dlvPrc": 1.0,
                    "fixTariffDateFrom": "fixTariffDateFrom",
                    "fixTariffDateTo": "fixTariffDateTo",
                    "subjectName": "subjectName",
                    "nmId": 1,
                    "brandName": "brandName",
                    "vendorCode": "vendorCode",
                    "title": "title",
                    "techSize": "techSize",
                    "sku": "sku",
                    "docTypeName": "docTypeName",
                    "quantity": 1,
                    "retailPrice": "retailPrice",
                    "retailAmount": "retailAmount",
                    "salePercent": 1,
                    "commissionPercent": 1.0,
                    "officeName": "officeName",
                    "sellerOperName": "sellerOperName",
                    "orderDt": "orderDt",
                    "saleDt": "saleDt",
                    "rrDate": "rrDate",
                    "shkId": 1,
                    "retailPriceWithDisc": "retailPriceWithDisc",
                    "deliveryAmount": 1,
                    "returnAmount": 1,
                    "deliveryService": "deliveryService",
                    "giBoxTypeName": "giBoxTypeName",
                    "productDiscountForReport": 1.0,
                    "sellerPromo": "sellerPromo",
                    "spp": 1.0,
                    "kvwBase": 1.0,
                    "kvw": 1.0,
                    "supRatingUp": 1.0,
                    "isKgvpV2": 1.0,
                    "ppvzSalesCommission": "ppvzSalesCommission",
                    "forPay": "forPay",
                    "ppvzReward": "ppvzReward",
                    "acquiringFee": "acquiringFee",
                    "acquiringPercent": 1.0,
                    "paymentProcessing": "paymentProcessing",
                    "acquiringBank": "acquiringBank",
                    "vw": "vw",
                    "vwNds": "vwNds",
                    "ppvzOfficeName": "ppvzOfficeName",
                    "ppvzOfficeId": 1,
                    "ppvzSupplierName": "ppvzSupplierName",
                    "ppvzSupplierInn": "ppvzSupplierInn",
                    "declarationNumber": "declarationNumber",
                    "bonusTypeName": "bonusTypeName",
                    "stickerId": "stickerId",
                    "country": "country",
                    "srvDbs": True,
                    "penalty": "penalty",
                    "additionalPayment": "additionalPayment",
                    "rebillLogisticCost": "rebillLogisticCost",
                    "rebillLogisticOrg": "rebillLogisticOrg",
                    "paidStorage": "paidStorage",
                    "deduction": "deduction",
                    "paidAcceptance": "paidAcceptance",
                    "orderId": 1,
                    "kiz": "kiz",
                    "isB2b": True,
                    "trbxId": "trbxId",
                    "installmentCofinancingAmount": "installmentCofinancingAmount",
                    "wibesDiscountPercent": 1.0,
                    "cashbackAmount": "cashbackAmount",
                    "cashbackDiscount": "cashbackDiscount",
                    "cashbackCommissionChange": "cashbackCommissionChange",
                    "paymentSchedule": "paymentSchedule",
                    "deliveryMethod": "deliveryMethod",
                    "sellerPromoId": 1,
                    "sellerPromoDiscount": 1.0,
                    "loyaltyId": 1,
                    "loyaltyDiscount": 1.0,
                    "uuidPromocode": "uuidPromocode",
                    "salePricePromocodeDiscountPrc": 1.0,
                    "articleSubstitution": "articleSubstitution",
                    "salePriceAffiliatedDiscountPrc": 1.0,
                    "agencyVat": 1.0,
                    "salePriceWholesaleDiscountPrc": 1.0,
                    "orderUid": "orderUid",
                    "srid": "srid",
                }
            ]
        )

        result = await api.details_for_the_sales_reports_by_report_id(report_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DetailsForTheSalesReportsByReportIdResponse)
        assert result[0].report_id == 1
        assert result[0].date_from == "dateFrom"
        assert result[0].date_to == "dateTo"
