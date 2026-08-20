from __future__ import annotations

import base64
import json
from typing import Any

import httpx
import pytest

from wbapi import WBApi
from wbapi.utils import Scope


ALL_SCOPES = sum(1 << scope for scope in Scope if scope is not Scope.READ_ONLY)


def make_token(
    *,
    acc: int = 3,
    scopes: int | None = None,
    seller_id: str = "seller-1",
    expires_at: int = 2_089_264_077,
    **extra: Any,
) -> str:
    payload: dict[str, Any] = {
        "acc": acc,
        "sid": seller_id,
        "exp": expires_at,
        **extra,
    }
    if scopes is not None:
        payload["s"] = scopes

    def encode(data: dict[str, Any]) -> str:
        return base64.urlsafe_b64encode(json.dumps(data).encode()).decode().rstrip("=")

    return f"{encode({'alg': 'ES256'})}.{encode(payload)}.signature"


TOKEN = make_token(scopes=ALL_SCOPES)


class Recorder:
    def __init__(self) -> None:
        self.requests: list[httpx.Request] = []
        self._queue: list[httpx.Response] = []
        self._handler: Any = None

    def add(self, data: Any = None, status: int = 200, **headers: str) -> None:
        self._queue.append(httpx.Response(status, json=data, headers=headers or None))

    def add_raw(self, response: httpx.Response) -> None:
        self._queue.append(response)

    def handle(self, handler: Any) -> None:
        self._handler = handler

    @property
    def last(self) -> httpx.Request:
        return self.requests[-1]

    @property
    def count(self) -> int:
        return len(self.requests)

    def body(self, index: int = -1) -> Any:
        content = self.requests[index].content
        return json.loads(content) if content else None

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)
        if self._handler is not None:
            return self._handler(request)
        if not self._queue:
            raise AssertionError(f"No response queued for {request.method} {request.url}")
        return self._queue.pop(0)


@pytest.fixture
def recorder() -> Recorder:
    return Recorder()


@pytest.fixture
def api(recorder: Recorder) -> WBApi:
    return WBApi(
        token=TOKEN,
        transport=httpx.MockTransport(recorder),
        max_retries=0,
        retry_backoff=0.001,
        max_retry_wait=0.01,
    )


@pytest.fixture
def retrying_api(recorder: Recorder) -> WBApi:
    return WBApi(
        token=TOKEN,
        transport=httpx.MockTransport(recorder),
        max_retries=3,
        retry_backoff=0.001,
        max_retry_wait=0.01,
    )
