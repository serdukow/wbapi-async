import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteThePass:

    async def test_delete_the_pass(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.delete_the_pass(pass_id=1)

        assert result is None
