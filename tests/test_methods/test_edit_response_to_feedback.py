import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestEditResponseToFeedback:

    async def test_edit_response_to_feedback(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.edit_response_to_feedback(id_="id_", text="text")

        assert result is None
