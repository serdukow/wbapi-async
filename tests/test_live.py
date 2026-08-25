"""Read-only calls against the live Wildberries API.

Skipped unless WB_TOKEN is set, and excluded from the default run: these
tests reach an external service and cannot pass in CI. Run them before a
release, when a mock cannot tell whether the client still matches the API:

    uv run pytest -m integration
    WB_SANDBOX=1 uv run pytest -m integration
"""

from __future__ import annotations

import importlib
import os
import re

import pytest

from wbapi import SECTIONS, WBApi
from wbapi.client.method import WBMethod
from wbapi.exceptions import WBAPIError, WBConfigurationError, WBDecodeError
from wbapi.utils import Scope


pytestmark = [
    pytest.mark.integration,
    pytest.mark.skipif(not os.environ.get("WB_TOKEN"), reason="WB_TOKEN is not set"),
]

SANDBOX = bool(os.environ.get("WB_SANDBOX"))


def _snake(name: str) -> str:
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name).lower()


def read_only_methods() -> list[tuple[str, str, Scope | None]]:
    """Every GET that takes no arguments, so calling it cannot change anything."""
    found = []
    for section in SECTIONS:
        methods = importlib.import_module(f"wbapi.{section}.methods")
        for name in dir(methods):
            cls = getattr(methods, name)
            if not isinstance(cls, type) or not issubclass(cls, WBMethod):
                continue
            if getattr(cls, "__http_method__", "") != "GET":
                continue
            # A method with fields needs arguments this cannot invent.
            if getattr(cls, "__struct_fields__", ()):
                continue
            if SANDBOX and not getattr(cls, "__sandbox_host__", ""):
                continue
            found.append((section, _snake(name), getattr(cls, "__scope__", None)))
    return sorted(found)


CHECKS = read_only_methods()


@pytest.fixture
async def live_api():
    async with WBApi(token=os.environ["WB_TOKEN"].strip(), sandbox=SANDBOX) as api:
        yield api


def test_there_is_something_to_check() -> None:
    assert len(CHECKS) > 10


@pytest.mark.parametrize(
    ("section", "method", "scope"),
    CHECKS,
    ids=lambda value: value if isinstance(value, str) else "",
)
async def test_endpoint_answers_in_the_shape_the_spec_promised(
    live_api: WBApi, section: str, method: str, scope: Scope | None
) -> None:
    if scope is not None and not live_api.token.allows(scope):
        pytest.skip(f"token lacks {scope.name}")

    try:
        await getattr(getattr(live_api, section), method)()
    except WBDecodeError as exc:
        pytest.fail(f"response does not match the spec: {exc}")
    except WBConfigurationError as exc:
        pytest.skip(str(exc))
    except WBAPIError as exc:
        if exc.status_code in (401, 403):
            pytest.skip(f"HTTP {exc.status_code}: not available to this token")
        raise
