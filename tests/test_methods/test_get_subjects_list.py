import pytest

from wbapi_async.types import SubjectsListItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSubjectsList:

    async def test_get_subjects_list(self, api: MockedAPI) -> None:
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

        result = await api.get_subjects_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SubjectsListItem)
        assert result[0].subject_id == 1
        assert result[0].parent_id == 1
        assert result[0].subject_name == "subjectName"
