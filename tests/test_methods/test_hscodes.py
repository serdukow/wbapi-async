import pytest

from wbapi_async.types.hscodes_item import HscodesItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestHscodes:

    async def test_hscodes(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{
                "tnved": "tnved",
                "isKiz": True,
            }]
        }
        )

        result = await api.hscodes(subject_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], HscodesItem)
        assert result[0].tnved == "tnved"
        assert result[0].is_kiz == True
