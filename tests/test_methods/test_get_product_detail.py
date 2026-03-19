import pytest

from wbapi_async.types import ProductDetail

from tests.mocked_api import MockedAPI

RESPONSE = {
    "products": [
        {
            "id": 999000111,
            "root": 55566677,
            "kindId": 0,
            "brand": "TestBrand",
            "brandId": 123456,
            "siteBrandId": 0,
            "colors": [],
            "subjectId": 1001,
            "subjectParentId": 10,
            "name": "Test Product Name",
            "entity": "test entity",
            "matchId": 7654321,
            "supplier": "TestSupplier",
            "supplierId": 654321,
            "supplierRating": 4.7,
            "supplierFlags": 1000,
            "pics": 5,
            "rating": 4,
            "reviewRating": 4.5,
            "nmReviewRating": 4.5,
            "feedbacks": 200,
            "nmFeedbacks": 200,
            "volume": 10,
            "weight": 0.5,
            "viewFlags": 100000,
            "promotions": [1000001, 1000002],
            "sizes": [
                {
                    "name": "",
                    "origName": "0",
                    "rank": 0,
                    "optionId": 300000001,
                    "stocks": [
                        {
                            "wh": 100001,
                            "dtype": 1000000000001,
                            "dist": 100,
                            "qty": 50,
                            "priority": 90000,
                            "time1": 1,
                            "time2": 10,
                        }
                    ],
                    "time1": 1,
                    "time2": 10,
                    "wh": 100001,
                    "dtype": 1000000000001,
                    "dist": 100,
                    "price": {
                        "basic": 150000,
                        "product": 80000,
                        "logistics": 0,
                        "return": 0,
                    },
                    "saleConditions": 0,
                    "payload": "dGVzdHBheWxvYWQ=",
                }
            ],
            "totalQuantity": 50,
            "time1": 1,
            "time2": 10,
            "wh": 100001,
            "dtype": 1000000000001,
            "dist": 100,
        }
    ]
}


class TestGetProductDetail:
    @pytest.mark.unit
    async def test_returns_list(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_product_detail(nm=999000111)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductDetail)

    @pytest.mark.unit
    async def test_product_fields(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_product_detail(nm=999000111)

        product = result[0]
        assert product.id == 999000111
        assert product.brand == "TestBrand"
        assert product.supplier_rating == 4.7
        assert product.total_quantity == 50

    @pytest.mark.unit
    async def test_nested_size_price(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        result = await api.get_product_detail(nm=999000111)

        size = result[0].sizes[0]
        assert size.price.basic == 150000
        assert size.price.product == 80000
        assert size.stocks[0].qty == 50

    @pytest.mark.unit
    async def test_request_url(self, api: MockedAPI) -> None:
        api.add_response(RESPONSE)

        await api.get_product_detail(nm=999000111)

        req = api.get_last_request()
        assert req.url == "https://card.wb.ru/cards/v4/detail"
        assert req.method == "GET"
        assert req.params["nm"] == 999000111
