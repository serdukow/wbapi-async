import pytest

from wbapi_async.types.generation_of_skus_item import GenerationOfSkusItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGenerationOfSkus:

    async def test_generation_of_skus(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{

            }]
        }
        )

        result = await api.generation_of_skus()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GenerationOfSkusItem)
