import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import StickersForCrossborderAssemblyOrdersItem


@pytest.mark.unit
class TestGetStickersForCrossborderAssemblyOrders:
    async def test_get_stickers_for_crossborder_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "stickers": [
                    {
                        "file": "JVBERi0xLjQKJSBjcmVhdGVkIGJ5IFBpbGxvdyBQREYgZHJpdmVyCjQgMCBvYmo8PAovVHlwZSAvQ2F0YWxvZwovUGFnZXMgNSAwIFIKPj5lbmRvYmoKNSAwIG9iajw8Ci9UeXBlIC9QYWdlcwovQ291bnQgMQovS2lkcyBbIDIgMCBSIF0KPj5lbmRvYmoKMSAwIG9iajw8Ci9UeXBlIC9YT2JqZWN0Ci9TdWJ0eXBlIC9JbWFnZQovV2lkdGggMjkwCi9IZWlnaHQgMjkwCi9GaWx0ZXIgWyAvQ0NJVFRGYXhEZWNvZGUgXQovRGVjb2RlUGFybXMgWyA8PAovSyAtMQovQmxhY2tJczEgdHJ1ZQovQ29sdW1ucyAyOTAKL1Jvd3MgMjkwCj4+IF0KL0JpdHNQZXJDb21wb25lbnQgMQovQ29sb3JTcGFjZSAvRGV2aWNlR3JheQovTGVuZ3RoIDY2Ngo+PnN0cmVhbQomoLYaX////////////8g2b4gpHITff///////////8nBSkIB8nBS/////////////////////+QgHkNB/IQD////////////////////////////+P//////////////////////////IQ5CHIQ////////////////////////////////jkNB/H/////////////////////4yEOQh+P//////////////////EhoKR//////yDYchDkIchDyBg2E4aCcFL////////////////////////IgFIiAhODQTg0f/////////////////+ThCICEQGgnDQTg0E4NBODZ////////////////////////4k4NESEOJCCP/////////////////8gpHIQ5CCCEEENB8hDyBg2f//////////////////////////xEZKQhOEJwhOB5f//////////////yDZviDQIjkDBS///////////////ycFLEnCCThP//////////////////kIB5CHkQEEnCEQEJwbP///////////////////////////4ycGgnBoIgFL/////////////////////+QhxIQ4kIcg0H////////////////////////8cSEOJCHEhAP//////////////////jIQDIQ+Qh5OE////////////////////////4iIiI/////////////wAQAQJAAABAwABAAAAIgEAAAEBAwABAAAAIgEAAAIBAwABAAAAAQAAAAMBAwABAAAABAAAAAYBAwABAAAAAQAAABEBBAABAAAACAAAABYBAwABAAAAIgEAABcBBAABAAAAKAIAABwBAwABAAAAAQAAAAAAAAAKZW5kc3RyZWFtCmVuZG9iagoyIDAgb2JqPDwKL1Jlc291cmNlcyA8PAovUHJvY1NldCBbIC9QREYgL0ltYWdlQiBdCi9YT2JqZWN0IDw8Ci9pbWFnZSAxIDAgUgo+Pgo+PgovTWVkaWFCb3ggWyAwIDAgMjkwLjAgMjkwLjAgXQovQ29udGVudHMgMyAwIFIKL1R5cGUgL1BhZ2UKL1BhcmVudCA1IDAgUgo+PmVuZG9iagozIDAgb2JqPDwKL0xlbmd0aCA0Nwo+PnN0cmVhbQpxIDI5MC4wMDAwMDAgMCAwIDI5MC4wMDAwMDAgMCAwIGNtIC9pbWFnZSBEbyBRCgplbmRzdHJlYW0KZW5kb2JqCjYgMCBvYmo8PAovQ3JlYXRpb25EYXRlIChEOjIwMjUxMTA3MTMzNTE1WikKL01vZERhdGUgKEQ6MjAyNTExMDcxMzM1MTVaKQo+PmVuZG9iagp4cmVmCjAgNwowMDAwMDAwMDAwIDY1NTM2IGYgCjAwMDAwMDAxNDQgMDAwMDAgbiAKMDAwMDAwMTA1MiAwMDAwMCBuIAowMDAwMDAxMjE0IDAwMDAwIG4gCjAwMDAwMDAwNDAgMDAwMDAgbiAKMDAwMDAwMDA4NyAwMDAwMCBuIAowMDAwMDAxMzA5IDAwMDAwIG4gCnRyYWlsZXIKPDwKL1Jvb3QgNCAwIFIKL1NpemUgNwovSW5mbyA2IDAgUgo+PgpzdGFydHhyZWYKMTM5MQolJUVPRg==",
                        "orderId": 3869227998,
                        "parcelId": "WB0000000001",
                    }
                ]
            }
        )

        result = await api.get_stickers_for_crossborder_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], StickersForCrossborderAssemblyOrdersItem)
        assert (
            result[0].file
            == "JVBERi0xLjQKJSBjcmVhdGVkIGJ5IFBpbGxvdyBQREYgZHJpdmVyCjQgMCBvYmo8PAovVHlwZSAvQ2F0YWxvZwovUGFnZXMgNSAwIFIKPj5lbmRvYmoKNSAwIG9iajw8Ci9UeXBlIC9QYWdlcwovQ291bnQgMQovS2lkcyBbIDIgMCBSIF0KPj5lbmRvYmoKMSAwIG9iajw8Ci9UeXBlIC9YT2JqZWN0Ci9TdWJ0eXBlIC9JbWFnZQovV2lkdGggMjkwCi9IZWlnaHQgMjkwCi9GaWx0ZXIgWyAvQ0NJVFRGYXhEZWNvZGUgXQovRGVjb2RlUGFybXMgWyA8PAovSyAtMQovQmxhY2tJczEgdHJ1ZQovQ29sdW1ucyAyOTAKL1Jvd3MgMjkwCj4+IF0KL0JpdHNQZXJDb21wb25lbnQgMQovQ29sb3JTcGFjZSAvRGV2aWNlR3JheQovTGVuZ3RoIDY2Ngo+PnN0cmVhbQomoLYaX////////////8g2b4gpHITff///////////8nBSkIB8nBS/////////////////////+QgHkNB/IQD////////////////////////////+P//////////////////////////IQ5CHIQ////////////////////////////////jkNB/H/////////////////////4yEOQh+P//////////////////EhoKR//////yDYchDkIchDyBg2E4aCcFL////////////////////////IgFIiAhODQTg0f/////////////////+ThCICEQGgnDQTg0E4NBODZ////////////////////////4k4NESEOJCCP/////////////////8gpHIQ5CCCEEENB8hDyBg2f//////////////////////////xEZKQhOEJwhOB5f//////////////yDZviDQIjkDBS///////////////ycFLEnCCThP//////////////////kIB5CHkQEEnCEQEJwbP///////////////////////////4ycGgnBoIgFL/////////////////////+QhxIQ4kIcg0H////////////////////////8cSEOJCHEhAP//////////////////jIQDIQ+Qh5OE////////////////////////4iIiI/////////////wAQAQJAAABAwABAAAAIgEAAAEBAwABAAAAIgEAAAIBAwABAAAAAQAAAAMBAwABAAAABAAAAAYBAwABAAAAAQAAABEBBAABAAAACAAAABYBAwABAAAAIgEAABcBBAABAAAAKAIAABwBAwABAAAAAQAAAAAAAAAKZW5kc3RyZWFtCmVuZG9iagoyIDAgb2JqPDwKL1Jlc291cmNlcyA8PAovUHJvY1NldCBbIC9QREYgL0ltYWdlQiBdCi9YT2JqZWN0IDw8Ci9pbWFnZSAxIDAgUgo+Pgo+PgovTWVkaWFCb3ggWyAwIDAgMjkwLjAgMjkwLjAgXQovQ29udGVudHMgMyAwIFIKL1R5cGUgL1BhZ2UKL1BhcmVudCA1IDAgUgo+PmVuZG9iagozIDAgb2JqPDwKL0xlbmd0aCA0Nwo+PnN0cmVhbQpxIDI5MC4wMDAwMDAgMCAwIDI5MC4wMDAwMDAgMCAwIGNtIC9pbWFnZSBEbyBRCgplbmRzdHJlYW0KZW5kb2JqCjYgMCBvYmo8PAovQ3JlYXRpb25EYXRlIChEOjIwMjUxMTA3MTMzNTE1WikKL01vZERhdGUgKEQ6MjAyNTExMDcxMzM1MTVaKQo+PmVuZG9iagp4cmVmCjAgNwowMDAwMDAwMDAwIDY1NTM2IGYgCjAwMDAwMDAxNDQgMDAwMDAgbiAKMDAwMDAwMTA1MiAwMDAwMCBuIAowMDAwMDAxMjE0IDAwMDAwIG4gCjAwMDAwMDAwNDAgMDAwMDAgbiAKMDAwMDAwMDA4NyAwMDAwMCBuIAowMDAwMDAxMzA5IDAwMDAwIG4gCnRyYWlsZXIKPDwKL1Jvb3QgNCAwIFIKL1NpemUgNwovSW5mbyA2IDAgUgo+PgpzdGFydHhyZWYKMTM5MQolJUVPRg=="
        )
        assert result[0].order_id == 3869227998
        assert result[0].parcel_id == "WB0000000001"
