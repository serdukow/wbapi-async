import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CreateWarehouseResponse


@pytest.mark.unit
class TestCreateWarehouse:
    async def test_create_warehouse(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "id": 1,
                }
            ]
        )

        result = await api.create_warehouse(name="name", office_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CreateWarehouseResponse)
        assert result[0].id_ == 1
