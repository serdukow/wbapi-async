import pytest

from wbapi_async.types.subjects_list_item import SubjectsListItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSubjectsList:

    async def test_subjects_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{
                "subjectID": 1,
                "parentID": 1,
                "subjectName": "subjectName",
                "parentName": "parentName",
            }]
        }
        )

        result = await api.subjects_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SubjectsListItem)
        assert result[0].subject_id == 1
        assert result[0].parent_id == 1
        assert result[0].subject_name == "subjectName"
