import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import BlockedProductCardsItem


@pytest.mark.unit
class TestGetBlockedProductCards:
    async def test_get_blocked_product_cards(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "report": [
                    {
                        "brand": "Тест22",
                        "nmId": 82722944,
                        "title": "Гуминовые кислоты - биоактивный противовирусный комплекс на",
                        "vendorCode": "пкdeир76",
                        "reason": "Контактные данные Продавца и ссылки на иные сайты/группы/сообщества на фотографиях Товара",
                    }
                ]
            }
        )

        result = await api.get_blocked_product_cards(sort="sort", order="order")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], BlockedProductCardsItem)
        assert result[0].brand == "Тест22"
        assert result[0].nm_id == 82722944
        assert result[0].title == "Гуминовые кислоты - биоактивный противовирусный комплекс на"
        assert result[0].vendor_code == "пкdeир76"
        assert (
            result[0].reason
            == "Контактные данные Продавца и ссылки на иные сайты/группы/сообщества на фотографиях Товара"
        )
