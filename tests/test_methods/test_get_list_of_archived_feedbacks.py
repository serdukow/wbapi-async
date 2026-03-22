import pytest

from wbapi_async.types import ListOfArchivedFeedbacksItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetListOfArchivedFeedbacks:

    async def test_get_list_of_archived_feedbacks(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "feedbacks": [{
                "id": "id",
                "text": "text",
                "pros": "pros",
                "cons": "cons",
                "productValuation": 1,
                "createdDate": "createdDate",
                "answer": {},
                "state": "state",
                "productDetails": {},
                "photoLinks": [],
                "video": {},
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
            }]
        }
        }
        )

        result = await api.get_list_of_archived_feedbacks(take=1, skip=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfArchivedFeedbacksItem)
        assert result[0].id == "id"
        assert result[0].text == "text"
        assert result[0].pros == "pros"
