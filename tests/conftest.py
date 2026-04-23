import pytest

from tests.mocked_api import MockedAPI
from wbapi.client.session import BaseSession


@pytest.fixture
def api() -> MockedAPI:
    return MockedAPI()


@pytest.fixture
def session() -> BaseSession:
    s = BaseSession(base="https://test.api", timeout=5)
    return s
