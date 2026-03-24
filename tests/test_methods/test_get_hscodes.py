import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import HscodesItem


@pytest.mark.unit
class TestGetHscodes:
    async def test_get_hscodes(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": [
                    {
                        "tnved": "tnved",
                        "isKiz": True,
                    }
                ]
            }
        )

        result = await api.get_hscodes(subject_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], HscodesItem)
        assert result[0].tnved == "tnved"
        assert result[0].is_kiz
