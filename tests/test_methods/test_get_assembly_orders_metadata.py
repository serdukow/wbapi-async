import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AssemblyOrdersMetadataItem


@pytest.mark.unit
class TestGetAssemblyOrdersMetadata:
    async def test_get_assembly_orders_metadata(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "orders": [
                    {
                        "id": 1,
                        "meta": {
                            "imei": {"value": "123456789012345"},
                            "uin": {"value": "123456789012345"},
                            "gtin": {"value": "123456789012345"},
                            "sgtin": {"value": []},
                            "expiration": {"value": "12.09.2030"},
                            "customsDeclaration": {"value": "10704010/010624/0000302"},
                        },
                    }
                ]
            }
        )

        result = await api.get_assembly_orders_metadata(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrdersMetadataItem)
        assert result[0].id_ == 1
