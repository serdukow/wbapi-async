import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import QuestionListItem


@pytest.mark.unit
class TestGetQuestionList:
    async def test_get_question_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "questions": [
                        {
                            "id": "id",
                            "text": "text",
                            "createdDate": "createdDate",
                            "state": "state",
                            "answer": {"text": "text", "editable": True, "createDate": "createDate"},
                            "productDetails": {
                                "nmId": 1,
                                "imtId": 1,
                                "productName": "productName",
                                "supplierArticle": "supplierArticle",
                                "supplierName": "supplierName",
                                "brandName": "brandName",
                            },
                            "wasViewed": True,
                            "isWarned": True,
                        }
                    ]
                }
            }
        )

        result = await api.get_question_list(is_answered=True, take=1, skip=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], QuestionListItem)
        assert result[0].id_ == "id"
        assert result[0].text == "text"
        assert result[0].created_date == "createdDate"
        assert result[0].state == "state"
