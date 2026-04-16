import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import GettingSellerPortalNewsItem


@pytest.mark.unit
class TestGetGettingSellerPortalNews:
    async def test_get_getting_seller_portal_news(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": [
                    {
                        "content": "content",
                        "date": "date",
                        "header": "header",
                        "id": 1,
                        "types": [{"id": 1, "name": "name"}],
                    }
                ]
            }
        )

        result = await api.get_getting_seller_portal_news()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GettingSellerPortalNewsItem)
        assert result[0].content == "content"
        assert result[0].date == "date"
        assert result[0].header == "header"
        assert result[0].id_ == 1
