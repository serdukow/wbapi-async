import pytest

from wbapi_async.types.vat_rate_item import VatRateItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestVatRate:

    async def test_vat_rate(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": [{

            }]
        }
        )

        result = await api.vat_rate()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], VatRateItem)
