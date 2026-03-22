import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAnswerBuyersApplication:

    async def test_answer_buyers_application(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.answer_buyers_application(id="id", action="action")

        assert result is None
