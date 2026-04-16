import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ProductDataItem


@pytest.mark.unit
class TestProductData:
    async def test_product_data(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "items": [
                        {
                            "nmID": 1,
                            "isDeleted": True,
                            "subjectName": "subjectName",
                            "name": "name",
                            "vendorCode": "vendorCode",
                            "brandName": "brandName",
                            "mainPhoto": "mainPhoto",
                            "hasSizes": True,
                            "metrics": None,
                        }
                    ]
                }
            }
        )

        result = await api.product_data()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ProductDataItem)
        assert result[0].nm_id == 1
        assert result[0].is_deleted
        assert result[0].subject_name == "subjectName"
