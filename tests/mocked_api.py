from collections import deque
from typing import Any

import httpx

from wbapi import WBApi


TOKEN = "test-token-abcd"


class MockedTransport:
    def __init__(self) -> None:
        self.requests: deque[httpx.Request] = deque()
        self.responses: deque[httpx.Response] = deque()
        self._handler: Any = None

    def add_response(self, data: Any = None, status: int = 200, **headers: str) -> None:
        self.responses.append(httpx.Response(status, json=data, headers=headers or None))

    def add_raw_response(self, response: httpx.Response) -> None:
        self.responses.append(response)

    def set_handler(self, handler: Any) -> None:
        self._handler = handler

    def get_last_request(self) -> httpx.Request:
        return self.requests[-1]

    @property
    def request_count(self) -> int:
        return len(self.requests)

    def __call__(self, request: httpx.Request) -> httpx.Response:
        request.read()
        self.requests.append(request)

        if self._handler is not None:
            return self._handler(request)
        if not self.responses:
            raise RuntimeError(f"No response provided for {request.method} {request.url}")
        return self.responses.popleft()


class MockedAPI(WBApi):
    def __init__(self, token: str = TOKEN, **kwargs: Any) -> None:
        self.mocked_transport = MockedTransport()
        kwargs.setdefault("max_retries", 0)
        kwargs.setdefault("retry_backoff", 0.001)
        kwargs.setdefault("max_retry_wait", 0.01)
        super().__init__(
            token=token,
            transport=httpx.MockTransport(self.mocked_transport),
            **kwargs,
        )

    def add_response(self, data: Any = None, status: int = 200, **headers: str) -> None:
        self.mocked_transport.add_response(data, status, **headers)

    def add_raw_response(self, response: httpx.Response) -> None:
        self.mocked_transport.add_raw_response(response)

    def set_handler(self, handler: Any) -> None:
        self.mocked_transport.set_handler(handler)

    def get_last_request(self) -> httpx.Request:
        return self.mocked_transport.get_last_request()

    @property
    def requests(self) -> deque[httpx.Request]:
        return self.mocked_transport.requests

    @property
    def request_count(self) -> int:
        return self.mocked_transport.request_count
