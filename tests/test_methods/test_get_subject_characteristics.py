import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SubjectCharacteristicsItem


@pytest.mark.unit
class TestGetSubjectCharacteristics:
    async def test_get_subject_characteristics(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": [
                    {
                        "charcID": 1,
                        "subjectName": "subjectName",
                        "subjectID": 1,
                        "name": "name",
                        "required": True,
                        "unitName": "unitName",
                        "maxCount": 1,
                        "popular": True,
                        "charcType": 1,
                    }
                ]
            }
        )

        result = await api.get_subject_characteristics(subject_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SubjectCharacteristicsItem)
        assert result[0].charc_id == 1
        assert result[0].subject_name == "subjectName"
        assert result[0].subject_id == 1
        assert result[0].name == "name"
        assert result[0].required
