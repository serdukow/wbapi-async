import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import VatRateItem


@pytest.mark.unit
class TestGetVatRate:
    async def test_get_vat_rate(self, api: MockedAPI) -> None:
        api.add_response({"data": [{}]})

        result = await api.get_vat_rate()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], VatRateItem)
