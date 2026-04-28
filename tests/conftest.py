import pytest

from tests.mocked_api import MockedAPI
from wbapi._core import BaseSession


@pytest.fixture
def api() -> MockedAPI:
    return MockedAPI()


@pytest.fixture
def session() -> BaseSession:
    return BaseSession(base="https://test.api", timeout=5)
