import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import GoodsReturnItem


@pytest.mark.unit
class TestGetGoodsReturn:
    async def test_get_goods_return(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "report": [
                    {
                        "barcode": "1680063403480",
                        "brand": "dub",
                        "completedDt": "2025-03-31T11:33:53",
                        "dstOfficeAddress": "Жуковский Улица Маяковского 19",
                        "dstOfficeId": 310105,
                        "expiredDt": "2025-03-31T11:33:53",
                        "isStatusActive": 0,
                        "nmId": 12862181,
                        "orderDt": "2024-08-26",
                        "orderId": 2034240826,
                        "readyToReturnDt": "2025-01-31T08:33:50",
                        "reason": "Цвет",
                        "returnType": "Возврат заблокированного товара",
                        "shkId": 23411783472,
                        "srid": "ad3817664d3046c5a8d55054d8be96d6",
                        "status": "В пути в пвз",
                        "stickerId": "33811984302",
                        "subjectName": "Багажные бирки",
                        "techSize": "0",
                    }
                ]
            }
        )

        result = await api.get_goods_return(date_from="2024-08-13", date_to="2024-08-27")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GoodsReturnItem)
        assert result[0].barcode == "1680063403480"
        assert result[0].brand == "dub"
        assert result[0].nm_id == 12862181
        assert result[0].is_status_active == 0
