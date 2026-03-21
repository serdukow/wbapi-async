import pytest

from wbapi_async.types.subject_characteristics_item import SubjectCharacteristicsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSubjectCharacteristics:

    async def test_subject_characteristics(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{
                "charcID": 1,
                "subjectName": "subjectName",
                "subjectID": 1,
                "name": "name",
                "required": True,
                "unitName": "unitName",
                "maxCount": 1,
                "popular": True,
                "charcType": 1,
            }]
        }
        )

        result = await api.subject_characteristics(subject_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SubjectCharacteristicsItem)
        assert result[0].charc_id == 1
        assert result[0].subject_name == "subjectName"
        assert result[0].subject_id == 1
