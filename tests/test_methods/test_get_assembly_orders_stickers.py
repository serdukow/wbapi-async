import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AssemblyOrdersStickersItem


@pytest.mark.unit
class TestGetAssemblyOrdersStickers:
    async def test_get_assembly_orders_stickers(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "stickers": [
                    {
                        "orderId": 5346346,
                        "partA": 231648,
                        "partB": 9753,
                        "barcode": "!uKEtQZVx",
                        "file": "iVBORw0KGgoAAAANSUhEUgAAASIAAAEiAQAAAAB1xeIbAAABiElEQVR4nO2YUW6DMAyGbUDaI0g9wI4Sjg5H2Q3IeyZPthNKV03tNiVdtf9/cFvXAvRhkh+z0G2t3R1FRKgqAokikCgCiSKQeDQJzho8yXMsmfmh1/UvqoKoNrsLdgN6S8hzXP2TV8Xc47KMyTPnx+DvX/1zVg1Xmch1z9ih6gv2HLZTuqIPXjX7ftSlPRLJ+prXnONLF9hXZL96q/fE4W1Q+O8XvQ/29djL/lvWiTg/Bt89Voeqn/j7OQ4eTLJY7tz8oEoVSFC28aN9JqKwqbX3kP+VBewrsg/KedE3qmXUn3IMYF/d3zONm38TiqckFKeyEaDv6/W96Nus9b2tPrbw2LOAvq/Pfpfn/Fb4HoA1p9UcU3SHJTLHExk+p8VeK3JwN0Q2UNPmR9+3m2OyDzPjoOFFML9vOMcUin0iHahR2CaGz/mkmo6P5zHtQdD3TeeY5NY++/sKZ+xQdUliNZszqePRkFd+tfvHqhtC1S/nmOQh7eH+Y3WoygKJIpAoAokikChqT+IDIkbb8/8OLskAAAAASUVORK5CYII=",
                    }
                ]
            }
        )

        result = await api.get_assembly_orders_stickers(type_="svg", width="58", height="40")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrdersStickersItem)
        assert result[0].order_id == 5346346
        assert result[0].part_a == 231648
        assert result[0].part_b == 9753
        assert result[0].barcode == "!uKEtQZVx"
        assert (
            result[0].file
            == "iVBORw0KGgoAAAANSUhEUgAAASIAAAEiAQAAAAB1xeIbAAABiElEQVR4nO2YUW6DMAyGbUDaI0g9wI4Sjg5H2Q3IeyZPthNKV03tNiVdtf9/cFvXAvRhkh+z0G2t3R1FRKgqAokikCgCiSKQeDQJzho8yXMsmfmh1/UvqoKoNrsLdgN6S8hzXP2TV8Xc47KMyTPnx+DvX/1zVg1Xmch1z9ih6gv2HLZTuqIPXjX7ftSlPRLJ+prXnONLF9hXZL96q/fE4W1Q+O8XvQ/29djL/lvWiTg/Bt89Voeqn/j7OQ4eTLJY7tz8oEoVSFC28aN9JqKwqbX3kP+VBewrsg/KedE3qmXUn3IMYF/d3zONm38TiqckFKeyEaDv6/W96Nus9b2tPrbw2LOAvq/Pfpfn/Fb4HoA1p9UcU3SHJTLHExk+p8VeK3JwN0Q2UNPmR9+3m2OyDzPjoOFFML9vOMcUin0iHahR2CaGz/mkmo6P5zHtQdD3TeeY5NY++/sKZ+xQdUliNZszqePRkFd+tfvHqhtC1S/nmOQh7eH+Y3WoygKJIpAoAokikChqT+IDIkbb8/8OLskAAAAASUVORK5CYII="
        )
