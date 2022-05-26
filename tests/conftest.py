import pytest
from clientapival_server import TmpValClientSvr as svr

@pytest.fixture(scope="function")
def test_client():
    tmpsvr = svr()
    yield

