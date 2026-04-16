import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PromotionsDetailsItem


@pytest.mark.unit
class TestGetPromotionsDetails:
    async def test_get_promotions_details(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "promotions": [
                        {
                            "id": 123,
                            "name": "ХИТЫ ГОДА",
                            "description": "В акции принимают участие самые популярные товары 2023 года. Карточки товаров будут выделены плашкой «ХИТ ГОДА», чтобы покупатели замечали эти товары среди других. Также они будут размещены под баннерами на главной странице и примут участие в PUSH-уведомлениях. С ценами для вступления в акцию вы можете ознакомиться ниже.",
                            "advantages": [],
                            "startDateTime": "2023-06-05T21:00:00Z",
                            "endDateTime": "2023-06-05T21:00:00Z",
                            "inPromoActionLeftovers": 45,
                            "inPromoActionTotal": 123,
                            "notInPromoActionLeftovers": 3,
                            "notInPromoActionTotal": 10,
                            "participationPercentage": 10,
                            "type": "regular",
                            "exceptionProductsCount": 10,
                            "ranging": [{"condition": "condition", "participationRate": 1, "boost": 1}],
                        }
                    ]
                }
            }
        )

        result = await api.get_promotions_details(promotion_i_ds=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PromotionsDetailsItem)
        assert result[0].id_ == 123
        assert result[0].name == "ХИТЫ ГОДА"
        assert (
            result[0].description
            == "В акции принимают участие самые популярные товары 2023 года. Карточки товаров будут выделены плашкой «ХИТ ГОДА», чтобы покупатели замечали эти товары среди других. Также они будут размещены под баннерами на главной странице и примут участие в PUSH-уведомлениях. С ценами для вступления в акцию вы можете ознакомиться ниже."
        )
        assert result[0].start_date_time == "2023-06-05T21:00:00Z"
