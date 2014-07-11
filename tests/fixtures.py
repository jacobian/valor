import os
import pytest
import requests
import requests_mock
from valor import Schema

@pytest.fixture
def schema_fname():
    return os.path.join(os.path.dirname(__file__), 'schema.json')

@pytest.fixture
def schema():
    return Schema.from_file(os.path.join(os.path.dirname(__file__), 'schema.json'))

@pytest.fixture
def session():
    sess = requests.Session()
    sess.requests_mock = requests_mock.Adapter()
    sess.mount('http://', sess.requests_mock)
    sess.mount('https://', sess.requests_mock)
    return sess
