import os
import pytest
from valor import Schema

@pytest.fixture
def schema_fname():
    return os.path.join(os.path.dirname(__file__), 'schema.json')

@pytest.fixture
def schema():
    return Schema.from_file(os.path.join(os.path.dirname(__file__), 'schema.json'))

@pytest.fixture
def session():
    # FIXME!
    return None
