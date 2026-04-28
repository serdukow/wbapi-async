from collections import deque
from typing import Any

from wbapi import WbAPI
from wbapi._core import BaseSession
from wbapi.exceptions import WBAPIError


class _CapturedRequest:
    def __init__(self, method: str, url: str, params: dict | None, json: Any | None) -> None:
        self.method = method
        self.url = url
        self.params = params
        self.json = json


class MockedSession(BaseSession):
    def __init__(self) -> None:
        super().__init__(base="https://test.api.com", timeout=0)
        self.requests: deque[_CapturedRequest] = deque()
        self._responses: deque[tuple[int, Any]] = deque()

    def add_response(self, data: Any, status: int = 200) -> None:
        self._responses.append((status, data))

    def get_last_request(self) -> _CapturedRequest:
        return self.requests[-1]

    async def _request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
        limit: Any = None,
    ) -> Any:
        self.requests.append(_CapturedRequest(method, url, params, json))

        if not self._responses:
            raise RuntimeError("No response provided")

        status, data = self._responses.popleft()
        if status >= 400:
            raise WBAPIError(http_status=status, **(data or {}))
        return data


class MockedAPI(WbAPI):
    def __init__(
        self,
        token: str = "eyJhbGciOiJFUzI1NiIsImtpZCI6InRlc3QiLCJ0eXAiOiJKV1QifQ"
        ".eyJpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCIsInNpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMSIsImFjYyI6MiwidCI6dHJ1ZSwicyI6MCwiZXhwIjoyMDg5MjY0MDc3fQ"
        ".fakesignature",
    ) -> None:
        from wbapi._core import MethodDispatcher
        super().__init__(token=token)
        self.mocked_session = MockedSession()
        self._session = self.mocked_session
        self._dispatcher = MethodDispatcher(self.mocked_session, token)

    def add_response(self, data: Any, status: int = 200) -> None:
        self.mocked_session.add_response(data, status)

    def get_last_request(self) -> _CapturedRequest:
        return self.mocked_session.get_last_request()
