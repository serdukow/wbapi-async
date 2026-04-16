import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ListOfArchivedFeedbacksItem


@pytest.mark.unit
class TestGetListOfArchivedFeedbacks:
    async def test_get_list_of_archived_feedbacks(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "feedbacks": [
                        {
                            "id": "id",
                            "text": "text",
                            "pros": "pros",
                            "cons": "cons",
                            "productValuation": 1,
                            "createdDate": "createdDate",
                            "answer": {"text": "text", "editable": True, "createDate": "createDate"},
                            "state": "state",
                            "productDetails": {
                                "nmId": 1,
                                "imtId": 1,
                                "productName": "productName",
                                "supplierArticle": "supplierArticle",
                                "supplierName": "supplierName",
                                "brandName": "brandName",
                            },
                            "photoLinks": [{"fullSize": "fullSize", "miniSize": "miniSize"}],
                            "video": {"previewImage": "previewImage", "link": "link", "durationSec": 1},
                            "wasViewed": True,
                            "userName": "userName",
                            "orderStatus": "orderStatus",
                            "matchingSize": "matchingSize",
                            "isAbleSupplierFeedbackValuation": True,
                            "supplierFeedbackValuation": 1,
                            "isAbleSupplierProductValuation": True,
                            "supplierProductValuation": 1,
                            "isAbleReturnProductOrders": True,
                            "returnProductOrdersDate": "returnProductOrdersDate",
                            "bables": [],
                            "lastOrderShkId": 1,
                            "lastOrderCreatedAt": "lastOrderCreatedAt",
                            "color": "color",
                            "subjectId": 1,
                            "subjectName": "subjectName",
                            "parentFeedbackId": "parentFeedbackId",
                            "childFeedbackId": "childFeedbackId",
                        }
                    ]
                }
            }
        )

        result = await api.get_list_of_archived_feedbacks(take=1, skip=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfArchivedFeedbacksItem)
        assert result[0].id_ == "id"
        assert result[0].text == "text"
        assert result[0].pros == "pros"
        assert result[0].cons == "cons"
        assert result[0].product_valuation == 1
