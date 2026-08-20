import pytest

from tests.mocked_api import MockedAPI


@pytest.fixture
def api() -> MockedAPI:
    return MockedAPI()


@pytest.fixture
def retrying_api() -> MockedAPI:
    return MockedAPI(max_retries=3)
